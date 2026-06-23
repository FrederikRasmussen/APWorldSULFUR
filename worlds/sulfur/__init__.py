import typing
from worlds.AutoWorld import World
from BaseClasses import Region, Location, Entrance, Item, ItemClassification
from Options import Toggle, Range, Choice, PerGameCommonOptions
from dataclasses import dataclass

from .item_names import ItemNames
from .item_tags import ItemTags
from .items import SulfurItem, ITEMS, ItemDetails
from .location_names import LocationNames
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
    origin_region_name = "Church"

    base_id = 1

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

    def create_regions(self) -> None:
        church_region = Region("Church", self.player, self.multiworld)
        church_region.add_locations(
            get_location_names_with_ids(
                [
                    LocationNames.reach_sulfur_caves_i,
                    LocationNames.reach_sulfur_caves_ii,
                    LocationNames.reach_sulfur_caves_iii,
                    LocationNames.reach_sulfur_caves_iv,
                    LocationNames.reach_sulfur_caves_v,
                    LocationNames.reach_sulfur_caves_vi,
                    LocationNames.reach_sulfur_caves_vii,
                ],
            ),
            SulfurLocation,
        )
        church_region.add_event(
            LocationNames.reach_sulfur_caves_vii,
            "Victory",
            location_type=SulfurLocation,
            item_type=SulfurItem,
        )

        #town_region = Region("Town", self.player, self.multiworld)
        #town_region.add_locations(
        #    get_location_names_with_ids(
        #        [
        #            "Trade Stamps for the Small Golden Wall Frame",
        #            "Trade Stamps for the Withered Wood Wall Frame",
        #            "Trade Stamps for the Cherry Wood Wall Frame",
        #            "Trade Stamps for the Luxurious Wall Frame",
        #            "Trade Stamps for the Bulk Ammo Box",
        #            "Trade Stamps for the Baptismal Font",
        #            "Trade Stamps for the Left Wall Mount",
        #            "Trade Stamps for the Center Wall Mount",
        #            "Trade Stamps for the Right Wall Mount",
        #            "Trade Stamps for the Snake Basket",
        #            "Trade Stamps for the Safe",
        #            "Trade Stamps for the Toilet",
        #            "Trade Stamps for the Wardrobe",
        #            "Trade Stamps for the Coffin",
        #            "Trade Stamps for the Gun Cabinet",
        #            "Trade Stamps for the Chrismatory",
        #            "Trade Stamps for the first Weapon Rack",
        #            "Trade Stamps for the second Weapon Rack",
        #            "Trade Stamps for the Delivery Demon",
        #            "Trade Stamps for the Holoreality Projector",
        #        ],
        #    ),
        #    SulfurLocation,
        #)
        #church_region.connect(town_region, "Church to Town")

        self.multiworld.regions.append(church_region)

    def create_item(self, item: ItemDetails) -> SulfurItem:
        classification = ItemClassification.filler
        return SulfurItem(
            item.name,
            classification,
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
        for item in map(self.create_item, ITEMS):
            self.multiworld.itempool.append(item)
        #number_of_items = 0
        #itempool: list[Item] = []
        #number_of_unfilled_locations = len(
        #    self.multiworld.get_unfilled_locations(self.player)
        #)
        #needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
        #itempool += [self.create_filler() for _ in
        #             range(needed_number_of_filler_items)]
        #junk = 0  # calculate this based on player options
        #self.multiworld.itempool += [self.create_item(ItemNames.Currency_SulfCoin) for _
        #                             in range(junk)]

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda \
                state: state.has("Victory", self.player)
