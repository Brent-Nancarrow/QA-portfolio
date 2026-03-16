import sqlite3
from pathlib import Path

import allure
import pytest

from utils.allure_helpers import attach_json, attach_text
from utils.sql_helpers import (
    create_database_from_sql,
    fetch_all_rows,
    fetch_one_value,
    load_expected_dashboard_values,
)

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
def expected_dashboard_values() -> dict:
    """
    Load the expected dashboard/report values from JSON.
    """
    return load_expected_dashboard_values(REPORTING_DIR / "dashboard_expected.json")


@allure.feature("Data Validation")
@allure.story("SQL-backed dashboard validation")
@allure.title("Orders table contains the expected number of records")
def test_total_orders_matches_expected_dashboard_value(
    orders_db: sqlite3.Connection,
    expected_dashboard_values: dict,
) -> None:
    query = "SELECT COUNT(*) FROM orders;"

    with allure.step("Run SQL query to count all orders"):
        actual_total_orders = fetch_one_value(orders_db, query)
        attach_text("sql-query-total-orders", query)

    with allure.step("Attach expected and actual results"):
        attach_json(
            "total-orders-comparison",
            {
                "expected_total_orders": expected_dashboard_values["total_orders"],
                "actual_total_orders": actual_total_orders,
            },
        )

    with allure.step("Check the dashboard total matches the database total"):
        assert actual_total_orders == expected_dashboard_values["total_orders"]


@allure.feature("Data Validation")
@allure.story("SQL-backed dashboard validation")
@pytest.mark.parametrize(
    ("status_name", "expected_key"),
    [
        ("Completed", "completed_orders"),
        ("Pending", "pending_orders"),
        ("Cancelled", "cancelled_orders"),
    ],
)
@allure.title("{status_name} order total matches the expected dashboard value")
def test_order_status_total_matches_expected_dashboard_value(
    orders_db: sqlite3.Connection,
    expected_dashboard_values: dict,
    status_name: str,
    expected_key: str,
) -> None:
    query = f"SELECT COUNT(*) FROM orders WHERE order_status = '{status_name}';"

    with allure.step(f"Run SQL query to count {status_name.lower()} orders"):
        actual_status_total = fetch_one_value(orders_db, query)
        attach_text(f"sql-query-{status_name.lower()}-orders", query)

    with allure.step("Attach expected and actual status totals"):
        attach_json(
            f"{status_name.lower()}-orders-comparison",
            {
                "status": status_name,
                "expected_total": expected_dashboard_values[expected_key],
                "actual_total": actual_status_total,
            },
        )

    with allure.step("Check the status total matches the expected dashboard value"):
        assert actual_status_total == expected_dashboard_values[expected_key]


@allure.feature("Data Validation")
@allure.story("SQL-backed dashboard validation")
@allure.title("Completed-order revenue matches the expected dashboard value")
def test_completed_order_revenue_matches_expected_dashboard_value(
    orders_db: sqlite3.Connection,
    expected_dashboard_values: dict,
) -> None:
    query = """
        SELECT ROUND(SUM(amount), 2)
        FROM orders
        WHERE order_status = 'Completed';
    """

    with allure.step("Run SQL query to calculate completed-order revenue"):
        actual_completed_revenue = fetch_one_value(orders_db, query)
        attach_text("sql-query-completed-revenue", query)

    with allure.step("Attach expected and actual revenue values"):
        attach_json(
            "completed-revenue-comparison",
            {
                "expected_completed_revenue": expected_dashboard_values["completed_revenue"],
                "actual_completed_revenue": actual_completed_revenue,
            },
        )

    with allure.step("Check the completed-order revenue matches the expected dashboard value"):
        assert actual_completed_revenue == expected_dashboard_values["completed_revenue"]


@allure.feature("Data Validation")
@allure.story("SQL-backed data quality checks")
@allure.title("Orders contain only valid status values")
def test_orders_contain_only_valid_status_values(orders_db: sqlite3.Connection) -> None:
    query = """
        SELECT DISTINCT order_status
        FROM orders
        ORDER BY order_status;
    """
    valid_statuses = {"Completed", "Pending", "Cancelled"}

    with allure.step("Run SQL query to get distinct order statuses"):
        rows = fetch_all_rows(orders_db, query)
        actual_statuses = {row[0] for row in rows}
        attach_text("sql-query-distinct-statuses", query)

    with allure.step("Attach the distinct statuses found in the database"):
        attach_json(
            "distinct-order-statuses",
            {
                "actual_statuses": sorted(actual_statuses),
                "valid_statuses": sorted(valid_statuses),
            },
        )

    with allure.step("Check only valid statuses are present"):
        assert actual_statuses == valid_statuses


@allure.feature("Data Validation")
@allure.story("SQL-backed data quality checks")
@allure.title("Orders do not contain duplicate order IDs")
def test_orders_do_not_contain_duplicate_order_ids(orders_db: sqlite3.Connection) -> None:
    query = """
        SELECT order_id, COUNT(*)
        FROM orders
        GROUP BY order_id
        HAVING COUNT(*) > 1;
    """

    with allure.step("Run SQL query to look for duplicate order IDs"):
        duplicate_rows = fetch_all_rows(orders_db, query)
        attach_text("sql-query-duplicate-order-ids", query)
        attach_json("duplicate-order-id-results", {"rows": duplicate_rows})

    with allure.step("Check there are no duplicate order IDs"):
        assert duplicate_rows == []


@allure.feature("Data Validation")
@allure.story("SQL-backed data quality checks")
@allure.title("Orders do not contain negative amounts")
def test_orders_do_not_contain_negative_amounts(orders_db: sqlite3.Connection) -> None:
    query = """
        SELECT order_id, amount
        FROM orders
        WHERE amount < 0;
    """

    with allure.step("Run SQL query to look for negative amounts"):
        negative_amount_rows = fetch_all_rows(orders_db, query)
        attach_text("sql-query-negative-amounts", query)
        attach_json("negative-amount-results", {"rows": negative_amount_rows})

    with allure.step("Check there are no negative amounts in the orders data"):
        assert negative_amount_rows == []
