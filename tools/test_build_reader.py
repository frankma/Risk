"""Tests for the reader build, run on the repo's chapters as they stand."""
import pytest

import build_reader


@pytest.fixture(scope="module")
def page(tmp_path_factory):
    return build_reader.build(tmp_path_factory.mktemp("reader") / "index.html")


def test_the_page_is_a_complete_document(page):
    assert page.startswith("<!doctype html>")
    assert page.endswith("</html>\n")
    assert "<title>Investment Risk Framework</title>" in page


def test_every_chapter_has_a_view(page):
    for vid, *_ in build_reader.CHAPTERS:
        assert f'id="view-{vid}"' in page
    assert 'id="view-overview"' in page


def test_every_chapter_file_is_in_the_reader():
    files = {f"{d.name}/{f.name}" for d in (build_reader.REPO / "framework", build_reader.REPO / "pillars")
             for f in d.glob("*.md")}
    assert files == set(build_reader.FILE_TO_VIEW)


def test_a_link_to_an_unknown_file_stops_the_build():
    with pytest.raises(SystemExit, match="Unmapped link"):
        build_reader.rewrite_links('<a href="missing.md">x</a>', "framework/00-philosophy.md")


def test_links_to_chapters_become_view_anchors():
    body = build_reader.rewrite_links('<a href="05-principles.md#4-exceptions">x</a>', "framework/00-philosophy.md")
    assert body == '<a href="#principles--4-exceptions">x</a>'
