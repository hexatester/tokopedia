import cattr
from tokopedia.response import ResponseHeader, ErrorResponseHeader
from tokopedia.product import ResponseVariantCategory, VariantCategory
from tokopedia.product.variant_category import VariantUnit


def test_get_variant_by_category_id():
    data = {
        "header": {
            "process_time": 0.755010807,
            "messages": "Your request has been processed successfully",
        },
        "data": [
            {
                "variant_id": 6,
                "name": "Ukuran Pakaian",
                "identifier": "size",
                "status": 1,
                "has_unit": 1,
                "units": [
                    {
                        "unit_id": 7,
                        "name": "International",
                        "short_name": "Intl",
                        "values": [
                            {
                                "value_id": 22,
                                "value": "XXS",
                                "hex_code": "",
                                "icon": "",
                            },
                            {"value_id": 23, "value": "XS", "hex_code": "", "icon": ""},
                        ],
                    }
                ],
            }
        ],
    }
    res: ResponseVariantCategory = cattr.structure(data, ResponseVariantCategory)
    assert isinstance(res.header, ResponseHeader)
    assert isinstance(res, ResponseVariantCategory)
    for variant in res.data:
        assert isinstance(variant, VariantCategory)
        for unit in variant.units:
            assert isinstance(unit, VariantUnit)


def test_get_variant_by_category_id_error():
    data = {
        "header": {
            "process_time": 0.000048264,
            "messages": "We could not process your request due to malformed request, please check again",
            "reason": "invalid fs_id format",
            "error_code": "VRT_DLV_002",
        },
        "data": None,
    }
    res: ResponseVariantCategory = cattr.structure(data, ResponseVariantCategory)
    assert isinstance(res.header, ErrorResponseHeader)
    assert res.data is None
