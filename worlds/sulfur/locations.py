from typing import List

from BaseClasses import Location
from worlds.sulfur import ItemNames
from worlds.sulfur.location_names import LocationNames
from worlds.sulfur.location_tags import LocationTags
from worlds.sulfur.weapon_types import WeaponTypes


class SulfurLocation(Location):
    game = "SULFUR"

CURRENT_LOCATION_ID: int = 0
def get_and_increment_current_location_id() -> int:
    global CURRENT_LOCATION_ID
    CURRENT_LOCATION_ID += 1
    return CURRENT_LOCATION_ID

class LocationDetails:
    def __init__(
            self,
            name: str,
            tags: List[str],
            required_item: str = None,
            requires_multiple_items: list[str] = None,
            required_amount: int = 0,
            requires_all_items: list[str] = None,
    ):
        self.requires_item = required_item
        self.requires_multiple_items = requires_multiple_items
        self.required_amount = required_amount
        self.requires_all_items = requires_all_items
        self.id: int = get_and_increment_current_location_id()
        self.name: str = name
        self.tags: List[str] = tags

def get_location_names_with_ids(locations: list[LocationDetails]) -> dict[str, int | None]:
    return_dict = {}
    for location in locations:
        return_dict[location.name] = location.id
    return return_dict

def location_name_to_id() -> dict[str, int]:
    return_dict: dict[str, int] = {}
    for details in LOCATIONS:
        return_dict[details.name] = details.id
    return return_dict

def tag_to_locations():
    return_dict = {}
    for details in LOCATIONS:
        for tag in details.tags:
            if not tag in return_dict:
                return_dict[tag] = []
            return_dict[tag].append(details)
    return return_dict

LOCATIONS = []

def add_game_area_location_details(
        region: str,
        stages: list[str],
        boss: str = None
):
    for stage in stages:
        LOCATIONS.append(
            LocationDetails(
                stage,
                [region]
            )
        )
    if boss is not None:
        LOCATIONS.append(
            LocationDetails(
                boss,
                [region, LocationTags.boss],
            )
        )

# The Church
add_game_area_location_details(
    LocationTags.region_church,
    [
        LocationNames.reach_church
    ]
)

# Sulfur Caves
add_game_area_location_details(
    LocationTags.region_sulfur_caves,
    [
        LocationNames.reach_sulfur_caves_i,
        LocationNames.reach_sulfur_caves_ii,
        LocationNames.reach_sulfur_caves_iii,
        LocationNames.reach_sulfur_caves_iv,
        LocationNames.reach_sulfur_caves_v,
        LocationNames.reach_sulfur_caves_vi,
        LocationNames.reach_sulfur_caves_vii,
    ],
    LocationNames.boss_cousin
)

# Town
add_game_area_location_details(
    LocationTags.region_town,
    [
        LocationNames.reach_town_i,
        LocationNames.reach_town_ii,
        LocationNames.reach_town_iii,
        LocationNames.reach_town_iv,
        LocationNames.reach_town_v,
    ],
)

# Sewers
add_game_area_location_details(
    LocationTags.region_sewers,
    [
        LocationNames.reach_sewers_i,
        LocationNames.reach_sewers_ii,
        LocationNames.reach_sewers_iii,
        LocationNames.reach_sewers_iv,
    ]
)

# Hedge Maze
add_game_area_location_details(
    LocationTags.region_hedge_maze,
    [
        LocationNames.reach_hedge_maze,
    ]
)

# Dungeon
add_game_area_location_details(
    LocationTags.region_dungeon,
    [
        LocationNames.reach_dungeon_i,
        LocationNames.reach_dungeon_ii,
        LocationNames.reach_dungeon_iii,
        LocationNames.reach_dungeon_iv,
    ],
)

# Castle
add_game_area_location_details(
    LocationTags.region_castle,
    [
        LocationNames.reach_castle_i,
        LocationNames.reach_castle_ii,
        LocationNames.reach_castle_iii,
    ],
    LocationNames.boss_st_lucia
)

# Forest
add_game_area_location_details(
    LocationTags.region_forest,
    [
        LocationNames.reach_forest_i,
        LocationNames.reach_forest_ii,
        LocationNames.reach_forest_iii,
        LocationNames.reach_forest_iv,
        LocationNames.reach_forest_v,
    ],
    LocationNames.boss_terrorbaum
)

