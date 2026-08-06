# ocb — Odoo Community Backports for Gentian OS

Builds a pure Community-only Odoo image (rung **L6** of the Gentian customization
ladder — see [`UPSTREAM`](UPSTREAM), [`CUSTOMIZATIONS.md`](CUSTOMIZATIONS.md), and
[gentian-os/docs/app-customization.md](https://github.com/gentian-org/gentian-os/blob/main/docs/app-customization.md))
for `gentian-apps/charts/odoo`.

**Before adding a new delta here**, check whether it can land at a cheaper rung
instead — an Odoo addon in
[`odoo-modules`](https://github.com/gentian-org/odoo-modules) (L3) survives
upgrades this repo cannot. Only source-level changes belong here.

Every existing deviation from pinned upstream is documented in
[`CUSTOMIZATIONS.md`](CUSTOMIZATIONS.md) with an owner, an upstream-first outcome,
and a review date. `patches/series` (empty by default — see
[`patches/README.md`](patches/README.md)) is validated against pinned upstream on
every CI run; a series that no longer applies fails the build on purpose.

## Usage

- Build the Docker image: `docker build -t ghcr.io/brandli/my_image:latest .` (replace "my_image" with the name of your branch)
- Make sure you are logged into github
- Push to github: `docker push ghcr.io/brandli/my_image:latest`