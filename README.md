# QA-portfolio

A **commercially credible QA portfolio** demonstrating practical **UI, API, SQL/data and dashboard validation** built in **PyCharm** using **Python, Playwright, pytest, SQLite, Allure and GitHub Actions**.

This repository is designed to show more than isolated browser checks. It demonstrates how I apply **hands-on testing, test assurance, risk-based thinking, stakeholder visibility and release-readiness judgement** in a practical way, while building confidence with modern tooling.

It is intentionally positioned for the kind of work I do and want to keep doing:

- **Senior Manual QA**
- **Workstream Test Lead (hands-on)**
- **Test Assurance / Release Readiness**
- **Quality visibility and stakeholder-facing reporting**

The aim is **not** to present as a senior SDET or framework specialist. The aim is to show a realistic portfolio for an assurance-led QA professional adding modern tooling in a commercially grounded way.

---

## What value this portfolio is intended to demonstrate

This project is meant to show that I can contribute value across more than one QA layer:

- **hands-on functional testing** across UI and API layers
- **risk-based coverage** focused on meaningful user, data and reporting risks
- **data / dashboard validation** rather than UI-only automation
- **failure evidence and reviewability** through screenshots, trace, video and Allure attachments
- **traceability thinking** linking requirements, tests and evidence
- **stakeholder-facing assurance outputs** rather than raw execution alone
- **AI-assisted but human-controlled QA workflow** with review, judgement and validation kept human-led

That combination is closer to the real value I bring in delivery environments: **test assurance, stakeholder reporting, quality visibility and release confidence**, while still being comfortable doing the testing work itself.

---

## At a glance

