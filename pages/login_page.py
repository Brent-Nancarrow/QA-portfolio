from playwright.sync_api import Page

from config.settings import BASE_URL


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_message = page.locator('[data-test="error"]')

    def open(self) -> None:
        self.page.goto(BASE_URL)

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def login_as_user(self, user: dict) -> None:
        self.login(user["username"], user["password"])

    def get_error_message(self) -> str:
        return self.error_message.inner_text()