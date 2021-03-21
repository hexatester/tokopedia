import cattr
import json
from tokopedia import BaseTokopedia

from . import ResponseProduct


class ProductApi(BaseTokopedia):
    def get_product_by_id(self, fsd_id: int, product_id: int):
        res = self.session.get(
            url=self.url(f"/inventory/v1/fs/{fsd_id}/product/info"),
            query={"product_id": product_id},
        )
        data = json.loads(res.text)
        return cattr.structure(data, ResponseProduct)

    def get_product_by_url(self, fsd_id: int, product_url: int):
        res = self.session.get(
            url=self.url(f"/inventory/v1/fs/{fsd_id}/product/info"),
            query={"product_url": product_url},
        )
        data = json.loads(res.text)
        return cattr.structure(data, ResponseProduct)
