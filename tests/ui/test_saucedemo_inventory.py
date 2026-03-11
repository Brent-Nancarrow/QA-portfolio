import pytest
from playwright.sync_api import Page

from data.users import STANDARD_USER
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.mark.ui
def test_inventory_page_shows_products(page: Page) -> None:
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login_as_user(STANDARD_USER)

    inventory_page.verify_loaded()
    assert inventory_page.get_item_count() > 0


@pytest.mark.ui
def test_adding_backpack_updates_cart_badge(page: Page) -> None:
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login_as_user(STANDARD_USER)

    inventory_page.verify_loaded()
    inventory_page.add_backpack_to_cart()

    assert inventory_page.get_cart_badge_text() == "1"


@pytest.mark.ui
def test_removing_backpack_hides_cart_badge(page: Page) -> None:
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.open()
    login_page.login_as_user(STANDARD_USER)

    inventory_page.verify_loaded()
    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_badge_text() == "1"

    inventory_page.remove_backpack_from_cart()

    assert inventory_page.is_cart_badge_visible() is False