# Fortress
add_game_area_location_details(
    LocationTags.region_fortress,
    [
        LocationNames.reach_shavwani_bridge,
        LocationNames.reach_shavwani_fortress_i,
        LocationNames.reach_shavwani_fortress_ii,
        LocationNames.reach_shavwani_fortress_iii,
        LocationNames.reach_shavwani_fortress_iv,
        LocationNames.reach_shavwani_fortress_v,
        LocationNames.reach_shavwani_fortress_vi,
    ],
    LocationNames.boss_the_emperor
)

# Desert
add_game_area_location_details(
    LocationTags.region_desert,
    [
        LocationNames.reach_desert_i,
        LocationNames.reach_desert_ii,
        LocationNames.reach_desert_iii,
        LocationNames.reach_desert_iv,
        LocationNames.reach_desert_v,
    ],
    LocationNames.boss_desert_claus
)

# Beyond the Veil
add_game_area_location_details(
    LocationTags.region_beyond_the_veil,
    [
        LocationNames.reach_beyond_the_veil,
    ]
)

'''
add_weapon_locations(
    WeaponTypes.assault_rifle,
    "an",
    [
        ItemNames.Weapon_Catacoil,
        ItemNames.Weapon_Corpsemaker,
        ItemNames.Weapon_M11Ramshack,
        ItemNames.Weapon_Typhoon,
        ItemNames.Weapon_Wingman,
        ItemNames.Weapon_SocomACR,
        ItemNames.Weapon_CYB47,
    ]
)

add_weapon_locations(
    WeaponTypes.light_machine_gun,
    "a",
    [
        ItemNames.Weapon_Duhar,
        ItemNames.Weapon_NeuraxisF22,
        ItemNames.Weapon_Rektor,
        ItemNames.Weapon_Warpig,
        ItemNames.Weapon_Chat_Pardeur98,
    ]
)

add_weapon_locations(
    WeaponTypes.pistol,
    "a",
    [
        ItemNames.Weapon_Beck,
        ItemNames.Weapon_Bronco,
        ItemNames.Weapon_Dirk,
        ItemNames.Weapon_FlickerZip,
        ItemNames.Weapon_Gravekeeper,
        ItemNames.Weapon_Salamander,
        ItemNames.Weapon_Socom9,
        ItemNames.Weapon_Unknown,
        ItemNames.Weapon_HellnBack,
        ItemNames.Weapon_StarAndWitness,
        ItemNames.Weapon_Cavalier,
        ItemNames.Weapon_TerrierURB,
    ]
)

add_weapon_locations(
    WeaponTypes.revolver,
    "a",
    [
        ItemNames.Weapon_Balthazar,
        ItemNames.Weapon_PalehorseTopclipper,
        ItemNames.Weapon_Snut38,
        ItemNames.Weapon_WyattPulsar,
        ItemNames.Weapon_Blackwater,
    ]
)

add_weapon_locations(
    WeaponTypes.rifle,
    "a",
    [
        ItemNames.Weapon_Farsight,
        ItemNames.Weapon_Knop,
        ItemNames.Weapon_PierreFusil,
        ItemNames.Weapon_TailorMarksman,
    ]
)

add_weapon_locations(
    WeaponTypes.shotgun,
    "a",
    [
        ItemNames.Weapon_Arbiter2,
        ItemNames.Weapon_Augusta,
        ItemNames.Weapon_Breacher8,
        ItemNames.Weapon_Flock,
        ItemNames.Weapon_Majordome,
        ItemNames.Weapon_Mario,
        ItemNames.Weapon_Mossman,
    ]
)

add_weapon_locations(
    WeaponTypes.submachine_gun,
    "a",
    [
        ItemNames.Weapon_DeathStar,
        ItemNames.Weapon_Drifter9,
        ItemNames.Weapon_Ferryman,
        ItemNames.Weapon_PloikaC,
        ItemNames.Weapon_Termite,
        ItemNames.Weapon_Valet,
        ItemNames.Weapon_Vrede,
        ItemNames.Weapon_Songbird,
        ItemNames.Weapon_ChimeraRapid,
    ]
)

add_weapon_locations(
    WeaponTypes.sniper,
    "a",
    [
        ItemNames.Weapon_D4RT,
        ItemNames.Weapon_Dolphin99,
        ItemNames.Weapon_ImpalaGravita,
        ItemNames.Weapon_Rokua,
        ItemNames.Weapon_Longboy,
    ]
)
'''

