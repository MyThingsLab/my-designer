from __future__ import annotations

from mydesigner.mockup import build_prompt, finish, slug


def test_slug_lowercases_and_dashes_punctuation() -> None:
    assert slug("Ecosystem Hub: v1!") == "ecosystem-hub-v1"


def test_slug_falls_back_when_nothing_alnum_survives() -> None:
    assert slug("...") == "mockup"


def test_build_prompt_includes_brief_when_present() -> None:
    assert build_prompt("Hub page", "grid of tool cards") == "Hub page\n\ngrid of tool cards"


def test_build_prompt_is_just_the_title_without_a_brief() -> None:
    assert build_prompt("Hub page", "") == "Hub page"


def test_finish_strips_and_appends_trailing_newline() -> None:
    assert finish("  <html></html>  ") == "<html></html>\n"


def test_finish_is_none_for_a_blank_reply() -> None:
    assert finish("   \n") is None
