# Patches (customization ladder rung L5, within an L6 fork)

This repository is already a rung-**L6** fork of Odoo (via OCA/OCB) — see
[`UPSTREAM`](../UPSTREAM) for the pinned source and
[gentian-os/docs/app-customization.md §2.7](https://github.com/gentian-org/gentian-os/blob/main/docs/app-customization.md).
Even inside a fork, individual deltas should still be tracked with L5 (patch)
discipline: pristine-upstream + an ordered, documented series, modelled on Debian's
`3.0 (quilt)` format. That discipline is what makes a fork *auditable* rather than
an opaque diff nobody can explain years later.

## Two kinds of delta live in this repo

1. **Byte-level patches** — small, mechanical changes. Belong in `series` as real
   unified diffs.
2. **Pattern-based transformations** — the Enterprise-cleanup logic in
   [`../cleanup_enterprise.py`](../cleanup_enterprise.py) and the `sed`/`rm`
   commands in the `Dockerfile`. These stay as scripts rather than literal diffs
   *deliberately*: they regex-match across many files and survive small upstream
   reshuffles that would break a line-numbered patch. Being a script instead of a
   `.patch` file does not exempt them from DEP-3 discipline — see
   [`../CUSTOMIZATIONS.md`](../CUSTOMIZATIONS.md), which documents each one with
   the same fields a patch header would carry.

## `series` is empty by default

A non-empty `series` is a real deviation and a debt signal, exactly as it is
upstream in `gentian-apps`. Add a patch here only when a change is small and
line-based enough that a diff is the more maintainable form than a script.

## Adding a patch

```
patches/
├── series                       # ordered list, one filename per line
└── 0001-short-description.patch
```

Every patch carries DEP-3 headers:

```
Description: <what this changes and why>
Author: <team@gentian.org>
Origin: other, <url, if applicable>
Bug-Upstream: <upstream issue url, if filed>
Forwarded: <url | no | not-needed>
Applied-Upstream: no
Last-Update: <YYYY-MM-DD>
```

`Forwarded: no` requires a written reason. CI applies `series` against the pinned
`UPSTREAM` commit on every build and **fails if any patch does not apply cleanly**
— that failure is the point: it forces someone to look at the delta instead of
silently drifting out of sync with upstream.

## Rules

- Never patch to bypass license validation or unlock features gated behind a
  commercial license.
- Every patch (and every script-based transformation in `CUSTOMIZATIONS.md`) needs
  an owner and a review date.
- Prefer upstreaming. `Forwarded:` is not decoration.
