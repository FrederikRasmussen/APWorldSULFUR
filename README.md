This repository is for the custom SULFUR APWorld, if you were looking for the generic [Archipelago Multi World](https://github.com/ArchipelagoMW/Archipelago/), you've gone to the wrong place.

# Vanilla Gameplay

SULFUR is an old-school modern shooter with light extraction elements. You traverse through areas and complete stages, with death sending you back to the Church. Completing all stages in an area unlocks the next area permanently.

Enemies drop Sulf (money), food, weapons, armour, and various other items. Food and ingredients can be combined as recipes at a cooking spot to make various stronger foods or useful items like grenades. Additionally, there are attachments, oils, and scrolls for weapons, which permanently alter their characteristics, like adding projectiles, increasing projectile gravity, adding penetration, or even making the projectile instant (hit-scan).

The traditional goal of the game is to complete every area, and then defeat the Witch at the end in an epic showdown.

# Randomiser elements

- Arthur's Stamp trading are locations in the multi world, and do not provide the normal furnishings to the Church.
- Starting (and respawn) gun and melee weapons are randomised once by the multi world. So every respawn will give the same weapons. The gun is automatically chambered in 9mm to avoid getting softlocked by ammo drops.

# Locations

The game has 881 total locations, with the 881st location being reserved for Victory by defeating The Witch.

- (42) One location for visiting every stage in the main game, excluding the onboarding stage and endless mode stage. 
- (5) One location for defeating each boss except The Witch, which goals the game.
- (20) One location for each of Arthur's Stamp trading options 
- (27) One location for each scroll combination craftable
- (6) A location for finding and for bringing to church each of the 3 findable base game furniture items (suitcase, refrigerator, and chest of drawers)
- (60) A location for finding each of the 55 guns and 5 melee weapons in the game
- (55) A location for contributing each of the 55 guns to Telia's cause.
- (275) A location for ranking up each of the 55 guns to rank 1, 2, 3, 4, and 5.
- (60) A location for finding X weapons in a specific category, without restrictions on _which_ specific weapon. (e.g. finding a Bo and Nunchaku is finding 2 melee weapons)
- (55) A location for contributing X weapons in a specific category, without restrictions on _which_ specific weapon. (e.g. contributing the P38 Dirk, Unknown, and Flicker is contributing 3 Pistols)
- (275) A location for ranking up X weapons in a specific category, without restrictions on _which_ specific weapon. (e.g. reaching at least rank 3 on each of the Mossman, Arbiter 2, 1889 Mario, and Augusta is reaching rank 3 on 4 shotguns)

# Archipelago implementation and options

No options are available at this time.

# Wishlist / Future plans

- Randomise loot lists for different factions of enemies (e.g. Goblin Enemies drop things usually reserved for Black Guild drops)

- Entrance randomiser (e.g. entering Sulfur Caves from The Church might send you to the Forest)

- Randomise enemies in each biome (e.g. Black Guild members in the Cave, Goblins in the Desert)

- Shopkeep randomiser (each shopkeep randomly swaps item lists)

- Area loot randomiser (each area randomly swaps its loot list for a different area)

- Weapon randomiser (each weapon's individual stats are randomly swapped around. E.g. the fire rate of the M11A2 Fisk may appear on the Bronco 89)

- Furniture randomiser (each furniture item randomly unlocks other furnishing)

- Furnishing auto-unlock (currently receiving furniture requires you to pick it up and reload the Church)

- Randomised furniture inventories (each furniture inventory is randomly selected from any of the other inventories, including the toilet)

- Gun Game mechanics (e.g. auto-swap on rank-up or every N kills or something)

- Kill enemy type locations (Each enemy type, excluding bosses, become a location, 9 goblins, 9 Black Guild members, 6 corrupted, 2 (3??) ghosts, 1 Haradrian, 4 Guttercliffians, 3 craws, 5 shav'was, 4 hellshrews, total of 43 locations)

- Make weapons not 'found' in the multiworld unobtainable (instead, on pickup, randomise for one of the found multiworld weapons)

- Separate filler items into "useful during run" and "useful at home" and deliver useful during run items during the run

- Make filler items generate in SULFUR directly, so it can roll loot tables and make small lootsplosions rarely

- Prevent non-unlocked weapons from dropping / being bought

- Progressive weapons

- Baptismal Font purging from run

- Hints on which weapons are important

- Fix stuttering when picking up weapons

- Fix prices on weapons
  - Make Telia's printing cost money for multi world weapons only once, use slot data or event to keep track
  - Set price on specific gun based on whether it was printed for free or not

- Sort weapons and armours into "rarity" tiers based on price and use to gate better equipment in logic

- Make equipment (accessories, armour, boots, helmet) purchasable or printable in the Church if acquired through multi world

- Randomise laser sight items so their colour is fully random (for all valid colours)

- Add purchasable multi world items to shopkeeps
  - Multi world inventory _per area_ _per shopkeep_

- Add hints from conversations with NPCs

- Block access to Town / Dungeon if player doesn't have access to those, yet

- Make church collection box reset on its own if new items are added while in the Church

- Golden run locations, one check for each stage (and boss) killed without going back to the Church in between. Sulfur Caves also included

- New goal option, acquire X out of 7 wall mounts and wall frames, and mount specific (random) items in them found throughout the multi world. Finishing this unlocks Beyond the Veil and The Witch boss fight

- Show on-screen when receiving or sending items to the multi world

- Enable a console for generic multi world messages and inputs

- Sacrifice Valuable items to Telia for free hints in the multi world

- Make unlocked weapons and other permanent unlocks drop through playing the game, with a 'bad luck' prevention mechanism, rather than requiring the printer or Scholar purchase

- Random weapon per respawn

- Locations based on calibre of weapon used

- Received equipment is auto-equipped, existing is voided or dropped base on options

- Separate randomiser and Archipelago implementation so one doesn't need the other

- Make either the .apworld capable of outputting clean information for the BepInEx plugin, or make the BepInEx plugin capable of outputting clean .apworld info. Maybe use an attached file from the generated world to ensure that the game plugin version doesn't get outdated location and item ids.

- Options and reasonable item groups
  - Simple deathlink
  - Starting weapon from categories or specifics
  - Randomise amount of specific and generic weapon location checks (e.g. only some weapons need rank 5, some weapons don't even need to be found)
  - Disable balancing tweaks (e.g. guns acquired through multi world sell for 0 Sulf)
  - Disable / enable any category of checks

- Traps / Deathlink
  - Stage reset (immediately reloads the current stage)
  - Forced chambering (immediately re-chambers all weapons in inventory)
  - Forced enchantment (immediately replaces or grants all weapons in inventory a random scroll effect)
  - Randomise oils (immediately randomises all oils in inventory and stash)
  - Shapeshift (shapeshifts all non-boss enemies in the area into random enemies, excluding bosses and corrupted amalgamations)
  - Force swap (immediately swaps current equipped weapons for other unlocked weapons, and carries over enchantments, oils, and XP)
  - Straitjacket (temporarily removes your armour and puts you in the straitjacket)
  - Amulet charge fizzle (amulet charge disappears)
  - Rudolph guide me (temporarily removes your helmet and puts on the Rudolf Nose. Unequipping it puts back your previous helmet)
  - Yakety Sax (gain and immediately equip the Yakety Sax)
  - Detective Pipe (gain and immediately equip the Detective Pipe)