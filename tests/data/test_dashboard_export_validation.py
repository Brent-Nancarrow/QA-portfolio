import sqlite3
from pathlib import Path

import allure
import pytest

from utils.allure_helpers import attach_json, attach_text
from utils.report_helpers import load_dashboard_export
from utils.traceability import traceability
from utils.sql_helpers import create_database_from_sql, fetch_one_value

pytestmark = pytest.mark.data

BASE_DIR = Path(__file__).resolve().parents[2]
REPORTING_DIR = BASE_DIR / "data" / "reporting"


@pytest.fixture
def orders_db(tmp_path) -> sqlite3.Connection:
    """
    Create a temporary SQLite database for each test run.
    """
    db_path = tmp_path / "orders.db"
    schema_path = REPORTING_DIR / "orders_schema.sql"
    seed_path = REPORTING_DIR / "orders_seed.sql"

    connection = create_database_from_sql(db_path, schema_path, seed_path)
    yield connection
    connection.close()


@pytest.fixture
def dashboard_export() -> dict:
    """
    Load the simulated dashboard/report export.
    """
    return load_dashboard_export(REPORTING_DIR / "dashboard_export.json")


@traceability("RQ-DATA-003")
@allure.feature("Dashboard Validation")
@allure.story("Report export matches source data")
@allure.title("Dashboard export totals match SQL query results")
def test_dashboard_export_totals_match_sql_results(
    orders_db: sqlite3.Connection,
    dashboard_export: dict,
) -> None:
    with allure.step("Record the linked requirement for this dashboard export validation"):
        allure.attach(
            "Requirement: RQ-DATA-003 - Dashboard export validation",
            name="traceability-reference",
            attachment_type=allure.attachment_type.TEXT,
        )

    queries = {
        "total_orders": "SELECT COUNT(*) FROM orders;",
        "completed_orders": "SELECT COUNT(*) FROM orders WHERE order_status = 'Completed';",
        "pending_orders": "SELECT COUNT(*) FROM orders WHERE order_status = 'Pending';",
        "cancelled_orders": "SELECT COUNT(*) FROM orders WHERE order_status = 'Cancelled';",
        "completed_revenue": """
            SELECT ROUND(SUM(amount), 2)
            FROM orders
            WHERE order_status = 'Completed';
        """,
    }

    actual_results = {
        metric_name: fetch_one_value(orders_db, query)
        for metric_name, query in queries.items()
    }

    with allure.step("Attach SQL queries used for dashboard validation"):
        attach_text(
            "dashboard-validation-sql-queries",
            "\n\n".join([f"{name}:\n{query.strip()}" for name, query in queries.items()]),
        )

    with allure.step("Attach exported dashboard metrics and SQL-derived results"):
        attach_json(
            "dashboard-export-vs-sql-results",
            {
                "dashboard_export_metrics": dashboard_export["metrics"],
                "sql_results": actual_results,
            },
        )

    with allure.step("Check the exported dashboard values match the SQL results"):
        assert dashboard_export["metrics"] == actual_results


@traceability("RQ-DATA-003")
@allure.feature("Dashboard Validation")
@allure.story("Report export structure")
@allure.title("Dashboard export contains the expected business metadata")
def test_dashboard_export_contains_expected_metadata(dashboard_export: dict) -> None:
    with allure.step("Record the linked requirement for this dashboard metadata validation"):
        allure.attach(
            "Requirement: RQ-DATA-003 - Dashboard export validation",
            name="traceability-reference",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Attach the dashboard export content"):
        attach_json("dashboard-export-json", dashboard_export)

    with allure.step("Check expected metadata fields are present"):
        assert dashboard_export["report_name"] == "Orders Dashboard Summary"
        assert dashboard_export["generated_for"] == "Portfolio demonstration"
        assert dashboard_export["source"] == "Local SQLite reporting dataset"
        assert "metrics" in dashboard_export