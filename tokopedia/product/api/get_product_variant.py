from tokopedia import BaseTokopedia
from tokopedia.product import ResponseVariantCategory, ResponseVariantProduct


class GetProductVariantApi(BaseTokopedia):
    def get_variant_by_category_id(
        self, fs_id: int, cat_id: int
    ) -> ResponseVariantCategory:
        """get_variant_by_category_id This endpoint retrieves a list of variants related to a category_id.

        Args:
            fs_id (int): Fulfillment service id.
            cat_id (int): Category id.

        Returns:
            ResponseVariantCategory: Variants related to category id
        """
        return self._get(
            url=self._url(f"/inventory/v1/fs/{fs_id}/category/get_variant"),
            query={"cat_id": cat_id},
            cl=ResponseVariantCategory,
        )

    def get_variant_by_product_id(
        self, fs_id: int, product_id: int
    ) -> ResponseVariantProduct:
        """get_variant_by_product_id This endpoint retrieves a list of variants related to a product_id.

        Args:
            fs_id (int): Fulfillment service id.
            product_id (int): Product id.

        Returns:
            ResponseVariantProduct: list of variants related to a product_id.
        """
        return self._get(
            url=self._url(f"GET /inventory/v1/fs/{fs_id}/product/variant/{product_id}"),
            query=None,
            cl=ResponseVariantProduct,
        )
