import cattr
import json
from typing import Optional

from tokopedia import BaseTokopedia
from tokopedia.product import ResponseProduct, ResponseProductV2


class GetProductApi(BaseTokopedia):
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

    def get_product_by_sku(self, fsd_id: int, sku: int):
        res = self.session.get(
            url=self.url(f"/inventory/v1/fs/{fsd_id}/product/info"),
            query={"sku": sku},
        )
        data = json.loads(res.text)
        return cattr.structure(data, ResponseProduct)

    def get_product_from_related_shop_id(
        self, fsd_id: int, shop_id: int, page: int, per_page: int, sort: int
    ):
        res = self.session.get(
            url=self.url(f"/inventory/v1/fs/{fsd_id}/product/info"),
            query={
                "shop_id": shop_id,
                "page": page,
                "per_page": per_page,
                "sort": sort,
            },
        )
        data = json.loads(res.text)
        return cattr.structure(data, ResponseProduct)

    def get_all_products(
        self,
        fs_id: int,
        page: int,
        per_page: int,
        product_id: Optional[int] = None,
    ):
        res = self.session.get(
            url=f"/v2/products/fs/{fs_id}/{page}/{per_page}",
            query={"product_id": product_id} if product_id else None,
        )
        data = json.loads(res.text)
        return cattr.structure(data, ResponseProductV2)
