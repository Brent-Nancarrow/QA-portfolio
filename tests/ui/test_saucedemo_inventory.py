import pytest
from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.ui
def test_inventory_page_shows_products(page: Page) -> None:
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.verify_loaded()
    assert inventory_page.get_item_count() > 0