import allure

from framework.interface_drivers.http.api_util import get, post
from test_project.models.access import AccessModel
from test_project.models.header import HeaderModel
from framework.utils.config_utils import config


@allure.step('Get access information')
def get_access_information():
    return post(f'{config.token_url}', AccessModel(config.client_id, config.client_secret), HeaderModel.Headers())


@allure.step('Get token and token type')
def get_tokens():
    status_code, private_information = get_access_information()
    assert status_code == 200

    access_token = private_information.get('access_token')
    token_type = private_information.get('token_type')

    return HeaderModel.Authorization(token_type, access_token)


@allure.step('Get artist')
def get_artist(artist_id):
    return get(f'{config.base_api_url}/artists/{artist_id}', get_tokens())


@allure.step('Get artist album')
def get_artist_albums(artist_id):
    return get(f'{config.base_api_url}/artists/{artist_id}/top-tracks', get_tokens())
