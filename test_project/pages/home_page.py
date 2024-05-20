from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from test_project.pages.base_page import BasePage
from framework.utils.settins_utils import settings

cookies_button_selector = (By.CSS_SELECTOR, '#onetrust-accept-btn-handler')
search_button_selector = (By.CSS_SELECTOR, 'a[href="/search"]')


class HomePage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def __get_cookies_button(self) -> WebElement:
        return self.find_element(cookies_button_selector)

    def click_cookies_button(self):
        self.__get_cookies_button().click()

    def is_cookies_button_displayed(self) -> bool:
        return self.__get_cookies_button().is_displayed()

    def wait_until_cookies_button_is_not_displayed(self):
        WebDriverWait(self.browser, settings.implicitly_wait).until(
            ec.invisibility_of_element_located(cookies_button_selector))

    def __get_search_button(self) -> WebElement:
        return self.find_element(search_button_selector)

    def click_search_button(self):
        self.__get_search_button().click()
