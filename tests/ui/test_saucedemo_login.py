import allure
import pytest
from playwright.sync_api import Page

from data.users import LOCKED_OUT_USER, STANDARD_USER
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@allure.feature("Sauce Demo UI")
@allure.story("Login")
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

    allure.dynamic.title(f"Login behaviour for user type: {user_data['username']}")

    with allure.step("Open the login page"):
        login_page.open()

    with allure.step(f"Attempt to log in as {user_data['username']}"):
        login_page.login_as_user(user_data)

    if should_login:
        with allure.step("Check the user reaches the inventory page"):
            inventory_page.verify_loaded()
    else:
        with allure.step("Check the correct locked-out error is shown"):
            assert expected_error in login_page.get_error_message()