from playwright.sync_api import Page, expect

from test_project.pages.base_page import BasePage


class HomePage(BasePage):

    @property
    def cookies_button(self):
        return self.page.get_by_role("button", name="Accept Cookies")

    @property
    def search_button(self):
        return self.page.get_by_test_id("root").get_by_label("Search")

    def click_accept_cookies(self):
        self.cookies_button.click()

    def click_search_button(self):
        self.search_button.click()

    def is_cookies_button_visible(self):
        expect(self.cookies_button).to_be_visible()

    def is_search_button_visible(self):
        expect(self.search_button).to_be_visible()
