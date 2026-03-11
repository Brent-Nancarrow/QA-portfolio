# QA-portfolio

A beginner-friendly but commercially credible QA automation portfolio project built with **Python, Playwright and pytest**.

This project is designed to demonstrate practical modern QA skills in a realistic and maintainable way, including:

- **UI testing** against Sauce Demo
- **API testing** against JSONPlaceholder
- **Page Object structure** for cleaner UI test design
- **Shared config and test data**
- **Responsive/mobile viewport coverage**
- **Failure evidence** such as trace, video and screenshots on failure
- **GitHub Actions CI** for automated test execution

The goal is not to present as a senior automation engineer, but to show practical hands-on capability as a **Senior Manual QA / Workstream Test Lead / Assurance-led QA professional** adding modern tooling.

---

## What this project demonstrates

This project currently covers:

- UI smoke and functional checks using Playwright
- API checks using pytest and requests
- Separation of UI and API tests
- Maintainable UI test structure using page objects
- Reusable test data and shared settings
- Local headed execution and CI headless execution
- Responsive testing using a mobile-style viewport
- Basic GitHub Actions CI pipeline

---

## Tech stack

- **Python**
- **PyCharm**
- **pytest**
- **Playwright**
- **requests**
- **Git / GitHub**
- **GitHub Actions**

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
├── config/
│   └── settings.py
├── data/
│   └── users.py
├── pages/
│   ├── inventory_page.py
│   └── login_page.py
├── tests/
│   ├── api/
│   │   └── test_api_jsonplaceholder.py
│   └── ui/
│       ├── test_saucedemo_inventory.py
│       ├── test_saucedemo_login.py
│       ├── test_saucedemo_responsive.py
│       └── test_saucedemo_smoke.py
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```

### Structure notes

- **pages/** contains the page objects for UI tests
- **data/** contains reusable test data such as demo users
- **config/** contains shared settings such as the base URL
- **tests/ui/** contains Playwright-based UI tests
- **tests/api/** contains API tests

---

## Why page objects were used

Page objects were introduced to keep the tests cleaner and easier to maintain.

In simple terms:

- the **test files** describe the behaviour being checked
- the **page files** hold the page locators and reusable page actions

This avoids repeating the same locator details across multiple tests and makes the project easier to scale.

---

## Test coverage included so far

### UI coverage

- login page smoke checks
- successful login flow
- locked out user validation
- inventory page validation
- responsive/mobile viewport login page check

### API coverage

- basic JSONPlaceholder endpoint checks
- API coverage now includes GET and POST checks against JSONPlaceholder, including response status, payload validation, and basic response structure checks.

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

### Run UI tests

```bash
pytest tests/ui -v
```

### Run API tests

```bash
pytest tests/api -v
```

### Run smoke tests

```bash
pytest -m smoke
```

### Run responsive tests

```bash
pytest -m responsive
```

---

## Test execution behaviour

The project is set up so that:

- **local runs** use a visible browser (**headed**) for easier learning and debugging
- **CI runs** use **headless** mode for automated execution in GitHub Actions

This is handled through project configuration rather than needing to change the tests manually each time.

---

## Failure evidence

The framework is configured to capture useful failure evidence for debugging, including:

- trace
- screenshot
- video

This helps make failures easier to understand and gives the project a more realistic QA workflow.

---

## Continuous Integration

This project includes a **GitHub Actions** workflow so tests can run automatically in CI.

This demonstrates:

- basic CI/CD awareness
- automated validation outside the local machine
- a more realistic portfolio workflow

---

## Why this project exists

I built this project as part of my QA upskilling journey to strengthen practical exposure to modern tooling while staying aligned to my main career direction in:

- Senior Manual QA
- Workstream Test Lead (hands-on)
- Test Assurance / Delivery Assurance
- Release confidence / embedded quality support

The intention is to show practical capability with modern tools without pretending to be an automation-first SDET.

---

## Future improvements

Planned or possible future additions include:

- improved README polish
- additional responsive coverage
- simple helper layer expansion
- more API scenarios
- light data validation examples
- Docker-based execution
- improved test reporting (for example Allure) to provide clearer execution summaries, richer failure evidence and more stakeholder-friendly results
- optional ReqRes API coverage
- optional small BDD example later if useful

---

## Notes

This is a portfolio learning project using public demo systems and APIs.

It is intentionally kept practical, readable and maintainable rather than over-engineered.

