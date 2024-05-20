from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing_extensions import List

from test_project.pages.base_page import BasePage

search_input_locator = (By.CSS_SELECTOR, 'input[data-testid="search-input"]')
track_list_locator = (By.CSS_SELECTOR, '[data-testid="tracklist-row"] a > [data-encore-id="text"]')


class SearchPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def __get_search_input(self) -> WebElement:
        return self.find_element(search_input_locator)

    def is_search_input_displayed(self) -> bool:
        return self.__get_search_input().is_displayed()

    def search_input_send_keys(self, text):
        self.__get_search_input().send_keys(text)

    def __get_track_list(self) -> List[WebElement]:
        return self.find_elements(track_list_locator)

    def get_track_names(self) -> List[str]:
        return [track.text for track in self.__get_track_list()]

