# Project 1 — Milestone log

Repo: **api-automation-pytest**  
Goal: Maintainable API test automation (Python + Pytest) for SDET / AI Test portfolio.

| Milestone | Title | Status | Date | Git tag |
|-----------|--------|--------|------|---------|
| M1 | Structure + `ApiClient` + 3 GET tests | ✅ Done | 2026-07-12 | `milestone-1` |
| M2 | Shared fixtures (`base_url`, `headers`, `api_client`) | ✅ Done | 2026-07-12 | `milestone-2` |
| M3 | Full GET coverage + parametrize | ✅ Done | 2026-07-12 | `milestone-3` |
| M4 | POST / PUT / DELETE + payloads | ✅ Done | 2026-07-12 | `milestone-4` |
| M5 | Schema validation | ✅ Done | 2026-07-12 | `milestone-5` |
| M6 | Negative tests | ✅ Done | 2026-07-12 | `milestone-6` |
| M7 | pytest-html + GitHub Actions CI | ✅ Done | 2026-07-12 | `milestone-7` |
| M8 | README polish + portfolio screenshots | ✅ Done | 2026-07-12 | `milestone-8` |

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
   https://github.com/nilima-satapathy/ai-career-journey  
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

### M3 — Full GET + parametrize
- Expanded GET coverage: users, posts, comments, todos, albums
- Nested routes: `/users/{id}/posts`, `/posts/{id}/comments`
- Query filters: `?userId=`, `?postId=`
- `@pytest.mark.parametrize` turns one function into many cases (33 GET tests)
- Learning: same assertions + different data = data-driven tests (no copy-paste)

### M4 — POST / PUT / PATCH / DELETE + payloads
- `ApiClient` methods: `post`, `put`, `patch`, `delete`
- Request bodies live in `data/payloads/*.json` (not hard-coded in tests)
- `utils/payload_loader.py` loads JSON files
- Write tests in `tests/test_users_write.py` (12 cases) → **45 tests total**
- Learning: CRUD = Create / Read / Update / Delete; keep data separate from code

### M5 — Schema validation
- JSON Schemas in `data/schemas/` (user, post, comment, todo, album + list shapes)
- `utils/schema_loader.py`: `load_schema` + `validate_schema` (jsonschema Draft 7)
- `tests/test_schema_validation.py` — 12 cases; suite total **57 tests**
- Dependency: `jsonschema>=4.20.0`
- Learning: status code ≠ contract; schemas catch missing fields / wrong types

### M6 — Negative tests
- `tests/test_negative.py` — 404s, empty filters, nested missing parents, write edge cases
- Distinguishes **404 (missing resource)** vs **200 + [] (valid query, no rows)**
- Documents JSONPlaceholder quirks (PUT unknown → 500, empty POST still 201)
- Learning: real quality = happy path + unhappy path; lock the contract you observe

### M7 — pytest-html + GitHub Actions CI
- Dependency: `pytest-html` — local report: `pytest --html=reports/report.html --self-contained-html`
- Workflow: `.github/workflows/ci.yml` runs suite on push/PR to `main`
- Uploads `reports/report.html` as a CI artifact (available even if tests fail)
- `.gitignore` ignores `reports/`, `.venv/`, caches
- Learning: CI = tests run on GitHub without opening your laptop; report = shareable proof

### M8 — README polish + portfolio assets
- Recruiter-ready README: quick start, features table, interview points, design choices
- Portfolio diagrams in `docs/assets/` (architecture, sample run, CI flow) — SVG for crisp text
- Project marked complete (M1–M8); suite **77** tests + green CI badge
- Learning: README is the product page for your code — structure, proof, and how to run
