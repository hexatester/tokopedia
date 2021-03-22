import cattr
from tokopedia.product import ResponseProduct
from tokopedia.utils import register_hooks


def test_product():
    register_hooks()
    data = {
        "header": {
            "process_time": 5.871520385,
            "messages": "Your request has been processed successfully",
        },
        "data": [
            {
                "basic": {
                    "productID": 15245228,
                    "shopID": 480829,
                    "status": 1,
                    "name": "hxh wallpaper best la zzzz",
                    "condition": 1,
                    "childCategoryID": 1828,
                    "shortDesc": "Best wallpaper for hxh",
                },
                "price": {
                    "value": 3000,
                    "currency": 1,
                    "LastUpdateUnix": 1557981264,
                    "idr": 3000,
                },
                "weight": {"value": 5, "unit": 1},
                "stock": {
                    "value": 10,
                    "stockWording": "<b>Stok hampir habis!</b> Tersisa &lt;20",
                },
                "main_stock": 7,
                "reserve_stock": 3,
                "variant": {
                    "isParent": True,
                    "isVariant": True,
                    "childrenID": [15245978, 15245979],
                },
                "menu": {"id": 1405065, "name": "Wallpapers"},
                "preorder": {},
                "extraAttribute": {
                    "minOrder": 1,
                    "lastUpdateCategory": 1554708202,
                    "isEligibleCOD": True,
                },
                "categoryTree": [
                    {
                        "id": 1759,
                        "name": "Fashion Pria",
                        "title": "Fashion Pria",
                        "breadcrumbURL": "https://staging.tokopedia.com/p/fashion-pria",
                    },
                    {
                        "id": 1787,
                        "name": "Celana",
                        "title": "Celana",
                        "breadcrumbURL": "https://staging.tokopedia.com/p/fashion-pria/celana",
                    },
                    {
                        "id": 1828,
                        "name": "Celana Jeans",
                        "title": "Celana Jeans",
                        "breadcrumbURL": "https://staging.tokopedia.com/p/fashion-pria/celana/celana-jeans",
                    },
                ],
                "pictures": [
                    {
                        "picID": 21189631,
                        "fileName": "5510908_a4b5f7a2-2451-45f2-8a83-979808fe28d3_1920_1080.jpg",
                        "filePath": "product-1/2019/3/12/5510908",
                        "status": 2,
                        "OriginalURL": "https://ecs7.tokopedia.net/img/cache/700/product-1/2019/3/12/5510908/5510908_a4b5f7a2-2451-45f2-8a83-979808fe28d3_1920_1080.jpg",
                        "ThumbnailURL": "https://ecs7.tokopedia.net/img/cache/200-square/product-1/2019/3/12/5510908/5510908_a4b5f7a2-2451-45f2-8a83-979808fe28d3_1920_1080.jpg",
                        "width": 1920,
                        "height": 1080,
                        "URL300": "https://ecs7.tokopedia.net/img/cache/300/product-1/2019/3/12/5510908/5510908_a4b5f7a2-2451-45f2-8a83-979808fe28d3_1920_1080.jpg",
                    },
                    {
                        "picID": 21191044,
                        "fileName": "5510908_a99b769d-5e7a-44da-9a04-2ed1cc6efa32_441_441",
                        "filePath": "product-1/2019/4/8/5510908",
                        "status": 1,
                        "OriginalURL": "https://ecs7.tokopedia.net/img/cache/700/product-1/2019/4/8/5510908/5510908_a99b769d-5e7a-44da-9a04-2ed1cc6efa32_441_441",
                        "ThumbnailURL": "https://ecs7.tokopedia.net/img/cache/200-square/product-1/2019/4/8/5510908/5510908_a99b769d-5e7a-44da-9a04-2ed1cc6efa32_441_441",
                        "width": 441,
                        "height": 441,
                        "URL300": "https://ecs7.tokopedia.net/img/cache/300/product-1/2019/4/8/5510908/5510908_a99b769d-5e7a-44da-9a04-2ed1cc6efa32_441_441",
                    },
                ],
                "GMStats": {
                    "transactionSuccess": 3,
                    "transactionReject": 69,
                    "countSold": 3,
                },
                "stats": {"countView": 163},
                "other": {
                    "sku": "12345",
                    "url": "https://staging.tokopedia.com/mattleeshoppe/hxh-wallpaper-best-la-zzzz",
                    "mobileURL": "https://m-staging.tokopedia.com/mattleeshoppe/hxh-wallpaper-best-la-zzzz",
                },
                "campaign": {
                    "StartDate": "0001-01-01T00:00:00Z",
                    "EndDate": "0001-01-01T00:00:00Z",
                },
                "warehouses": [
                    {
                        "productID": 15245228,
                        "warehouseID": 5,
                        "price": {
                            "value": 3000,
                            "currency": 1,
                            "LastUpdateUnix": 1558006464,
                            "idr": 3000,
                        },
                        "stock": {"useStock": True, "value": 10},
                    },
                    {
                        "productID": 15245228,
                        "warehouseID": 84,
                        "price": {
                            "value": 3000,
                            "currency": 1,
                            "LastUpdateUnix": 1558006464,
                            "idr": 3000,
                        },
                        "stock": {"useStock": True, "value": 1},
                    },
                    {
                        "productID": 15245228,
                        "warehouseID": 96,
                        "price": {
                            "value": 3000,
                            "currency": 1,
                            "LastUpdateUnix": 1558006464,
                            "idr": 3000,
                        },
                        "stock": {"useStock": True, "value": 1000},
                    },
                ],
            }
        ],
    }
    res = cattr.structure(data, ResponseProduct)
    assert isinstance(res, ResponseProduct)


def test_product_error():
    data = {
        "header": {
            "process_time": 0.000166507,
            "messages": "Our server encounters an error, please try again later",
            "reason": "Error Convert number format into string",
            "error_code": "PRD_USC_024",
        },
        "data": None,
    }
    res = cattr.structure(data, ResponseProduct)
    assert isinstance(res, ResponseProduct)
