#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = ["markdown==3.7"]
# ///
"""Build the framework reader, one HTML page with every chapter, from the repo's Markdown.

Run: uv run tools/build_reader.py OUTPUT.html
The output is a complete page. GitHub Pages publishes it at the site's root after each merge to master, with the film
from docs/ beside it at film/ (see .github/workflows/pages.yml). The reader links to the film from its rail, so the
film must sit at film/ next to the page. The chapters are the source; the page is never edited by hand.
"""
import html
import pathlib
import posixpath
import re
import subprocess
import sys

import markdown

REPO = pathlib.Path(__file__).resolve().parent.parent
THEME = (pathlib.Path(__file__).resolve().parent / "theme.css").read_text()
SHELL_HEAD = ('<!doctype html>\n<html lang="en">\n<meta charset="utf-8">\n'
              '<meta name="viewport" content="width=device-width, initial-scale=1">\n')
REPO_URL = "https://github.com/frankma/Risk"

BACKDROP, PRACTICE, REDESIGN, PILLARS = "Foundations", "Practice", "The redesign around AI", "The pillars"
GROUPS = (BACKDROP, PILLARS, PRACTICE, REDESIGN)
CHAPTERS = [
    ("philosophy", "framework/00-philosophy.md", BACKDROP, "00"),
    ("investment-risk", "framework/01-investment-risk.md", BACKDROP, "01"),
    ("sources-of-return", "framework/02-sources-of-return.md", BACKDROP, "02"),
    ("market-risk", "pillars/market-risk.md", PILLARS, ""),
    ("liquidity-risk", "pillars/liquidity-risk.md", PILLARS, ""),
    ("performance-risk", "pillars/performance-risk.md", PILLARS, ""),
    ("integrated-view", "pillars/integrated-view.md", PILLARS, ""),
    ("risk-data", "framework/03-risk-data.md", PRACTICE, "03"),
    ("limits-and-escalation", "framework/04-limits-and-escalation.md", PRACTICE, "04"),
    ("new-portfolio-review", "pillars/new-portfolio-review.md", PRACTICE, ""),
    ("alpha-and-beta-method", "pillars/alpha-and-beta-method.md", PRACTICE, ""),
    ("principles", "framework/05-principles.md", REDESIGN, "05"),
    ("working-with-ai", "framework/06-working-with-ai.md", REDESIGN, "06"),
    ("redesign-method", "framework/07-redesign-method.md", REDESIGN, "07"),
    ("controls", "framework/08-controls.md", REDESIGN, "08"),
    ("measuring-value", "framework/09-measuring-value.md", REDESIGN, "09"),
    ("decision-rights", "framework/10-decision-rights.md", REDESIGN, "10"),
]
FILE_TO_VIEW = {path: vid for vid, path, _, _ in CHAPTERS}
FILE_TO_VIEW["framework/concept-map.md"] = "overview"

# Drawn from the pillar chapters and the philosophy's three decisions.
GLANCE = [
    ("", "Market risk", "Liquidity risk", "Performance risk", "Integrated view"),
    ("Question", "How much could a portfolio lose, in total and against its benchmark?",
     "Can the portfolio meet every call on its cash, in time and at a fair cost, without disadvantaging the investors "
     "who stay?",
     "Is the portfolio delivering what was promised, in the way it was promised?", "Where are signals combining?"),
    ("Lens", "Forward-looking: what could happen, absolute and relative", "Calls on cash against assets",
     "Realised: whether the promise is kept", "Combinations across pillars"),
    ("Decision served", "Construct, Oversee", "Oversee", "Assess", "Oversee"),
    ("Main measures",
     "VaR, ex-ante tracking error, risk budget, drawdown headroom, sensitivities, concentration, leverage, "
     "counterparty exposure",
     "Redemption coverage, margin and collateral calls, time and cost to sell, investor concentration, stale prices",
     "Realised return, ex-post tracking error, realised drawdown, attribution, alpha and beta split",
     "None of its own; reads the pillars"),
    ("Cadence", "Daily", "Daily, and on events", "Daily on rolling windows; monthly and quarterly reviews", "Daily"),
    ("Flagship redesign", "Daily monitoring as a ranked queue",
     "Continuous monitoring, with event-triggered stress tests", "Portfolio manager review with a challenge pack",
     "A daily ranking of portfolios where signals combine"),
    ("The human decides", "What matters and what to escalate", "The recommendation on liquidity tools",
     "What to challenge", "Watch list or escalate"),
]


