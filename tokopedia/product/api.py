import cattr
import json
from tokopedia import BaseTokopedia

from . import Product


class ProductApi(BaseTokopedia):
    def get_product_by_id(self, fsd_id: int, product_id: int):
        res = self.session.get(
            url=self.url(f"/inventory/v1/fs/{fsd_id}/product/info"),
            query={"product_id": product_id},
        )
        data = json.loads(res.text)
        return cattr.structure(data, Product)
