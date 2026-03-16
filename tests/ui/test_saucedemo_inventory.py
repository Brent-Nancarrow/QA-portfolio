import allure
import pytest
from playwright.sync_api import Page

from data.users import STANDARD_USER
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@allure.feature("Sauce Demo UI")
@allure.story("Inventory")
@allure.title("Inventory page shows available products after a successful login")
@pytest.mark.ui
def test_inventory_page_shows_products(page: Page) -> None:
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    with allure.step("Open the login page"):
        login_page.open()

    with allure.step("Log in as the standard user"):
        login_page.login_as_user(STANDARD_USER)

    with allure.step("Check the inventory page loads"):
        inventory_page.verify_loaded()

    with allure.step("Check at least one product is shown"):
        assert inventory_page.get_item_count() > 0


@allure.feature("Sauce Demo UI")
@allure.story("Cart")
@allure.title("Adding the backpack updates the cart badge to 1")
@pytest.mark.ui
def test_adding_backpack_updates_cart_badge(page: Page) -> None:
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    with allure.step("Open the login page"):
        login_page.open()

    with allure.step("Log in as the standard user"):
        login_page.login_as_user(STANDARD_USER)

    with allure.step("Check the inventory page loads"):
        inventory_page.verify_loaded()

    with allure.step("Add the backpack to the cart"):
        inventory_page.add_backpack_to_cart()

    with allure.step("Check the cart badge shows 1 item"):
        assert inventory_page.get_cart_badge_text() == "1"


@allure.feature("Sauce Demo UI")
@allure.story("Cart")
@allure.title("Removing the backpack hides the cart badge")
@pytest.mark.ui
def test_removing_backpack_hides_cart_badge(page: Page) -> None:
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    with allure.step("Open the login page"):
        login_page.open()

    with allure.step("Log in as the standard user"):
        login_page.login_as_user(STANDARD_USER)

    with allure.step("Check the inventory page loads"):
        inventory_page.verify_loaded()

    with allure.step("Add the backpack so the cart badge appears"):
        inventory_page.add_backpack_to_cart()
        assert inventory_page.get_cart_badge_text() == "1"

    with allure.step("Remove the backpack from the cart"):
        inventory_page.remove_backpack_from_cart()

    with allure.step("Check the cart badge is no longer visible"):
        assert inventory_page.is_cart_badge_visible() is False