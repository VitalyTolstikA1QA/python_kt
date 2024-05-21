import json
from pathlib import Path


def get_value():
    config_path = Path(__file__).parent.parent.parent / 'configuration' / 'config.json'
    with open(config_path, 'r') as config_file:
        return json.load(config_file)


class Configuration:

    def __init__(self):
        self.client_id = get_value().get('client_id')
        self.client_secret = get_value().get('client_secret')
        self.token_url = get_value().get('token_url')
        self.base_api_url = get_value().get('base_api_url')
        self.base_ui_url = get_value().get('base_ui_url')


config = Configuration()
