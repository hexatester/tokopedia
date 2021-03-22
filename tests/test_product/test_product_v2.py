import cattr
from tokopedia.product import ResponseProductV2, ProductV2


def test_get_product_v2():
    data = {
        "data": [
            {
                "product_id": 34,
                "name": "Kemeja Pria",
                "sku": "BF10",
                "shop_id": 479573,
                "shop_name": "I`nti.Cosmetic",
                "category_id": 1805,
                "desc": "A shirt is a cloth garment for the upper body. Originally an undergarment worn exclusively by men, it has become, in American English, a catch-all term for a broad variety of upper-body garments and undergarments.",
                "stock": 100,
                "price": 10000,
                "status": "Active",
            },
            {
                "product_id": 14286600,
                "name": "STABILO Paket Ballpoint Premium Bionic Rollerball - Multicolor",
                "sku": "",
                "shop_id": 479573,
                "shop_name": "I`nti.Cosmetic",
                "category_id": 1774,
                "desc": "Paket\n pulpen premium membuat kegiatan menulis kamu bisa lebih berwarna kenyamanan yang maksimal- memiliki 4 warna Paket\n pulpen premium membuat kegiatan menulis kamu bisa lebih berwarna kenyamanan yang maksimal- memiliki 4 warna",
                "stock": 11,
                "price": 75000,
                "status": "Active",
            },
        ]
    }
    res: ResponseProductV2 = cattr.structure(data, ResponseProductV2)
    assert isinstance(res, ResponseProductV2)
    for data in res.data:
        assert isinstance(data, ProductV2)


def test_get_product_v2_erro():
    data = {"data": [], "status": "200 Ok", "error_message": []}
    res: ResponseProductV2 = cattr.structure(data, ResponseProductV2)
    assert not res.data
    assert isinstance(res.status, str)
    assert isinstance(res.error_message, list)
