import cattr
import json
from requests import Session
from typing import Any, Optional, Type, TypeVar

from tokopedia.utils import register_hooks
from . import AccessToken
from .constants import BASE_URL


T = TypeVar("T", bound=object)


class BaseTokopedia(object):
    def __init__(
        self,
        client_id: str,
        client_secret: str,
        access_token: Optional[AccessToken] = None,
        session: Optional[Session] = None,
        base_url: str = BASE_URL,
    ):
        self._client_id = client_id
        self._client_secret = client_secret
        self._access_token = access_token or AccessToken.create(
            client_id=client_id,
            client_secret=client_secret,
        )
        self._base_url = base_url
        self._session = session or Session()
        if not session:
            self.session.headers.update(self.access_token.create_headers())
        self._register_hooks()

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
            self.session.headers.update(self._access_token.create_headers())
            return self._access_token
        return self._access_token

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def session(self) -> Session:
        return self._session

    def _get(self, url: str, query: Optional[dict], cl: Type[T]) -> T:
        if not url.startswith(self.base_url):
            url = self._url(url)
        res = self.session.get(url=url, query=query)
        data = json.loads(res.text)
        return self._cast(data, cl)

    def _cast(self, obj: Any, cl: Type[T]) -> T:
        return cattr.structure(obj, cl)

    def _url(self, path: str) -> str:
        """url create full url from path

        Args:
            path (str): url path

        Returns:
            str: full url
        """
        return self.base_url + path.lstrip("/")

    def _query(self, *args, **kwargs: Any) -> dict:
        """_query to create query using kwargs

        Returns:
            dict: query
        """
        query = dict()
        key: str
        val: Any
        for key, val in kwargs.keys():  # type: ignore
            if val is not None:
                query[key] = val
        return query

    _register_hooks = staticmethod(register_hooks)
