import cattr
from tokopedia.product import CreateProductV3, ResponsesCreateProductV3


def test_create_product_v3():
    data = {
        "name": "Product Testing V3 1.36",
        "condition": "NEW",
        "description": "Product Testing Descr V2",
        "sku": "TST21",
        "price": 10000,
        "status": "LIMITED",
        "stock": 900,
        "min_order": 1,
        "category_id": 562,
        "dimension": {"height": 2, "width": 3, "length": 4},
        "custom_product_logistics": [24, 4, 64],
        "annotations": ["1"],
        "price_currency": "IDR",
        "weight": 200,
        "weight_unit": "GR",
        "is_free_return": False,
        "is_must_insurance": False,
        "etalase": {"id": 1402922},
        "pictures": [
            {
                "file_path": "https://ecs7.tokopedia.net/img/cache/700/product-1/2017/9/27/5510391/5510391_9968635e-a6f4-446a-84d0-ff3a98a5d4a2.jpg"
            }
        ],
        "wholesale": [{"min_qty": 2, "price": 9500}, {"min_qty": 3, "price": 9000}],
    }
    create_product_v3 = cattr.structure(data, CreateProductV3)
    assert isinstance(create_product_v3, CreateProductV3)


def test_response_success_create_product_v3():
    data = {
        "header": {
            "process_time": 1.054341405,
            "messages": "Your request has been processed successfully",
        },
        "data": {
            "total_data": 1,
            "success_data": 1,
            "fail_data": 0,
            "success_rows_data": [{"product_id": 2147732129}],
        },
    }
    response_create_product_v3 = cattr.structure(data, ResponsesCreateProductV3)
    assert isinstance(response_create_product_v3, ResponsesCreateProductV3)


def test_response_error_create_product_v3():
    data = {
        "header": {
            "process_time": 0.702986751,
            "messages": "Your request has been processed successfully",
        },
        "data": {
            "total_data": 1,
            "success_data": 0,
            "fail_data": 1,
            "failed_rows_data": [
                {
                    "product_name": "Product Testing V3 1.39",
                    "product_price": 10000,
                    "sku": "TST21",
                    "error": [
                        "Value [Product Testing V3 1.39] of field [name] is already used, please use different value"
                    ],
                }
            ],
        },
    }
    response_create_product_v3 = cattr.structure(data, ResponsesCreateProductV3)
    assert isinstance(response_create_product_v3, ResponsesCreateProductV3)
