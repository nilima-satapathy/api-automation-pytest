# API Automation Framework (Pytest)

[![Project](https://img.shields.io/badge/Project-01-1F4E79)](https://github.com/nilima-satapathy/ai-career-journey)
[![Milestones](https://img.shields.io/badge/Milestones-M1–M6%20done-2ea44f)](./MILESTONES.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-9-yellow)](https://pytest.org/)

Maintainable **REST API test automation** using Python, Pytest, and a thin `ApiClient` wrapper.

Part of my AI / SDET transition portfolio → **[ai-career-journey](https://github.com/nilima-satapathy/ai-career-journey)**

| | |
|--|--|
| **Target API** | [JSONPlaceholder](https://jsonplaceholder.typicode.com) (free, no auth) |
| **Status** | Milestone 6 complete — 77 tests (negative + edge cases) green |
| **Next** | Milestone 7 — pytest-html + GitHub Actions CI |

---

## Why this project

Shows SDET fundamentals: reusable client, fixtures, data-driven tests, write ops with payloads, JSON Schema contracts, negative cases, and (next) CI.  
Builds the base for later **LLM API testing** in my AI Test Engineer path.

---

## Setup (Windows)

```powershell
git clone https://github.com/nilima-satapathy/api-automation-pytest.git
cd api-automation-pytest
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run tests

```powershell
pytest
```

Optional base URL override:

```powershell
$env:API_BASE_URL = "https://jsonplaceholder.typicode.com"
pytest
```

---

## Structure

```
api-automation-pytest/
├── MILESTONES.md              # progress log for this repo
├── README.md
├── requirements.txt
├── pytest.ini
├── tests/
│   ├── conftest.py            # fixtures: base_url, headers, api_client
│   ├── test_users_get.py      # GET tests (parametrize)
│   ├── test_users_write.py    # POST/PUT/PATCH/DELETE
│   ├── test_schema_validation.py  # JSON Schema contract checks
│   └── test_negative.py       # 404s, empty filters, write edge cases
├── utils/
│   ├── api_client.py          # HTTP helper (GET + write methods)
│   ├── payload_loader.py      # load JSON from data/payloads/
│   └── schema_loader.py       # load + validate JSON Schema
└── data/
    ├── schemas/               # response contracts
    └── payloads/              # request bodies for write tests
```

---

## Milestone status

See **[MILESTONES.md](./MILESTONES.md)** for the full checklist and how I tag each milestone on Git.

| # | Milestone | Status |
|---|-----------|--------|
| 1 | Structure + api_client + 3 GET tests | ✅ Done |
| 2 | Fixtures in conftest | ✅ Done |
| 3 | Full GET + parametrize | ✅ Done |
| 4 | POST/PUT/DELETE + payloads | ✅ Done |
| 5 | Schema validation | ✅ Done |
| 6 | Negative tests | ✅ Done (77 tests total) |
| 7 | pytest-html + GitHub Actions | ⬜ Next |
| 8 | README polish | ⬜ |

---

## Interview talking points (so far)

1. **ApiClient** keeps base URL, headers, and timeout in one place (DRY).
2. **Fixtures** separate setup/teardown from assertions.
3. Assert on **status + body shape + business rules**, not status alone.
4. **Parametrize** = one test body, many data rows (data-driven).
5. **Payloads in JSON files** keep request data out of test code.
6. **JSON Schema** = reusable contract; catches missing fields / wrong types early.
7. **Negative tests** prove 404 / empty results / error paths — not only happy path.
