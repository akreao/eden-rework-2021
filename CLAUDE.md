# Working in this repository

This is **eden-rework-2021**, a mod for [Ragnarok Offline](https://github.com/Flux159/ragnarokoffline.app)
that brings the Eden Group (Paradise Group) up to kRO's April 2021 rework.
It is renewal only, and it is self-contained: NPC scripts, import tables and
client files, with no rAthena or app changes. It has to load on the app's
rAthena fork ([Flux159/rathena](https://github.com/Flux159/rathena), branch
`ragnarokoffline`) as that fork is.

## Layout

| Path | What it is |
|---|---|
| `eden-rework-2021/` | The mod, exactly as it goes in a player's mods folder. Its own `README.md` says what each file does. |
| `eden-rework-2021/mod.json` | Name, version, `requires`, and the player settings. |
| `CHANGELOG.md` | One `## <version>` section per release. It becomes the release notes players read in the app. |
| `scripts/build-release.py` | `--check` checks the mod against the app's limits; no flag builds `dist/eden-rework-2021-<version>.zip`; `--notes` prints this version's changelog section. |
| `.github/workflows/` | `check.yml` on every push; `release.yml` publishes a release; `delete-release.yml` (run by hand) removes one. |

## Where changes are made

In the "Eden/Paradise 2021 Rework" Claude project, the mod package in the
project files (`eden/mod/eden-rework-2021/`) is the source of truth. Change
it there, then copy the whole folder over `eden-rework-2021/` here when
releasing. Don't edit the copy here alone, or the next copy overwrites it.
Outside that project, edit `eden-rework-2021/` directly.

## Content rules

- **Sources.** When sources disagree, kRO client data wins, then other Korean
  sources. kRO data also beats what stock rAthena has, where that's feasible.
  The English text comes from the iRO client.
- **Unverified values.** Any value that two sources don't confirm is marked
  `[unverified]` (or `[unverified: what is in doubt]`) in a comment where it's
  used. Keep the existing markers, and
  add one for each new value that has no second source. Remove a marker only
  when you can name the second source.
- **All or nothing.** With the mod on, the rework fully replaces the old Eden
  gear and mission content. The old NPCs are hidden, not left beside the new
  ones. There are no switches for running old and new side by side, and no
  half states. Turning the mod off brings stock Eden back.
- **Tables are imports.** `db/` holds only the entries the mod adds or
  changes, not whole copies of rAthena's tables.
- **Settings.** Player options are declared in `mod.json` `settings` and read
  in scripts with `callfunc("F_ModSetting","eden-rework-2021",<key>,<default>)`.
  Never rename a setting key: the app stores players' choices by key, so a
  rename silently resets them.
- **Script style.** Follow rAthena's script and YAML conventions.

## Releasing

1. Copy the mod in (see above), raise `version` in
   `eden-rework-2021/mod.json`, and add a `## <version>` section to
   `CHANGELOG.md`. Write that section for players, not developers.
2. Run `python3 scripts/build-release.py --check`.
3. Commit and push to `main`.

`release.yml` runs on every push to `main`. When `mod.json` has a version
that has no release yet, it builds the zip from that commit, tags
`v<version>` and publishes a full release. A push that doesn't raise the
version publishes nothing.

- Don't push tags yourself. The workflow makes them, and Claude's cloud
  sessions can't push tags anyway.
- Don't rebuild or edit a version that's already released. Players compare
  versions, so a fix gets a new version.
- Don't commit zips. `dist/` and `*.zip` are ignored.
- Raise `requires.app` in `mod.json` when the mod starts relying on something
  a newer app added. Players on older apps then keep the last release that
  works for them.

The app's rules for release archives: at most 50 MB zipped, 96 MB and
2000 files unpacked, no links, and `mod.json` at the top or inside one
top-level folder. `build-release.py --check` enforces the first three.

## Testing

Build the zip, then in the app use Settings → Mods → Install from a folder…
and pick it. Restart the server for scripts and tables, and the app for client
files. The mod's own `README.md` lists what to look for in the map-server log
and in game.

## Getting listed in the app

The app lists mods from `registry/` in its own repository. This mod would be a
"your own repository" entry; the draft is in `README.md`. See the app's
`docs/MOD_REGISTRY.md`.
