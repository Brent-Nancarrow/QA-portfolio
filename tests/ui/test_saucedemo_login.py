import pytest
from playwright.sync_api import Page

from data.users import LOCKED_OUT_USER, STANDARD_USER
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.smoke
def test_successful_login(page: Page) -> None:
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login_as_user(STANDARD_USER)

    inventory_page.verify_loaded()


@pytest.mark.ui
def test_locked_out_user_sees_error(page: Page) -> None:
    login_page = LoginPage(page)

    login_page.open()
    login_page.login_as_user(LOCKED_OUT_USER)

    assert "Sorry, this user has been locked out." in login_page.get_error_message()