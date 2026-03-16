import os

import allure
import pytest
from allure_commons.types import AttachmentType
from playwright.sync_api import Playwright

from config.settings import API_BASE_URL


@pytest.fixture(scope="session")
def browser_type_launch_args():
    is_ci = os.getenv("CI") == "true"

    return {
        "headless": is_ci,
        "slow_mo": 0 if is_ci else 500,
    }


@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
    request_context = playwright.request.new_context(base_url=API_BASE_URL)
    yield request_context
    request_context.dispose()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(autouse=True)
def attach_ui_artifacts_on_failure(request):
    """Attach a screenshot and page URL to Allure if a UI test fails."""
    yield

    if "page" not in request.fixturenames:
        return

    report = getattr(request.node, "rep_call", None)
    if not report or not report.failed:
        return

    page = request.getfixturevalue("page")
    allure.attach(
        page.screenshot(full_page=True),
        name="failure-screenshot",
        attachment_type=AttachmentType.PNG,
    )
    allure.attach(page.url, name="page-url", attachment_type=AttachmentType.TEXT)