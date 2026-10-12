# UI Automation Tests by Vitaly Miller

[![UI tests](https://github.com/Vitaly-Miller/autotests-ui-playwright/actions/workflows/tests.yml/badge.svg)](https://github.com/Vitaly-Miller/autotests-ui-playwright/actions/workflows/tests.yml)

Automated end-to-end UI tests for the [Web Application](https://nikita-filonov.github.io/qa-automation-engineer-ui-course/) —
a web application with registration, login, dashboard, courses and exercises.

Built with: **Python**, **Playwright**, **Pytest**, **Pydantic**, **Allure** and **Faker**.

---
- <picture><img src="https://allurereport.org/svg/logo-report-sign.svg" height="16" alt=""></picture> [My Allure Report](https://vitaly-miller.github.io/autotests-ui-playwright/) — test results with history, video and Playwright traces, published on GitHub Pages
- <picture><img src="https://playwright.dev/img/playwright-logo.svg" height="16" alt=""></picture> [Application Under Test](https://nikita-filonov.github.io/qa-automation-engineer-ui-course/) — the web app the tests run against
---

> **⚠️ A note on code comments.**  
> The code is deliberately annotated in detail — nearly every line
> carries a comment explaining what it does and why. This is an intentional choice for
> a portfolio project: it lets a reviewer follow every implementation decision without leaving the
> file. In production code I would keep comments far more sparing, reserving them for non-obvious
> constraints and decisions.

---
## ✨ Highlights

### 🏗️ Architecture
- **Page Object Model with three layers** — Pages are composed of reusable Components
  (navbar, sidebar, forms, toolbars, widgets), and Components are built from typed Elements
  (`Button`, `InputField`, `InputFile`, `Link`, `Text`, `Icon`, `Image`)
- **Element layer** — every action and check is wrapped in an Allure step, logged, and fails with
  a readable error message that points to the exact place on the page (`❌ Create course page > Image upload widget > [Remove image button] - visible!`)
- **Stable locators** — elements are located by `data-testid` attributes
- **Authentication via Storage State** — a new user is registered once per session through the UI;
  the authorized state is reused by every test that needs a logged-in user
- **Typed settings** loaded from `.env` via `pydantic-settings` (base URL, browsers, headless, slow-mo, test user)
- **Fake data generation** with Faker — a unique test user for every run

### 📋 Reporting & Observability
- **Allure reporting** with epics / features / stories, tags, severity and run history, published on GitHub Pages
- **Video recording** of every test, attached to the Allure Report
- **Playwright Tracing** (screenshots, DOM snapshots, sources) — a `trace.zip` attached to every test,
  ready to open in the Playwright Trace Viewer
- **Environment info** — OS, Python, browser, run mode and base URL are shown on the Allure *Environment* tab
- **Logging** — every page, component and element action is logged via a custom logger

### 🧪 Test Design
- **Cross-browser** — Chromium, Firefox and WebKit; browsers are selected in `.env`
  and every test is parametrized by them automatically
- **Markers** by type (`regression`, `negative`, `e2e`, `ui`) and by domain (`auth`, `login`, `registration`, `dashboard`, `courses`, `files`)
- **Parametrized negative tests** — e.g. several invalid credential sets in one login test
- **Parallel execution** (pytest-xdist) and **automatic reruns** of flaky tests (pytest-rerunfailures)

### ♾️ CI/CD
- **GitHub Actions pipeline** — installs Playwright browsers, runs the full suite in headless mode
  in parallel, and publishes the Allure Report to GitHub Pages with history preserved between runs

---

## Project Structure

```
├─ 📁 .github/       # CI/CD workflow (GitHub Actions)
├─ 📁 pages/         # Page Objects: auth (login, registration), dashboard, courses
├─ 📁 components/    # Reusable page components: navbar, sidebar, forms, toolbars, widgets, views
├─ 📁 elements/      # Typed UI elements with Allure steps, logging and checks
├─ 📁 fixtures/      # Pytest fixtures (browsers & storage state, pages, Allure environment)
├─ 📁 tests/         # Test suites grouped by domain: auth, dashboard, courses
├─ 📁 tools/         # Allure annotations, Playwright helpers, data generator, logger
├─ 📁 testdata/      # Static test data (e.g. images for upload tests)
├─ config.py         # Typed settings loaded from .env via pydantic-settings
├─ conftest.py       # Root fixtures (via Pytest Plugins)
└─ pytest.ini        # Pytest configuration and markers
```
---
## Getting Started


### ⤵️ Clone the Repository

```bash
git clone https://github.com/Vitaly-Miller/autotests-ui-playwright.git
cd autotests-ui-playwright
```

### 🔘 Create a Virtual Environment

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 🔀 Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

### ⚙️ Configure the Run

All run settings live in [`.env`](.env) and are loaded through `pydantic-settings` (see `config.py`):

```dotenv
BASE_URL=https://nikita-filonov.github.io/qa-automation-engineer-ui-course/
BROWSER=["chromium"]                  # or ["chromium","firefox","webkit"]
HEADLESS=True                         # False — watch the browser
SLOW_MO=0                             # delay between actions, ms
```

Environment variables take precedence over `.env`, e.g. `HEADLESS=false python -m pytest`.

## 🚀️ Running the Tests

### Run the full suite with Allure results:

```bash
python -m pytest --alluredir=allure-results --clean-alluredir
```

### Selective Runs with Markers:

Tests are tagged by type (`regression`, `negative`, `e2e`, `ui`) and by domain
(`auth`, `login`, `registration`, `dashboard`, `courses`, `files`):

```bash
python -m pytest -m negative               # negative tests only
python -m pytest -m "regression and auth"  # regression tests for the auth domain
```

### Parallel Execution & Reruns:

```bash
python -m pytest -n auto          # run in parallel (pytest-xdist)
python -m pytest --reruns 2       # retry flaky tests (pytest-rerunfailures)
```

## 📋 Reports

### <picture><img src="https://allurereport.org/svg/logo-report-sign.svg" height="16"></picture> Allure Report

```bash
allure serve allure-results
```

Opens an interactive report in your browser. Each test includes step-by-step execution details
(every page, component and element action is a separate step) and attachments added automatically
in the fixture teardown:

- **video** recording of the test;
- **Playwright trace** (`.zip`) with screenshots, DOM snapshots and sources;
- the captured **log** of all actions and checks during the test.

### <picture><img src="https://playwright.dev/img/playwright-logo.svg" height="16" alt=""></picture> Playwright Trace Viewer

```bash
playwright show-trace tracing/<test_name>.zip
```

Replays the test step by step: actions, DOM snapshots before/after each action, console and network.
A trace downloaded from the Allure Report can also be opened at [trace.playwright.dev](https://trace.playwright.dev).

## <picture><img src="https://innovationspace.ansys.com/knowledge/wp-content/uploads/sites/4/2024/02/scade-009-ci-cd-workflow.svg"  height="16"></picture> CI/CD 

Every push and pull request to `main` triggers the [GitHub Actions pipeline](.github/workflows/tests.yml):

1. **run-tests** — installs dependencies and Playwright browsers, runs the full test suite
   in headless mode in 2 parallel workers and uploads the Allure results as an artifact;
2. **publish-report** — builds the Allure report with run history and deploys it
   to [GitHub Pages](https://vitaly-miller.github.io/autotests-ui-playwright/)
   (runs even if tests fail, so failures are always visible in the report).
