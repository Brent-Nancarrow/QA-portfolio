from playwright.sync_api import Page, expect


def test_saucedemo_login_page_loads(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")

    expect(page).to_have_title("Swag Labs")
    expect(page.locator('[data-test="username"]')).to_be_visible()
    expect(page.locator('[data-test="password"]')).to_be_visible()
    expect(page.locator('[data-test="login-button"]')).to_be_visible()
    expect(page.locator('[data-test="login-button"]')).to_have_value("Login")