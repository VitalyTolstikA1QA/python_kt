import json


def get_value():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)


class Configuration:

    def __init__(self):
        self.client_id = get_value().get('client_id')
        self.client_secret = get_value().get('client_secret')
        self.token_url = get_value().get('token_url')
        self.base_api_url = get_value().get('base_api_url')


config = Configuration()
