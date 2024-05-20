import pytest
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
def test_spotify_tracks(browser, artist, song_name):
    home_page = HomePage(browser)
    home_page.open('https://spotify.com')
    assert home_page.is_cookies_button_displayed(), 'Accept cookies button is not displayed'
    home_page.click_cookies_button()
    home_page.wait_until_cookies_button_is_not_displayed()
    assert not home_page.is_cookies_button_displayed(), 'Accept cookies button is displayed'
    home_page.click_search_button()
    search_page = SearchPage(browser)
    assert search_page.is_search_input_displayed(), 'Search input field is not displayed'
    search_page.search_input_send_keys(artist)
    track_names = search_page.get_track_names()
    assert song_name in track_names, f'{song_name} is not present in current list - {track_names}'
