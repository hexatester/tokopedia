from typing import Optional

from . import BaseTokopedia
from . import ProductApi
from .constants import BASE_URL


class Tokopedia(BaseTokopedia):
    def __init__(
        self,
        client_id,
        client_secret,
        access_token=None,
        session=None,
        base_url=BASE_URL,
    ):
        super().__init__(
            client_id,
            client_secret,
            access_token=access_token,
            session=session,
            base_url=base_url,
        )
        self._product: Optional[ProductApi] = None

    @property
    def product(self) -> ProductApi:
        if self._product:
            return self._product
        self._product = ProductApi(
            self.client_id,
            self._client_secret,
            self.access_token,
            self.session,
            self.base_url,
        )
        return self._product
