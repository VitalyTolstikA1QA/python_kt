import pytest
from test_project.api_call_builders.request import get_artist, get_artist_albums
from test_project.models.artist import Artist
from framework.data_processors.json.json_util import get_value


@pytest.mark.parametrize(
    'artist_id, genre',
    [
        (Artist.DRAKE.value, 'Rap'),
        (Artist.THE_BEATLES.value, 'British Invasion'),
    ]
)
def test_genre_is_present(artist_id, genre):
    status_code, artist = get_artist(artist_id)
    assert status_code == 200
    genres = get_value(artist, 'genres')
    assert genre.lower() in genres, f'{genre} was not found in {genres}'


@pytest.mark.parametrize(
    'artist_id, song_name',
    [
        (Artist.THE_BEATLES.value, 'Here Comes The Sun - Remastered 2009'),
        (Artist.DRAKE.value, 'One Dance'),
    ]
)
def test_song_is_present(artist_id, song_name):
    status_code, album = get_artist_albums(artist_id)
    assert status_code == 200
    tracks = get_value(album, 'tracks')
    track_list = [i['name'] for i in tracks if i['name'] is not None]
    assert song_name in track_list, f'{song_name} was not found in {tracks}'
