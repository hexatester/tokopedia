import cattr
import json

from tokopedia import BaseTokopedia
from tokopedia.product import ResponseVariantCategory


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
        res = self.session.get(
            url=self._url("/inventory/v1/fs/:fs_id/category/get_variant"),
            query={"cat_id": cat_id},
        )
        data = json.loads(res.text)
        return cattr.structure(data, ResponseVariantCategory)
