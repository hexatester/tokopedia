from typing import Optional

from . import AccessToken
from .constants import BASE_URL


class BaseTokopedia(object):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        access_token: Optional[AccessToken] = None,
        base_url: str = BASE_URL,
    ):
        self._client_id = client_id
        self._client_secret = client_secret
        self._access_token = access_token or AccessToken.create(
            client_id=client_id,
            client_secret=client_secret,
        )
        self._base_url = base_url

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

    @property
    def base_url(self) -> str:
        return self._base_url
