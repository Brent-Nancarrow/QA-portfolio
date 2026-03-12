# QA-portfolio

A beginner-friendly but commercially credible QA portfolio project built with **Python, Playwright and pytest**.

This project is designed to demonstrate practical modern QA skills in a realistic and maintainable way, including:

- **UI testing** against Sauce Demo
- **API testing** against JSONPlaceholder
- **Page Object Model (POM)** structure for cleaner UI test design
- **Shared config and reusable test data**
- **Responsive/mobile viewport coverage**
- **Failure evidence** such as trace, video and screenshots on failure
- **GitHub Actions CI** for automated test execution
- **Selective test execution using pytest markers**

The goal is not to present as a senior automation engineer, but to show practical hands-on capability as a **Senior Manual QA / Workstream Test Lead / assurance-led QA professional** adding modern tooling in a commercially realistic way.

---

## What this project demonstrates

This project currently demonstrates:

- UI smoke and functional checks using Playwright
- API checks using Playwright API request support with pytest
- Separation of UI and API test coverage
- Maintainable UI structure using page objects
- Reusable helpers, shared settings and test data
- Local headed execution and CI headless execution
- Responsive testing using a mobile-style viewport
- GitHub Actions CI pipeline
- Failure investigation support using trace, video and screenshots on failure

---

## Tech stack

- **Python**
- **PyCharm**
- **pytest**
- **Playwright**
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
│   │   ├── test_api_create_post.py
│   │   ├── test_api_get_posts.py
│   │   └── test_api_users.py
│   └── ui/
│       ├── test_saucedemo_inventory.py
│       ├── test_saucedemo_login.py
│       ├── test_saucedemo_responsive.py
│       └── test_saucedemo_smoke.py
├── utils/
│   └── api_helpers.py
├── conftest.py
├── pytest.ini
├── README.md
└── requirements.txt
```

### Structure notes

- **pages/** contains the page objects for UI tests
- **data/** contains reusable test data such as demo users
- **config/** contains shared settings such as base URLs
- **tests/ui/** contains Playwright-based UI tests
- **tests/api/** contains API tests
- **utils/** contains small reusable helper logic

---

## Why page objects were used

Page objects were introduced to keep the UI tests cleaner and easier to maintain.

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
- add-to-cart cart badge validation
- remove-from-cart cart badge validation
- responsive/mobile viewport login page check

### API coverage

- GET `/posts` checks
- GET `/users` checks
- POST `/posts` checks
- response status validation
- response body/content validation
- basic response structure/key validation
- negative API coverage for a non-existent post returning `404`

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

This helps demonstrate that the project can run both locally and in an automated pipeline.

---

## Why this project matters for my portfolio

This repository is intended to show practical, honest capability in modern QA tooling without pretending to be an advanced automation specialist.

It supports my positioning as a **Senior Manual QA / Workstream Test Lead / assurance-led QA professional** who is adding:

- Python
- Playwright
- pytest
- API coverage
- CI awareness
- maintainable test structure

in a realistic and commercially grounded way.

---

## Future improvements

Potential future improvements include:

- improved test reporting
- richer README visuals or screenshots
- Docker support
- expanded API coverage
- additional UI journeys
- cleaner reusable helper layers where appropriate