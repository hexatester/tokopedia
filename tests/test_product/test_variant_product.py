import cattr
from tokopedia.response import ResponseHeader, ErrorResponseHeader
from tokopedia.product import ResponseVariantProduct, VariantProduct
from tokopedia.product.variant_product import VariantChildren, Variant


def test_get_variant_by_product_id():
    data = {
        "header": {
            "process_time": 0.92548774,
            "messages": "Your request has been processed successfully",
        },
        "data": {
            "parent_id": 15330203,
            "default_child": 15330204,
            "sizechart": "",
            "variant": [
                {
                    "name": "warna",
                    "identifier": "colour",
                    "unit_name": "",
                    "position": 1,
                    "option": [
                        {"id": 41368, "value": "Hijau", "hex": "#006400"},
                        {"id": 41369, "value": "Merah", "hex": "#ff0016"},
                    ],
                },
                {
                    "name": "ukuran",
                    "identifier": "size",
                    "unit_name": "Default",
                    "position": 2,
                    "option": [
                        {"id": 41371, "value": "XL", "hex": ""},
                        {"id": 41370, "value": "All Size", "hex": ""},
                    ],
                },
            ],
            "children": [
                {
                    "name": "Toped Ijo - Hijau, All Size",
                    "url": "https://staging.tokopedia.com/tkpdcoba/toped-ijo-hijau-all-size",
                    "product_id": 15330204,
                    "price": 100,
                    "price_fmt": "Rp 100",
                    "stock": 29,
                    "main_stock": 27,
                    "reserve_stock": 2,
                    "sku": "ijo-all",
                    "option_ids": [41368, 41370],
                    "enabled": True,
                    "is_buyable": True,
                    "is_wishlist": False,
                    "picture": {
                        "original": "https://ecs7.tokopedia.net/img/cache/700/product-1/2020/2/3/8974926/8974926_d0a57f36-c4fc-45a5-9ff1-7f23187ff18a_2048_2047",
                        "thumbnail": "https://ecs7.tokopedia.net/img/cache/200-square/product-1/2020/2/3/8974926/8974926_d0a57f36-c4fc-45a5-9ff1-7f23187ff18a_2048_2047",
                    },
                    "campaign": {
                        "is_active": False,
                        "discounted_percentage": 0,
                        "discounted_price": 0,
                        "discounted_price_fmt": "",
                        "campaign_type": 0,
                        "campaign_type_name": "",
                        "start_date": "",
                        "end_date": "",
                    },
                    "always_available": False,
                    "stock_wording": "Stok terbatas! Tersedia >20",
                    "other_variant_stock": "available",
                    "is_limited_stock": False,
                },
                {
                    "name": "Toped Ijo - Merah, All Size",
                    "url": "https://staging.tokopedia.com/tkpdcoba/toped-ijo-merah-all-size",
                    "product_id": 15330205,
                    "price": 200,
                    "price_fmt": "Rp 200",
                    "stock": 10,
                    "main_stock": 10,
                    "sku": "abang-all",
                    "option_ids": [41369, 41370],
                    "enabled": True,
                    "is_buyable": True,
                    "is_wishlist": False,
                    "picture": {
                        "original": "https://ecs7.tokopedia.net/img/cache/700/product-1/2020/2/3/8974926/8974926_d0a57f36-c4fc-45a5-9ff1-7f23187ff18a_2048_2047",
                        "thumbnail": "https://ecs7.tokopedia.net/img/cache/200-square/product-1/2020/2/3/8974926/8974926_d0a57f36-c4fc-45a5-9ff1-7f23187ff18a_2048_2047",
                    },
                    "campaign": {
                        "is_active": False,
                        "discounted_percentage": 0,
                        "discounted_price": 0,
                        "discounted_price_fmt": "",
                        "campaign_type": 0,
                        "campaign_type_name": "",
                        "start_date": "",
                        "end_date": "",
                    },
                    "always_available": False,
                    "stock_wording": "Stok hampir habis! Tersisa <20",
                    "other_variant_stock": "available",
                    "is_limited_stock": False,
                },
                {
                    "name": "Toped Ijo - Hijau, XL",
                    "url": "https://staging.tokopedia.com/tkpdcoba/toped-ijo-hijau-xl",
                    "product_id": 15330206,
                    "price": 300,
                    "price_fmt": "Rp 300",
                    "stock": 40,
                    "main_stock": 40,
                    "sku": "ijo-xl",
                    "option_ids": [41368, 41371],
                    "enabled": True,
                    "is_buyable": True,
                    "is_wishlist": False,
                    "picture": {
                        "original": "https://ecs7.tokopedia.net/img/cache/700/product-1/2020/2/3/8974926/8974926_d0a57f36-c4fc-45a5-9ff1-7f23187ff18a_2048_2047",
                        "thumbnail": "https://ecs7.tokopedia.net/img/cache/200-square/product-1/2020/2/3/8974926/8974926_d0a57f36-c4fc-45a5-9ff1-7f23187ff18a_2048_2047",
                    },
                    "campaign": {
                        "is_active": False,
                        "discounted_percentage": 0,
                        "discounted_price": 0,
                        "discounted_price_fmt": "",
                        "campaign_type": 0,
                        "campaign_type_name": "",
                        "start_date": "",
                        "end_date": "",
                    },
                    "always_available": False,
                    "stock_wording": "Stok terbatas! Tersedia >20",
                    "other_variant_stock": "available",
                    "is_limited_stock": False,
                },
                {
                    "name": "Toped Ijo - Merah, XL",
                    "url": "https://staging.tokopedia.com/tkpdcoba/toped-ijo-merah-xl",
                    "product_id": 15330207,
                    "price": 400,
                    "price_fmt": "Rp 400",
                    "stock": 10,
                    "main_stock": 10,
                    "sku": "abang-all",
                    "option_ids": [41369, 41371],
                    "enabled": True,
                    "is_buyable": True,
                    "is_wishlist": False,
                    "picture": {
                        "original": "https://ecs7.tokopedia.net/img/cache/700/product-1/2020/2/3/8974926/8974926_d0a57f36-c4fc-45a5-9ff1-7f23187ff18a_2048_2047",
                        "thumbnail": "https://ecs7.tokopedia.net/img/cache/200-square/product-1/2020/2/3/8974926/8974926_d0a57f36-c4fc-45a5-9ff1-7f23187ff18a_2048_2047",
                    },
                    "campaign": {
                        "is_active": False,
                        "discounted_percentage": 0,
                        "discounted_price": 0,
                        "discounted_price_fmt": "",
                        "campaign_type": 0,
                        "campaign_type_name": "",
                        "start_date": "",
                        "end_date": "",
                    },
                    "always_available": False,
                    "stock_wording": "Stok hampir habis! Tersisa <20",
                    "other_variant_stock": "available",
                    "is_limited_stock": False,
                },
            ],
        },
    }
    res: ResponseVariantProduct = cattr.structure(data, ResponseVariantProduct)
    assert isinstance(res, ResponseVariantProduct)
    assert isinstance(res.data, VariantProduct)
    assert isinstance(res.header, ResponseHeader)
    for variant in res.data.variant:
        assert isinstance(variant, Variant)
    for children in res.data.children:
        assert isinstance(children, VariantChildren)


def test_get_variant_by_product_id_error():
    data = {
        "header": {
            "process_time": 0.903005513,
            "messages": "We could not process your request due to malformed request, please check again",
            "reason": "Failed Send GRPC Request",
            "error_code": "PRD_GRPC_001",
        },
        "data": None,
    }
    res: ResponseVariantProduct = cattr.structure(data, ResponseVariantProduct)
    assert isinstance(res, ResponseVariantProduct)
    assert res.data is None
    assert isinstance(res.header, ErrorResponseHeader)
