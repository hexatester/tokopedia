from . import GetProductApi
from . import GetProductVariantApi
from . import CreateProductApi


class ProductApi(GetProductApi, GetProductVariantApi, CreateProductApi):
    pass
