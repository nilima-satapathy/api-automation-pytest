# API Automation Framework (Pytest)

[![Project](https://img.shields.io/badge/Project-01-1F4E79)](https://github.com/nilima-satapathy/ai-career-journey)
[![Milestones](https://img.shields.io/badge/Milestones-M1–M4%20done-2ea44f)](./MILESTONES.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-9-yellow)](https://pytest.org/)

Maintainable **REST API test automation** using Python, Pytest, and a thin `ApiClient` wrapper.

Part of my AI / SDET transition portfolio → **[ai-career-journey](https://github.com/nilima-satapathy/ai-career-journey)**

| | |
|--|--|
| **Target API** | [JSONPlaceholder](https://jsonplaceholder.typicode.com) (free, no auth) |
| **Status** | Milestone 4 complete — 45 tests (GET + write ops) green |
| **Next** | Milestone 5 — schema validation |

---

## Why this project

Shows SDET fundamentals: reusable client, fixtures, data-driven tests, write ops with payloads, and (soon) CI.  
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
│   ├── test_users_get.py      # GET tests (parametrize → 33 cases)
│   └── test_users_write.py    # POST/PUT/PATCH/DELETE (12 cases)
├── utils/
│   ├── api_client.py          # HTTP helper (GET + write methods)
│   └── payload_loader.py      # load JSON from data/payloads/
└── data/
    ├── schemas/               # M5
    └── payloads/              # request bodies for write tests
```

---

## Milestone status

See **[MILESTONES.md](./MILESTONES.md)** for the full checklist and how I tag each milestone on Git.

| # | Milestone | Status |
|---|-----------|--------|
| 1 | Structure + api_client + 3 GET tests | ✅ Done |
| 2 | Fixtures in conftest | ✅ Done |
| 3 | Full GET + parametrize | ✅ Done (33 GET tests) |
| 4 | POST/PUT/DELETE + payloads | ✅ Done (45 tests total) |
| 5 | Schema validation | ⬜ Next |
| 6 | Negative tests | ⬜ |
| 7 | pytest-html + GitHub Actions | ⬜ |
| 8 | README polish | ⬜ |

---

## Interview talking points (so far)

1. **ApiClient** keeps base URL, headers, and timeout in one place (DRY).
2. **Fixtures** separate setup/teardown from assertions.
3. Assert on **status + body shape + business rules**, not status alone.
4. **Parametrize** = one test body, many data rows (data-driven).
5. **Payloads in JSON files** keep request data out of test code; easier to maintain and review.
