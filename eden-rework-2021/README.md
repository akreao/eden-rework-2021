# eden-rework-2021

Eden Group as kRO reworked it in April 2021, for Ragnarok Offline (renewal).
Everything is in this folder: no server rebuild, no rAthena changes.
Turning the mod off brings back stock Eden.

**Playing the Druid line?** Install the regional-items mod from Find Mods too. The English translation doesn't cover the Druid-only items, so without it their names and descriptions aren't in English. The items work either way.

## What is in the mod

| File | What it does |
|---|---|
| `npc/eden_paradise_gear.txt` | Instructors Ur and Boya, Administrators BK, Michael, Thorn and Emil (gear quests 17528-17537). Hides the old Eden Team gear NPCs. Druids get the intermediate Druid Axe and Mace, Karnos the advanced Karnos Mace and Two-Handed Axe and the Karnos advanced shadow weapon. |
| `npc/eden_paradise_missions.txt` | Six mission boards (each placed twice), the champion hunt board and Diligent Sogil (with the champion_tickets setting on, the Lv130 and Lv140 champion hunts also give a +7 Weapon and a +7 Armor Refine Ticket, a mod addition), the Logistics Officer, cave shortcuts Rigel, Aker, Ayla and Minmin, and the mission field NPCs. Hides the old mission boards and 100-140 mission NPCs. |
| `npc/eden_paradise_warps.txt` | Adds the portal at 48,39 beside the Eden door, as kRO has it; it replaces the door's click dialog (kRO client navigation table); the door itself is map graphics and stays. Also moves two stock warps' landing spots to kRO's, and enters the Paramarket by kRO's portal at 106,43 instead of the Market Group Hustler (hidden). Adds kRO's portal from Odin Temple 3 into Odin's Past (276,236); the server's World Sync has the way back. |
| `npc/eden_lime_evenor.txt` | A copy of stock Secretary Lime Evenor (stock one hidden) whose Eden Group Mark line says what the Mark does. |
| `npc/eden_neede.txt` | A copy of stock Office Assistant Neede (stock one hidden) whose emote for Lime shows over the mod's Lime. |
| `npc/eden_paramarket.txt` | The Paramarket as kRO has run it since its 2019 renewal: every shop open every day, kRO's shop NPCs and positions (adds Seth, Zerenia, Peary and Milk), and hazyforest's stock and prices (unverified). Hides the stock shop NPCs it replaces. |
| `npc/eden_consumable_converter.txt` | Nyang Time on the 2nd floor (29,171), kRO's consumable converter: premium consumables into their 60-minute True versions. Also the optional premium drops. |
| `db/barters.yml` | The Paramarket's trades paid in items (Seth, Zerenia's tickets, Earl, Peary, Whiteberry, Blackphone) as barter shops, so the trade window shows each price in the item it's paid in. Needs an app whose rAthena reads `db/import/barters.yml`. |
| `db/item_db.yml` | The Eden Group Mark (22508) warps to moc_para01 30,16, the Eden Group's entrance hall. The Karnos Mace and Two-Handed Axe get the line of their kRO bonus that the server's table leaves out. The four Paradise caps get the headgear View their client itemInfo gives them (1529, 465), so they show on the character. |
| `db/item_combos.yml` | The Karnos advanced shadow weapon's set bonus with the five Advanced Paradise shadow pieces, from the kRO client. |
| `db/quest_db.yml` | The quests those NPCs hand out, with their cooldowns. Area hunts use the map name from the quest text as the tracker label, shortened where the client's 23-character limit forces it. |
| `db/mob_db.yml`, `db/mob_skill_db.txt` | The Valkyries' slaves in Odin's Past, and kRO's skills for the Odin's Past monsters (the server's World Sync spawns them; its Valkyries summon nothing without these). `mob_db.yml` also sets JapaneseName to the English Name for 43 hunted monsters, because the quest tracker shows JapaneseName (Green Iguana instead of Grove), and gives 32 look-alike monsters the board's labels (Venatu (Purple), Sky Deleter) so two-target hunts read differently. |
| `data/luafiles514/lua files/SignBoardList.lub` | kRO's signs over the four Administrators (110,79 / 83 / 87 / 91) and the Paramarket portal (105,41), in English, so they match on any client. iRO's client also has two old signs at 112,79 and 112,83 that a mod can't remove; they float beside BK and Michael. |
| `System/OngoingQuestInfoList.lub` | English quest-window text for 762 Eden quests and cooldowns, loaded after the English translation. |

## Settings

- **Permanent shadow gear** (off): Emil's shadow gear is permanent instead of rented.
- **Shadow gear rental (hours)** (72): rental length while it is rented.
- **Eden Coin multiplier** (1, up to 100): multiplies the Eden Coins mission board rewards give.
- **Premium consumable drops** (off): any monster kill can give one of Nyang Time's premium consumables. Not in kRO.
- **Premium drop chance** (10 in 10,000, so 0.1%; up to 10,000): the chance per kill.

Emil's script, the mission boards and the premium drops read these through `F_ModSetting`, and they change on **Apply**.

## Installing

Settings → Mods → Add mod from folder…, and choose the zip or this folder.
Or copy the folder to the mods directory
(`~/.local/share/Ragnarok Offline/state/mods` on Linux). Restart the server
for the NPCs and tables, and the app for the quest text.

## Checking it

- The map server log shows `Loading '526' entries in 'db/import/quest_db.yml'`
  and `Loading '77' entries in 'db/import/mob_db.yml'`,
  and `Loading '27' entries in 'db/import/barters.yml'`.
- In Eden (moc_para01), the new boards stand at y=38 and y=98 and the old
  mission boards are gone.

## Sources

Values come from the kRO client (Dec 2025), twRO, Bahamut 2838486,
hazyforest, Inven and Divine Pride. Anything not confirmed by two sources is
marked `[unverified]` where it is used. Built from akreao/rathena PRs #1 and #2.
