# podpack demo

A [podpack](https://github.com/holdenweb/podpack) site whose only job is to be a
worked example: it installs [podpack-notes](https://github.com/holdenweb/podpack-notes)
from that app's own repository, which is the one thing podpack's repository
cannot demonstrate. podpack is a framework and installs no app; installing apps
is what a *site* is for.

It was built by following podpack's `creating-a-site.md` step by step rather
than by copying podpack — so if the guide stops working, this stops building,
which is the point.

```bash
./scripts/prepare-host-dirs.sh && ./scripts/up.sh
```

Then <http://localhost:8459/> — the site, with `/notes/` wearing its chrome.
Ports are 8459 and 5434, clear of podpack's own lab on 8458/5433, so both can
run at once.

## What is worth looking at

| | |
| --- | --- |
| `pyproject.toml` | both packages, from git. An app does not pull in its framework, so a site names both. |
| `config/app.toml` | `apps = ["podpack_notes"]` — the import name — and `[apps.notes]`, keyed by the app's own name |
| `src/podpack_demo/templates/base.html` | the site's chrome, which the installed app extends without knowing whose it is |
| `alembic/versions/` | this site's own history. The migration creating the notes table was **generated here**, not copied: a migration history belongs to the site, not to the app. |

Local development, without containers, is in podpack's `creating-a-site.md`.
The one trap worth repeating: use an **absolute** SQLite path, because
Flask-SQLAlchemy resolves a relative one against the instance folder while
alembic resolves it against the working directory, and migrations then appear to
succeed against a different file from the one the site reads.
