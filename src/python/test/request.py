import requests

from config.config import settings
from model.header import HeaderModel
from model.access import AccessModel


def get_access_information():
    headers = dict(HeaderModel.Headers())
    body = dict(AccessModel(settings.client_id, settings.client_secret))
    return requests.post(
        f'{settings.token_url}',
        data=body,
        headers=headers
    ).json()


private_information = get_access_information()

access_token = private_information.get('access_token')
token_type = private_information.get('token_type')


def get_artist(artist_id):
    headers = dict(HeaderModel.Authorization(token_type, access_token))
    return requests.get(
        f'{settings.base_api_url}/artists/{artist_id}',
        headers=headers
    ).json()


def get_artist_albums(artist_id):
    headers = dict(HeaderModel.Authorization(token_type, access_token))
    return requests.get(
        f'{settings.base_api_url}/artists/{artist_id}/top-tracks',
        headers=headers
    ).json()
