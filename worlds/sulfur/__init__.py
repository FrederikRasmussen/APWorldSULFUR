import typing

from Utils import visualize_regions
from rule_builder.rules import Has, HasFromList
from worlds.AutoWorld import World
from BaseClasses import Region, Location, Entrance, Item, ItemClassification, \
    CollectionState
from Options import Toggle, Range, Choice, PerGameCommonOptions
from dataclasses import dataclass

from . import item_names
from .item_names import ItemNames, VirtualNames
from .item_tags import ItemTags
from .items import SulfurItem, ITEMS, ItemDetails
from .location_names import LocationNames
from .location_tags import LocationTags
from .locations import SulfurLocation, LOCATIONS, LocationDetails, \
    get_location_names_with_ids


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

    def generate_early(self) -> None:
        self.noop = True

    def create_region_with_connection(self, region_connection, region_name, required_item) -> Region:
        new_region = Region(region_name, self.player, self.multiworld)
        new_locations = []
        location_details: LocationDetails
        for location_details in self.locations_by_tag[region_name]:
            new_location = SulfurLocation(self.player, location_details.name, parent=new_region)
            if location_details.requires_item is not None:
                self.set_rule(new_location, Has(location_details.requires_item))
            if location_details.requires_multiple_items is not None:
                self.set_rule(new_location, HasFromList(
                    *location_details.requires_multiple_items,
                    count=location_details.required_amount,
                ))
            new_locations.append(new_location)
        new_region.locations.extend(new_locations)
        region_connection.connect(
            new_region, f"{region_name} to {region_connection.name}",
            rule=Has(required_item)
        )
        self.multiworld.regions.append(new_region)
        return new_region

    def create_regions(self) -> None:
        church_region = Region(LocationTags.region_church, self.player, self.multiworld)
        church_region.add_locations(
            get_location_names_with_ids(
                self.locations_by_tag[LocationTags.region_church],
            ),
            SulfurLocation
        )
        self.multiworld.regions.append(church_region)

        full_church_region = self.create_region_with_connection(church_region, LocationTags.region_full_church, VirtualNames.UnlockAreaChurchGrounds)
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

    def create_item(self, item: ItemDetails) -> SulfurItem:
        if item.default_classification is None:
            item.default_classification = ItemClassification.filler
        return SulfurItem(
            item.name,
            item.default_classification,
            item.id,
            self.player,
        )

    def create_event(self, event: str) -> SulfurItem:
        return SulfurItem(
            event,
            ItemClassification.progression,
            None,
            self.player,
        )

    def get_filler_item_name(self) -> str:
        return ItemNames.Currency_SulfCoin

    def create_items(self) -> None:
        for item in ITEMS:
            if (ItemTags.unknown or ItemTags.do_not_generate) in item.tags:
                continue
            self.multiworld.itempool.append(self.create_item(item))

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda \
                state: state.has("Victory", self.player)
