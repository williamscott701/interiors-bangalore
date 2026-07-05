import json

with open("interiors.json", encoding="utf-8") as f:
    entries = json.load(f)

lines = [
    "# Interior Designers – Whitefield / Bangalore Area",
    "",
    "| # | Name | Rating | Reviews | Type | Address |",
    "|---|------|--------|---------|------|---------|",
]

for i, e in enumerate(entries, 1):
    name = e["name"].replace("|", "\\|")
    if e["sponsored"]:
        name += " `Sponsored`"
    rating = e["rating"] if e["rating"] is not None else "—"
    reviews = e["reviews"] if e["reviews"] else "—"
    biz_type = e.get("type", "") or "—"
    address = e["address"].strip(" ·").strip().replace("|", "\\|") or "*(no address)*"
    lines.append(f"| {i} | {name} | {rating} | {reviews} | {biz_type} | {address} |")

with open("interiors.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines) + "\n")

print(f"Written {len(entries)} entries to interiors.md")
