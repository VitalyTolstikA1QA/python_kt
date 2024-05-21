import pytest
from playwright.sync_api import Page

from test_project.pages.home_page import HomePage
from test_project.pages.search_page import SearchPage


@pytest.mark.ui
@pytest.mark.parametrize(
    'artist, song_name',
    [
        ('Drake', 'One Dance'),
        ('The Beatles', 'Here Comes The Sun - Remastered 2009')
    ]
)
def test_spotify_tracks(page: Page, artist, song_name):
    home_page = HomePage(page)
    home_page.open()
    home_page.is_cookies_button_visible()
    home_page.click_accept_cookies()
    home_page.is_search_button_visible()
    home_page.click_search_button()
    search_page = SearchPage(page)
    search_page.is_search_input_visible()
    search_page.fill(artist)
    search_page.is_track_visible(song_name)
