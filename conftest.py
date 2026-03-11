import os
import pytest
from playwright.sync_api import Playwright
from config.settings import API_BASE_URL


@pytest.fixture(scope="session")
def browser_type_launch_args():
    is_ci = os.getenv("CI") == "true"

    return {
        "headless": is_ci,
        "slow_mo": 0 if is_ci else 500
    }


@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
    request_context = playwright.request.new_context(base_url=API_BASE_URL)
    yield request_context
    request_context.dispose()