from enum import Enum


class AccessModel:

    def __init__(self, client_id, client_secret):
        self.grant_type: str = 'client_credentials'
        self.client_id: str = client_id
        self.client_secret: str = client_secret

    def __iter__(self):
        for field in AccessModel.AccessModelEnum:
            yield field.value, getattr(self, field.value)

    class AccessModelEnum(Enum):
        GRAND_TYPE = 'grant_type'
        CLIENT_ID = 'client_id'
        CLIENT_SECRET = 'client_secret'
