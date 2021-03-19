import attr
import requests
from base64 import b64encode
from datetime import datetime
from typing import Dict, Optional

from tokopedia.constants import USER_AGENT


@attr.dataclass(slots=True)
class AccessToken:
    access_token: str
    expires_in: int
    token_type: str
    created: datetime = attr.ib(factory=datetime.now)

    @property
    def when_expires(self) -> datetime:
        return datetime.fromtimestamp(self.created.timestamp() + self.expires_in)

    @property
    def is_expires(self) -> bool:
        return self.when_expires > datetime.now()

    def create_headers(self, headers: Optional[Dict] = None) -> Dict:
        headers = headers or dict()
        headers.update({"Authorization": f"{self.token_type} {self.access_token}"})
        return headers

    @classmethod
    def create(
        cls,
        client_id: str,
        client_secret: str,
        url: str = "https://accounts.tokopedia.com/token",
    ) -> "AccessToken":
        auth = b64encode(f"{client_id}:{client_secret}")
        headers = {"Authorization": f"Basic {auth}", "User-Agent": USER_AGENT}
        query = {"grant_type": "client_credentials"}
        res = requests.post(
            url=url,
            data=None,
            headers=headers,
            query=query,
        )
        return cls(**res.json())
