This repository is for the custom SULFUR APWorld, if you were looking for the
generic [Archipelago Multi World](https://github.com/ArchipelagoMW/Archipelago/),
you've gone to the wrong place.

# Vanilla Gameplay

SULFUR is an old-school modern shooter with light extraction elements. You
traverse through areas and complete stages, with death sending you back to the
Church. Completing all stages in an area unlocks the next area permanently.

Enemies drop Sulf (money), food, weapons, armour, and various other items. Food
and ingredients can be combined as recipes at a cooking spot to make various
stronger foods or useful items like grenades. Additionally, there are
attachments, oils, and scrolls for weapons, which permanently alter their
characteristics, like adding projectiles, increasing projectile gravity, adding
penetration, or even making the projectile instant (hit-scan).

The traditional goal of the game is to complete every area, and then defeat the
Witch at the end in an epic showdown.

# Randomiser elements

- Arthur's Stamp trading are locations in the multi world, and do not provide
  the normal furnishings to the Church.
- Starting (and respawn) gun and melee weapons are randomised once by the multi
  world. So every respawn will give the same weapons. The gun is automatically
  chambered in 9mm to avoid getting softlocked by ammo drops.

# Locations

The game has 881 total locations, with the 881st location being reserved for
Victory by defeating The Witch.

- (42) One location for visiting every stage in the main game, excluding the
  onboarding stage and endless mode stage.
- (5) One location for defeating each boss except The Witch, which goals the
  game.
- (20) One location for each of Arthur's Stamp trading options
- (27) One location for each scroll combination craftable
- (6) A location for finding and for bringing to church each of the 3 findable
  base game furniture items (suitcase, refrigerator, and chest of drawers)
- (60) A location for finding each of the 55 guns and 5 melee weapons in the
  game
- (55) A location for contributing each of the 55 guns to Telia's cause.
- (275) A location for ranking up each of the 55 guns to rank 1, 2, 3, 4, and 5.
- (60) A location for finding X weapons in a specific category, without
  restrictions on _which_ specific weapon. (e.g. finding a Bo and Nunchaku is
  finding 2 melee weapons)
- (55) A location for contributing X weapons in a specific category, without
  restrictions on _which_ specific weapon. (e.g. contributing the P38 Dirk,
  Unknown, and Flicker is contributing 3 Pistols)
- (275) A location for ranking up X weapons in a specific category, without
  restrictions on _which_ specific weapon. (e.g. reaching at least rank 3 on
  each of the Mossman, Arbiter 2, 1889 Mario, and Augusta is reaching rank 3 on
  4 shotguns)

# Archipelago implementation and options

No options are available at this time.

# Wishlist / Future plans

- Fix stuttering when picking up weapons

- Show on-screen when receiving or sending items to the multi world

- Furnishing auto-unlock (currently receiving furniture requires you to pick it
  up and reload the Church)

- Make weapons not 'found' in the multiworld unobtainable (instead, on pickup,
  randomise for one of the found multiworld weapons)

- Hints on which weapons are important

- Baptismal Font purging from run. Sacrifice a gun at the Baptismal Font, if
  that gun has no more progression items involved in its locations,
  automatically unlock all locations and permanently remove the gun from
  drops and printing

- Use location groups and slot data to send all required information from
  .apworld generation to the C# plugin to avoid any hardcoded dictionaries

- Automatic item and location groups based on tags

- Options and reasonable item groups
    - Simple deathlink
    - Starting weapon from categories or specifics
    - Ranksanity, Findsanity, Contributesanity options
        - Max rank required
        - Toggle between specifics, class-based, or totals
    - Stampsanity
    - Mixing the Magic Sanity
    - Enable/disable any specific guns/melee weapons from pool, supports
      item groups
    - Toggle 'out of logic' weapon obtaining
    - Enable/disable items to be used for filler

- Remove recipe scraps and manuals from filler list, give the whole item list a
  once over to ensure things are tagged right and ready for future progressive
  information
    - Sort food / healing by amount healed and speed categories
    - Put buff-only consumables in their own category
    - Tag equipment with downsides (e.g. Turtle Shell) with high or low severity

- Redo filler generation so it only generates 'final' items like meals,
  health potions, sodas, oils, etc.
    - Exclude tier 2 scrolls by default from filler
    - Add all furniture unlocks as 'useful' generation

- Rebalance Sulf
    - Make Telia's printing cost money for multi world weapons only once, use
      slot data or event to keep track
    - Set price on specific gun based on whether it was printed for free or not
    - Make crafted scrolls at most worth 2000 Sulf to avoid infinite Sulf
      printing, or alternatively limit Scholar to one sale of each scroll
      per vendor reset

- New goal: Defeat X boss (and the bosses before them) for shorter runs

- Enable a console for generic multi world messages and commands

- Sacrifice Valuable items to Telia for free hints in the multi world
    - Add tooltip hint to let the player know

- Make filler items generate in SULFUR directly, so it can roll loot tables and
  make small lootsplosions rarely. Combine with Progressive Luck (better
  chances and more rerolls on loot tables, or vanilla Luck stat) and
  Progressive Charity (every visit to the church triggered by death or
  amulet provides filler in the collection box)

- Randomise laser sight items so their colour is fully random (for all valid
  colours)

- Separate filler items into "useful during run" and "useful at home" and
  deliver useful during run items during the run

- Randomised furniture inventories (each furniture inventory is randomly
  selected from any of the other inventories, including the toilet)

- Shopkeep randomiser (each shopkeep randomly swaps item lists)

- Randomise enemies in each biome (e.g. Black Guild members in the Cave, Goblins
  in the Desert)

- Kill enemy type locations (Each enemy type, excluding bosses, become a
  location, 9 goblins, 9 Black Guild members, 6 corrupted, 2 (3??) ghosts, 1
  Haradrian, 4 Guttercliffians, 3 craws, 5 shav'was, 4 hellshrews, total of 43
  locations)

- Add 'pacts of punishment' style difficulty modifiers that are removed as
  the multi world finds the right items, like guaranteed traps at the start.
  Any of these can be optionally kept on permanently.
    - Amulet only charges from boss kills
    - More enemies with modifiers
    - More enemies full stop
    - Healing items heal less / more slowly
    - Ammunition shortage (less ammunition found)
    - Limited capacity (inventory is smaller, max ammos are smaller)
    - World is faster (forced Yakety Sax)
    - More expensive shops (everywhere)
    - Healthier enemies
    - Higher damage taken
    - Higher environmental damage taken (explosives, poison, lava, falling,
      etc.)
    - Tight deadline

- New goal option, acquire X out of 7 wall mounts and wall frames, and mount
  specific (random) items in them found throughout the multi world. Finishing
  this unlocks Beyond the Veil and The Witch boss fight

- Make church collection box reset on its own if new items are added while in
  the Church

- Add purchasable multi world items to shopkeeps
    - Multi world inventory _per area_ _per shopkeep_

- Progressive weapons (e.g. sort weapons into cost brackets)

- Make unlocked weapons and other permanent unlocks drop through playing the
  game, with a 'bad luck' prevention mechanism, rather than requiring the
  printer or Scholar purchase

- Make equipment (accessories, armour, boots, helmet) purchasable or printable
  in the Church if acquired through multi world

- Armours and accessories into "rarity" tiers based on price and use
  completion / spheres during generation / progressives to give better
  equipment later

- Block access to Town / Dungeon if player doesn't have access to those, yet

- Make recipes into progressive unlocks similar to Minecraft, with automatic
  discovery of the recipes.

- Random weapon per respawn

- Entrance randomiser (e.g. entering Sulfur Caves from The Church might send you
  to the Forest)

- Add hints from conversations with NPCs

- Locations based on calibre of weapon used

- Gun Game mechanics (e.g. auto-swap on rank-up or every N kills or something)

- Weapon randomiser (each weapon's individual stats are randomly swapped around.
  E.g. the fire rate of the M11A2 Fisk may appear on the Bronco 89)

- Furniture randomiser (each furniture item randomly unlocks other furnishing)

- Randomise loot lists for different factions of enemies (e.g. Goblin Enemies
  drop things usually reserved for Black Guild drops)

- Area loot randomiser (each area randomly swaps its loot list for a different
  area)

- Golden run locations, one check for each stage (and boss) killed without going
  back to the Church in between. Sulfur Caves also included

- Traps / Deathlink
    - Stage reset (immediately reloads the current stage)
    - Forced chambering (immediately re-chambers all weapons in inventory)
    - Forced enchantment (immediately replaces or grants all weapons in
      inventory a random scroll effect)
    - Randomise oils (immediately randomises all oils in inventory and stash)
    - Shapeshift (shapeshifts all non-boss enemies in the area into random
      enemies, excluding bosses and corrupted amalgamations)
    - Force swap (immediately swaps current equipped weapons for other unlocked
      weapons, and carries over enchantments, oils, and XP)
    - Straitjacket (temporarily removes your armour and puts you in the
      straitjacket)
    - Amulet charge fizzle (amulet charge disappears)
    - Rudolph guide me (temporarily removes your helmet and puts on the Rudolf
      Nose. Unequipping it puts back your previous helmet)
    - Yakety Sax (gain and immediately equip the Yakety Sax)
    - Detective Pipe (gain and immediately equip the Detective Pipe)