def gh_slug(text):
    text = html.unescape(re.sub(r"<[^>]+>", "", text)).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def preprocess(text):
    """Python-Markdown needs a blank line before a list; GitHub does not."""
    out, prev = [], ""
    for line in text.splitlines():
        is_item = re.match(r"^(- |\d+\. )", line)
        prev_item = re.match(r"^(- |\d+\. |\s+)", prev)
        if is_item and prev.strip() and not prev_item:
            out.append("")
        out.append(line)
        prev = line
    return "\n".join(out) + "\n"


NUM = re.compile(r"^[+\-−]?\d[\d,.]*\s*(%|x|h)?$")


def plain(cell):
    return html.unescape(re.sub(r"<[^>]+>", "", cell)).strip()


def style_table(match):
    """Right-align columns that hold only numbers, and wrap the table so it scrolls by itself."""
    body = match.group(0)
    rows = re.findall(r"<tr>(.*?)</tr>", body, flags=re.S)
    grid = [re.findall(r"<t[hd][^>]*>.*?</t[hd]>", r, flags=re.S) for r in rows]
    if len(grid) > 1:
        cols = max(len(r) for r in grid)
        numeric = []
        for c in range(cols):
            cells = [plain(r[c]) for r in grid[1:] if c < len(r)]
            filled = [x for x in cells if x]
            numeric.append(bool(filled) and all(NUM.match(x) for x in filled))
        for r_i, row in enumerate(rows):
            new = row
            for c, cell in enumerate(grid[r_i]):
                if c < len(numeric) and numeric[c]:
                    tagged = re.sub(r"^<(t[hd])[^>]*>", r'<\1 class="num">', cell)
                    new = new.replace(cell, tagged, 1)
            body = body.replace(f"<tr>{row}</tr>", f"<tr>{new}</tr>", 1)
    return f'<div class="table-wrap">{body}</div>'


def rewrite_links(body, source):
    base = posixpath.dirname(source)

    def fix(match):
        href = match.group(1)
        if href.startswith(("http://", "https://", "#")):
            return match.group(0)
        path, _, anchor = href.partition("#")
        full = posixpath.normpath(posixpath.join(base, path))
        if full not in FILE_TO_VIEW:
            sys.exit(f"Unmapped link in {source}: {href}")
        view = FILE_TO_VIEW[full]
        return f'href="#{view}--{anchor}"' if anchor else f'href="#{view}"'

    return re.sub(r'href="([^"]+)"', fix, body)


def render(vid, source):
    text = preprocess((REPO / source).read_text())
    md = markdown.Markdown(
        extensions=["tables", "sane_lists", "toc"],
        extension_configs={"toc": {"slugify": lambda v, s: f"{vid}--{gh_slug(v)}", "toc_depth": "1-3"}},
    )
    body = md.convert(text)
    title = plain(re.search(r"<h1[^>]*>(.*?)</h1>", body, flags=re.S).group(1))
    body = re.sub(r"<h1[^>]*>.*?</h1>\s*", "", body, count=1, flags=re.S)
    body = re.sub(r"<table>.*?</table>", style_table, body, flags=re.S)
    body = rewrite_links(body, source)
    heads = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', body, flags=re.S)
    return title, body, [(i, plain(t)) for i, t in heads]


