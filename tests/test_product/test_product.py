import cattr
from tokopedia.product import ResponseProduct
from tokopedia.response import ResponseHeader, ErrorResponseHeader


def test_product_by_id():
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
    res: ResponseProduct = cattr.structure(data, ResponseProduct)
    assert isinstance(res, ResponseProduct)
    assert isinstance(res.header, ResponseHeader)


def test_product_by_url_error():
    data = {
        "header": {
            "process_time": 0.000166507,
            "messages": "Our server encounters an error, please try again later",
            "reason": "Error Convert number format into string",
            "error_code": "PRD_USC_024",
        },
        "data": None,
    }
    res: ResponseProduct = cattr.structure(data, ResponseProduct)
    assert isinstance(res, ResponseProduct)
    assert isinstance(res.header, ErrorResponseHeader)


def test_product_by_shop_id():
    data = {
        "header": {
            "process_time": 1.596558594,
            "messages": "Your request has been processed successfully",
        },
        "data": [
            {
                "basic": {
                    "productID": 15330470,
                    "shopID": 479573,
                    "status": 3,
                    "name": "Apple Ceri Bulk 3 Kg 3 kg Sayurbox",
                    "condition": 1,
                    "childCategoryID": 1166,
                    "shortDesc": "Apple Ceri Bulk 3 kg \n [SAYURBOX INFO]\nJam Operasional Toko : 09.00 – 18.00\nOrder di luar jam operasional toko, akan direspon pada jam 09.00 (di hari berikutnya)\nHari Sabtu dan Minggu tetap beroperasional dan ada pengiriman\n\n-Info Pengiriman-\n1. Order yang masuk pukul 00.00-16.00 akan dikirimkan H+1\n2. Order yang masuk oukul 16.01-23.59 akan dikirimkan H+2 \n3. Pengiriman akan dilakukan dengan menggunakan mitra kurir logistik kami agar menjaga kualitas produk kami hingga ke tangan customer\n4. Gratis ongkos kirim untuk minimal order 100.000 dengan KODE: \"SAYURBOXKURIR\"-Info Refund dan Retur(pengiriman kembali) \n\n-Produk-\nDi Sayurbox, kami selalu berusaha menjaga kualitas produk hasil pertanian yang kami sediakan untuk dikirim kepada konsumen kami. Namun, apabila Anda mengalami kendala dari produk yang Anda terima dari Sayurbox, mohon untuk mengklik 'KOMPLAIN PESANAN' agar dapat segera kami prosesUntuk klaim terkait dengan produk Sayurbox hanya untuk barang yang rusak akibat pengantaran atau terdapat barang yang tidak terkirim, maka dari itu kami memerlukan beberapa informasi berikut ini: 1. Foto dari produk yang Anda terima dari Sayurbox sebagai bukti\n1. Proses pengembalian dana atau pengiriman kembali akan dilakukan sehari setelah solusi pada bagian komplain pesanan disetujui\n2. Tidak dikenanakan biaya kirim untuk pengiriman barang kembaliJika ada pertanyaan, silahkan menghubungi kami lewat pesan pribadi di akun Tokopedia Sayurbox ya Sayur Friends. Thank you and happy shopping Sayur Friends ",
                },
                "price": {
                    "value": 180000,
                    "currency": 1,
                    "LastUpdateUnix": 1580804513,
                    "idr": 180000,
                },
                "weight": {"value": 1, "unit": 2},
                "stock": {"useStock": True, "value": 1},
                "main_stock": 1,
                "variant": {},
                "menu": {"id": 1404719, "name": "New Etalase 34561"},
                "preorder": {
                    "order_id": 0,
                    "preorder_type": 0,
                    "preorder_process_time": 0,
                    "preorder_process_start": "",
                    "preorder_deadline": "",
                    "shop_id": 0,
                    "customer_id": 0,
                },
                "extraAttribute": {"minOrder": 1, "lastUpdateCategory": 1580829713},
                "categoryTree": [
                    {
                        "id": 35,
                        "name": "Makanan & Minuman",
                        "title": "Makanan & Minuman",
                        "breadcrumbURL": "https://staging.tokopedia.com/p/makanan-minuman",
                    },
                    {
                        "id": 1159,
                        "name": "Bumbu & Bahan Dasar",
                        "title": "Bumbu & Bahan Dasar",
                        "breadcrumbURL": "https://staging.tokopedia.com/p/makanan-minuman/bumbu-bahan-dasar",
                    },
                    {
                        "id": 1166,
                        "name": "Bumbu & Bahan Dasar Lainnya",
                        "title": "Bumbu & Bahan Dasar Lainnya",
                        "breadcrumbURL": "https://staging.tokopedia.com/p/makanan-minuman/bumbu-bahan-dasar/lainnya",
                    },
                ],
                "pictures": [
                    {
                        "picID": 21356770,
                        "fileName": "479573_93fbd731-e047-4f8b-a292-68123e005420.jpg",
                        "filePath": "product-1/2020/2/4/479573",
                        "status": 2,
                        "OriginalURL": "https://ecs7.tokopedia.net/img/cache/700/product-1/2020/2/4/479573/479573_93fbd731-e047-4f8b-a292-68123e005420.jpg",
                        "ThumbnailURL": "https://ecs7.tokopedia.net/img/cache/200-square/product-1/2020/2/4/479573/479573_93fbd731-e047-4f8b-a292-68123e005420.jpg",
                        "description": "Apel Ceri 3 kg",
                        "width": 300,
                        "height": 300,
                        "URL300": "https://ecs7.tokopedia.net/img/cache/300/product-1/2020/2/4/479573/479573_93fbd731-e047-4f8b-a292-68123e005420.jpg",
                    }
                ],
                "GMStats": {},
                "stats": {},
                "other": {
                    "sku": "1000407",
                    "url": "https://staging.tokopedia.com/icl/apple-ceri-bulk-3-kg-3-kg-sayurbox",
                    "mobileURL": "https://m-staging.tokopedia.com/icl/apple-ceri-bulk-3-kg-3-kg-sayurbox",
                },
                "campaign": {
                    "StartDate": "0001-01-01T00:00:00Z",
                    "EndDate": "0001-01-01T00:00:00Z",
                },
                "warehouses": [
                    {
                        "productID": 15330470,
                        "warehouseID": 1610,
                        "price": {
                            "value": 180000,
                            "currency": 1,
                            "LastUpdateUnix": 1580829713,
                            "idr": 180000,
                        },
                        "stock": {"useStock": True, "value": 1},
                    }
                ],
            },
            {
                "basic": {
                    "productID": 15330458,
                    "shopID": 479573,
                    "status": 1,
                    "name": "A Surprise Fruit Box Promo SPecial 1 pack Sayurbox",
                    "condition": 1,
                    "childCategoryID": 1160,
                    "shortDesc": "A box mix of fruits \n [SAYURBOX INFO]\nJam Operasional Toko : 09.00 – 18.00\nOrder di luar jam operasional toko, akan direspon pada jam 09.00 (di hari berikutnya)\nHari Sabtu dan Minggu tetap beroperasional dan ada pengiriman\n\n-Info Pengiriman-\n1. Order yang masuk pukul 00.00-16.00 akan dikirimkan H+1\n2. Order yang masuk oukul 16.01-23.59 akan dikirimkan H+2 \n3. Pengiriman akan dilakukan dengan menggunakan mitra kurir logistik kami agar menjaga kualitas produk kami hingga ke tangan customer\n4. Gratis ongkos kirim untuk minimal order 100.000 dengan KODE: \"SAYURBOXKURIR\"-Info Refund dan Retur(pengiriman kembali) \n\n-Produk-\nDi Sayurbox, kami selalu berusaha menjaga kualitas produk hasil pertanian yang kami sediakan untuk dikirim kepada konsumen kami. Namun, apabila Anda mengalami kendala dari produk yang Anda terima dari Sayurbox, mohon untuk mengklik 'KOMPLAIN PESANAN' agar dapat segera kami prosesUntuk klaim terkait dengan produk Sayurbox hanya untuk barang yang rusak akibat pengantaran atau terdapat barang yang tidak terkirim, maka dari itu kami memerlukan beberapa informasi berikut ini: 1. Foto dari produk yang Anda terima dari Sayurbox sebagai bukti\n1. Proses pengembalian dana atau pengiriman kembali akan dilakukan sehari setelah solusi pada bagian komplain pesanan disetujui\n2. Tidak dikenanakan biaya kirim untuk pengiriman barang kembaliJika ada pertanyaan, silahkan menghubungi kami lewat pesan pribadi di akun Tokopedia Sayurbox ya Sayur Friends. Thank you and happy shopping Sayur Friends ",
                },
                "price": {
                    "value": 220000,
                    "currency": 1,
                    "LastUpdateUnix": 1580799059,
                    "idr": 220000,
                },
                "weight": {"value": 1, "unit": 2},
                "stock": {
                    "useStock": True,
                    "value": 2000,
                    "stockWording": "<b>Stok terbatas!</b> Tersedia &gt;50",
                },
                "main_stock": 1950,
                "reserve_stock": 50,
                "variant": {},
                "menu": {"id": 1405482, "name": "test etalase"},
                "preorder": {
                    "order_id": 0,
                    "preorder_type": 0,
                    "preorder_process_time": 0,
                    "preorder_process_start": "",
                    "preorder_deadline": "",
                    "shop_id": 0,
                    "customer_id": 0,
                },
                "extraAttribute": {"minOrder": 1, "lastUpdateCategory": 1580824259},
                "categoryTree": [
                    {
                        "id": 35,
                        "name": "Makanan & Minuman",
                        "title": "Makanan & Minuman",
                        "breadcrumbURL": "https://staging.tokopedia.com/p/makanan-minuman",
                    },
                    {
                        "id": 1159,
                        "name": "Bumbu & Bahan Dasar",
                        "title": "Bumbu & Bahan Dasar",
                        "breadcrumbURL": "https://staging.tokopedia.com/p/makanan-minuman/bumbu-bahan-dasar",
                    },
                    {
                        "id": 1160,
                        "name": "Minyak",
                        "title": "Minyak",
                        "breadcrumbURL": "https://staging.tokopedia.com/p/makanan-minuman/bumbu-bahan-dasar/minyak",
                    },
                ],
                "pictures": [
                    {
                        "picID": 21356742,
                        "fileName": "479573_7e98f4e6-d7f9-4e83-b734-c9f494424cd3.jpg",
                        "filePath": "product-1/2020/2/4/479573",
                        "status": 2,
                        "OriginalURL": "https://ecs7.tokopedia.net/img/cache/700/product-1/2020/2/4/479573/479573_7e98f4e6-d7f9-4e83-b734-c9f494424cd3.jpg",
                        "ThumbnailURL": "https://ecs7.tokopedia.net/img/cache/200-square/product-1/2020/2/4/479573/479573_7e98f4e6-d7f9-4e83-b734-c9f494424cd3.jpg",
                        "description": "A Surprise Fruit Box 1 pack",
                        "width": 500,
                        "height": 500,
                        "URL300": "https://ecs7.tokopedia.net/img/cache/300/product-1/2020/2/4/479573/479573_7e98f4e6-d7f9-4e83-b734-c9f494424cd3.jpg",
                    }
                ],
                "GMStats": {},
                "stats": {},
                "other": {
                    "sku": "1001103",
                    "url": "https://staging.tokopedia.com/icl/a-surprise-fruit-box-promo-special-1-pack-sayurbox",
                    "mobileURL": "https://m-staging.tokopedia.com/icl/a-surprise-fruit-box-promo-special-1-pack-sayurbox",
                },
                "campaign": {
                    "StartDate": "0001-01-01T00:00:00Z",
                    "EndDate": "0001-01-01T00:00:00Z",
                },
                "warehouses": [
                    {
                        "productID": 15330458,
                        "warehouseID": 1610,
                        "price": {
                            "value": 220000,
                            "currency": 1,
                            "LastUpdateUnix": 1580824259,
                            "idr": 220000,
                        },
                        "stock": {"useStock": True, "value": 2000},
                    }
                ],
            },
        ],
    }
    res: ResponseProduct = cattr.structure(data, ResponseProduct)
    assert isinstance(res, ResponseProduct)
    assert isinstance(res.header, ResponseHeader)
