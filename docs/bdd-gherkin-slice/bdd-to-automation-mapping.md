# BDD Scenario to Automation Mapping

This mapping links the BDD / Gherkin scenarios to the existing automated checks and traceability artefacts.

It is intentionally lightweight. The goal is to show how business-readable scenarios can support test design, traceability and stakeholder conversations without creating a second heavy automation framework.

## Mapping table

| Feature file | Scenario | Requirement IDs | Existing supporting automated checks | Evidence source |
|---|---|---|---|---|
| `features/login.feature` | Standard user can access the inventory page | RQ-UI-001, RQ-UI-002 | `tests/ui/test_saucedemo_login.py::test_login_behaviour_by_user_type`; `tests/ui/test_saucedemo_inventory.py::test_inventory_page_shows_products` | Allure UI steps; Playwright trace/video/screenshots on failure |
| `features/login.feature` | Locked-out user receives a controlled error | RQ-UI-003 | `tests/ui/test_saucedemo_login.py::test_login_behaviour_by_user_type` | Allure UI steps; error message assertion |
| `features/reporting-dashboard.feature` | Dashboard totals align with source data | RQ-DATA-001 | `tests/data/test_orders_dashboard_sql.py::test_total_orders_matches_expected_dashboard_value`; `tests/data/test_orders_dashboard_sql.py::test_completed_order_revenue_matches_expected_dashboard_value` | SQL query attachments; expected-vs-actual JSON evidence |
| `features/reporting-dashboard.feature` | Dashboard export includes expected reporting metadata | RQ-DATA-003 | `tests/data/test_dashboard_export_validation.py::test_dashboard_export_contains_expected_metadata` | Export JSON evidence; metadata assertions |
| `features/reporting-dashboard.feature` | Dashboard mock displays stakeholder-visible values | RQ-DATA-004 | `tests/ui/test_reporting_dashboard_mock.py::test_reporting_dashboard_mock_displays_expected_values` | UI execution evidence; dashboard mock checks |

## Assurance interpretation

The Gherkin files are not a replacement for the automated checks. They are a readable bridge between:

- requirement intent
- acceptance criteria
- automation coverage
- stakeholder-facing evidence

This is especially useful in roles where QA needs to explain coverage and residual risk to non-technical stakeholders.
