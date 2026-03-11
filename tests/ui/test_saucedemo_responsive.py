import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


@pytest.mark.ui
@pytest.mark.responsive
def test_saucedemo_login_page_on_mobile_viewport(page: Page) -> None:
    page.set_viewport_size({"width": 375, "height": 812})

    login_page = LoginPage(page)
    login_page.open()

    expect(page).to_have_title("Swag Labs")
    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.login_button).to_be_visible()