import pytest
from playwright.sync_api import Page

from data.users import LOCKED_OUT_USER, STANDARD_USER
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.parametrize(
    "user_data, should_login, expected_error",
    [
        (STANDARD_USER, True, None),
        (LOCKED_OUT_USER, False, "Sorry, this user has been locked out."),
    ],
)
def test_login_behaviour_by_user_type(
    page: Page,
    user_data: dict,
    should_login: bool,
    expected_error: str | None,
) -> None:
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login_as_user(user_data)

    if should_login:
        inventory_page.verify_loaded()
    else:
        assert expected_error in login_page.get_error_message()