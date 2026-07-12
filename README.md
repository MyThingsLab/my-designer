# my-designer

[![CI](https://github.com/MyThingsLab/my-designer/actions/workflows/ci.yml/badge.svg)](https://github.com/MyThingsLab/my-designer/actions/workflows/ci.yml) [![codecov](https://codecov.io/gh/MyThingsLab/my-designer/branch/main/graph/badge.svg)](https://codecov.io/gh/MyThingsLab/my-designer) ![Python](https://img.shields.io/badge/python-3.11%2B-blue) [![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A [MyThingsLab](../my-things-core) `My[X]` tool: the fleet's prototyping tool
for the ecosystem's web presence. Given a design brief filed as a labeled
issue, it drafts one self-contained HTML/CSS mockup as a draft PR — a look to
review and iterate on before anyone wires it into a real app.

```bash
mydesigner run --engine noop   # or: python -m mydesigner run
```

is a safe end-to-end dry run: zero tokens, no branch, no PR, one honest
ledger entry (a blank Engine reply is a no-op, same as every other harness
tool in the fleet).

## How it works

The harness loop in `tool.py` is fixed (read one labeled issue →
deterministic pre-work → one Engine call → apply inside an isolated
`Workspace` → draft PR, Policy-gated and ledgered); the judgment lives in
`src/mydesigner/mockup.py`:

- `build_prompt` — the issue title + body become the design brief.
- The single Engine call drafts one self-contained HTML page (inline CSS,
  no JS, no live data — see `SYSTEM` in `mockup.py` for the full brief).
- `finish` degrades a blank reply to a no-op; otherwise the mockup lands at
  `mockups/<slug-of-the-issue-title>.html`.

## Install (development)

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ../my-things-core -e ".[dev]"
pytest
```

## License

MIT — see [`LICENSE`](LICENSE).
