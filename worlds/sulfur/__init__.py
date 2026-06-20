import typing
from worlds.AutoWorld import World
from BaseClasses import Region, Location, Entrance, Item, ItemClassification
from Options import Toggle, Range, Choice, PerGameCommonOptions
from dataclasses import dataclass

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

# The rest
class SulfurItem(Item):
    game = "SULFUR"

class SulfurLocation(Location):
    game = "SULFUR"

sulfur_items = [
    "Mac 'N' Cheese"
]

sulfur_locations = [
    "Sulfur Caves"
]

class SulfurWorld(World):
    """A priest is stuck at the whims of a witch in SULFUR."""
    game = "SULFUR"
    options_dataclass = SulfurOptions
    options: SulfurOptions
    topology_present = True

    base_id = 1

    item_name_to_id = {name: id for id, name in enumerate(sulfur_items, base_id)}
    location_name_to_id = {name: id for id, name in enumerate(sulfur_locations, base_id)}

    item_name_group = {
        "foodstuffs": {"Mac 'N' Cheese"}
    }

    def generate_early(self) -> None:
        self.noop = True
    
    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        menu_region.locations.append(SulfurLocation(self.player, "Sulfur Caves", None, menu_region))
        self.multiworld.regions.append(menu_region)
    
    def create_item(self, item: str) -> SulfurItem:
        classification = ItemClassification.filler
        return SulfurItem(item, classification, self.item_name_to_id[item], self.player)

    def create_event(self, event: str) -> SulfurItem:
        return SulfurItem(event, ItemClassification.progression, None, self.player)

    def create_items(self) -> None:
        for item in map(self.create_item, sulfur_items):
            self.multiworld.itempool.append(item)
        junk = 0  # calculate this based on player options
        self.multiworld.itempool += [self.create_item("nothing") for _ in range(junk)]
    
    def set_rules(self) -> None:
        self.multiworld.get_location("Sulfur Caves", self.player).place_locked_item(self.create_event("Victory"))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)