- **Primary focus:** practical QA automation with commercially realistic scope
- **UI target:** Sauce Demo
- **API target:** JSONPlaceholder
- **Data target:** local SQLite dataset for reporting-style validation
- **Test types shown:** UI, API, smoke, responsive/mobile, negative and data/report validation
- **Evidence shown:** Playwright trace/video/screenshots plus Allure reporting
- **Execution modes:** headed locally, headless in CI
- **Portfolio goal:** demonstrate maintainable test design, assurance thinking, evidence capture and stakeholder-friendly QA communication
- **Published execution report:** [GitHub Pages-hosted Allure report](https://brent-nancarrow.github.io/QA-portfolio/)

---

## Tech stack and versions

The key runtime and framework versions are listed below so the portfolio is easier to reproduce and assess.

| Component | Version / note |
|---|---|
| Python | **3.13** (GitHub Actions workflow) |
| Playwright | **1.58.0** |
| pytest | **9.0.2** |
| pytest-playwright | **0.7.2** |
| allure-pytest | **2.15.3** |
| SQLite | used for local SQL-backed validation |
| IDE | developed locally in **PyCharm** on **Windows 11** |
| CI | **GitHub Actions** |

> I have included versions for the main runtime and test frameworks because they are useful for reproducibility. I have not tried to version every possible local tool, because that would add noise rather than value.

---

## What this project demonstrates

### Testing capability
- UI smoke and functional checks using Playwright
- API validation using Playwright API request support with pytest
- SQL-backed data quality and report validation using SQLite
- responsive/mobile viewport coverage
- negative-path coverage in both API and data validation

### Test design and maintainability
- Page Object Model structure for cleaner UI tests
- shared config, reusable test data and helper utilities
- selective execution using pytest markers
- local vs CI execution handled in a practical way

### Evidence and reporting
- Playwright trace, screenshots and video on failure
- Allure titles, steps and attachments for reviewable execution evidence
- CI artifact retention in GitHub Actions
- documentation that explains how tests, evidence and assurance outputs fit together

### Assurance and stakeholder value
- stakeholder-facing assurance artefacts
- traceability from requirement to test and evidence
- coverage and gaps visibility rather than pretending everything is covered
- release-readiness style communication and confidence statements

### Modern workflow awareness
- AI-assisted QA workflow pack showing controlled, review-led use of GenAI
- explicit positioning that AI is used to **support** QA, not replace evidence-led judgement

---

## Quick portfolio navigation

If you are reviewing this repository for interview or hiring purposes, these are the most useful places to start:

- **`tests/ui/`** → browser-based UI coverage
- **`tests/api/`** → API validation examples
- **`tests/data/`** → SQL-backed reporting and dashboard validation
- **`docs/stakeholder-assurance-pack/`** → stakeholder-facing assurance artefacts
- **`docs/traceability-pack/`** → requirement-to-test mapping and coverage visibility
- **`docs/ai-assisted-qa-workflow/`** → practical AI-assisted QA workflow examples
- **GitHub Actions + GitHub Pages** → CI execution evidence and published Allure report output

---

## Public test targets

### UI
- Sauce Demo

### API
- JSONPlaceholder

These public targets were chosen because they are safe, accessible and suitable for portfolio demonstration work.

---

## Project structure

```text
QA-portfolio/
├── .github/
│   └── workflows/
│       └── playwright.yml
├── assets/
│   ├── reporting/
│   │   └── orders_dashboard.html
│   └── screenshots/
├── config/
│   └── settings.py
├── data/
│   ├── reporting/
│   │   ├── dashboard_expected.json
│   │   ├── dashboard_export.json
│   │   ├── orders_schema.sql
│   │   └── orders_seed.sql
│   └── users.py
├── docs/
│   ├── ai-assisted-qa-workflow/
│   ├── stakeholder-assurance-pack/
│   └── traceability-pack/
├── pages/
│   ├── inventory_page.py
│   └── login_page.py
├── tests/
│   ├── api/
│   ├── data/
│   └── ui/
├── utils/
│   ├── allure_helpers.py
│   ├── api_helpers.py
│   ├── report_helpers.py
│   ├── sql_helpers.py
│   └── traceability.py
├── allure-results/
├── allure-report/
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```

### Structure notes

- **pages/** contains the page objects for UI tests
- **data/** contains reusable test data plus SQL/reporting seed and export files
- **assets/reporting/** contains a simple stakeholder-facing dashboard mock
- **docs/ai-assisted-qa-workflow/** contains the AI workflow pack showing how GenAI can support QA work in a controlled, review-led way
- **docs/stakeholder-assurance-pack/** contains stakeholder-facing release-readiness style artefacts
- **docs/traceability-pack/** contains a lightweight requirement-to-test mapping pack
- **config/** contains shared settings such as base URLs
- **tests/ui/** contains Playwright-based UI tests
- **tests/api/** contains API tests
- **tests/data/** contains SQL/data/report validation tests
- **utils/** contains small reusable helper logic
- **allure-results/** contains raw Allure execution output plus small tracked metadata files
- **allure-report/** is a generated HTML report folder created locally or in CI and can also be published through GitHub Pages

---

## Why page objects were used

Page objects were introduced to keep the UI tests cleaner and easier to maintain.

In simple terms:

- the **test files** describe the behaviour being checked
- the **page files** hold the page locators and reusable page actions

This avoids repeating the same locator details across multiple tests and makes the project easier to scale.

---

## Test coverage included

### UI coverage
- login page smoke checks
- successful login flow
- locked-out user validation
- inventory page validation
- add-to-cart cart badge validation
- remove-from-cart cart badge validation
- responsive/mobile viewport login page check
- dashboard mock value display check

### API coverage
- GET `/posts` checks
- GET `/users` checks
- POST `/posts` checks
- response status validation
- response body/content validation
- basic response structure/key validation
- negative API coverage for a non-existent post returning `404`

### Data / dashboard coverage
- SQL-backed total order validation against a local SQLite dataset
- status breakdown validation
- completed-order revenue validation
- valid status checks
- duplicate ID detection
- negative amount detection
- exported dashboard/report validation against SQL-derived results
- dashboard metadata validation

### Stakeholder / assurance coverage
- release-readiness summary
- test scope and key risk summary
- defect-priority summary
- go / no-go style recommendation
- stakeholder-facing coverage summary linked to traceability

### AI-assisted QA workflow coverage
- example prompt patterns for AI-assisted test design
- checklist for reviewing AI-generated output before trusting it
- worked example of story-level analysis using AI as a starting point
- worked example of defect investigation support with human-led evidence review
- explicit demonstration that AI output is draft material, not trusted QA evidence

### Traceability / requirement mapping coverage
- lightweight sample requirements aligned to the existing portfolio tests
- requirement-to-test mapping across UI, API and data/report validation
- spreadsheet-friendly traceability matrix in CSV format
- coverage and gap visibility to support stakeholder review
- explicit linking of requirements, mapped tests and execution evidence sources
- light code-level requirement tags in selected representative tests

---

## Screenshots

### Inventory page after successful login

![Inventory page after login](assets/screenshots/inventory-page.png)

### Cart badge updates after adding an item

![Cart badge showing 1 item](assets/screenshots/cart-badge.png)

### GitHub Actions CI run

![GitHub Actions passing workflow](assets/screenshots/github-actions-pass.png)

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Brent-Nancarrow/QA-portfolio
cd QA-portfolio
```

### 2. Create and activate a virtual environment

#### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

```bash
playwright install
```

If needed:

```bash
python -m playwright install
```

---

## Running the tests

### Run all tests

```bash
pytest
```

### Run only UI tests

```bash
pytest -m ui -v
```

### Run only API tests

```bash
pytest -m api -v
```

### Run only smoke tests

```bash
pytest -m smoke -v
```

### Run only responsive tests

```bash
pytest -m responsive -v
```

### Run only SQL/data validation tests

```bash
pytest -m data -v
```

### Run dashboard export validation directly

```bash
pytest tests/data/test_dashboard_export_validation.py -v
```

### Run the dashboard mock UI check directly

```bash
pytest tests/ui/test_reporting_dashboard_mock.py -v
```

---

## Local vs CI execution

This project is configured so that:

- **local runs** open the browser in headed mode for easier visibility
- **CI runs** execute headless in GitHub Actions

This is controlled in `conftest.py` using the `CI` environment variable.

---

## Failure evidence

The project is configured to retain useful evidence on failure, including:

- **Playwright trace**
- **video**
- **screenshots**

This helps support investigation and debugging when a test fails.

---

## Continuous Integration

GitHub Actions is configured to run the test suite automatically on:

- push to `main`
- pull requests
- manual workflow dispatch

The workflow also retains:

- **Playwright test results** for failure investigation support
- **Allure raw results** for report generation and execution review
- **a published Allure HTML report in GitHub Pages** for easier stakeholder-style access

This helps show that the project can run both locally and in an automated pipeline while keeping reviewable evidence.

---

## SQL / data / dashboard validation slice

This portfolio includes a lightweight **SQL-backed reporting validation slice** using **SQLite** and **pytest**.

It demonstrates:

- validating source data using SQL queries
- checking dashboard/report-style totals and status breakdowns
- validating completed-order revenue
- basic data quality checks such as valid statuses, duplicate ID detection and negative amount detection
- validating an exported dashboard/report JSON against SQL-derived results
- checking a simple dashboard mock displays the expected figures
- attaching SQL queries and result evidence into **Allure**

This was added deliberately to reflect commercially realistic QA work beyond UI/API checks, especially where confidence in **reports, dashboards and business-critical outputs** matters.

---

## Allure reporting

This project includes **Allure-ready test reporting** to make execution results easier for stakeholders to review.

### What Allure adds

- clearer pass/fail execution status
- named test titles and test steps
- JSON request/response evidence for API checks
- SQL query/result evidence for data checks
- screenshot and page URL attachments for failed UI tests
- optional report metadata such as environment, execution source and defect categories

### Install the Allure pytest plugin

```bash
pip install allure-pytest
```

### Run tests and save Allure results

```bash
pytest --alluredir=allure-results
```

### Open a temporary Allure report

```bash
allure serve allure-results
```

### Generate a saved report folder

```bash
allure generate allure-results --clean -o allure-report
allure open allure-report
```

### View the published CI report

After a successful GitHub Actions run, this project can also publish the generated Allure HTML report to **GitHub Pages**.

That gives a more stakeholder-friendly way to review execution output without needing to regenerate the report locally every time.

Typical published URL pattern:

```text
https://<github-username>.github.io/QA-portfolio/
```

> Note: the Allure command-line tool also needs to be installed separately on your machine for local report generation.

### Why this matters in the portfolio

Allure improves the visibility of:

- what ran
- what passed or failed
- which steps were executed
- what API or SQL evidence was captured
- what UI evidence was attached on failure
- which environment and execution context produced the result

That makes the project more useful for interview discussion because it shows not just test execution, but also **evidence, traceability, reviewability and stakeholder-friendly report access**.

---

## AI-assisted QA workflow pack

This portfolio includes a small **AI-assisted QA workflow pack** under `docs/ai-assisted-qa-workflow/`.

It is designed to show a practical, controlled and commercially realistic approach to using Generative AI in QA work.

### What it includes

- example prompts for test idea generation and exploratory support
- a checklist for reviewing AI-generated output
- story-analysis examples showing AI as a starting point, not an authority
- defect-investigation examples showing where AI can assist communication without replacing evidence-led QA judgement

### Why it matters

The aim is not to claim that AI should replace testers. The aim is to show how AI can support:

- faster test idea generation
- exploratory structure
- requirement gap analysis
- defect communication drafting
- workflow efficiency

while keeping:

- QA judgement
- risk prioritisation
- evidence review
- validation
- release confidence decisions human-led

See: `docs/ai-assisted-qa-workflow/`

---

## Stakeholder-facing assurance artefacts

This portfolio includes a small **stakeholder assurance pack** to show how hands-on QA execution can be translated into release-readiness style outputs.

The aim is to demonstrate not only test execution, but also quality communication, scope/risk visibility and evidence-led go / no-go style thinking.

See: `docs/stakeholder-assurance-pack/`

---

## Traceability / requirement-to-test mapping pack

This portfolio also includes a lightweight **traceability pack** to show how requirements, acceptance criteria, tests and evidence can be linked together.

The aim is to demonstrate requirement coverage thinking in a commercially realistic way, without over-claiming full enterprise traceability.

It includes:

- sample requirements and acceptance criteria
- a readable requirement-to-test matrix
- a CSV version for spreadsheet-style review
- a short coverage and gaps summary
- a stakeholder-facing coverage summary linked back to the matrix
- light code-level requirement tags in selected representative tests

Selected tests also use a small `utils/traceability.py` helper so requirement IDs can be reflected in code and Allure output without over-engineering the project.

See: `docs/traceability-pack/`

---

## Why this project matters for my portfolio

This repository is intended to show practical, honest capability in modern QA tooling while staying aligned to my real market positioning.

It supports my positioning as a **Senior Manual QA / Workstream Test Lead / assurance-led QA professional** who adds value through:

- **hands-on testing where it matters**
- **test assurance and release confidence thinking**
- **stakeholder reporting and quality visibility**
- **risk-based coverage decisions**
- **data / dashboard validation**, not just browser checks
- **AI-assisted but human-controlled workflow support**

## How to talk about this project in interviews

A simple and honest way to describe this portfolio is:

> I built this project to demonstrate practical QA capability using Python, Playwright and pytest in a way that reflects my real background. It shows UI, API and SQL-backed data/report validation coverage, maintainable structure, CI execution, failure evidence, Allure reporting, stakeholder-facing assurance artefacts, traceability from requirements to evidence, and an AI-assisted QA workflow pack that demonstrates how I would use Generative AI as a support tool rather than a substitute for testing judgement.

It also supports conversations around:

- modern tooling adoption as a hands-on QA lead / senior manual QA
- stakeholder-friendly reporting and evidence
- maintainability over automation for automation’s sake
- quality visibility and release confidence
- practical AI-assisted QA workflows with human-led review
