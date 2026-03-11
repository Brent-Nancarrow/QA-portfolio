from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator('[data-test="title"]')
        self.inventory_items = page.locator('[data-test="inventory-item"]')
        self.add_backpack_button = page.locator('[data-test="add-to-cart-sauce-labs-backpack"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')

    def verify_loaded(self) -> None:
        expect(self.title).to_have_text("Products")

    def get_item_count(self) -> int:
        return self.inventory_items.count()

    def add_backpack_to_cart(self) -> None:
        self.add_backpack_button.click()

    def get_cart_badge_text(self) -> str:
        return self.cart_badge.inner_text()