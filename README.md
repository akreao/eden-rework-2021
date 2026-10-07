# Eden Group rework (kRO, April 2021) for Ragnarok Offline

A mod for [Ragnarok Offline](https://github.com/Flux159/ragnarokoffline.app)
(renewal) that brings the Eden Group up to kRO's April 2021 rework: new gear
quests and Administrators, six mission boards with champion hunts and
deliveries, cave shortcuts, Odin's Past, and English quest text. It replaces
the old Eden gear and mission NPCs while it is on, and turning it off brings
stock Eden back. No server rebuild or rAthena change is needed.

What each file does, the settings, and how to check it loaded are in the
mod's own [README](eden-rework-2021/README.md).

## Installing

Download `eden-rework-2021-<version>.zip` from the latest
[release](../../releases/latest), then in the app: Settings → Mods → Install
from a folder…, and pick the zip. Restart the server for the NPCs and tables,
and the app for the quest text.

## Unverified values

Values come from the kRO client (Dec 2025), twRO, Bahamut 2838486,
hazyforest, Inven and Divine Pride. Anything not confirmed by two sources is
marked `[unverified]` in the script or table that uses it:

```sh
grep -rn unverified eden-rework-2021/
```

Corrections with a source are welcome, Korean sources and kRO client data
first.

## Repository layout

| Path | |
|---|---|
| `eden-rework-2021/` | The mod, exactly as it goes in a player's mods folder. |
| `CHANGELOG.md` | One `## <version>` section per release; it becomes the release notes. |
| `scripts/build-release.py` | Checks the mod against the app's limits and builds the release zip. |
| `.github/workflows/` | `check.yml` runs the check on every push; `release.yml` publishes a release for a tag. |

## Making a release

1. Change the mod, raise `version` in `eden-rework-2021/mod.json`, and add a
   `## <version>` section to `CHANGELOG.md`.
2. `python3 scripts/build-release.py --check`, commit and push.
3. Tag the commit `v<version>` and push the tag:
   `git tag v0.2.6 && git push origin v0.2.6`.

The release workflow checks that the tag matches `mod.json`, builds
`eden-rework-2021-<version>.zip` from the tagged commit, and publishes it as a
full release with that version's changelog section. The app offers players
the newest full release; publish a pre-release by hand to test with a few
people first.

## Getting listed in the app

The app lists mods from its repository's `registry/`. This one would be a
"your own repository" entry, `registry/mods/eden-rework-2021/mod.json`:

```json
{
  "name": "eden-rework-2021",
  "author": "akreao",
  "description": "Eden Group as kRO reworked it in April 2021: new gear quests and Administrators, six mission boards with champion hunts and deliveries, cave shortcuts, Odin's Past, and English quest text. Replaces the old Eden gear and mission NPCs while on. Renewal only.",
  "tags": ["quest", "eden", "npc", "kro", "renewal", "missions"],
  "homepage": "https://github.com/akreao/eden-rework-2021",
  "requires": { "era": "renewal" },
  "source": {
    "github": "akreao/eden-rework-2021",
    "asset": "eden-rework-2021-*.zip"
  }
}
```

opened as a pull request there with the regenerated `registry/index.json`
(`python3 scripts/mod-index.py`). See the app's `docs/MOD_REGISTRY.md`.

## Licence

GPL-3.0, the same as rAthena, whose Eden scripts these are built from. See
[LICENSE](LICENSE). The English quest text (`System/OngoingQuestInfoList.lub`)
and sign captions come from Gravity's official clients and remain theirs.
