from typing import Mapping, Any


class CSharp:
    @staticmethod
    def add_loot_table_data(data: dict[str, Any], name: str, instant_delivery: bool = False) -> dict[str, Any]:
        data["loot_table"] = {
            "name": name,
            "instant_delivery": instant_delivery
        }
        return data

    @staticmethod
    def add_item_id_data(data: dict[str, Any], name: str, instant_delivery: bool = False) -> dict[str, Any]:
        data["item_id"] = {
            "name": name,
            "instant_delivery": instant_delivery
        }
        return data

    @staticmethod
    def add_vendor_table_extension_data(data: dict[str, Any], vendor: str, item: str) -> dict[str, Any]:
        data["vendor_table_extension"] = {
            "vendor": vendor,
            "item": item
        }
        return data;