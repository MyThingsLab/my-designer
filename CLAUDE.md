# my-designer — agent instructions

You are developing **my-designer**, a MyThingsLab My[X] tool.

**Inherited rules:** obey [`./HARNESS.md`](./HARNESS.md) in full — the vendored
MyThingsLab build-harness rules. Do not restate or override them. Anything not
covered here defers to `HARNESS.md`, then `my-things-core/docs/CONVENTIONS.md`.

## This tool

- **Purpose:** given a design brief filed as an issue, produces a self-contained
  static HTML/CSS mockup as a draft PR — the fleet's prototyping tool for the
  ecosystem's web presence (the dashboard hub, per-tool web apps), so a look can
  be iterated and reviewed before anyone wires it into a real app.
- **The single Engine call:** "write a self-contained HTML+inline-CSS mockup
  implementing this design brief."
- **Invariants / rules:** output always lands in this repo's own `mockups/`
  directory — this tool never touches another tool's repo. Every mockup is
  static (inline CSS, no JS wired to real APIs or data, no secrets) — a
  prototype, not production code. This tool decides how something should look,
  never what to build; turning an approved mockup into real code in a target
  tool's repo is a separate, human-triggered step.
- **Backlog label:** `my-designer`

## Testing

Fakes come from `mythings.testing` (opt-in via `pytest_plugins` in
`tests/conftest.py`; see `my-things-core/docs/CONVENTIONS.md`, "Shared test
fixtures"). Never copy fixture code into a conftest — only domain-specific
helpers live there.