'''
LOCATIONS.extend([
    LocationDetails(
        f"Find {ItemNames.Weapon_Bo}",
        [LocationTags.find_specific_weapon, WeaponTypes.melee, LocationTags.region_church],
        required_item=ItemNames.Weapon_Bo
    ),
    LocationDetails(
        f"Find {ItemNames.Weapon_Katana}",
        [LocationTags.find_specific_weapon, WeaponTypes.melee, LocationTags.region_church],
        required_item=ItemNames.Weapon_Katana
    ),
    LocationDetails(
        f"Find {ItemNames.Weapon_Nunchaku}",
        [LocationTags.find_specific_weapon, WeaponTypes.melee, LocationTags.region_church],
        required_item=ItemNames.Weapon_Nunchaku
    ),
    LocationDetails(
        f"Find {ItemNames.Weapon_Sai}",
        [LocationTags.find_specific_weapon, WeaponTypes.melee, LocationTags.region_church],
        required_item=ItemNames.Weapon_Sai
    ),
    LocationDetails(
        f"Find {ItemNames.Weapon_Wakizashi}",
        [LocationTags.find_specific_weapon, WeaponTypes.melee, LocationTags.region_church],
        required_item=ItemNames.Weapon_Wakizashi
    ),
    LocationDetails(
        f"Find a {WeaponTypes.melee}",
        [LocationTags.find_weapon_model, WeaponTypes.melee, LocationTags.region_church],
        requires_multiple_items=[ItemNames.Weapon_Bo, ItemNames.Weapon_Katana, ItemNames.Weapon_Nunchaku, ItemNames.Weapon_Sai, ItemNames.Weapon_Wakizashi],
        required_amount=1,
    ),
    LocationDetails(
        f"Find {amount_strings[1]} different {WeaponTypes.melee}s",
        [LocationTags.find_weapon_model, WeaponTypes.melee, LocationTags.region_church],
        requires_multiple_items=[ItemNames.Weapon_Bo, ItemNames.Weapon_Katana, ItemNames.Weapon_Nunchaku, ItemNames.Weapon_Sai, ItemNames.Weapon_Wakizashi],
        required_amount=2,
    ),
    LocationDetails(
        f"Find {amount_strings[2]} different {WeaponTypes.melee}s",
        [LocationTags.find_weapon_model, WeaponTypes.melee, LocationTags.region_church],
        requires_multiple_items=[ItemNames.Weapon_Bo, ItemNames.Weapon_Katana, ItemNames.Weapon_Nunchaku, ItemNames.Weapon_Sai, ItemNames.Weapon_Wakizashi],
        required_amount=3,
    ),
    LocationDetails(
        f"Find {amount_strings[3]} different {WeaponTypes.melee}s",
        [LocationTags.find_weapon_model, WeaponTypes.melee, LocationTags.region_church],
        requires_multiple_items=[ItemNames.Weapon_Bo, ItemNames.Weapon_Katana, ItemNames.Weapon_Nunchaku, ItemNames.Weapon_Sai, ItemNames.Weapon_Wakizashi],
        required_amount=4,
    ),
    LocationDetails(
        f"Find {amount_strings[4]} different {WeaponTypes.melee}s",
        [LocationTags.find_weapon_model, WeaponTypes.melee, LocationTags.region_church],
        requires_multiple_items=[ItemNames.Weapon_Bo, ItemNames.Weapon_Katana, ItemNames.Weapon_Nunchaku, ItemNames.Weapon_Sai, ItemNames.Weapon_Wakizashi],
        required_amount=5,
    ),
])
'''

# Storage locations
LOCATIONS.extend([
    LocationDetails(
        LocationNames.furniture_place_suitcase,
        [LocationTags.place_furniture, LocationTags.region_sulfur_caves],
    ),
    LocationDetails(
        LocationNames.furniture_place_refrigerator,
        [LocationTags.place_furniture, LocationTags.region_sewers],
    ),
    LocationDetails(
        LocationNames.furniture_place_chest_of_drawers,
        [LocationTags.place_furniture, LocationTags.region_castle],
    ),
])

for item in [
    ItemNames.Item_Painting1,
    ItemNames.Item_Painting2,
    ItemNames.Item_Painting3,
    ItemNames.Item_Painting4,
    ItemNames.Item_BulkAmmoBox,
    ItemNames.Item_BaptismalFont,
    ItemNames.Item_WallMount0,
    ItemNames.Item_WallMount1,
    ItemNames.Item_WallMount2,
    ItemNames.Item_SnakeBasket,
    ItemNames.Item_Safe,
    ItemNames.Item_Toilet,
    ItemNames.Item_Wardrobe,
    ItemNames.Item_Coffin,
    ItemNames.Item_GunCabinet,
    ItemNames.Item_Chrismatory,
    ItemNames.Item_WeaponRack0,
    ItemNames.Item_WeaponRack1,
    ItemNames.Item_DeliveryDemon,
    ItemNames.Item_HolorealityProjector,
]:
    LOCATIONS.append(
        LocationDetails(
            f"Trade stamps for the {item}",
            [LocationTags.stamp_trading, LocationTags.region_full_church]
        )
    )

