"""Build and verify the explicitly allowlisted trial package; standard library only."""
from pathlib import Path
import hashlib
import json
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
assert re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version), "Invalid version"
files = sorted((ROOT / "project-change-delivery").rglob("*.md"))
files += [ROOT / name for name in ("TRYOUT.md", "VERSION", "RELEASE-NOTES.md")]
assert ROOT / "project-change-delivery/SKILL.md" in files
for path in files:
    assert path.resolve().is_relative_to(ROOT)
    content = path.read_text(encoding="utf-8")
    assert not re.search(r"(?<![A-Za-z])[A-Za-z]:[\\/]", content), f"Machine path in {path.name}"
    assert not re.search(r"(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|sk-[A-Za-z0-9]{24,})", content), f"Possible credential in {path.name}"
    for target in re.findall(r"\]\(([^)]+)\)", content):
        if "://" not in target and not target.startswith("#"):
            resolved = (path.parent / target.split("#")[0]).resolve()
            assert resolved.is_file() and resolved in [p.resolve() for p in files], f"Missing packaged link: {target}"
out = ROOT / "dist"
out.mkdir(exist_ok=True)
archive = out / f"project-change-delivery-v{version}.zip"
with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as z:
    for path in files:
        info = zipfile.ZipInfo(path.relative_to(ROOT).as_posix(), (2026, 10, 26, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        z.writestr(info, path.read_bytes())
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert set(z.namelist()) == {p.relative_to(ROOT).as_posix() for p in files}
    for path in files:
        assert z.read(path.relative_to(ROOT).as_posix()) == path.read_bytes()
manifest = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
(out / "MANIFEST.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
checks = [archive, out / "MANIFEST.json"]
(out / "SHA256SUMS.txt").write_text("".join(hashlib.sha256(p.read_bytes()).hexdigest() + "  " + p.name + "\n" for p in checks), encoding="utf-8")
print(json.dumps({"archive": str(archive), "files": len(files), "sha256": hashlib.sha256(archive.read_bytes()).hexdigest()}))
