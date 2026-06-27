from typing import Any, Mapping

from rule_builder.rules import Has, HasAll, HasFromListUnique, CanReachLocation
from worlds.AutoWorld import World
from BaseClasses import Region, ItemClassification, Item
from Options import Toggle, Range, Choice, PerGameCommonOptions
from dataclasses import dataclass

from .item_names import ItemNames, VirtualNames
from .item_tags import ItemTags
from .items import SulfurItem, ITEMS, ItemDetails
from .location_names import LocationNames
from .location_tags import LocationTags
from .locations import SulfurLocation, LOCATIONS, LocationDetails, \
    get_location_names_with_ids
from .weapon_types import WeaponTypes


# Options
class Deathlink(Toggle):
    """Enables deathlink."""
    display_name = "Deathlink"


class StartingWeapon(Choice):
    """Pick which weapon to respawn with after every death."""
    display_name = "Starting Weapon"
    option_dirk = 0
    option_wakizashi = 1
    option_m19a1 = 2
    default = 0


class AverageSulfPerFiller(Range):
    """Sets how much Sulf (on average) you want to receive when given Sulf as a filler"""
    display_name = "Average Sulf as Filler"
    range_start = 25
    range_end = 10000
    default = 250


@dataclass
class SulfurOptions(PerGameCommonOptions):
    deathlink: Deathlink
    starting_weapon: StartingWeapon
    average_sulf_per_filler: AverageSulfPerFiller

