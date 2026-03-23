# Requirements-to-Test Matrix

This matrix links sample requirements to the portfolio's current automated checks and to the evidence sources that support execution review.

## How to read this

- **Requirement ID** = the requirement being traced
- **Acceptance criteria** = the testable behaviour expected
- **Mapped tests** = the current automated tests that support coverage
- **Evidence source** = where execution evidence can be reviewed
- **Coverage status** = covered / partially covered / gap

---

| Requirement ID | Acceptance criteria covered | Mapped tests | Evidence source | Coverage status | Notes |
|---|---|---|---|---|---|
| RQ-UI-001 | AC-UI-001.1 to AC-UI-001.4 | `tests/ui/test_saucedemo_smoke.py::test_saucedemo_login_page_loads` | Allure steps and Playwright UI execution evidence | Covered | Confirms page title and core login controls are visible |
| RQ-UI-002 | AC-UI-002.1 to AC-UI-002.3 | `tests/ui/test_saucedemo_login.py::test_login_behaviour_by_user_type[standard_user]`; `tests/ui/test_saucedemo_inventory.py::test_inventory_page_shows_products` | Allure steps; UI execution evidence; screenshots on failure | Covered | Uses a valid user path and verifies inventory visibility |
| RQ-UI-003 | AC-UI-003.1 to AC-UI-003.2 | `tests/ui/test_saucedemo_login.py::test_login_behaviour_by_user_type[locked_out_user]` | Allure steps; UI execution evidence | Covered | Verifies controlled failure path for locked-out user |
| RQ-UI-004 | AC-UI-004.1 to AC-UI-004.2 | `tests/ui/test_saucedemo_inventory.py::test_adding_backpack_updates_cart_badge`; `tests/ui/test_saucedemo_inventory.py::test_removing_backpack_hides_cart_badge` | Allure steps; UI execution evidence; screenshots on failure | Covered | Focused functional traceability for add/remove behaviour |
| RQ-UI-005 | AC-UI-005.1 to AC-UI-005.2 | `tests/ui/test_saucedemo_responsive.py::test_saucedemo_login_page_on_mobile_viewport` | Allure steps; UI execution evidence | Covered | Lightweight responsive assurance rather than full device matrix |
| RQ-API-001 | AC-API-001.1 to AC-API-001.3 | `tests/api/test_api_get_posts.py::test_get_all_posts_returns_200`; `tests/api/test_api_get_posts.py::test_get_all_posts_returns_a_non_empty_list`; `tests/api/test_api_get_posts.py::test_first_post_contains_expected_fields` | Allure steps; attached JSON API evidence | Covered | Good baseline availability + structure coverage |
| RQ-API-002 | AC-API-002.1 to AC-API-002.2 | `tests/api/test_api_get_posts.py::test_get_non_existent_post_returns_404` | Allure steps; attached JSON API evidence | Covered | Negative-path API validation |
| RQ-API-003 | AC-API-003.1 to AC-API-003.2 | `tests/api/test_api_create_post.py::test_create_post_returns_expected_status_and_data` | Allure steps; attached request/response JSON | Covered | Covers status and echoed payload behaviour |
| RQ-API-004 | AC-API-004.1 to AC-API-004.4 | `tests/api/test_api_users.py::test_get_users_returns_200`; `tests/api/test_api_users.py::test_get_users_returns_a_list`; `tests/api/test_api_users.py::test_first_user_contains_expected_fields`; `tests/api/test_api_users.py::test_first_user_email_looks_valid` | Allure steps; attached JSON API evidence | Covered | Good simple data-structure assurance for users endpoint |
| RQ-DATA-001 | AC-DATA-001.1 to AC-DATA-001.5 | `tests/data/test_orders_dashboard_sql.py::test_total_orders_matches_expected_dashboard_value`; `tests/data/test_orders_dashboard_sql.py::test_order_status_total_matches_expected_dashboard_value`; `tests/data/test_orders_dashboard_sql.py::test_completed_order_revenue_matches_expected_dashboard_value` | Allure SQL query attachments; expected-vs-actual JSON evidence | Covered | Strong requirement-to-data check linkage |
| RQ-DATA-002 | AC-DATA-002.1 to AC-DATA-002.3 | `tests/data/test_orders_dashboard_sql.py::test_orders_contain_only_valid_status_values`; `tests/data/test_orders_dashboard_sql.py::test_orders_do_not_contain_duplicate_order_ids`; `tests/data/test_orders_dashboard_sql.py::test_orders_do_not_contain_negative_amounts` | Allure SQL query attachments; JSON evidence for failing rows if present | Covered | Shows data quality assurance beyond simple totals |
| RQ-DATA-003 | AC-DATA-003.1 to AC-DATA-003.5 | `tests/data/test_dashboard_export_validation.py::test_dashboard_export_totals_match_sql_results`; `tests/data/test_dashboard_export_validation.py::test_dashboard_export_contains_expected_metadata` | Allure SQL query attachments; export JSON evidence | Covered | Links exported report content to source data checks |
| RQ-DATA-004 | AC-DATA-004.1 to AC-DATA-004.4 | `tests/ui/test_reporting_dashboard_mock.py::test_reporting_dashboard_mock_displays_expected_values` | UI execution evidence; local dashboard mock validation | Covered | Useful for output assurance and stakeholder-facing discussion |

---

## Important interpretation note

This matrix shows **portfolio-level sample traceability**, not a claim of full production-grade requirement coverage.

That distinction matters because strong QA traceability is not about pretending everything is covered. It is about making:

- coverage visible
- assumptions explicit
- evidence reviewable
- gaps honest

