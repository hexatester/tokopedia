import cattr
import json
from typing import Optional

from tokopedia import BaseTokopedia
from tokopedia.product import ResponseProduct, ResponseProductV2, ResponseActiveProducts


class GetProductApi(BaseTokopedia):
    def get_product_by_id(self, fsd_id: int, product_id: int) -> ResponseProduct:
        """get_product_by_id This method will retrieve single product information by product id from related fs_id

        Args:
            fsd_id (int): Fulfillment service unique identifier
            product_id (int): product id

        Returns:
            ResponseProduct: Response
        """
        res = self.session.get(
            url=self.url(f"/inventory/v1/fs/{fsd_id}/product/info"),
            query={"product_id": product_id},
        )
        data = json.loads(res.text)
        return cattr.structure(data, ResponseProduct)

    def get_product_by_url(self, fsd_id: int, product_url: int) -> ResponseProduct:
        """get_product_by_url This method will retrieve single product information by product url from related fs_id

        Args:
            fsd_id (int): Fulfillment service unique identifier
            product_url (int): product url

        Returns:
            ResponseProduct: Response
        """
        res = self.session.get(
            url=self.url(f"/inventory/v1/fs/{fsd_id}/product/info"),
            query={"product_url": product_url},
        )
        data = json.loads(res.text)
        return cattr.structure(data, ResponseProduct)

    def get_product_by_sku(self, fsd_id: int, sku: int) -> ResponseProduct:
        """get_product_by_sku This method will retrieve single product information by product sku from related fs_id

        Args:
            fsd_id (int): Fulfillment service unique identifier
            sku (int): Product’s SKU

        Returns:
            ResponseProduct: Response
        """
        res = self.session.get(
            url=self.url(f"/inventory/v1/fs/{fsd_id}/product/info"),
            query={"sku": sku},
        )
        data = json.loads(res.text)
        return cattr.structure(data, ResponseProduct)

    def get_product_from_related_shop_id(
        self,
        fsd_id: int,
        shop_id: int,
        page: int,
        per_page: int,
        sort: int,
    ) -> ResponseProduct:
        """get_product_from_related_shop_id This method will retrieve all product information from related shop id that associate with fs id. This method also support pagination pages.

        Args:
            fsd_id (int): Fulfillment service unique identifier
            shop_id (int): ShopID
            page (int): Page (required if shop_id is filled)
            per_page (int): Page per item (required if shop_id is filled). Maximun items are 50 for 1 page
            sort (int): Sort List Product By available values includes:1 Default, 2 Last Update Product, 3 Highest Sold, 4 Lowest Sold, 5 Highest Price 6 Lowest Price, 7 Product Name Ascending (A-Z), 8 Product Name Descending (Z-A), 9 Fewest Stock, 10 Highest Stock

        Returns:
            ResponseProduct: Response
        """
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

    def get_all_active_products(
        self,
        fs_id: int,
        shop_id: int,
        rows: int,
        start: int,
        order_by: Optional[int] = None,
        keyword: Optional[str] = None,
        exclude_keyword: Optional[str] = None,
        sku: Optional[str] = None,
        price_min: Optional[str] = None,
        price_max: Optional[str] = None,
        preorder: Optional[str] = None,
        free_return: Optional[str] = None,
        wholesale: Optional[str] = None,
    ):
        query = self._query(
            fs_id=fs_id,
            shop_id=shop_id,
            rows=rows,
            start=start,
            order_by=order_by,
            keyword=keyword,
            exclude_keyword=exclude_keyword,
            sku=sku,
            price_min=price_min,
            price_max=price_max,
            preorder=preorder,
            free_return=free_return,
            wholesale=wholesale,
        )
        res = self.session.get(
            url=f"/inventory/v1/fs/{fs_id}/product/list",
            query=query,
        )
        data = json.loads(res.text)
        return cattr.structure(data, ResponseActiveProducts)
