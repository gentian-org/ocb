# Customizations carried in this fork

This repo is a rung-**L6** fork (see [`UPSTREAM`](UPSTREAM) and
[gentian-os/docs/app-customization.md §2.7](https://github.com/gentian-org/gentian-os/blob/main/docs/app-customization.md)).
Every delta against pinned upstream is listed here with the same fields a Debian
DEP-3 patch header or a Gentian `Customization` record would carry, whether the
delta is implemented as a literal patch (`patches/`) or a pattern-based script
(regex transformations survive small upstream reshuffles better than line-numbered
diffs — see [`patches/README.md`](patches/README.md) for why both forms are used).

**Owner of this whole fork:** `platform-erp` · **CVE watch:** yes — track
[OCA/OCB security advisories](https://github.com/OCA/OCB/security) and Odoo's own
release notes for the pinned `19.0` branch.

---

## 1. Enterprise reference cleanup

**Where:** `cleanup_enterprise.py`, `Dockerfile` (the two `sed` lines removing
`WorkIntervals`/`hr_work_entry_contract` references, and the manifest-category
`sed` block).

**Description:** OCB ships references to Enterprise-only module categories and a
few Enterprise-only imports that raise `ModuleNotFoundError` in a Community-only
build. This removes those references — Enterprise *records*, category tags on
manifests, and one import — so the build stays a coherent Community-only tree
instead of one with dangling references to modules that were never installed.

**Author:** platform-erp
**Origin:** Gentian-specific — OCB does not ship a Community-only build variant.
**Bug-Upstream:** none filed
**Forwarded:** not-needed — OCA/OCB's stated scope includes Enterprise-adjacent
metadata; a Community-only strip is a Gentian distribution choice, not a defect.
**Applied-Upstream:** no
**Last-Update:** 2026-08-06
**Review by:** 2027-02-06

**Licensing effect:** none. This *removes* references and advertising for
functionality the build cannot run — it does not unlock, bypass, or crack any
licensed capability. See the absolute prohibition on licensing bypass in
`gentian-apps/docs/app-profile-guide.md`.

---

## 2. Enterprise module removal

**Where:** `Dockerfile` (the `rm -rf hr_work_entry* hr_contract* ...` block).

**Description:** Deletes addon directories that hard-depend on Enterprise modules
and would otherwise fail to load or register broken menu entries in a
Community-only install.

**Author:** platform-erp
**Origin:** Gentian-specific
**Bug-Upstream:** none filed
**Forwarded:** not-needed — same rationale as above.
**Applied-Upstream:** no
**Last-Update:** 2026-08-06
**Review by:** 2027-02-06

**Exit criteria for both #1 and #2:** drop if/when OCA/OCB ships an official
Community-only build profile, or if Gentian's catalogue starts offering an
Enterprise edition (see `gentian-apps/profiles/odoo-cb-base/customization.md`,
which documents the corresponding `hide_enterprise_modules` addon at rung L3 —
that addon and this repo's build-time removal are two layers of the same
distribution decision and should be reviewed together).

---

## Verifying this list is current

CI (`patches/series` gate) checks that any literal patches still apply cleanly
against the pinned `UPSTREAM` tag on every build. The pattern-based
transformations above are checked by the build itself failing loudly if their
target files or patterns no longer exist (see the "Validate Enterprise reference
removal" step in the Dockerfile) — a script that silently matches nothing is a
signal upstream has already changed shape, at which point this table needs review,
not more permissive matching.
