import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.smoke
def test_saucedemo_login_page_loads(page: Page) -> None:
    login_page = LoginPage(page)

    login_page.open()

    expect(page).to_have_title("Swag Labs")
    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.login_button).to_be_visible()
    expect(login_page.login_button).to_have_value("Login")