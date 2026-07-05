import re
import json
import sys


def parse_listings(text):
    """
    Parse raw Google Maps listings export into structured dicts.
    Strips sponsored markers, ads, and noise lines.
    """
    NOISE = {
        "Results", "Share", "Website", "Directions", "On-site services",
        "Online estimates", "Online appointments", "In-store shopping",
        "Kerbside pickup", "Delivery", "On-site services not available",
        "Visit site", "You've reached the end of the list.",
        "Sponsored", "",
    }
    AD_PREFIXES = (
        "Trusted Home", "Get expert", "Top Interior", "Home Interior",
        "Get a Free", "End to End", "Unbeatable", "50+", "2 BHK",
        "Custom Home", "Contact our", "Bangalore Home", "Interior Designers Yelahanka",
    )

    lines = [l.strip() for l in text.splitlines()]
    entries = []
    sponsored_next = False
    i = 0

    while i < len(lines):
        line = lines[i]

        if line == "Sponsored":
            sponsored_next = True
            i += 1
            continue

        if line in NOISE or line.startswith('"') or any(line.startswith(p) for p in AD_PREFIXES):
            i += 1
            continue

        # A listing starts with a name line followed by a rating line
        if i + 1 < len(lines) and re.match(r'^(\d+\.\d+\(\d[\d,]*\)|No reviews)$', lines[i + 1]):
            name = line
            rating_raw = lines[i + 1]
            i += 2

            m = re.match(r'^(\d+\.\d+)\((\d[\d,]*)\)$', rating_raw)
            if m:
                rating = float(m.group(1))
                reviews = int(m.group(2).replace(",", ""))
            else:
                rating = None
                reviews = 0

            type_address = lines[i] if i < len(lines) else ""
            i += 1
            parts = type_address.split(" · ", 1)
            biz_type = parts[0].strip() if parts else ""
            address = re.sub(r'^[^a-zA-Z0-9#/(]+', '', parts[1]).strip() if len(parts) > 1 else ""

            hours_line = lines[i] if i < len(lines) else ""
            i += 1
            phone = ""
            hours = hours_line
            if " · " in hours_line:
                hp = hours_line.rsplit(" · ", 1)
                hours = hp[0].strip()
                phone = hp[1].strip()

            entries.append({
                "name": name,
                "rating": rating,
                "reviews": reviews,
                "type": biz_type,
                "address": address,
                "hours": hours,
                "phone": phone,
                "sponsored": sponsored_next,
            })
            sponsored_next = False
        else:
            i += 1

    return entries


def deduplicate(entries):
    """Remove duplicates by address, then collapse same-name entries keeping the longer address."""
    seen_addr = set()
    result = []
    for e in entries:
        key = e["address"].lower().strip() if e["address"] else None
        if key and key in seen_addr:
            continue
        if key:
            seen_addr.add(key)
        result.append(e)

    # Collapse same-name duplicates (e.g. sponsored entry with truncated address)
    by_name = {}
    for e in result:
        k = e["name"].lower().strip()
        if k in by_name:
            existing = by_name[k]
            if len(e["address"]) > len(existing["address"]):
                e["sponsored"] = e["sponsored"] or existing["sponsored"]
                by_name[k] = e
            else:
                existing["sponsored"] = existing["sponsored"] or e["sponsored"]
        else:
            by_name[k] = e

    return list(by_name.values())


if __name__ == "__main__":
    paths = sys.argv[1:] if len(sys.argv) > 1 else ["raw.md"]

    all_entries = []
    for path in paths:
        with open(path, encoding="utf-8") as f:
            all_entries.extend(parse_listings(f.read()))

    all_entries = deduplicate(all_entries)
    all_entries.sort(key=lambda e: (-(e["rating"] or 0), -e["reviews"]))

    print(json.dumps(all_entries, indent=2, ensure_ascii=False))
    print(f"# {len(all_entries)} unique listings", file=sys.stderr)
