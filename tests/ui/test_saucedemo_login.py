from playwright.sync_api import Page, expect


def test_valid_login(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator('[data-test="title"]')).to_have_text("Products")


def test_invalid_login(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("locked_out_user")
    page.locator('[data-test="password"]').fill("wrong_password")
    page.locator('[data-test="login-button"]').click()

    expect(page.locator('[data-test="error"]')).to_be_visible()