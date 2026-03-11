from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator('[data-test="title"]')
        self.inventory_items = page.locator('[data-test="inventory-item"]')

    def verify_loaded(self) -> None:
        expect(self.title).to_have_text("Products")

    def get_item_count(self) -> int:
        return self.inventory_items.count()