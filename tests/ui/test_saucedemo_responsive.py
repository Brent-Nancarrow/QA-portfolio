import allure
import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


@allure.feature("Sauce Demo UI")
@allure.story("Responsive layout")
@allure.title("Login page is usable on a mobile-sized viewport")
@pytest.mark.ui
@pytest.mark.responsive
def test_saucedemo_login_page_on_mobile_viewport(page: Page) -> None:
    with allure.step("Set a mobile-sized viewport"):
        page.set_viewport_size({"width": 375, "height": 812})

    login_page = LoginPage(page)

    with allure.step("Open the login page"):
        login_page.open()

    with allure.step("Check the page title and that key controls stay visible"):
        expect(page).to_have_title("Swag Labs")
        expect(login_page.username_input).to_be_visible()
        expect(login_page.password_input).to_be_visible()
        expect(login_page.login_button).to_be_visible()