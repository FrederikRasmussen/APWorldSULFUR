from typing import Optional, Mapping, Any

from BaseClasses import Item, ItemClassification
from .csharp_data import CSharp
from .tags import ItemTags

class SulfurItem(Item):
    def __init__(
            self,
            player: int,
            code: Optional[int],
            classification: ItemClassification,
            name: str,
            tags: list[str],
            slot_data:  Optional[Mapping[str, Any]] = None
    ):
        super().__init__(name, classification, code, player)
        self.sulfur_tags = tags
        self.sulfur_slot_data = slot_data

def all_items(player: int) -> list[Item]:
    code = 0
    def new_item(
            classification: ItemClassification,
            name: str,
            tags: list[str],
            slot_data: Optional[Mapping[str, Any]] = None
    ):
        nonlocal code
        code = code + 1
        return SulfurItem(player, code, classification, name, tags, slot_data)
    return [
        # Misc filler
        new_item(
            ItemClassification.filler,
            "Mining explosive",
            [ItemTags.csharp_loot_table, ItemTags.group_repeatable],
            slot_data=CSharp.add_loot_table_data(
                {}, "LooseLoot_Weapon_MiningExplosive", True
            )
        ),
        new_item(
            ItemClassification.filler,
            "Sulf",
            [ItemTags.csharp_sulf, ItemTags.group_repeatable],
        ),

        # Food
        new_item(
            ItemClassification.filler,
            "Goblin cooking",
            [ItemTags.csharp_loot_table, ItemTags.group_repeatable],
            slot_data=CSharp.add_loot_table_data(
                {}, "Archipelago_Food_Goblin", True
            )
        ),
        new_item(
            ItemClassification.filler,
            "Town market meal",
            [ItemTags.csharp_loot_table, ItemTags.group_repeatable],
            slot_data=CSharp.add_loot_table_data(
                {}, "Archipelago_Food_Town", True
            )
        ),
        new_item(
            ItemClassification.filler,
            "Questionable sewer treats",
            [ItemTags.csharp_loot_table, ItemTags.group_repeatable],
            slot_data=CSharp.add_loot_table_data(
                {}, "Archipelago_Food_Sewer", True
            )
        ),
        new_item(
            ItemClassification.filler,
            "Prisoner's last meal",
            [ItemTags.csharp_loot_table, ItemTags.group_repeatable],
            slot_data=CSharp.add_loot_table_data(
                {}, "Archipelago_Food_Dungeon", True
            )
        ),
        new_item(
            ItemClassification.filler,
            "Castle feast",
            [ItemTags.csharp_loot_table, ItemTags.group_repeatable],
            slot_data=CSharp.add_loot_table_data(
                {}, "Archipelago_Food_Castle", True
            )
        ),
        new_item(
            ItemClassification.filler,
            "Camping-compatible eats",
            [ItemTags.csharp_loot_table, ItemTags.group_repeatable],
            slot_data=CSharp.add_loot_table_data(
                {}, "Archipelago_Food_Forest", True
            )
        ),
        new_item(
            ItemClassification.filler,
            "Wash'oku",
            [ItemTags.csharp_loot_table, ItemTags.group_repeatable],
            slot_data=CSharp.add_loot_table_data(
                {}, "Archipelago_Food_Fortress", True
            )
        ),
        new_item(
            ItemClassification.filler,
            "Sandy plates",
            [ItemTags.csharp_loot_table, ItemTags.group_repeatable],
            slot_data=CSharp.add_loot_table_data(
                {}, "Archipelago_Food_Desert", True
            )
        ),
        new_item(
            ItemClassification.filler,
            "Fast food",
            [ ItemTags.csharp_loot_table, ItemTags.group_repeatable],
            slot_data=CSharp.add_loot_table_data(
                {}, "Archipelago_Food_Fast_Food", True
            )
        ),

        # Cooking recipes
        new_item(
            ItemClassification.filler,
            "Food for Desert Survival",
            [ItemTags.csharp_item_id, ItemTags.group_recipes],
            slot_data=CSharp.add_item_id_data(
                {}, "Manual_DesertCooking"
            )
        ),
        new_item(
            ItemClassification.filler,
            "GABBA FOODMAKE",
            [ItemTags.csharp_item_id, ItemTags.group_recipes],
            slot_data=CSharp.add_item_id_data(
                {}, "Manual_GoblinCooking"
            )
        ),
        new_item(
            ItemClassification.filler,
            "From the Cellar",
            [ItemTags.csharp_item_id, ItemTags.group_recipes],
            slot_data=CSharp.add_item_id_data(
                {}, "Manual_CookingDungeon"
            )
        ),
        new_item(
            ItemClassification.filler,
            "Delicacies of the Forest",
            [ItemTags.csharp_item_id, ItemTags.group_recipes],
            slot_data=CSharp.add_item_id_data(
                {}, "Manual_ForestCooking"
            )
        ),
        new_item(
            ItemClassification.filler,
            "Shav'Wani delights",
            [ItemTags.csharp_item_id, ItemTags.group_recipes],
            slot_data=CSharp.add_item_id_data(
                {}, "Manual_CookingFortress"
            )
        ),
        new_item(
            ItemClassification.filler,
            "Eating as Royals",
            [ItemTags.csharp_item_id, ItemTags.group_recipes],
            slot_data=CSharp.add_item_id_data(
                {}, "Manual_CookingCastle"
            )
        ),
        new_item(
            ItemClassification.filler,
            "Tastes From the Sewers™️",
            [ItemTags.csharp_item_id, ItemTags.group_recipes],
            slot_data=CSharp.add_item_id_data(
                {}, "Manual_CookingSewers"
            )
        ),
        new_item(
            ItemClassification.filler,
            "Guild Approved Cuisine",
            [ItemTags.csharp_item_id, ItemTags.group_recipes],
            slot_data=CSharp.add_item_id_data(
                {}, "Manual_BlackGuildCooking"
            )
        ),
        new_item(
            ItemClassification.filler,
            "The Chequered Cookbook",
            [ItemTags.csharp_item_id, ItemTags.group_recipes],
            slot_data=CSharp.add_item_id_data(
                {}, "Manual_ChequeredCookbook"
            )
        ),

        # Scrolls
        new_item(
            ItemClassification.progression,
            "Scholar sells Scroll of Dark",
            [ItemTags.csharp_vendor_table_extension, ItemTags.group_scroll],
            slot_data=CSharp.add_vendor_table_extension_data(
                {}, "Scholar", "Enchantment_Dark"
            )
        ),
        new_item(
            ItemClassification.progression,
            "Scholar sells Scroll of Earth",
            [ItemTags.csharp_vendor_table_extension, ItemTags.group_scroll],
            slot_data=CSharp.add_vendor_table_extension_data(
                {}, "Scholar", "Enchantment_Earth"
            )
        ),
        new_item(
            ItemClassification.progression,
            "Scholar sells Scroll of Surge",
            [ItemTags.csharp_vendor_table_extension, ItemTags.group_scroll],
            slot_data=CSharp.add_vendor_table_extension_data(
                {}, "Scholar", "Enchantment_Electricity"
            )
        ),
        new_item(
            ItemClassification.progression,
            "Scholar sells Scroll of Embers",
            [ItemTags.csharp_vendor_table_extension, ItemTags.group_scroll],
            slot_data=CSharp.add_vendor_table_extension_data(
                {}, "Scholar", "Enchantment_Fire"
            )
        ),
        new_item(
            ItemClassification.progression,
            "Scholar sells Scroll of Frost",
            [ItemTags.csharp_vendor_table_extension, ItemTags.group_scroll],
            slot_data=CSharp.add_vendor_table_extension_data(
                {}, "Scholar", "Enchantment_Frost"
            )
        ),
        new_item(
            ItemClassification.progression,
            "Scholar sells Scroll of Light",
            [ItemTags.csharp_vendor_table_extension, ItemTags.group_scroll],
            slot_data=CSharp.add_vendor_table_extension_data(
                {}, "Scholar", "Enchantment_Light"
            )
        ),
        new_item(
            ItemClassification.progression,
            "Scholar sells Scroll of Nature",
            [ItemTags.csharp_vendor_table_extension, ItemTags.group_scroll],
            slot_data=CSharp.add_vendor_table_extension_data(
                {}, "Scholar", "Enchantment_Nature"
            )
        ),
        new_item(
            ItemClassification.progression,
            "Scholar sells Scroll of Plague",
            [ItemTags.csharp_vendor_table_extension, ItemTags.group_scroll],
            slot_data=CSharp.add_vendor_table_extension_data(
                {}, "Scholar", "Enchantment_Poison"
            )
        ),
        new_item(
            ItemClassification.progression,
            "Scholar sells Scroll of Water",
            [ItemTags.csharp_vendor_table_extension, ItemTags.group_scroll],
            slot_data=CSharp.add_vendor_table_extension_data(
                {}, "Scholar", "Enchantment_Water"
            )
        ),

        # Service stations
        ## chrismatory
        ## font
        ## delivery demon
        ## holoreality projector
        ## ammunition crate

        # Shortcuts

        # Storages

        # Useful / Collection / Faith
        ## Gift for the Church (valuables, strong piece of equipment, top tier attachment, good oil or stamps)
        ## Recurring donations (recurring scavenge loot)
        ## Divine providence (better loot chance, can do individual ones per loot weight)

        # Valuables
    ]