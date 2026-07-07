# Interiors Bangalore

A personal data project that scrapes, cleans, and ranks interior designers in Bangalore (originally focused on Whitefield, later expanded citywide) from Google Maps listings, then presents them as a static, filterable, self-contained HTML directory — `index.html` — for comparing studios before choosing one for a home renovation.

There is no build system, server, or framework here. It's a small pipeline of Python scripts that turn raw pasted Google Maps text into structured JSON, which is then hand-embedded into a single-page HTML app with vanilla JS/CSS.

## What it does

1. **Scrape (manual)** — Google Maps search results for "interior designer" across various Bangalore zones are copy-pasted into `raw.md`, `raw2.md`, `raw3.md`, `raw4.md` as plain text exports (name, rating, review count, business type, address, hours, phone).
2. **Parse** (`parse.py`) — regex-based parser that strips ads/sponsored noise and known promotional prefixes, extracts structured fields (name, rating, review count, type, address, hours, phone, sponsored flag) from the raw text blocks, deduplicates by address and by name, and prints sorted JSON to stdout.
3. **Enrich/curate** — the parsed listings are manually classified into 4 tiers (`interiors.json`, `archive.json`):
   - Category 1: High-Volume Tech Platforms & Aggregators (e.g. Livspace, HomeLane, DesignCafe, Arrivae)
   - Category 2: Organized Mid-to-Large Mid-Premium Players
   - Category 3: Boutique & Bespoke Studios
   - Category 4: High-End Custom Luxury Designers

   Each entry also carries an estimated annual project volume, a star-rating breakdown (5★–1★ counts), a zone/region (East/West/North/South/Central), an area name, a Google Maps search URL, and whether the studio owns its own factory. Lower-review/lower-confidence listings are split off into `archive.json`.
4. **Render** — two generator scripts turn the JSON into human-usable outputs:
   - `to_md.py`: writes a simple markdown comparison table (`interiors.md`) with rank, name, rating, reviews, type, and address.
   - `generate_shortlist_html.py`: builds a richer, interactive HTML table (`interiors_shortlist.html`) with category color-coding, a stacked star-distribution bar per studio, volume badges, sliders for minimum project volume and maximum "bad review" percentage, checkbox filters by category/volume, search, sorting, and a "hide" feature (persisted to `localStorage`) for entries the user wants to dismiss from consideration.
5. **`index.html`** (identical to `interiors.html`) is the polished, final standalone directory page — a larger, more complete version of the shortlist tool (~2,000 lines, SEO meta tags, "how to choose a category" guidance, zone-based filtering, factory-ownership filter, direct Google Maps links per listing) intended to be opened directly in a browser or hosted as a static page.

## Tech stack

- **Python 3** (stdlib only: `re`, `json`, `sys`, `collections`) — no dependencies, no `requirements.txt`, no package manager.
- **Static HTML/CSS/vanilla JavaScript** for the output pages — no frameworks, no bundler, no npm/build step. Data is embedded directly as a JS array literal (`const DATA = [...]`) inside the HTML.
- No server, no database, no tests, no CI configuration.

## Project structure

```
parse.py                     # Parses raw Google Maps text exports into structured JSON
to_md.py                     # interiors.json -> interiors.md (simple table)
generate_shortlist_html.py   # interiors.json -> interiors_shortlist.html (interactive tool)

raw.md, raw2.md, raw3.md, raw4.md   # Raw pasted Google Maps listing exports (source data)
interiors.json               # Curated/categorized listings (active shortlist)
archive.json                 # Lower-confidence / excluded listings
interiors.md, _shortlist.md  # Generated markdown tables
interiors.html, index.html   # Final standalone interactive directory (same content)
_interiors_shortlist.html    # Earlier/alternate generated shortlist output
```

## Setup / usage

No installation required beyond Python 3.

```bash
# Parse one or more raw Google Maps export files into JSON
python3 parse.py raw.md raw2.md raw3.md raw4.md > interiors.json

# Generate a plain markdown comparison table from interiors.json
python3 to_md.py            # writes interiors.md

# Generate the interactive HTML shortlist tool from interiors.json
python3 generate_shortlist_html.py   # writes interiors_shortlist.html
```

To view the final directory, just open `index.html` (or `interiors.html`) in a browser — no server needed.

Note: the category assignments, volume estimates, and star-distribution numbers embedded in `generate_shortlist_html.py` and in `interiors.json`/`archive.json` were curated/estimated by hand for this specific dataset; they are not recomputed automatically from `raw*.md`, so re-running `parse.py` on new raw data will not regenerate the tiering — that step is manual.

## Status

This is a personal, single-purpose research tool (comparison-shopping for a home interior designer in Bangalore), not a maintained software product. There are no automated tests, no CI, and no plans evident in the code for turning this into a service — it's a one-off scrape-clean-render pipeline with its output committed directly to the repo.
