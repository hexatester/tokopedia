from . import GetProductApi
from . import GetProductVariantApi


class ProductApi(GetProductApi, GetProductVariantApi):
    pass
