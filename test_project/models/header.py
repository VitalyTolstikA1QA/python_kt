class HeaderModel:
    class Headers:
        def __init__(self, content_type='application/x-www-form-urlencoded'):
            self.content_type: str = content_type

        def __iter__(self):
            yield 'Content-Type', self.content_type

    class Authorization:
        def __init__(self, token_type, access_token):
            self.token_type: str = token_type
            self.access_token: str = access_token

        def make_authorization(self) -> str:
            return f'{self.token_type} {self.access_token}'

        def __iter__(self):
            yield 'Authorization', self.make_authorization()


