import cattr
from tokopedia.response import ResponseHeader, ErrorResponseHeader
from tokopedia.product import ResponseActiveProducts
from tokopedia.product.active_products import ActiveProducts
from tokopedia.product.active_products import ActiveProductsShop
from tokopedia.product.active_products import ActiveProduct
from tokopedia.product.active_products import ActiveProductShop
from tokopedia.product.active_products import ActiveProductBadge


def test_get_active_products():
    data = {
        "header": {
            "process_time": 5.871520385,
            "messages": "Your request has been processed successfully",
        },
        "data": {
            "total_data": 30,
            "shop": {
                "id": 479573,
                "name": "I`nti.Cosmetic",
                "uri": "https://staging.tokopedia.com/icl",
                "location": "DKI Jakarta",
            },
            "products": [
                {
                    "id": 15245041,
                    "name": "girl",
                    "childs": None,
                    "url": "https://staging.tokopedia.com/icl/girl?trkid=f%3DCa0000L000P0W0S0Sh%2CCo0Po0Fr0Cb0_src%3Dos-inventory-service_page%3D2_ob%3D3_q%3D_po%3D1_catid%3D599",
                    "image_url": "https://ecs7.tokopedia.net/img/cache/200-square/product-1/2019/3/8/5510391/5510391_014c736f-1d7e-4554-bf27-ad0c1a264d1c_843_843.jpg",
                    "image_url_700": "https://ecs7.tokopedia.net/img/cache/700/product-1/2019/3/8/5510391/5510391_014c736f-1d7e-4554-bf27-ad0c1a264d1c_843_843.jpg",
                    "price": "Rp 1.000",
                    "shop": {
                        "id": 479573,
                        "name": "I`nti.Cosmetic",
                        "url": "https://staging.tokopedia.com/icl",
                        "is_gold": False,
                        "location": "Jakarta",
                        "city": "Jakarta",
                        "reputation": "https://inbox.tokopedia.com/reputation/v1/badge/shop/479573",
                        "clover": "https://clover-staging.tokopedia.com/badges/merchant/v1?shop_id=479573",
                    },
                    "wholesale_price": [],
                    "courier_count": 11,
                    "condition": 1,
                    "category_id": 65,
                    "category_name": "Handphone & Tablet",
                    "category_breadcrumb": "handphone-tablet/aksesoris-handphone/skin-handphone",
                    "department_id": 599,
                    "labels": [],
                    "badges": [
                        {
                            "title": "Official Store",
                            "image_url": "https://ecs7.tokopedia.net/img/official_store/badge/OS-Badge-40.png",
                        }
                    ],
                    "is_featured": 0,
                    "rating": 0,
                    "count_review": 0,
                    "original_price": "",
                    "discount_expired": "",
                    "discount_percentage": 0,
                    "sku": "14807",
                    "stock": 500,
                }
            ],
        },
    }
    res: ResponseActiveProducts = cattr.structure(data, ResponseActiveProducts)
    assert isinstance(res.header, ResponseHeader)
    assert isinstance(res, ResponseActiveProducts)
    assert isinstance(res.data, ActiveProducts)
    assert isinstance(res.data.total_data, int)
    assert isinstance(res.data.shop, ActiveProductsShop)
    for product in res.data.products:
        assert isinstance(product, ActiveProduct)
        assert isinstance(product.shop, ActiveProductShop)
        for badge in product.badges:
            assert isinstance(badge, ActiveProductBadge)
        break


def test_get_active_products_error():
    data = {
        "header": {
            "process_time": 0.000048463,
            "messages": "We could not process your request due to malformed request, please check again",
            "reason": "invalid shop_id format",
            "error_code": "PRD_DLV_003",
        },
        "data": None,
    }
    res: ResponseActiveProducts = cattr.structure(data, ResponseActiveProducts)
    assert isinstance(res.header, ErrorResponseHeader)
    assert res.data is None
