import pytest
from request import get_artist, get_artist_albums
from model.artist import Artist


@pytest.mark.parametrize(
    'artist_id, genre',
    [
        (Artist.DRAKE.value, 'Rap'),
        (Artist.THE_BEATLES.value, 'British Invasion'),
    ]
)
def test_genre_is_present(artist_id, genre):
    response = get_artist(artist_id)
    genres = response.get('genres')
    assert genre.lower() in genres, f'{genre} was not found in {genres}'


@pytest.mark.parametrize(
    'artist_id, song_name',
    [
        (Artist.THE_BEATLES.value, 'Here Comes The Sun - Remastered 2009'),
        (Artist.DRAKE.value, 'One Dance'),
    ]
)
def test_song_is_present(artist_id, song_name):
    response = get_artist_albums(artist_id)
    tracks = response.get('tracks')
    track_list = [i['name'] for i in tracks if i['name'] is not None]
    assert song_name in track_list, f'{song_name} was not found in {tracks}'
