from playwright.sync_api import Locator, expect

from test_project.pages.base_page import BasePage


class SearchPage(BasePage):

    @property
    def search_input(self) -> Locator:
        return self.page.get_by_test_id("search-input")

    def __track_textbox(self, track) -> Locator:
        return self.page.locator('css=[data-testid="tracklist-row"] a > [data-encore-id="text"]', has_text=track)

    def is_search_input_visible(self):
        expect(self.search_input).to_be_visible()

    def fill(self, artist):
        self.search_input.fill(artist)

    def is_track_visible(self, song_name):
        expect(self.__track_textbox(song_name)).to_be_visible()
