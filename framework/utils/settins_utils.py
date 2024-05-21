import json


def get_value():
    with open('settings.json', 'r') as config_file:
        return json.load(config_file)


class Settings:

    def __init__(self):
        self.browser = get_value().get('browser')
        self.implicitly_wait = get_value().get('implicitly_wait')


settings = Settings()
