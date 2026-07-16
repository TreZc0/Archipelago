This file documents the logic needed to write a tracker for this APWorld, particularly anything unintuitive or different than the core implementation. In general, the logic here is the same as the core implementation for the same settings, unless stated otherwise.

## Goals

Dungeons goal is based on pendants/crystals, not boss kills, although both Aga's must be defeated. New goals Trinity and Completionist, both pretty self-explanatory.

## Inverted

OWR uses Inverted 2.0, with a few changes intended to make Inverted closer to the vanilla game experience.
* Bomb Shop and Link's House are at their vanilla locations, so Link's House requires Moon Pearl + Light World access, Bomb Shop does not
* Ice Palace entrance requires Mirror
* Spiral and Mimic caves are connected by a bridge that also drops down to both Fairy Ascension entrances, which could have crossed entrance implications
* The Flute is always pre-activated
* Flute Spot 1 is next to GT
* There is no ladder from southwest Dark Death Mountain to near Ganons Tower
* Bumper Cave/Death Mountain Descent are both vanilla
  * Bumper Cave Ledge only requires Cape
  * Light World is logically assessible with Flute + Lamp, and reachable out of logic with just Flute

## Shuffle Link's House

* Link's House could be in the Dark World and its check would require Moon Pearl
* If Link's House is in Death Mountain or the Dark World and Sanctuary is at Pyramid, the list of accessible entrances gets weird
* The above also applies to Inverted if Link's House is in the Light World

## Shuffle back of Tavern
Self explanatory. Could require Moon Pearl on top of reaching the entrance

## Zelgawoods
Self explanatory?

## Door Shuffle
Good luck :) Without lobby shuffle, some logic can be added for accessing each dungeon (Swamp is Flippers/Dam locked, etc.). Is there anything I could add to the slot data to help with this? Like a list of locations per dungeon?

## Logical Enemizer
TODO

## Prize Shuffle
Self explanatory.

## Flute Shuffle
### Open/Standard mode
Exactly one Flute spot will always be West Death Mountain (Bottom), East Death Mountain (Bottom), or Death Mountain TR Pegs Area. With Death Mountain TR Pegs Area, all of East Death Mountain (except Mimic Cave and Floating Island) is accessible with Flute.
Hera area can be reached with Flute/Hammer or Flute/Hookshot/Mirror, and southwest DM is available with Flute and either Hammer or Hookshot. West Dark DM has the same requirements, while Southeast Dark DM is accessible with Flute/Mitts, and Northeast Dark DM with entrance shuffle needs Flute/Mitts/Hammer.

If the Flute spot is East Death Mountain (Bottom), it's identical to TR Pegs without crossed entrance shuffle, but with it you need to Hookshot to southwest DM, Hookshot/Mirror to Hera area, and Hookshot/Mirror/Hammer to reach northeast DM and every entrance on the dropdowns.

Zora is accessible with only Flute if the Flute spots contain Zora Waterfall Area or Zora Approach Ledge

### Inverted
Exactly one Flute spot will always be West Dark Death Mountain (Top), East Dark Death Mountain (Bottom), or Turtle Rock Area. All of Dark Death Mountain is accessible with just the Flute, except for crossed entrance shuffle with the Flute spot at East Dark Death Mountain (Bottom). In that case, everything except the two bottom-right entrances must be reached by either a connector to the top of Dark DM, or a connector to the top of Light DM + Mirror.

Catfish is accessible in Inverted with only Flute if the Flute spots are Catfish Area or Catfish Approach Ledge. The area around Dark Potion Shop can be reached using Flute if a Flute spot is Dark Witch Area or Qirn Jump East Bank. East Dark World is available with Flute if any of the following are Flute spots:
* Pyramid Area
* Palace of Darkness Area
* Darkness Nook Area (Dark World Flute 5 spot)
* Dark Tree Line Area (to the southwest of PoD area)
* Dark Dunes Area (the rocks east of Pyramid)