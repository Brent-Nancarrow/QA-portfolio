from pathlib import Path

import allure
import pytest

from utils.traceability import traceability

pytestmark = pytest.mark.ui

BASE_DIR = Path(__file__).resolve().parents[2]
DASHBOARD_HTML = BASE_DIR / "assets" / "reporting" / "orders_dashboard.html"


@traceability("RQ-DATA-004")
@allure.feature("Reporting UI")
@allure.story("Dashboard mock")
@allure.title("Reporting dashboard mock displays the expected values")
def test_reporting_dashboard_mock_displays_expected_values(page) -> None:
    """
    Open the local dashboard mock and check the visible values.
    """
    with allure.step("Record the linked requirement for this dashboard output check"):
        allure.attach(
            "Requirement: RQ-DATA-004 - Dashboard mock display",
            name="traceability-reference",
            attachment_type=allure.attachment_type.TEXT,
        )

    with allure.step("Open the local dashboard mock"):
        page.goto(DASHBOARD_HTML.resolve().as_uri())

    expect_title = page.get_by_test_id("dashboard-title")
    expect_meta = page.get_by_test_id("dashboard-meta")
    total_orders = page.get_by_test_id("card-total-orders")
    completed_orders = page.get_by_test_id("card-completed-orders")
    pending_orders = page.get_by_test_id("card-pending-orders")
    cancelled_orders = page.get_by_test_id("card-cancelled-orders")
    completed_revenue = page.get_by_test_id("card-completed-revenue")

    with allure.step("Check the dashboard header and metadata"):
        assert expect_title.text_content() == "Orders Dashboard Summary"
        assert "Portfolio demonstration" in expect_meta.text_content()
        assert "Local SQLite reporting dataset" in expect_meta.text_content()

    with allure.step("Check the visible dashboard card values"):
        assert "8" in total_orders.text_content()
        assert "4" in completed_orders.text_content()
        assert "2" in pending_orders.text_content()
        assert "2" in cancelled_orders.text_content()
        assert "730.49" in completed_revenue.text_content()
