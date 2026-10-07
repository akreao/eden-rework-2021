#!/usr/bin/env python3
"""Check the mod and build its release zip.

    python3 scripts/build-release.py            # check, then build dist/eden-rework-2021-<version>.zip
    python3 scripts/build-release.py --check    # check only
    python3 scripts/build-release.py --notes    # print this version's CHANGELOG section

The zip holds one top-level folder, eden-rework-2021/, with mod.json in it,
which is one of the two layouts the Ragnarok Offline app installs
(docs/MOD_REGISTRY.md in the app repository). CHANGELOG.md is copied in so
players who open the folder can read it too.
"""
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MOD = ROOT / "eden-rework-2021"
CHANGELOG = ROOT / "CHANGELOG.md"

# Limits the app enforces on a release archive.
MAX_ZIP = 50 * 1024 * 1024
MAX_UNPACKED = 96 * 1024 * 1024
MAX_FILES = 2000


def fail(msg):
    sys.exit(f"build-release: {msg}")


def manifest():
    data = json.loads((MOD / "mod.json").read_text(encoding="utf-8"))
    if data.get("name") != MOD.name:
        fail(f'mod.json name is {data.get("name")!r}, expected {MOD.name!r}')
    if not re.fullmatch(r"\d+(\.\d+)*", str(data.get("version", ""))):
        fail(f'mod.json version {data.get("version")!r} is not dotted numbers')
    return data


def notes(version):
    """The CHANGELOG section headed '## <version>', without the heading."""
    out, inside = [], False
    for line in CHANGELOG.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            inside = line[3:].strip() == version
            continue
        if inside:
            out.append(line)
    text = "\n".join(out).strip()
    if not text:
        fail(f"CHANGELOG.md has no '## {version}' section")
    return text + "\n"


def files():
    found = []
    for p in sorted(MOD.rglob("*")):
        if p.is_symlink():
            fail(f"{p.relative_to(ROOT)} is a link; the app refuses links")
        if p.is_file():
            found.append(p)
    if len(found) + 1 > MAX_FILES:
        fail(f"{len(found)} files, the app takes at most {MAX_FILES}")
    if sum(p.stat().st_size for p in found) > MAX_UNPACKED:
        fail("unpacks to more than 96 MB")
    return found


def main():
    data = manifest()
    version = data["version"]
    if "--notes" in sys.argv:
        sys.stdout.write(notes(version))
        return
    notes(version)
    paths = files()
    if "--check" in sys.argv:
        print(f"{MOD.name} {version}: {len(paths)} files, ok")
        return
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    out = dist / f"{MOD.name}-{version}.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in paths:
            z.write(p, f"{MOD.name}/{p.relative_to(MOD).as_posix()}")
        z.write(CHANGELOG, f"{MOD.name}/CHANGELOG.md")
    if out.stat().st_size > MAX_ZIP:
        fail(f"{out.name} is over 50 MB")
    print(out.relative_to(ROOT))


if __name__ == "__main__":
    main()
