from . import AccessToken
from .constants import BASE_URL


class Tokopedia:
    def __init__(self, client_id: str, client_secret: str):
        self._client_id = client_id
        self._client_secret = client_secret
        self._access_token = AccessToken.create(
            client_id=client_id,
            client_secret=client_secret,
        )

    @property
    def client_id(self) -> str:
        return self._client_id

    @property
    def access_token(self) -> AccessToken:
        if not self._access_token:
            self._access_token.update(
                client_id=self.client_id,
                client_secret=self._client_secret,
            )
            return self._access_token
        return self._access_token