class MixMagic:
    def __init__(self, item_name: str, required_scrolls: list[str]) -> None:
        self.item_name: str = item_name
        self.required_scrolls: list[str] = required_scrolls

    def as_location_details(self):
        return LocationDetails(
            f"Mix the magic '{self.item_name}'",
        [LocationTags.mix_magic, LocationTags.region_church],
            requires_all_items = self.required_scrolls
        )

for magicMixing in [
    MixMagic(ItemNames.Enchantment_Aftershock, [ItemNames.Enchantment_Earth]),
    MixMagic(ItemNames.Enchantment_ChainLightning, [ItemNames.Enchantment_Electricity]),
    MixMagic(ItemNames.Enchantment_ChaosStrike, [ItemNames.Enchantment_Dark, ItemNames.Enchantment_Electricity]),
    MixMagic(ItemNames.Enchantment_Charm, [ItemNames.Enchantment_Light, ItemNames.Enchantment_Nature]),
    MixMagic(ItemNames.Enchantment_CorpseExplosion, [ItemNames.Enchantment_Fire, ItemNames.Enchantment_Poison]),
    MixMagic(ItemNames.Enchantment_CorrosiveBlood, [ItemNames.Enchantment_Poison]),
    MixMagic(ItemNames.Enchantment_Crusader, [ItemNames.Enchantment_Light, ItemNames.Enchantment_Poison]),
    MixMagic(ItemNames.Enchantment_Fear, [ItemNames.Enchantment_Dark, ItemNames.Enchantment_Nature]),
    MixMagic(ItemNames.Enchantment_FlameThrower, [ItemNames.Enchantment_Dark, ItemNames.Enchantment_Fire]),
    MixMagic(ItemNames.Enchantment_HolyFire, [ItemNames.Enchantment_Fire, ItemNames.Enchantment_Light]),
    MixMagic(ItemNames.Enchantment_HolyPurge, [ItemNames.Enchantment_Light]),
    MixMagic(ItemNames.Enchantment_Lava, [ItemNames.Enchantment_Earth, ItemNames.Enchantment_Fire]),
    MixMagic(ItemNames.Enchantment_LeastResistance, [ItemNames.Enchantment_Electricity, ItemNames.Enchantment_Nature]),
    MixMagic(ItemNames.Enchantment_Noxiosa, [ItemNames.Enchantment_Earth, ItemNames.Enchantment_Poison]),
    MixMagic(ItemNames.Enchantment_Pesticide, [ItemNames.Enchantment_Poison, ItemNames.Enchantment_Water]),
    MixMagic(ItemNames.Enchantment_Petrification, [ItemNames.Enchantment_Earth, ItemNames.Enchantment_Poison]),
    MixMagic(ItemNames.Enchantment_Petroleum, [ItemNames.Enchantment_Fire, ItemNames.Enchantment_Nature]),
    MixMagic(ItemNames.Enchantment_Prism, [ItemNames.Enchantment_Frost, ItemNames.Enchantment_Light]),
    MixMagic(ItemNames.Enchantment_Pyroclasm, [ItemNames.Enchantment_Fire]),
    MixMagic(ItemNames.Enchantment_RocketLauncher, [ItemNames.Enchantment_Electricity, ItemNames.Enchantment_Fire]),
    MixMagic(ItemNames.Enchantment_Sacrifice, [ItemNames.Enchantment_Dark, ItemNames.Enchantment_Earth]),
    MixMagic(ItemNames.Enchantment_Slush, [ItemNames.Enchantment_Frost, ItemNames.Enchantment_Water]),
    MixMagic(ItemNames.Enchantment_StormSurge, [ItemNames.Enchantment_Earth, ItemNames.Enchantment_Electricity]),
    MixMagic(ItemNames.Enchantment_Thunderbolt, [ItemNames.Enchantment_Electricity, ItemNames.Enchantment_Water]),
    MixMagic(ItemNames.Enchantment_ToxicLobotomy, [ItemNames.Enchantment_Electricity, ItemNames.Enchantment_Poison]),
    MixMagic(ItemNames.Enchantment_Voodoo, [ItemNames.Enchantment_Dark, ItemNames.Enchantment_Poison]),
    MixMagic(ItemNames.Enchantment_Water,[ItemNames.Enchantment_Fire, ItemNames.Enchantment_Frost])
]:
    LOCATIONS.append(
        magicMixing.as_location_details()
    )
