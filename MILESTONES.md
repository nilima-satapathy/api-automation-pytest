# Project 1 — Milestone log

Repo: **api-automation-pytest**  
Goal: Maintainable API test automation (Python + Pytest) for SDET / AI Test portfolio.

| Milestone | Title | Status | Date | Git tag |
|-----------|--------|--------|------|---------|
| M1 | Structure + `ApiClient` + 3 GET tests | ✅ Done | 2026-07-12 | `milestone-1` |
| M2 | Shared fixtures (`base_url`, `headers`, `api_client`) | ✅ Done | 2026-07-12 | `milestone-2` |
| M3 | Full GET coverage + parametrize | ⬜ Pending | | |
| M4 | POST / PUT / DELETE + payloads | ⬜ Pending | | |
| M5 | Schema validation | ⬜ Pending | | |
| M6 | Negative tests | ⬜ Pending | | |
| M7 | pytest-html + GitHub Actions CI | ⬜ Pending | | |
| M8 | README polish + portfolio screenshots | ⬜ Pending | | |

---

## How I log a milestone (copy this every time)

1. Finish the code and run `pytest` (all green).
2. Update this file: status → Done, add date.
3. Commit:

```powershell
git add -A
git commit -m "feat(mX): short description of what shipped"
git tag -a milestone-X -m "Project 1 Milestone X complete"
git push origin main --tags
```

4. Update the central tracker:  
   https://github.com/satnil2608-glitch/ai-career-journey  
   (edit `PROGRESS.md` and tick the box)

---

## Milestone notes

### M1 — Structure + client + 3 GETs
- Scaffolded project under `Desktop/Code/api-automation-pytest`
- `ApiClient` wraps `requests` for GET
- 3 tests against JSONPlaceholder (reqres.in requires API key)
- Learning: separate “how we call API” from “what we assert”

### M2 — Fixtures
- `conftest.py`: `base_url`, `default_headers`, `api_client`
- Tests only assert; fixture creates/closes client
- Optional override: env var `API_BASE_URL`
- Learning: Pytest fixtures = shared setup (like test preconditions in one place)
