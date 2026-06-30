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

class SulfurItems:
    def __init(self, player: int):
        self.player = player
        self.current_item_code = 0
        self.items: list[SulfurItem] = []
        self.items_by_tag: dict[str, list[SulfurItem]] = {}
        self.items_by_name: dict[str, SulfurItem] = {}
        self.items_by_id: dict[int, SulfurItem] = {}
    def new_item(
            self,
            classification: ItemClassification,
            name: str,
            tags: list[str],
            slot_data: Optional[Mapping[str, Any]] = None
    ):
        self.current_item_code += 1
        new_item = SulfurItem(
            self.player,
            self.current_item_code,
            classification,
            name,
            tags,
            slot_data
        )
        self.items.append(new_item)
        self.items_by_name[name] = new_item
        self.items_by_id[self.current_item_code] = new_item
        for tag in tags:
            if self.items_by_tag[tag] is None:
                self.items_by_tag[tag] = []
            self.items_by_tag[tag].append(new_item)

        return new_item

    # all items
    ## Misc filler
    item_mining_explosive = new_item(
        ItemClassification.filler,
        "Mining explosive",
        [ItemTags.csharp_loot_table, ItemTags.group_repeatable],
        slot_data=CSharp.add_loot_table_data(
            {}, "LooseLoot_Weapon_MiningExplosive", True
        )
    )
    item_sulf = new_item(
        ItemClassification.filler,
        "Sulf",
        [ItemTags.csharp_sulf, ItemTags.group_repeatable],
    )

    ## Food
    item_food_goblin = new_item(
        ItemClassification.filler,
        "Goblin cooking",
        [ItemTags.csharp_loot_table, ItemTags.group_repeatable],
        slot_data=CSharp.add_loot_table_data(
            {}, "Archipelago_Food_Goblin", True
        )
    )
    item_food_town = new_item(
        ItemClassification.filler,
        "Town market meal",
        [ItemTags.csharp_loot_table, ItemTags.group_repeatable],
        slot_data=CSharp.add_loot_table_data(
            {}, "Archipelago_Food_Town", True
        )
    )
    item_food_sewers = new_item(
        ItemClassification.filler,
        "Questionable sewer treats",
        [ItemTags.csharp_loot_table, ItemTags.group_repeatable],
        slot_data=CSharp.add_loot_table_data(
            {}, "Archipelago_Food_Sewer", True
        )
    )
    item_food_dungeon = new_item(
        ItemClassification.filler,
        "Prisoner's last meal",
        [ItemTags.csharp_loot_table, ItemTags.group_repeatable],
        slot_data=CSharp.add_loot_table_data(
            {}, "Archipelago_Food_Dungeon", True
        )
    )
    item_food_castle = new_item(
        ItemClassification.filler,
        "Castle feast",
        [ItemTags.csharp_loot_table, ItemTags.group_repeatable],
        slot_data=CSharp.add_loot_table_data(
            {}, "Archipelago_Food_Castle", True
        )
    )
    item_food_forest = new_item(
        ItemClassification.filler,
        "Camping-compatible eats",
        [ItemTags.csharp_loot_table, ItemTags.group_repeatable],
        slot_data=CSharp.add_loot_table_data(
            {}, "Archipelago_Food_Forest", True
        )
    )
    item_food_fortress = new_item(
        ItemClassification.filler,
        "Wash'oku",
        [ItemTags.csharp_loot_table, ItemTags.group_repeatable],
        slot_data=CSharp.add_loot_table_data(
            {}, "Archipelago_Food_Fortress", True
        )
    )
    item_food_desert = new_item(
        ItemClassification.filler,
        "Sandy plates",
        [ItemTags.csharp_loot_table, ItemTags.group_repeatable],
        slot_data=CSharp.add_loot_table_data(
            {}, "Archipelago_Food_Desert", True
        )
    )
    item_food_fast_food = new_item(
        ItemClassification.filler,
        "Fast food",
        [ ItemTags.csharp_loot_table, ItemTags.group_repeatable],
        slot_data=CSharp.add_loot_table_data(
            {}, "Archipelago_Food_Fast_Food", True
        )
    )

    ## Cooking recipes
    item_cookbook_basic = new_item(
        ItemClassification.filler,
        "The Chequered Cookbook",
        [ItemTags.csharp_item_id, ItemTags.group_cookbooks],
        slot_data=CSharp.add_item_id_data(
            {}, "Manual_ChequeredCookbook"
        )
    )
    item_cookbook_caves = new_item(
        ItemClassification.filler,
        "GABBA FOODMAKE",
        [ItemTags.csharp_item_id, ItemTags.group_cookbooks],
        slot_data=CSharp.add_item_id_data(
            {}, "Manual_GoblinCooking"
        )
    )
    item_cookbook_town = new_item(
        ItemClassification.filler,
        "Guild Approved Cuisine",
        [ItemTags.csharp_item_id, ItemTags.group_cookbooks],
        slot_data=CSharp.add_item_id_data(
            {}, "Manual_BlackGuildCooking"
        )
    )
    item_cookbook_sewers = new_item(
        ItemClassification.filler,
        "Tastes From the Sewers™️",
        [ItemTags.csharp_item_id, ItemTags.group_cookbooks],
        slot_data=CSharp.add_item_id_data(
            {}, "Manual_CookingSewers"
        )
    )
    item_cookbook_dungeon = new_item(
        ItemClassification.filler,
        "From the Cellar",
        [ItemTags.csharp_item_id, ItemTags.group_cookbooks],
        slot_data=CSharp.add_item_id_data(
            {}, "Manual_CookingDungeon"
        )
    )
    item_cookbook_castle = new_item(
        ItemClassification.filler,
        "Eating as Royals",
        [ItemTags.csharp_item_id, ItemTags.group_cookbooks],
        slot_data=CSharp.add_item_id_data(
            {}, "Manual_CookingCastle"
        )
    )
    item_cookbook_forest = new_item(
        ItemClassification.filler,
        "Delicacies of the Forest",
        [ItemTags.csharp_item_id, ItemTags.group_cookbooks],
        slot_data=CSharp.add_item_id_data(
            {}, "Manual_ForestCooking"
        )
    )
    item_cookbook_fortress = new_item(
        ItemClassification.filler,
        "Shav'Wani Delights",
        [ItemTags.csharp_item_id, ItemTags.group_cookbooks],
        slot_data=CSharp.add_item_id_data(
            {}, "Manual_CookingFortress"
        )
    )
    item_cookbook_desert = new_item(
        ItemClassification.filler,
        "Food for Desert Survival",
        [ItemTags.csharp_item_id, ItemTags.group_cookbooks],
        slot_data=CSharp.add_item_id_data(
            {}, "Manual_DesertCooking"
        )
    )

    ## Scrolls
    item_scroll_dark = new_item(
        ItemClassification.progression,
        "Scholar sells Scroll of Dark",
        [ItemTags.csharp_vendor_table_extension, ItemTags.group_scroll],
        slot_data=CSharp.add_vendor_table_extension_data(
            {}, "Scholar", "Enchantment_Dark"
        )
    )
    item_scroll_earth = new_item(
        ItemClassification.progression,
        "Scholar sells Scroll of Earth",
        [ItemTags.csharp_vendor_table_extension, ItemTags.group_scroll],
        slot_data=CSharp.add_vendor_table_extension_data(
            {}, "Scholar", "Enchantment_Earth"
        )
    )
    item_scroll_surge = new_item(
        ItemClassification.progression,
        "Scholar sells Scroll of Surge",
        [ItemTags.csharp_vendor_table_extension, ItemTags.group_scroll],
        slot_data=CSharp.add_vendor_table_extension_data(
            {}, "Scholar", "Enchantment_Electricity"
        )
    )
    item_scroll_embers = new_item(
        ItemClassification.progression,
        "Scholar sells Scroll of Embers",
        [ItemTags.csharp_vendor_table_extension, ItemTags.group_scroll],
        slot_data=CSharp.add_vendor_table_extension_data(
            {}, "Scholar", "Enchantment_Fire"
        )
    )
    item_scroll_frost = new_item(
        ItemClassification.progression,
        "Scholar sells Scroll of Frost",
        [ItemTags.csharp_vendor_table_extension, ItemTags.group_scroll],
        slot_data=CSharp.add_vendor_table_extension_data(
            {}, "Scholar", "Enchantment_Frost"
        )
    )
    item_scroll_light = new_item(
        ItemClassification.progression,
        "Scholar sells Scroll of Light",
        [ItemTags.csharp_vendor_table_extension, ItemTags.group_scroll],
        slot_data=CSharp.add_vendor_table_extension_data(
            {}, "Scholar", "Enchantment_Light"
        )
    )
    item_scroll_nature = new_item(
        ItemClassification.progression,
        "Scholar sells Scroll of Nature",
        [ItemTags.csharp_vendor_table_extension, ItemTags.group_scroll],
        slot_data=CSharp.add_vendor_table_extension_data(
            {}, "Scholar", "Enchantment_Nature"
        )
    )
    item_scroll_plague = new_item(
        ItemClassification.progression,
        "Scholar sells Scroll of Plague",
        [ItemTags.csharp_vendor_table_extension, ItemTags.group_scroll],
        slot_data=CSharp.add_vendor_table_extension_data(
            {}, "Scholar", "Enchantment_Poison"
        )
    )
    item_scroll_water = new_item(
        ItemClassification.progression,
        "Scholar sells Scroll of Water",
        [ItemTags.csharp_vendor_table_extension, ItemTags.group_scroll],
        slot_data=CSharp.add_vendor_table_extension_data(
            {}, "Scholar", "Enchantment_Water"
        )
    )

    ## Service stations
    item_station_chrismatory = new_item(
        ItemClassification.useful,
        "Chrismatory",
        [ItemTags.csharp_checkpoint, ItemTags.group_service_stations],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ItemBroughtToChurch_Item_Chrimatory"
        )
    )
    item_station_baptismal_font = new_item(
        ItemClassification.useful,
        "Baptismal Font",
        [ItemTags.csharp_checkpoint, ItemTags.group_service_stations],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ItemBroughtToChurch_Item_BaptismalFont"
        )
    )
    item_station_delivery_demon = new_item(
        ItemClassification.useful,
        "Delivery Demon",
        [ItemTags.csharp_checkpoint, ItemTags.group_service_stations],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ItemBroughtToChurch_Item_DeliveryDemon"
        )
    )
    item_station_holoreality_projector = new_item(
        ItemClassification.useful,
        "Holoreality Projector",
        [ItemTags.csharp_checkpoint, ItemTags.group_service_stations],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ItemBroughtToChurch_Item_HolorealityProjector"
        )
    )
    item_station_bulk_ammo_box = new_item(
        ItemClassification.useful,
        "Bulk Ammo Box",
        [ItemTags.csharp_checkpoint, ItemTags.group_service_stations],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ItemBroughtToChurch_Item_BulkAmmoBox"
        )
    )

    ## Church grounds
    item_church_grounds = new_item(
        ItemClassification.progression,
        "Unlock Town and Church Grounds",
        [ItemTags.csharp_checkpoint, ItemTags.group_shortcut],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ReachedEnvironment_WorldEnvironment_Act_01_Shanty"
        )
    )

    ## Shortcuts
    item_shortcut_sewers = new_item(
        ItemClassification.progression,
        "Unlock Sewers Shortcut",
        [ItemTags.csharp_checkpoint, ItemTags.group_shortcut],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ReachedEnvironment_WorldEnvironment_Act_01_Sewers"
        )
    )
    item_shortcut_hedgemaze = new_item(
        ItemClassification.progression,
        "Unlock Hedge Maze Shortcut",
        [ItemTags.csharp_checkpoint, ItemTags.group_shortcut],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ReachedEnvironment_WorldEnvironment_Act_01_Hedgemaze"
        )
    )
    item_shortcut_castle = new_item(
        ItemClassification.progression,
        "Unlock Castle Shortcut after Hedge Maze",
        [ItemTags.csharp_checkpoint, ItemTags.group_shortcut],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ReachedEnvironment_WorldEnvironment_Act_01_Castle"
        )
    )
    item_shortcut_forest = new_item(
        ItemClassification.progression,
        "Unlock Forest Shortcut",
        [ItemTags.csharp_checkpoint, ItemTags.group_shortcut],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ReachedEnvironment_WorldEnvironment_Act_02_Forest"
        )
    )
    item_shortcut_fortress = new_item(
        ItemClassification.progression,
        "Unlock Shav'Wani Fortress Bridge Shortcut",
        [ItemTags.csharp_checkpoint, ItemTags.group_shortcut],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ReachedEnvironment_WorldEnvironment_Act_02_Bridge"
        )
    )
    item_shortcut_desert = new_item(
        ItemClassification.progression,
        "Unlock Desert Shortcut",
        [ItemTags.csharp_checkpoint, ItemTags.group_shortcut],
        slot_data=CSharp.add_checkpoint_data(
            {}, "BossDead_Emperor"
        )
    )

    ## Storages
    item_storage_safe = new_item(
        ItemClassification.useful,
        "Safe",
        [ItemTags.csharp_checkpoint, ItemTags.group_storage],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ItemBroughtToChurch_Item_Safe"
        )
    )
    item_storage_wardrobe = new_item(
        ItemClassification.useful,
        "Wardrobe",
        [ItemTags.csharp_checkpoint, ItemTags.group_storage],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ItemBroughtToChurch_Item_Wardrobe"
        )
    )
    item_storage_weapon_rack = new_item(
        ItemClassification.useful,
        "Weapon Rack",
        [ItemTags.csharp_checkpoint, ItemTags.group_storage],
        slot_data=CSharp.add_progressive_checkpoint_data(
            {}, ["ItemBroughtToChurch_Item_WeaponRack0", "ItemBroughtToChurch_Item_WeaponRack1"]
        )
    )
    item_storage_gun_cabinet = new_item(
        ItemClassification.useful,
        "Gun Cabinet",
        [ItemTags.csharp_checkpoint, ItemTags.group_storage],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ItemBroughtToChurch_Item_GunCabinet"
        )
    )
    item_storage_snake_basket = new_item(
        ItemClassification.useful,
        "Snake Basket",
        [ItemTags.csharp_checkpoint, ItemTags.group_storage],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ItemBroughtToChurch_Item_SnakeBasket"
        )
    )
    item_storage_wall_frame1 = new_item(
        ItemClassification.filler,
        "Small Golden Wall Frame",
        [ItemTags.csharp_checkpoint, ItemTags.group_storage],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ItemBroughtToChurch_Item_Painting1"
        )
    )
    item_storage_wall_frame2 = new_item(
        ItemClassification.filler,
        "Withered Wood Wall Frame",
        [ItemTags.csharp_checkpoint, ItemTags.group_storage],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ItemBroughtToChurch_Item_Painting2"
        )
    )
    item_storage_wall_frame3 = new_item(
        ItemClassification.filler,
        "Cherry Wood Wall Frame",
        [ItemTags.csharp_checkpoint, ItemTags.group_storage],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ItemBroughtToChurch_Item_Painting3"
        )
    )
    item_storage_wall_frame4 = new_item(
        ItemClassification.filler,
        "Luxurious Wall Frame",
        [ItemTags.csharp_checkpoint, ItemTags.group_storage],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ItemBroughtToChurch_Item_Painting4"
        )
    )
    item_storage_coffin = new_item(
        ItemClassification.useful,
        "Coffin",
        [ItemTags.csharp_checkpoint, ItemTags.group_storage],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ItemBroughtToChurch_Item_Coffin"
        )
    )
    item_storage_wall_mount1 = new_item(
        ItemClassification.filler,
        "Left Wall Mount",
        [ItemTags.csharp_checkpoint, ItemTags.group_storage],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ItemBroughtToChurch_Item_WallMount0"
        )
    )
    item_storage_wall_mount2 = new_item(
        ItemClassification.filler,
        "Center Wall Mount",
        [ItemTags.csharp_checkpoint, ItemTags.group_storage],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ItemBroughtToChurch_Item_WallMount1"
        )
    )
    item_storage_wall_mount3 = new_item(
        ItemClassification.filler,
        "Right Wall Mount",
        [ItemTags.csharp_checkpoint, ItemTags.group_storage],
        slot_data=CSharp.add_checkpoint_data(
            {}, "ItemBroughtToChurch_Item_WallMount2"
        )
    )

    # Valuables
    item_valuable_car_stereo = new_item(
        ItemClassification.filler,
        "Car Stereo",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableCarStereo"
        )
    )
    item_valuable_craw_guano = new_item(
        ItemClassification.filler,
        "Craw Guano",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableCrawGuano"
        )
    )
    item_valuable_diamond_ring = new_item(
        ItemClassification.filler,
        "Diamond Ring",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableDiamondRing"
        )
    )
    item_valuable_drivers_license = new_item(
        ItemClassification.filler,
        "Drivers License",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableDriversLicense"
        )
    )
    item_valuable_dvd_player = new_item(
        ItemClassification.filler,
        "DVD Player",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableDVDPlayer"
        )
    )
    item_valuable_famous_painting = new_item(
        ItemClassification.filler,
        "Famous Painting",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableFamousPainting"
        )
    )
    item_valuable_fancy_watch = new_item(
        ItemClassification.filler,
        "Fancy Watch",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableFancyWatch"
        )
    )
    item_valuable_fine_china = new_item(
        ItemClassification.filler,
        "Fine China",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableFineChina"
        )
    )
    item_valuable_flatscreen_tv = new_item(
        ItemClassification.filler,
        "Flatscreen TV",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableFlatscreenTV"
        )
    )
    item_valuable_gaming_laptop = new_item(
        ItemClassification.filler,
        "Gaming Laptop",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableGamingLaptop"
        )
    )
    item_valuable_gold_chain = new_item(
        ItemClassification.filler,
        "Gold Chain",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableGoldChain"
        )
    )
    item_valuable_golden_figurine = new_item(
        ItemClassification.filler,
        "Golden Figurine",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableGoldenFigurine"
        )
    )
    item_valuable_golden_ticket = new_item(
        ItemClassification.filler,
        "Golden Ticket",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableGoldenTicket"
        )
    )
    item_valuable_minidisc_player = new_item(
        ItemClassification.filler,
        "MiniDisc Player",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableMinidisc"
        )
    )
    item_valuable_mp3_player = new_item(
        ItemClassification.filler,
        "MP3 Player",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableMP3Player"
        )
    )
    item_valuable_old_vintage = new_item(
        ItemClassification.filler,
        "Old Vintage",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableOldVintage"
        )
    )
    item_valuable_ornamental_vase = new_item(
        ItemClassification.filler,
        "Ornamental Vase",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableOrnamentalVase"
        )
    )
    item_valuable_poker_chips = new_item(
        ItemClassification.filler,
        "Poker Chips",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuablePokerChips"
        )
    )
    item_valuable_silver_spoon = new_item(
        ItemClassification.filler,
        "Silver Spoon",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableQuaintLittleSpoon"
        )
    )
    item_valuable_shavwa_soap = new_item(
        ItemClassification.filler,
        "Shav'Wa Soap",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableShavwaSoap"
        )
    )
    item_valuable_smartphone = new_item(
        ItemClassification.filler,
        "Smartphone",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableSmartphone"
        )
    )
    item_valuable_soul_resin = new_item(
        ItemClassification.filler,
        "Soul Resin",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableSoulResin"
        )
    )
    item_valuable_the_cost = new_item(
        ItemClassification.filler,
        "The Cost",
        [ItemTags.csharp_checkpoint, ItemTags.group_valuables],
        slot_data=CSharp.add_item_id_data(
            {}, "ValuableTheCost"
        )
    )

    ## Gifts
    item_gift = new_item(
        ItemClassification.filler,
        "Gift for the Church",
        [ItemTags.csharp_loot_table],
        slot_data=CSharp.add_loot_table_data(
            {}, "Archipelago_Gift"
        )
    )

    ## Recurring Donations
    item_recurring_scavenge_goblin = new_item(
        ItemClassification.filler,
        "Recurring Anonymous Goblin Donations",
        [ItemTags.csharp_charity, ItemTags.group_charity],
        slot_data=CSharp.as_recurring(CSharp.add_loot_table_data(
            {}, "Archipelago_Donation_Caves"
        ))
    )
    item_recurring_scavenge_town = new_item(
        ItemClassification.filler,
        "Recurring Concerned Citizen Contributions",
        [ItemTags.csharp_charity],
        slot_data=CSharp.as_recurring(CSharp.add_loot_table_data(
            {}, "Archipelago_Donation_Town"
        ))
    )
    item_recurring_scavenge_sewers = new_item(
        ItemClassification.filler,
        "Recurring Ill-Smelling Donations",
        [ItemTags.csharp_charity],
        slot_data=CSharp.as_recurring(CSharp.add_loot_table_data(
            {}, "Archipelago_Donation_Sewers"
        ))
    )
    item_recurring_scavenge_dungeon = new_item(
        ItemClassification.filler,
        "Recurring Confiscated Prisoner Belongings",
        [ItemTags.csharp_charity],
        slot_data=CSharp.as_recurring(CSharp.add_loot_table_data(
            {}, "Archipelago_Donation_Dungeon"
        ))
    )
    item_recurring_scavenge_castle = new_item(
        ItemClassification.filler,
        "Recurring Redistribution of Castle Wealth",
        [ItemTags.csharp_charity],
        slot_data=CSharp.as_recurring(CSharp.add_loot_table_data(
            {}, "Archipelago_Donation_Castle"
        ))
    )
    item_recurring_scavenge_forest = new_item(
        ItemClassification.filler,
        "Recurring Foraging Freebies",
        [ItemTags.csharp_charity],
        slot_data=CSharp.as_recurring(CSharp.add_loot_table_data(
            {}, "Archipelago_Donation_Forest"
        ))
    )
    item_recurring_scavenge_fortress = new_item(
        ItemClassification.filler,
        "Recurring Shav'Wa Imports",
        [ItemTags.csharp_charity],
        slot_data=CSharp.as_recurring(CSharp.add_loot_table_data(
            {}, "Archipelago_Donation_Fortress"
        ))
    )
    item_recurring_scavenge_desert = new_item(
        ItemClassification.filler,
        "Recurring Sandy Gift Boxes",
        [ItemTags.csharp_charity, ItemTags.group_recurring_donations],
        slot_data=CSharp.as_recurring(CSharp.add_loot_table_data(
            {}, "Archipelago_Donation_Desert"
        ))
    )

    ## Divine Providence
    item_loot_chance = new_item(
        ItemClassification.useful,
        "Divine Luck",
        [ItemTags.csharp_loot_chance]
    )