class SulfurWorld(World):
    """A priest is stuck at the whims of a witch in SULFUR."""
    game = "SULFUR"
    options_dataclass = SulfurOptions
    options: SulfurOptions
    topology_present = True
    origin_region_name = LocationTags.region_church

    base_id = 1

    locations_by_tag = locations.tag_to_locations()
    item_name_to_details = items.item_identifier_to_details()
    item_name_to_id = items.item_name_to_id()
    location_name_to_id = locations.location_name_to_id()

    item_name_groups = {
        ItemTags.accessory: items.get_item_names_from_tag(ItemTags.accessory),
        ItemTags.ammunition: items.get_item_names_from_tag(ItemTags.ammunition),
        ItemTags.armour: items.get_item_names_from_tag(ItemTags.armour),
        ItemTags.boots: items.get_item_names_from_tag(ItemTags.boots),
        ItemTags.chambering_tools: items.get_item_names_from_tag(
            ItemTags.chambering_tools
        ),
        ItemTags.explosive: items.get_item_names_from_tag(ItemTags.explosive),
        ItemTags.food: items.get_item_names_from_tag(ItemTags.food),
        ItemTags.furniture: items.get_item_names_from_tag(ItemTags.furniture),
        ItemTags.gun: items.get_item_names_from_tag(ItemTags.gun),
        ItemTags.helmet: items.get_item_names_from_tag(ItemTags.helmet),
        ItemTags.melee: items.get_item_names_from_tag(ItemTags.melee),
        ItemTags.oil: items.get_item_names_from_tag(ItemTags.oil),
        ItemTags.recipe_book: items.get_item_names_from_tag(
            ItemTags.recipe_book
        ),
        ItemTags.repair: items.get_item_names_from_tag(ItemTags.repair),
        ItemTags.scroll_ingredient: items.get_item_names_from_tag(
            ItemTags.scroll_ingredient
        ),
        ItemTags.scroll: items.get_item_names_from_tag(ItemTags.scroll),
        ItemTags.sulf: items.get_item_names_from_tag(ItemTags.sulf),
        ItemTags.throwable: items.get_item_names_from_tag(ItemTags.throwable),
        ItemTags.valuable: items.get_item_names_from_tag(ItemTags.valuable),
        ItemTags.weapon_attachment: items.get_item_names_from_tag(
            ItemTags.weapon_attachment
        ),
    }

    location_name_groups = {
        LocationTags.stamp_trading: map(lambda details : details.name, locations_by_tag[LocationTags.stamp_trading]),
        LocationTags.find_specific_weapon: map(
            lambda details: details.name,
            locations_by_tag[LocationTags.find_specific_weapon]
        ),
        LocationTags.rank_up_specific_weapon: map(
            lambda details: details.name,
            locations_by_tag[LocationTags.rank_up_specific_weapon]
        ),
        LocationTags.sacrifice_specific_weapon: map(
            lambda details: details.name,
            locations_by_tag[LocationTags.sacrifice_specific_weapon]
        ),
        LocationTags.rank_1: map(
            lambda details: details.name,
            locations_by_tag[LocationTags.rank_1]
        ),
        LocationTags.rank_2: map(
            lambda details: details.name,
            locations_by_tag[LocationTags.rank_2]
        ),
        LocationTags.rank_3: map(
            lambda details: details.name,
            locations_by_tag[LocationTags.rank_3]
        ),
        LocationTags.rank_4: map(
            lambda details: details.name,
            locations_by_tag[LocationTags.rank_4]
        ),
        LocationTags.rank_5: map(
            lambda details: details.name,
            locations_by_tag[LocationTags.rank_5]
        ),
        WeaponTypes.melee: map(
            lambda details: details.name,
            locations_by_tag[WeaponTypes.melee]
        ),
        WeaponTypes.assault_rifle: map(
            lambda details: details.name,
            locations_by_tag[WeaponTypes.assault_rifle]
        ),
        WeaponTypes.light_machine_gun: map(
            lambda details: details.name,
            locations_by_tag[WeaponTypes.light_machine_gun]
        ),
        WeaponTypes.pistol: map(
            lambda details: details.name,
            locations_by_tag[WeaponTypes.pistol]
        ),
        WeaponTypes.revolver: map(
            lambda details: details.name,
            locations_by_tag[WeaponTypes.revolver]
        ),
        WeaponTypes.rifle: map(
            lambda details: details.name,
            locations_by_tag[WeaponTypes.rifle]
        ),
        WeaponTypes.shotgun: map(
            lambda details: details.name,
            locations_by_tag[WeaponTypes.shotgun]
        ),
        WeaponTypes.sniper: map(
            lambda details: details.name,
            locations_by_tag[WeaponTypes.sniper]
        ),
        WeaponTypes.submachine_gun: map(
            lambda details: details.name,
            locations_by_tag[WeaponTypes.submachine_gun]
        ),
    }

    def generate_early(self) -> None:
        self.noop = True

    def create_region(self, region_name) -> Region:
        new_region = Region(region_name, self.player, self.multiworld)
        new_locations = []
        location_details: LocationDetails
        for location_details in self.locations_by_tag[region_name]:
            new_location = SulfurLocation(
                self.player,
                location_details.name,
                address=location_details.id,
                parent=new_region
            )
            if location_details.requires_item is not None:
                self.set_rule(new_location, Has(location_details.requires_item))
            if location_details.requires_multiple_items is not None:
                self.set_rule(
                    new_location, HasFromListUnique(
                        *location_details.requires_multiple_items,
                        count=location_details.required_amount,
                    )
                )
            if location_details.requires_all_items is not None:
                self.set_rule(
                    new_location, HasAll(
                        *location_details.requires_all_items
                    )
                )
            new_locations.append(new_location)
        new_region.set_locations(new_locations)
        self.multiworld.regions.append(new_region)
        return new_region

    def create_region_with_connection(self, region_connection, region_name, required_item) -> Region:
        new_region = self.create_region(region_name)
        region_connection.connect(
            new_region, f"{region_name} to {region_connection.name}",
            rule=Has(required_item)
        )
        return new_region

    def create_regions(self) -> None:
        church_region = self.create_region(LocationTags.region_church)

        full_church_region = self.create_region_with_connection(church_region, LocationTags.region_full_church, VirtualNames.UnlockAreaChurchGrounds)
        sulfur_caves_region = self.create_region_with_connection(church_region, LocationTags.region_sulfur_caves, VirtualNames.UnlockAreaSulfurCaves)
        town_region = self.create_region_with_connection(full_church_region, LocationTags.region_town, VirtualNames.UnlockAreaTown)
        sewers_region = self.create_region_with_connection(full_church_region, LocationTags.region_sewers, VirtualNames.UnlockAreaSewers)
        hedge_maze_region = self.create_region_with_connection(full_church_region, LocationTags.region_hedge_maze, VirtualNames.UnlockAreaHedgeMaze)
        dungeon_region = self.create_region_with_connection(full_church_region, LocationTags.region_dungeon, VirtualNames.UnlockAreaDungeon)
        castle_region = self.create_region_with_connection(full_church_region, LocationTags.region_castle, VirtualNames.UnlockAreaCastle)
        forest_region = self.create_region_with_connection(full_church_region, LocationTags.region_forest, VirtualNames.UnlockAreaForest)
        fortress_region = self.create_region_with_connection(full_church_region, LocationTags.region_fortress, VirtualNames.UnlockAreaBridge)
        desert_region = self.create_region_with_connection(full_church_region, LocationTags.region_desert, VirtualNames.UnlockAreaDesert)
        beyond_the_veil_region = self.create_region_with_connection(full_church_region, LocationTags.region_beyond_the_veil, VirtualNames.UnlockAreaVeil)
        beyond_the_veil_region.add_event(
            LocationNames.boss_the_witch,
            "Victory",
            location_type=SulfurLocation,
            item_type=SulfurItem,
        )

        self.set_rule(
            self.get_location(LocationNames.boss_the_witch),
            CanReachLocation(
                *[LocationNames.boss_cousin]
            ) & CanReachLocation(
                *[LocationNames.boss_st_lucia]
            ) & CanReachLocation(
                *[LocationNames.boss_terrorbaum]
            ) & CanReachLocation(
                *[LocationNames.boss_the_emperor]
            ) & CanReachLocation(
                *[LocationNames.boss_desert_claus]
            )
        )

    def create_sulfur_item(self, item: ItemDetails) -> SulfurItem:
        if item.default_classification is None:
            item.default_classification = ItemClassification.filler
        return SulfurItem(
            item.name,
            item.default_classification,
            code=item.id,
            player=self.player,
        )

    def create_item(self, item: str) -> SulfurItem:
        return self.create_sulfur_item(self.item_name_to_details[item])

    def create_event(self, event: str) -> SulfurItem:
        return SulfurItem(
            event,
            ItemClassification.progression,
            None,
            self.player,
        )

    def get_filler_item_name(self) -> str:
        return ItemNames.Currency_SulfCoin

    starting_gun = None
    starting_melee = None
    def create_items(self) -> None:
        weapon_candidates: dict[ItemDetails, Item] = {}
        #generated_item_details: list[ItemDetails] = []
        for item in ITEMS:
            if (ItemTags.unknown or ItemTags.do_not_generate) in item.tags:
                continue
            generated_item = self.create_sulfur_item(item)
            self.multiworld.itempool.append(generated_item)
            if ItemTags.gun in item.tags:
                weapon_candidates[item] = generated_item
            if ItemTags.melee in item.tags:
                weapon_candidates[item] = generated_item
            if item.name is VirtualNames.UnlockAreaSulfurCaves:
                self.push_precollected(generated_item)
            #generated_item_details.append(item)

        # TODO: Check for options here
        # Give random starting gun
        if True:
            weapon_types = [
                ItemTags.gun_rifle,
                ItemTags.gun_pistol,
                ItemTags.gun_sniper,
                ItemTags.gun_shotgun,
                ItemTags.gun_revolver,
                ItemTags.gun_assault_rifle,
                ItemTags.gun_submachine_gun,
                ItemTags.gun_light_machine_gun,
            ]
            weapon_type_index = self.random.randint(1, len(weapon_types)) - 1
            weapons_with_type = items.TAG_TO_ITEMS[weapon_types[weapon_type_index]]
            weapon_index = self.random.randint(1, len(weapons_with_type)) - 1
            weapon_details = weapons_with_type[weapon_index]
            weapon = weapon_candidates[weapon_details]
            self.starting_gun = weapon_details
            self.push_precollected(weapon)

        # TODO: Check for options here
        # Give random melee start
        if True:
            melee_options = [
                self.item_name_to_details[ItemNames.Weapon_Bo],
                self.item_name_to_details[ItemNames.Weapon_Nunchaku],
                self.item_name_to_details[ItemNames.Weapon_Wakizashi],
                self.item_name_to_details[ItemNames.Weapon_Katana],
                self.item_name_to_details[ItemNames.Weapon_Sai],
            ]
            melee_index = self.random.randint(1, len(melee_options)) - 1
            melee_details = melee_options[melee_index]
            melee = weapon_candidates[melee_details]
            self.starting_melee = melee_details
            self.push_precollected(melee)

        #generated_item_details.sort(key=lambda d: d.id)
        #print(ItemNames.__dict__)
        #item_name_to_enum = {v: k for k, v in ItemNames.__dict__.items()}
        #for details in generated_item_details:
            #if details.name in item_name_to_enum:
                #print(f"new ItemSulfur({details.id}, \"{details.name}\", ItemIds.{item_name_to_enum[details.name]}),")
            #else:
                #print(f"new ItemCheckpoint({details.id}, \"{details.name}\"),")

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda \
                state: state.has("Victory", self.player)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return_dict = {
            "StartGun": self.starting_gun.id,
            "StartMelee": self.starting_melee.id
        }
        return return_dict
