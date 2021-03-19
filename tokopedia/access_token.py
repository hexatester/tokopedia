import attr
import requests
from base64 import b64encode
from datetime import datetime

from tokopedia.constants import USER_AGENT


@attr.dataclass(slots=True)
class AccessToken:
    access_token: str
    expires_in: int
    token_type: str
    created: datetime = attr.ib(factory=datetime.now)

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