def readme_parts():
    text = (REPO / "README.md").read_text()
    owners = r"Analytics engine|AI assistant|The risk manager and head of risk"
    rows = [(w, o, y or "") for w, o, y in
            re.findall(rf"^\| (.+?) \| ({owners}) \|(?: (.+?) \|)?$", text, flags=re.M)]
    # The two rules: an intro line and the bullet list after it, up to the next heading.
    rules = re.search(r"^Two rules make it \w+:.*?(?=\n\n## )", text, flags=re.M | re.S).group(0)
    disclaimer = re.search(r"## Disclaimer\n(.+)\Z", text, flags=re.S).group(1).replace("\n", " ").strip()
    identity = re.search(r"^\*\*(.+?)\*\*$", text, flags=re.M).group(1)
    m = re.search(r"^An asset manager .*?(?=\n\n)", text, flags=re.M | re.S)
    backdrop = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", m.group(0).replace("\n", " ")) if m else ""
    return rows, rewrite_links(markdown.markdown(rules), "README.md"), disclaimer, identity, backdrop


def build(out):
    """Write the reader to `out` and return the page."""
    commit = subprocess.check_output(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"], text=True).strip()
    dirty = subprocess.check_output(["git", "-C", str(REPO), "status", "--short"], text=True).strip()
    branch = subprocess.check_output(["git", "-C", str(REPO), "rev-parse", "--abbrev-ref", "HEAD"], text=True).strip()
    built_from = (f"commit {commit}" if branch in ("master", "HEAD") else f"the {branch} branch at commit {commit}") \
        + (", plus uncommitted edits" if dirty else "")

    rendered = {vid: render(vid, path) for vid, path, _, _ in CHAPTERS}
    map_title, map_body, map_heads = render("overview", "framework/concept-map.md")
    map_body = map_body.replace('<div class="table-wrap">', '<div class="table-wrap concepts">')
    core, rules, disclaimer, identity, backdrop = readme_parts()

    order = [("overview", "Overview")] + [(vid, rendered[vid][0]) for vid, *_ in CHAPTERS]
    pos = {vid: i for i, (vid, _) in enumerate(order)}

    def pager(vid):
        i = pos[vid]
        prev_link = (f'<a href="#{order[i - 1][0]}"><span class="kicker">Previous</span>'
                     f"{html.escape(order[i - 1][1])}</a>" if i > 0 else "<span></span>")
        next_link = (f'<a class="next" href="#{order[i + 1][0]}"><span class="kicker">Next</span>'
                     f"{html.escape(order[i + 1][1])}</a>" if i + 1 < len(order) else "<span></span>")
        return f'<nav class="pager" aria-label="Chapter pages">{prev_link}{next_link}</nav>'

    # Rail
    def sublist(vid, heads):
        items = "".join(f'<li><a href="#{i}">{html.escape(t)}</a></li>' for i, t in heads)
        return f'<ul class="sub" data-sub="{vid}" hidden>{items}</ul>'

    nav = [f'<li><a data-nav="overview" href="#overview">Overview and concept map</a>'
           f'{sublist("overview", map_heads)}</li>']
    for group in GROUPS:
        nav.append(f'<li class="group kicker">{group}</li>')
        for vid, _, g, number in CHAPTERS:
            if g != group:
                continue
            title, _, heads = rendered[vid]
            num = f'<span class="n">{number}</span>' if number else ""
            nav.append(f'<li><a data-nav="{vid}" href="#{vid}">{num}{html.escape(title)}</a>{sublist(vid, heads)}</li>')

    options = ['<option value="overview">Overview and concept map</option>']
    for group in GROUPS:
        options.append(f'<optgroup label="{group}">')
        options += [f'<option value="{v}">{html.escape(rendered[v][0])}</option>'
                    for v, _, g, _ in CHAPTERS if g == group]
        options.append("</optgroup>")

    # Overview
    strip = "".join(
        f'<div class="cell"><p class="kicker">{html.escape(owner)}</p><p class="work">{html.escape(work)}</p>'
        + (f'<p class="why">{html.escape(why)}</p>' if why else "") + '</div>'
        for work, owner, why in core
    )
    head_cells = "".join(f"<th>{html.escape(c)}</th>" for c in GLANCE[0])
    glance_rows = "".join(
        "<tr>" + "".join(f"<td>{html.escape(c)}</td>" for c in row) + "</tr>" for row in GLANCE[1:]
    )
    overview = f"""
<section class="view" id="view-overview" data-id="overview" data-title="Overview" hidden>
  <header class="masthead">
    <p class="mark">Asset management</p>
    <h1>Investment Risk Framework</h1>
    <p class="lede">{html.escape(identity)}</p>
    {f'<p class="backdrop">{html.escape(backdrop)}</p>' if backdrop else ""}
  </header>
  <div class="strip" aria-label="The core pattern">{strip}</div>
  <div class="rules">{rules}</div>
  <div class="content">
    <h2 id="overview--the-pillars-at-a-glance">The pillars at a glance</h2>
    <figure class="exhibit">
      <div class="table-wrap glance"><table><thead><tr>{head_cells}</tr></thead>
      <tbody>{glance_rows}</tbody></table></div>
      <figcaption>The philosophy's three decisions run through the pillars: Construct before a trade, Oversee during the
      investment, Assess after it.</figcaption>
    </figure>
    <h2 id="overview--concept-map" class="section-title">{html.escape(map_title)}</h2>
    {map_body}
  </div>
  {pager("overview")}
</section>"""

    views = [overview]
    for vid, _, group, number in CHAPTERS:
        title, body, _ = rendered[vid]
        body = body.replace("<p>", '<p class="lede">', 1)
        label = (f"Chapter {number}" if number else
                 {"integrated-view": "Across the pillars", "new-portfolio-review": "Across the pillars",
                  "alpha-and-beta-method": "Performance risk method"}.get(vid, "Pillar"))
        hidden = "" if vid == "philosophy" else " hidden"
        views.append(
            f'<section class="view" id="view-{vid}" data-id="{vid}" data-title="{html.escape(title)}"{hidden}>'
            f'<header class="masthead"><p class="mark">{label}</p><h1>{html.escape(title)}</h1></header>'
            f'<div class="content">{body}</div>{pager(vid)}</section>'
        )

    css = THEME + PAGE_CSS
    page = PAGE.format(
        css=css,
        nav="".join(nav),
        options="".join(options),
        views="".join(views),
        built=html.escape(built_from),
        repo=REPO_URL,
        disclaimer=html.escape(disclaimer),
        js=PAGE_JS,
    )

    # Every internal link must land on a view or a heading.
    ids = set(re.findall(r'id="([^"]+)"', page))
    missing = sorted({h for h in re.findall(r'href="#([^"]*)"', page) if f"view-{h}" not in ids and h not in ids})
    if missing:
        sys.exit("Unresolved links: " + ", ".join(missing))
    page = SHELL_HEAD + page + "</html>\n"
    out.write_text(page, encoding="utf-8")
    words = len(re.sub(r"<[^>]+>", " ", "".join(views)).split())
    print(f"{out}: {len(page) // 1024} KB, {words} words, {len(order)} views, {len(ids)} ids, built from {built_from}")
    return page


PAGE_CSS = """
/* Kinari page CSS: only paper, sumi and beni tokens. Hairlines and space do the grouping; no boxes.
   Layout: a reading column beside a sticky chapter rail; the rail stacks above the text under 900px. */
body::before { content: ""; position: fixed; inset: 0 0 auto; height: env(safe-area-inset-top, 0px); z-index: 10;
  background: var(--bg); }
.shell { display: grid; grid-template-columns: 240px minmax(0, 1fr); gap: 56px; max-width: 1140px; margin: 0 auto;
  padding-left: max(20px, env(safe-area-inset-left, 0px)); padding-right: max(20px, env(safe-area-inset-right, 0px));
  padding-block: 32px 56px; }
.rail { position: sticky; top: env(safe-area-inset-top, 0px); align-self: start; max-height: 100vh; overflow-y: auto;
  padding-block: 4px 24px; min-width: 0; }
.rail-name { font: 700 17px/1.3 var(--sans); color: var(--ink); text-decoration: none; display: block;
  border-top: 1px solid var(--ink); padding-top: 10px; margin-bottom: 18px; }
.rail label { display: block; font: 400 12.5px/1.3 var(--sans); color: var(--muted); margin-bottom: 6px; }
.rail input, .rail select { width: 100%; box-sizing: border-box; }
.find { margin-bottom: 18px; }
.kicker { display: block; font: 400 12.5px/1.3 var(--sans); color: var(--muted); }
.results { list-style: none; margin: 10px 0 0; padding: 0; font-size: 13.5px; line-height: 1.4; }
.results li { border-top: 1px solid var(--line); padding: 8px 0; }
.results a { display: block; text-decoration: none; color: var(--ink); }
.results .where { display: block; color: var(--faint); font-size: 12px; }
.results .head { display: block; font-weight: 700; color: var(--ink); }
.results .snip { display: block; color: var(--muted); margin-top: 2px; }
.results mark { background: none; color: var(--beni); }
.count { font-size: 12.5px; color: var(--faint); margin-top: 8px; }
.chapters { list-style: none; margin: 0; padding: 0; font-size: 14.5px; line-height: 1.35; }
.chapters > li > a { display: block; padding: 5px 0 5px 10px; color: var(--ink); text-decoration: none;
  border-left: 1px solid transparent; }
.chapters > li > a:hover { border-left-color: var(--line); }
.chapters > li > a[aria-current="page"] { font-weight: 700; border-left-color: var(--ink); }
.chapters .n { font-size: 12.5px; font-variant-numeric: tabular-nums; color: var(--faint); margin-right: 8px; }
.chapters .group { margin: 18px 0 4px; }
.sub { list-style: none; margin: 2px 0 8px; padding: 0 0 0 12px; font-size: 13px; }
.sub a { display: block; padding: 3px 0; color: var(--muted); text-decoration: none; }
.sub a:hover { color: var(--ink); text-decoration: underline; text-decoration-color: var(--beni); }
.rail-select { display: none; margin-bottom: 14px; }
main { min-width: 0; }
.masthead { display: grid; gap: 12px; margin-bottom: 8px; }
.masthead .lede { max-width: 64ch; }
.backdrop { max-width: 66ch; }
.content { font-size: 17px; }
.content > .lede { margin: 16px 0 28px; }
.content p, .content ul, .content ol, .content blockquote { max-width: 66ch; }
.content p { margin-block: 0 14px; }
.content ul, .content ol { padding-left: 22px; margin-block: 0 14px; }
.content li { margin-bottom: 8px; }
.content li > p { margin-bottom: 6px; }
.content h2 { border-top: 1px solid var(--line); padding-top: 28px; margin: 48px 0 14px; scroll-margin-top: 12px; }
.content h3 { margin: 28px 0 8px; scroll-margin-top: 12px; }
.content blockquote { border-left: 1px solid var(--ink); margin: 0 0 18px; padding: 2px 0 2px 18px; }
.content blockquote p:last-child { margin-bottom: 0; }
.table-wrap { overflow-x: auto; margin: 0 0 18px; }
.table-wrap table { min-width: 520px; }
.table-wrap td { overflow-wrap: break-word; }
.concepts table { min-width: 640px; table-layout: fixed; }
.concepts th:nth-child(1), .concepts td:nth-child(1) { width: 21%; }
.concepts td:nth-child(1) { font-weight: 700; }
.concepts th:nth-child(2), .concepts td:nth-child(2) { width: 39%; }
.concepts th:nth-child(3), .concepts td:nth-child(3) { width: 17%; }
.concepts th:nth-child(4), .concepts td:nth-child(4) { width: 23%; }
.section-title { font-size: 28px; }
.strip { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); border-top: 1px solid var(--ink);
  border-bottom: 1px solid var(--line); margin-top: 32px; }
.strip .cell { padding: 14px 18px 16px; border-left: 1px solid var(--line); display: grid; gap: 6px;
  align-content: start; }
.strip .cell:first-child { border-left: 0; padding-left: 0; }
.strip .work { font: 400 19px/1.3 var(--sans); }
.strip .why { font: 400 13.5px/1.5 var(--sans); color: var(--muted); }
.rules { font: 400 14px/1.55 var(--sans); color: var(--muted); margin-top: 14px; max-width: 80ch; }
.rules p { margin: 0 0 6px; max-width: 80ch; }
.rules ul { margin: 0; padding-left: 18px; }
.rules li { margin-bottom: 6px; }
.rules strong { color: var(--ink); }
.exhibit { margin: 0 0 18px; }
.exhibit .table-wrap { margin-bottom: 0; }
.glance table { min-width: 760px; table-layout: fixed; }
.glance th:first-child, .glance td:first-child { width: 15%; color: var(--muted); }
.rail-film { display: block; font: 700 14px/1.3 var(--sans); margin: -8px 0 18px; }
.pager { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 24px;
  border-top: 1px solid var(--line); margin-top: 48px; padding-top: 14px; font: 400 15px/1.35 var(--sans); }
.pager a { display: grid; gap: 4px; text-decoration: none; }
.pager a:hover { text-decoration: underline; text-decoration-color: var(--beni); }
.pager .next { text-align: right; }
.page-foot { margin-top: 32px; }
.page-foot p { max-width: 80ch; margin-bottom: 6px; }
@media (max-width: 900px) {
  .shell { grid-template-columns: minmax(0, 1fr); gap: 20px; padding-block: 20px 44px; }
  .rail { position: static; max-height: none; overflow: visible; padding-block: 0; }
  .rail-select { display: block; }
  .chapters { display: none; }
  .strip { grid-template-columns: minmax(0, 1fr); }
  .strip .cell { border-left: 0; border-top: 1px solid var(--line); padding-left: 0; padding-right: 0; }
  .strip .cell:first-child { border-top: 0; }
}
"""

PAGE_JS = """
(function () {
  var views = Array.prototype.slice.call(document.querySelectorAll('.view'));
  var select = document.getElementById('chapter-select');
  var find = document.getElementById('find');
  var results = document.getElementById('results');
  var count = document.getElementById('find-count');

  function route() {
    var hash = location.hash.slice(1);
    var id = hash.split('--')[0];
    var view = document.getElementById('view-' + id) || document.getElementById('view-philosophy');
    views.forEach(function (v) { v.hidden = v !== view; });
    var current = view.getAttribute('data-id');
    document.querySelectorAll('[data-nav]').forEach(function (a) {
      if (a.getAttribute('data-nav') === current) { a.setAttribute('aria-current', 'page'); }
      else { a.removeAttribute('aria-current'); }
    });
    document.querySelectorAll('[data-sub]').forEach(function (u) {
      u.hidden = u.getAttribute('data-sub') !== current;
    });
    select.value = current;
    var target = hash.indexOf('--') > 0 ? document.getElementById(hash) : null;
    if (target) { target.scrollIntoView(); } else { window.scrollTo(0, 0); }
  }

  var index = [];
  views.forEach(function (v) {
    var title = v.getAttribute('data-title');
    var cur = { id: v.getAttribute('data-id'), where: title, head: title, text: '' };
    Array.prototype.slice.call(v.querySelector('.content').children).forEach(function (el) {
      if (el.tagName === 'H2' || el.tagName === 'H3') {
        index.push(cur);
        cur = { id: el.id, where: title, head: el.textContent, text: '' };
      } else { cur.text += ' ' + el.textContent; }
    });
    index.push(cur);
  });

  function snippet(item, term, line) {
    var text = item.text.replace(/\\s+/g, ' ').trim();
    var at = text.toLowerCase().indexOf(term);
    if (at < 0) { line.textContent = text.slice(0, 90) + (text.length > 90 ? '\\u2026' : ''); return; }
    var start = Math.max(0, at - 40);
    var end = Math.min(text.length, at + term.length + 60);
    line.appendChild(document.createTextNode((start > 0 ? '\\u2026' : '') + text.slice(start, at)));
    var mark = document.createElement('mark');
    mark.textContent = text.slice(at, at + term.length);
    line.appendChild(mark);
    line.appendChild(document.createTextNode(text.slice(at + term.length, end) + (end < text.length ? '\\u2026' : '')));
  }

  function search() {
    var query = find.value.trim().toLowerCase();
    results.textContent = '';
    if (query.length < 2) { results.hidden = true; count.hidden = true; return; }
    var terms = query.split(/\\s+/);
    var hits = index.filter(function (item) {
      var hay = (item.head + ' ' + item.text).toLowerCase();
      return terms.every(function (t) { return hay.indexOf(t) >= 0; });
    }).sort(function (a, b) {
      return (b.head.toLowerCase().indexOf(terms[0]) >= 0) - (a.head.toLowerCase().indexOf(terms[0]) >= 0);
    });
    count.hidden = false;
    count.textContent = hits.length === 0 ? 'No sections match.' :
      (hits.length > 12 ? 'Showing 12 of ' + hits.length + ' sections.' :
        hits.length + (hits.length === 1 ? ' section.' : ' sections.'));
    results.hidden = hits.length === 0;
    hits.slice(0, 12).forEach(function (item) {
      var li = document.createElement('li');
      var a = document.createElement('a');
      a.href = '#' + item.id;
      var where = document.createElement('span'); where.className = 'where'; where.textContent = item.where;
      var head = document.createElement('span'); head.className = 'head'; head.textContent = item.head;
      var snip = document.createElement('span'); snip.className = 'snip';
      snippet(item, terms[0], snip);
      a.appendChild(where);
      if (item.head !== item.where) { a.appendChild(head); }
      a.appendChild(snip);
      li.appendChild(a);
      results.appendChild(li);
    });
  }

  select.addEventListener('change', function () { location.hash = select.value; });
  find.addEventListener('input', search);
  window.addEventListener('hashchange', route);
  route();
})();
"""

PAGE = """<title>Investment Risk Framework</title>
<style>
{css}
</style>
<div class="shell">
  <aside class="rail">
    <a class="rail-name" href="#philosophy">Investment Risk Framework</a>
    <a class="rail-film" href="film/">Watch the film</a>
    <div class="find">
      <label for="find">Find in the framework</label>
      <input id="find" type="search" placeholder="unintended beta, escalation" autocomplete="off">
      <p class="count" id="find-count" role="status" hidden></p>
      <ul class="results" id="results" hidden></ul>
    </div>
    <div class="rail-select">
      <label for="chapter-select">Chapter</label>
      <select id="chapter-select">{options}</select>
    </div>
    <nav aria-label="Chapters"><ul class="chapters">{nav}</ul></nav>
  </aside>
  <main>
    {views}
    <footer class="page-foot">
      <p>Built from the Markdown chapters in the public <a href="{repo}">Risk repository</a>, at {built}. The
      chapters are the source, and this page is rebuilt from them. All funds and figures are illustrative.</p>
      <p>{disclaimer}</p>
    </footer>
  </main>
</div>
<script>
{js}
</script>
"""

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: build_reader.py OUTPUT.html")
    build(pathlib.Path(sys.argv[1]))
