# eden-rework-2021

Eden Group as kRO reworked it in April 2021, for Ragnarok Offline (renewal).
Everything is in this folder: no server rebuild, no rAthena changes.
Turning the mod off brings back stock Eden.

## What is in the mod

| File | What it does |
|---|---|
| `npc/eden_paradise_gear.txt` | Instructors Ur and Boya, Administrators BK, Michael, Thorn and Emil (gear quests 17528-17537). Hides the old Eden Team gear NPCs. |
| `npc/eden_paradise_missions.txt` | Six mission boards (each placed twice), the champion hunt board and Sogil, the Logistics Officer, cave shortcuts Rigel, Aker, Ayla and Minmin, and the mission field NPCs. Hides the old mission boards and 100-140 mission NPCs. |
| `npc/eden_paradise_warps.txt` | Adds the portal at 48,39 beside the Eden door, as kRO has it; it replaces the door's click dialog (kRO client navigation table); the door itself is map graphics and stays. Also moves two stock warps' landing spots to kRO's. |
| `npc/odin_past.txt` | Odin's Past (odin_past) spawns, including Valkyries Reginleif and Ingrid. |
| `db/quest_db.yml` | The quests those NPCs hand out, with their cooldowns. |
| `db/mob_db.yml`, `db/mob_skill_db.txt` | Odin's Past monsters and their skills. |
| `data/luafiles514/lua files/SignBoardList.lub` | kRO's signs over the four Administrators (110,79 / 83 / 87 / 91), in English, so they match on any client. iRO's client also has two old signs at 112,79 and 112,83 that a mod can't remove; they float beside BK and Michael. |
| `System/OngoingQuestInfoList.lub` | English quest-window text for 762 Eden quests and cooldowns, loaded after the English translation. |

## Settings

- **Permanent shadow gear** (off): Emil's shadow gear is permanent instead of rented.
- **Shadow gear rental (hours)** (72): rental length while it is rented.

Both are read by Emil's script through `F_ModSetting`, and change on **Apply**.

## Installing

Settings → Mods → Add mod from folder…, and choose the zip or this folder.
Or copy the folder to the mods directory
(`~/.local/share/Ragnarok Offline/state/mods` on Linux). Restart the server
for the NPCs and tables, and the app for the quest text.

## Checking it

- The map server log shows `Loading '526' entries in 'db/import/quest_db.yml'`
  and `Loading '10' entries in 'db/import/mob_db.yml'`.
- In Eden (moc_para01), the new boards stand at y=38 and y=98 and the old
  mission boards are gone.

## Sources

Values come from the kRO client (Dec 2025), twRO, Bahamut 2838486,
hazyforest, Inven and Divine Pride. Anything not confirmed by two sources is
marked `[unverified]` where it is used. Built from akreao/rathena PRs #1 and #2.
