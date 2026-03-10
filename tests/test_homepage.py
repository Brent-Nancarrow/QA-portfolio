from playwright.sync_api import Page


def test_playwright_homepage_title(page: Page) -> None:
    page.goto("https://playwright.dev/")
    assert "Playwright" in page.title()