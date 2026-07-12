from __future__ import annotations

import re

# Seam: the system prompt for the single Engine call.
SYSTEM = """You design mockups for the MyThingsLab tool fleet's web presence.

Given a design brief, write ONE self-contained HTML page: a <!DOCTYPE html>
document with all CSS inline in a <style> tag. No external stylesheets, no
JavaScript, no fetches to real APIs, no placeholder secrets or tokens. This is
a visual prototype only — use representative sample content, never wire it to
live data. Reply with the HTML document and nothing else: no prose, no
markdown fences."""

_SLUG_RE = re.compile(r"[^a-z0-9]+")


def slug(title: str) -> str:
    stripped = _SLUG_RE.sub("-", title.lower()).strip("-")
    return stripped or "mockup"


def build_prompt(title: str, brief: str) -> str:
    return f"{title}\n\n{brief}" if brief else title


def finish(text: str) -> str | None:
    stripped = text.strip()
    if not stripped:
        return None
    return stripped + "\n"
