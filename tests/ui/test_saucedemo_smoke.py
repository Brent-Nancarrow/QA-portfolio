import allure
import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


@allure.feature("Sauce Demo UI")
@allure.story("Smoke")
@allure.title("Login page loads and shows core controls")
@pytest.mark.ui
@pytest.mark.smoke
def test_saucedemo_login_page_loads(page: Page) -> None:
    login_page = LoginPage(page)

    with allure.step("Open the Sauce Demo login page"):
        login_page.open()

    with allure.step("Check the page title and core login controls"):
        expect(page).to_have_title("Swag Labs")
        expect(login_page.username_input).to_be_visible()
        expect(login_page.password_input).to_be_visible()
        expect(login_page.login_button).to_be_visible()
        expect(login_page.login_button).to_have_value("Login")