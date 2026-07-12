# API Automation Framework (Pytest)

[![CI](https://github.com/nilima-satapathy/api-automation-pytest/actions/workflows/ci.yml/badge.svg)](https://github.com/nilima-satapathy/api-automation-pytest/actions/workflows/ci.yml)
[![Project](https://img.shields.io/badge/Project-01-1F4E79)](https://github.com/nilima-satapathy/ai-career-journey)
[![Milestones](https://img.shields.io/badge/Milestones-M1–M7%20done-2ea44f)](./MILESTONES.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Pytest-9-yellow)](https://pytest.org/)

Maintainable **REST API test automation** using Python, Pytest, and a thin `ApiClient` wrapper.

Part of my AI / SDET transition portfolio → **[ai-career-journey](https://github.com/nilima-satapathy/ai-career-journey)**

| | |
|--|--|
| **Target API** | [JSONPlaceholder](https://jsonplaceholder.typicode.com) (free, no auth) |
| **Status** | Milestone 7 complete — HTML reports + GitHub Actions CI |
| **Next** | Milestone 8 — README polish + portfolio screenshots |
| **Tests** | 77 automated cases (GET, write, schema, negative) |

---

## Why this project

Shows SDET fundamentals: reusable client, fixtures, data-driven tests, write ops with payloads, JSON Schema contracts, negative cases, HTML reporting, and **CI on every push**.  
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
# Terminal output only
pytest

# With self-contained HTML report (opens in any browser)
mkdir reports -Force
pytest --html=reports/report.html --self-contained-html
```

Optional base URL override:

```powershell
$env:API_BASE_URL = "https://jsonplaceholder.typicode.com"
pytest
```

Open `reports/report.html` after a run to share pass/fail details with teammates or recruiters.

---

## CI (GitHub Actions)

On every **push** and **pull request** to `main`:

1. Install dependencies  
2. Run the full Pytest suite against JSONPlaceholder  
3. Upload **`pytest-html-report`** as a downloadable artifact  

Workflow file: [`.github/workflows/ci.yml`](./.github/workflows/ci.yml)

Badge at the top of this README reflects the latest CI status.

---

## Structure

```
api-automation-pytest/
├── .github/workflows/ci.yml   # GitHub Actions CI (M7)
├── MILESTONES.md
├── README.md
├── requirements.txt
├── pytest.ini
├── tests/
│   ├── conftest.py
│   ├── test_users_get.py
│   ├── test_users_write.py
│   ├── test_schema_validation.py
│   └── test_negative.py
├── utils/
│   ├── api_client.py
│   ├── payload_loader.py
│   └── schema_loader.py
└── data/
    ├── schemas/
    └── payloads/
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
| 6 | Negative tests | ✅ Done |
| 7 | pytest-html + GitHub Actions | ✅ Done |
| 8 | README polish | ⬜ Next |

---

## Interview talking points (so far)

1. **ApiClient** keeps base URL, headers, and timeout in one place (DRY).
2. **Fixtures** separate setup/teardown from assertions.
3. Assert on **status + body shape + business rules**, not status alone.
4. **Parametrize** = one test body, many data rows (data-driven).
5. **Payloads in JSON files** keep request data out of test code.
6. **JSON Schema** = reusable contract; catches missing fields / wrong types early.
7. **Negative tests** prove 404 / empty results / error paths — not only happy path.
8. **CI + HTML report** = green check on every push and a shareable evidence artifact.
