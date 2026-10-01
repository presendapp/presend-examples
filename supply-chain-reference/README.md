# Supply-chain checks: reference code and test sets

Snapshot (2026-09-27) of the code behind Presend's `typosquat-check` and `maintainer-change-check` endpoints, and of the test sets used to measure them. It is kept here so that the measurements quoted in public discussions can be reproduced.

**Frozen copy: it is not updated.** The current code and tests are in [presend-source](https://github.com/presendapp/presend-source) (`functions/api/typosquat-check.js`, `functions/api/maintainer-change-check.js`, `tests/typosquat/`, `tests/maintainer-change/`), and the latest measurements are on [presend.pages.dev/measurements](https://presend.pages.dev/measurements).

- `functions/api/typosquat-check.js`, `functions/api/maintainer-change-check.js`: endpoint code.
- `tests/typosquat/fixtures.json`: legitimate packages, known typosquats, and names that are flagged on purpose after review.
- `tests/typosquat/run.mjs` (offline), `tests/typosquat/top-pypi.mjs` (top 15,000 PyPI packages) and `tests/typosquat/top-npm.mjs` (npm-high-impact): run them with Node from this folder, e.g. `node tests/typosquat/run.mjs`.
