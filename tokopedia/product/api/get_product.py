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
        return self._get(
            url=self._url(f"/inventory/v1/fs/{fsd_id}/product/info"),
            query={"product_id": product_id},
            cl=ResponseProduct,
        )

    def get_product_by_url(self, fsd_id: int, product_url: int) -> ResponseProduct:
        """get_product_by_url This method will retrieve single product information by product url from related fs_id

        Args:
            fsd_id (int): Fulfillment service unique identifier
            product_url (int): product url

        Returns:
            ResponseProduct: Response
        """
        return self._get(
            url=self._url(f"/inventory/v1/fs/{fsd_id}/product/info"),
            query={"product_url": product_url},
            cl=ResponseProduct,
        )

    def get_product_by_sku(self, fsd_id: int, sku: int) -> ResponseProduct:
        """get_product_by_sku This method will retrieve single product information by product sku from related fs_id

        Args:
            fsd_id (int): Fulfillment service unique identifier
            sku (int): Product’s SKU

        Returns:
            ResponseProduct: Response
        """
        return self._get(
            url=self._url(f"/inventory/v1/fs/{fsd_id}/product/info"),
            query={"sku": sku},
            cl=ResponseProduct,
        )

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
        return self._get(
            url=self._url(f"/inventory/v1/fs/{fsd_id}/product/info"),
            query={
                "shop_id": shop_id,
                "page": page,
                "per_page": per_page,
                "sort": sort,
            },
            cl=ResponseProduct,
        )

    def get_all_products(
        self,
        fs_id: int,
        page: int,
        per_page: int,
        product_id: Optional[int] = None,
    ) -> ResponseProductV2:
        """get_all_products This is the new version of Get All Products V1, which adds sku field to the product object.

        Args:
            fs_id (int): Fulfillment service id.
            page (int): Page number to shown.
            per_page (int): The total number of products to be shown on one page.
            product_id (Optional[int], optional): Product ID. Defaults to None.

        Returns:
            ResponseProductV2: Response
        """
        return self._get(
            url=f"/v2/products/fs/{fs_id}/{page}/{per_page}",
            query={"product_id": product_id} if product_id else None,
            cl=ResponseProductV2,
        )

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
    ) -> ResponseActiveProducts:
        """get_all_active_products This endpoint retrieves a list of active products related to shop_id.

        Args:
            fs_id (int): Fulfillment service id.
            shop_id (int): For every fs_id that related to more than one shop_id, request must contain shop_id.
            rows (int): The total number of products to be shown.
            start (int): Show results from n-th product.
            order_by (Optional[int], optional): Product sort options. The default value is sort by name. Available values includes: 1 by promo, 3 by lowest price, 4 by highest price, 5 by highest rating, 8 by highest transaction, 9 by newest, 10 by latest update, 11 by position, 12 by name, 13 by view count, 14 by item sold, 15 by review count, 16 by discussion count, and 23 by best match. Defaults to None.
            keyword (Optional[str], optional): Search by keyword (case insensitive). Defaults to None.
            exclude_keyword (Optional[str], optional): Keyword to be excluded from search. Defaults to None.
            sku (Optional[str], optional): Search by SKU. Defaults to None.
            price_min (Optional[str], optional): Show only product with the minimum price of price_min. Valid value is 1 to 500.000.000. Defaults to None.
            price_max (Optional[str], optional): Show only product with the maximum price of price_max. Valid value is 1 to 500.000.000. Defaults to None.
            preorder (Optional[str], optional): Show only preorder products. Defaults to None.
            free_return (Optional[str], optional): Show only products with free return. Defaults to None.
            wholesale (Optional[str], optional): Show only wholesale products. Defaults to None.

        Returns:
            ResponseActiveProducts: Response
        """
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
        return self._get(
            url=f"/inventory/v1/fs/{fs_id}/product/list",
            query=query,
            cl=ResponseActiveProducts,
        )
