from attr import asdict
from typing import List

from tokopedia import BaseTokopedia
from tokopedia.product import CreateProductV3, ResponsesCreateProductV3


class CreateProductApi(BaseTokopedia):
    def create_product_v3(
        self,
        fs_id: int,
        shop_id: int,
        products: List[CreateProductV3],
    ) -> ResponsesCreateProductV3:
        return self._post(
            url=self._url(f"/inventory/v1/fs/{fs_id}/product/info"),
            data={"products": [asdict(produk) for produk in products]},
            cl=ResponsesCreateProductV3,
        )

    def create_product_v3_with_variant(self):
        pass
