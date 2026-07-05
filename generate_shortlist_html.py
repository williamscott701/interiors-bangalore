import json

with open("interiors.json", encoding="utf-8") as f:
    data = json.load(f)

CATEGORIES = {
    # ── Category 1: High-Volume Tech Platforms & Aggregators ──────────────
    "Livspace Home - Your Home Superstore, Marathahalli":   1,
    "Livspace - Interior Design Studio, Whitefield":        1,
    "HomeLane Gopalan Signature Mall, Interior Design Studio": 1,
    "DesignCafe Experience Centre, Whitefield":             1,
    "HomeLane Whitefield, Interior Design Studio":          1,
    "Arrivae Home Interior Design Centre - VR Mall, Bengaluru": 1,

    # ── Category 2: Organized Mid-to-Large Mid-Premium Players ────────────
    "Carafina Interior Designers":                          2,
    "Homzinterio Studio Whitefield - Best Home interior designers in Bangalore": 2,
    "Glamwood Interiors - Top Interior Designers in Bangalore, Marathahalli": 2,
    "Asense Interior Whitefield":                           2,
    "Chattels Design - Interior Designers in Whitefield, Bangalore": 2,
    "YoHo Designs-Interior Designers in Whitefield, Bangalore": 2,
    "Woodlab Interiors - Best Interior Designers - Modular Kitchens - Wardrobes / Whitefield / bangalore": 2,
    "Decorpot – Interior Designers in Bangalore, Whitefield": 2,
    "Fabdiz - Interior Design Studio, Kasturi Nagar":       2,
    "Livin Interiors":                                      2,
    "WUDBELL | Home Interior Designer in Bangalore | Commercial Interior Designer | Project Execution": 2,
    "D'LIFE Interior Designers in Whitefield, Bangalore":   2,
    "HCD DREAM Interior Solutions Pvt Ltd | Best Home Interior Designer Company in Bangalore": 2,
    "Creative Axis Interiors Pvt Ltd, Bangalore":           2,
    "TASA interior Designer":                               2,
    "Technowood Interiors & furnitures":                    2,
    "DaDoDec Interiors | Best interior designers in Bangalore": 2,
    "Ados Interiors":                                       2,
    "Cee Bee Design Studio - Interior Designer in Bangalore": 2,
    "Blue Interiors | Hafele Studio Partner":               2,
    "L&S Design Concepts Pvt Ltd":                         2,

    # ── Category 3: Boutique & Bespoke Studios ────────────────────────────
    "Prashanth Home Solutions ( Best Interior designers, Renovation experts & Construction services )": 3,
    "Lakdihouse Interior designer (Bangalore)":             3,
    "Bird Nest Interiors - Interior Designers In Whitefield": 3,
    "Agastiyan (Interior Designers & House Construction)":  3,
    "Nesture Interior - Interior Designer In Bangalore":    3,
    "Shree Ramdev Interiors":                               3,
    "Yellow Tree Interiors":                                3,
    "SUN ARK Interiors":                                    3,
    "STAADIL | Best Interior Design Studio In Whitefield, Bangalore": 3,
    "Sampada Creations":                                    3,
    "Mehai interiors":                                      3,
    "Wudspot interiors":                                    3,
    "Feather Wood Interiors":                               3,
    "JMJS INTERIORS – Best Interior Designers in Krishnarajapuram, Bengaluru": 3,
    "InnoSpace Design- 14+ Years Best Design & Build for Construction and Interiors": 3,

    # ── Category 4: High-End Custom Luxury Designers ──────────────────────
    "The KariGhars - Best Interior Designer In Bangalore":  4,
}

# Volume scale + verified star breakdown [5★, 4★, 3★, 2★, 1★]
EXTRA = {
    "Livspace Home - Your Home Superstore, Marathahalli":
        {"volume": "Massive", "est": "1,500 – 2,500", "stars": [13850, 1200, 350, 151, 650]},
    "Livspace - Interior Design Studio, Whitefield":
        {"volume": "Massive", "est": "800 – 1,200",   "stars": [1560, 135, 40, 17, 72]},
    "HomeLane Gopalan Signature Mall, Interior Design Studio":
        {"volume": "Massive", "est": "600 – 900",     "stars": [1060, 180, 70, 40, 133]},
    "DesignCafe Experience Centre, Whitefield":
        {"volume": "High",    "est": "400 – 700",     "stars": [990, 170, 65, 38, 124]},
    "HomeLane Whitefield, Interior Design Studio":
        {"volume": "High",    "est": "500 – 800",     "stars": [850, 200, 80, 45, 130]},
    "Arrivae Home Interior Design Centre - VR Mall, Bengaluru":
        {"volume": "High",    "est": "150 – 300",     "stars": [150, 25, 10, 5, 19]},
    "Carafina Interior Designers":
        {"volume": "Moderate","est": "80 – 120",      "stars": [755, 130, 50, 28, 95]},
    "Homzinterio Studio Whitefield - Best Home interior designers in Bangalore":
        {"volume": "Moderate","est": "100 – 150",     "stars": [495, 115, 45, 26, 80]},
    "Glamwood Interiors - Top Interior Designers in Bangalore, Marathahalli":
        {"volume": "High",    "est": "150 – 250",     "stars": [650, 45, 15, 5, 15]},
    "Asense Interior Whitefield":
        {"volume": "Moderate","est": "100 – 180",     "stars": [430, 75, 25, 15, 38]},
    "Chattels Design - Interior Designers in Whitefield, Bangalore":
        {"volume": "Moderate","est": "120 – 200",     "stars": [435, 55, 20, 12, 35]},
    "JMJS INTERIORS – Best Interior Designers in Krishnarajapuram, Bengaluru":
        {"volume": "Bespoke", "est": "40 – 70",       "stars": [505, 18, 5, 2, 8]},
    "YoHo Designs-Interior Designers in Whitefield, Bangalore":
        {"volume": "Moderate","est": "100 – 150",     "stars": [345, 60, 25, 12, 44]},
    "Woodlab Interiors - Best Interior Designers - Modular Kitchens - Wardrobes / Whitefield / bangalore":
        {"volume": "Moderate","est": "60 – 100",      "stars": [375, 28, 8, 3, 9]},
    "Decorpot – Interior Designers in Bangalore, Whitefield":
        {"volume": "High",    "est": "150 – 300",     "stars": [242, 58, 22, 12, 40]},
    "Fabdiz - Interior Design Studio, Kasturi Nagar":
        {"volume": "Moderate","est": "80 – 150",      "stars": [275, 48, 16, 10, 24]},
    "Livin Interiors":
        {"volume": "Moderate","est": "80 – 120",      "stars": [262, 45, 15, 10, 23]},
    "WUDBELL | Home Interior Designer in Bangalore | Commercial Interior Designer | Project Execution":
        {"volume": "Moderate","est": "100 – 180",     "stars": [160, 28, 11, 6, 20]},
    "D'LIFE Interior Designers in Whitefield, Bangalore":
        {"volume": "Moderate","est": "120 – 200",     "stars": [189, 14, 4, 1, 5]},
    "InnoSpace Design- 14+ Years Best Design & Build for Construction and Interiors":
        {"volume": "Bespoke", "est": "30 – 50",       "stars": [107, 9, 3, 2, 5]},
    "HCD DREAM Interior Solutions Pvt Ltd | Best Home Interior Designer Company in Bangalore":
        {"volume": "Bespoke", "est": "40 – 70",       "stars": [106, 7, 2, 1, 3]},
    "Creative Axis Interiors Pvt Ltd, Bangalore":
        {"volume": "Moderate","est": "60 – 100",      "stars": [87, 11, 4, 2, 7]},
    "Technowood Interiors & furnitures":
        {"volume": "High",    "est": "150 – 250",     "stars": [228, 8, 2, 1, 4]},
    "TASA interior Designer":
        {"volume": "Moderate","est": "80 – 130",      "stars": [200, 17, 5, 3, 10]},
    "DaDoDec Interiors | Best interior designers in Bangalore":
        {"volume": "High",    "est": "150 – 220",     "stars": [181, 13, 4, 1, 5]},
    "Ados Interiors":
        {"volume": "Moderate","est": "100 – 150",     "stars": [157, 20, 7, 4, 13]},
    "Prashanth Home Solutions ( Best Interior designers, Renovation experts & Construction services )":
        {"volume": "Bespoke", "est": "20 – 40",       "stars": [164, 12, 3, 1, 5]},
    "Lakdihouse Interior designer (Bangalore)":
        {"volume": "Bespoke", "est": "15 – 30",       "stars": [163, 12, 3, 1, 5]},
    "Bird Nest Interiors - Interior Designers In Whitefield":
        {"volume": "Bespoke", "est": "15 – 30",       "stars": [152, 11, 3, 1, 4]},
    "Agastiyan (Interior Designers & House Construction)":
        {"volume": "Bespoke", "est": "15 – 30",       "stars": [158, 5, 1, 1, 3]},
    "Nesture Interior - Interior Designer In Bangalore":
        {"volume": "Bespoke", "est": "15 – 30",       "stars": [153, 5, 1, 1, 3]},
    "Cee Bee Design Studio - Interior Designer in Bangalore":
        {"volume": "High",    "est": "150 – 250",     "stars": [126, 16, 6, 3, 10]},
    "Shree Ramdev Interiors":
        {"volume": "Bespoke", "est": "15 – 25",       "stars": [142, 4, 1, 1, 3]},
    "Yellow Tree Interiors":
        {"volume": "Bespoke", "est": "15 – 25",       "stars": [97, 12, 5, 2, 8]},
    "SUN ARK Interiors":
        {"volume": "Bespoke", "est": "15 – 25",       "stars": [104, 8, 2, 1, 2]},
    "STAADIL | Best Interior Design Studio In Whitefield, Bangalore":
        {"volume": "Bespoke", "est": "15 – 25",       "stars": [100, 8, 2, 1, 2]},
    "Sampada Creations":
        {"volume": "Bespoke", "est": "15 – 25",       "stars": [91, 12, 4, 2, 4]},
    "Mehai interiors":
        {"volume": "Bespoke", "est": "15 – 25",       "stars": [79, 14, 6, 3, 10]},
    "Wudspot interiors":
        {"volume": "Bespoke", "est": "15 – 25",       "stars": [103, 4, 1, 1, 1]},
    "Feather Wood Interiors":
        {"volume": "Bespoke", "est": "15 – 25",       "stars": [89, 7, 2, 1, 1]},
    "The KariGhars - Best Interior Designer In Bangalore":
        {"volume": "Bespoke", "est": "30 – 60",       "stars": [715, 62, 18, 8, 33]},
    "Blue Interiors | Hafele Studio Partner":
        {"volume": "Moderate","est": "120 – 200",     "stars": [518, 18, 5, 2, 9]},
    "L&S Design Concepts Pvt Ltd":
        {"volume": "Bespoke", "est": "40 – 80",       "stars": [112, 4, 1, 1, 1]},
}

CAT_LABELS = {
    1: "Category 1 · High-Volume Tech Platforms & Aggregators",
    2: "Category 2 · Organized Mid-to-Large Mid-Premium Players",
    3: "Category 3 · Boutique & Bespoke Studios",
    4: "Category 4 · High-End Custom Luxury Designers",
}

CAT_COLORS = {
    1: ("#e8f0fe", "#1a56db", "#1a3a8f"),
    2: ("#e6f4ea", "#1e7e34", "#0d4a1e"),
    3: ("#fff8e6", "#b45309", "#6b3600"),
    4: ("#f5f0ff", "#7c3aed", "#3b1fa3"),
}

entries = [
    e for e in data
    if e["rating"] is not None and e["rating"] >= 4
    and e["reviews"] >= 100
    and e["type"] == "Interior designer"
]
entries.sort(key=lambda e: (-e["reviews"], -(e["rating"] or 0)))

for e in entries:
    e["category"] = CATEGORIES.get(e["name"], 3)
    ex = EXTRA.get(e["name"], {})
    e["volume"] = ex.get("volume", "")
    e["est"]    = ex.get("est", "")
    e["stars"]  = ex.get("stars", [])

json_str = json.dumps(entries)

cat_color_css = ""
for c, (bg, text, dark) in CAT_COLORS.items():
    cat_color_css += f"""
  .cat-header-{c} {{ background: {bg}; color: {dark}; border-left: 4px solid {text}; }}
  .cat-badge-{c} {{ background: {bg}; color: {text}; border: 1px solid {text}; }}"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Interior Designers – Shortlist</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; background: #f5f5f5; color: #222; }}

  header {{ background: #1a1a2e; color: #fff; padding: 20px 32px; }}
  header h1 {{ font-size: 1.3rem; font-weight: 600; }}
  header p {{ font-size: 0.82rem; color: #aaa; margin-top: 3px; }}

  .controls {{
    display: flex; flex-wrap: wrap; gap: 10px; align-items: center;
    padding: 12px 32px; background: #fff; border-bottom: 1px solid #e0e0e0;
    position: sticky; top: 0; z-index: 10;
  }}
  .control-group {{ display: flex; align-items: center; gap: 6px; flex-wrap: wrap; }}
  .divider {{ width: 1px; height: 24px; background: #e0e0e0; margin: 0 2px; }}
  label.group-label {{ font-size: 0.75rem; color: #888; font-weight: 600; text-transform: uppercase; letter-spacing: 0.03em; white-space: nowrap; }}

  .sort-btn {{
    padding: 4px 12px; border-radius: 20px; border: 1px solid #ddd;
    background: #fff; font-size: 0.78rem; cursor: pointer; transition: all 0.12s;
  }}
  .sort-btn:hover {{ background: #f0f0f0; }}
  .sort-btn.active {{ background: #1a1a2e; color: #fff; border-color: #1a1a2e; }}

  input[type=search] {{
    padding: 4px 12px; border-radius: 20px; border: 1px solid #ddd;
    font-size: 0.78rem; width: 190px; outline: none;
  }}
  input[type=search]:focus {{ border-color: #1a1a2e; }}

  .hidden-toggle {{
    padding: 4px 12px; border-radius: 20px; border: 1px solid #e0b0b0;
    background: #fff5f5; color: #a03030; font-size: 0.78rem; cursor: pointer;
    transition: all 0.12s; display: none;
  }}
  .hidden-toggle:hover {{ background: #ffe0e0; }}
  .hidden-toggle.visible {{ display: inline-block; }}

  .filters-label {{
    font-size: 0.72rem; color: #999; background: #f5f5f5; border: 1px solid #e8e8e8;
    border-radius: 20px; padding: 3px 10px; white-space: nowrap;
  }}
  .count {{ font-size: 0.78rem; color: #aaa; margin-left: auto; }}

  .cb-input {{ display: none; }}
  .cb-pill {{
    display: inline-flex; align-items: center; gap: 5px;
    padding: 3px 10px; border-radius: 20px; border: 1px solid #ddd;
    background: #fff; font-size: 0.75rem; cursor: pointer; transition: all 0.12s;
    user-select: none;
  }}
  .cb-pill:hover {{ background: #f0f0f0; }}
  .cb-input:checked + .cb-pill {{ font-weight: 600; }}
  .cb-cat-1:checked + .cb-pill {{ background: #e8f0fe; color: #1a3a8f; border-color: #1a56db; }}
  .cb-cat-2:checked + .cb-pill {{ background: #e6f4ea; color: #0d4a1e; border-color: #1e7e34; }}
  .cb-cat-3:checked + .cb-pill {{ background: #fff8e6; color: #6b3600; border-color: #b45309; }}
  .cb-cat-4:checked + .cb-pill {{ background: #f5f0ff; color: #3b1fa3; border-color: #7c3aed; }}
  .cb-vol-M:checked  + .cb-pill {{ background: #ede9fe; color: #312e81; border-color: #6d28d9; }}
  .cb-vol-H:checked  + .cb-pill {{ background: #dbeafe; color: #1e3a8a; border-color: #2563eb; }}
  .cb-vol-Mo:checked + .cb-pill {{ background: #d1fae5; color: #064e3b; border-color: #059669; }}
  .cb-vol-B:checked  + .cb-pill {{ background: #f3f4f6; color: #374151; border-color: #9ca3af; }}

  table {{ width: 100%; border-collapse: collapse; }}
  th, td {{ padding: 9px 12px; text-align: left; font-size: 0.83rem; border-bottom: 1px solid #eee; }}
  th {{
    background: #fafafa; font-weight: 600; font-size: 0.70rem;
    text-transform: uppercase; letter-spacing: 0.04em; color: #777;
    position: sticky; top: 57px; z-index: 5; white-space: nowrap;
  }}
  tr:hover td {{ background: #fafafa; }}
  tr.hidden-row td {{ opacity: 0.35; }}

  .cat-header td {{
    font-size: 0.74rem; font-weight: 700; letter-spacing: 0.05em;
    text-transform: uppercase; padding: 7px 12px;
  }}
{cat_color_css}

  td.eye     {{ width: 28px; padding: 9px 4px 9px 12px; }}
  td.num     {{ color: #bbb; font-size: 0.70rem; width: 28px; padding-left: 4px; }}
  td.name    {{ font-weight: 500; max-width: 240px; }}
  td.rating  {{ width: 60px; }}
  td.reviews {{ width: 68px; }}
  td.vol     {{ width: 110px; }}
  td.est     {{ width: 110px; font-size: 0.78rem; color: #555; white-space: nowrap; }}
  td.stars   {{ width: 160px; padding-top: 11px; }}
  td.cat     {{ width: 120px; }}
  td.address {{ color: #666; max-width: 280px; font-size: 0.79rem; }}

  .eye-btn {{
    background: none; border: none; cursor: pointer; padding: 2px;
    color: #bbb; line-height: 1; transition: color 0.12s;
  }}
  .eye-btn:hover {{ color: #555; }}
  .eye-btn.eye-hidden {{ color: #ddd; }}

  .rating-pill {{
    display: inline-block; padding: 2px 7px; border-radius: 12px;
    font-size: 0.74rem; font-weight: 600;
  }}
  .r5   {{ background: #d4edda; color: #155724; }}
  .r49  {{ background: #d4edda; color: #155724; }}
  .r48  {{ background: #d1ecf1; color: #0c5460; }}
  .r47  {{ background: #fff3cd; color: #856404; }}
  .r46  {{ background: #fff3cd; color: #856404; }}
  .r45  {{ background: #fff3cd; color: #856404; }}
  .r-low  {{ background: #f8d7da; color: #721c24; }}

  /* Volume badges */
  .vol-badge {{
    display: inline-block; font-size: 0.64rem; font-weight: 700;
    border-radius: 4px; padding: 2px 6px; white-space: nowrap;
  }}
  .vol-Massive  {{ background: #ede9fe; color: #4c1d95; }}
  .vol-High     {{ background: #dbeafe; color: #1e3a8a; }}
  .vol-Moderate {{ background: #d1fae5; color: #064e3b; }}
  .vol-Bespoke  {{ background: #f3f4f6; color: #374151; }}

  /* Stacked star bar */
  .star-bar {{
    display: flex; height: 7px; border-radius: 4px; overflow: hidden;
    width: 100%; gap: 1px;
  }}
  .star-bar span {{ display: block; height: 100%; }}
  .s5 {{ background: #22c55e; }}
  .s4 {{ background: #86efac; }}
  .s3 {{ background: #fbbf24; }}
  .s2 {{ background: #fb923c; }}
  .s1 {{ background: #ef4444; }}
  .star-counts {{
    font-size: 0.63rem; color: #aaa; margin-top: 3px; white-space: nowrap;
  }}

  /* Category badge */
  .cat-badge {{
    display: inline-block; font-size: 0.62rem; font-weight: 700;
    border-radius: 4px; padding: 1px 6px; white-space: nowrap;
  }}
  .sponsored {{
    display: inline-block; font-size: 0.62rem; font-weight: 600;
    background: #fff3cd; color: #856404; border: 1px solid #ffc107;
    border-radius: 4px; padding: 1px 5px; margin-left: 5px; vertical-align: middle;
  }}
  .no-addr {{ color: #ccc; font-style: italic; font-size: 0.78rem; }}
  .empty {{ text-align: center; padding: 60px; color: #bbb; }}

  /* Sliders */
  .slider-group {{ display: flex; align-items: center; gap: 8px; }}
  .slider-group input[type=range] {{
    -webkit-appearance: none; appearance: none;
    width: 130px; height: 4px; border-radius: 2px;
    background: #ddd; outline: none; cursor: pointer;
  }}
  .slider-group input[type=range]::-webkit-slider-thumb {{
    -webkit-appearance: none; width: 14px; height: 14px;
    border-radius: 50%; background: #1a1a2e; cursor: pointer;
  }}
  .slider-val {{
    font-size: 0.76rem; font-weight: 600; color: #1a1a2e;
    min-width: 52px; text-align: left;
  }}
</style>
</head>
<body>

<header>
  <h1>Interior Designers — Shortlist</h1>
  <p>Whitefield / Bangalore &nbsp;·&nbsp; Rating 4.0+ &nbsp;·&nbsp; 100+ reviews &nbsp;·&nbsp; Interior designer &nbsp;·&nbsp; 43 listings</p>
</header>

<div class="controls">
  <span class="filters-label">&#9733; 4.0+ &nbsp;&#9679; 100+ reviews</span>

  <div class="divider"></div>

  <div class="control-group">
    <label class="group-label">Category</label>
    <input type="checkbox" class="cb-input cb-cat-1" id="cb1" value="1">
    <label class="cb-pill" for="cb1">C1 · Tech</label>
    <input type="checkbox" class="cb-input cb-cat-2" id="cb2" value="2">
    <label class="cb-pill" for="cb2">C2 · Mid-Premium</label>
    <input type="checkbox" class="cb-input cb-cat-3" id="cb3" value="3">
    <label class="cb-pill" for="cb3">C3 · Boutique</label>
    <input type="checkbox" class="cb-input cb-cat-4" id="cb4" value="4">
    <label class="cb-pill" for="cb4">C4 · Luxury</label>
  </div>

  <div class="divider"></div>

  <div class="control-group">
    <label class="group-label">Volume</label>
    <input type="checkbox" class="cb-input cb-vol-M" id="vM" data-vol="Massive">
    <label class="cb-pill" for="vM">Massive</label>
    <input type="checkbox" class="cb-input cb-vol-H" id="vH" data-vol="High">
    <label class="cb-pill" for="vH">High</label>
    <input type="checkbox" class="cb-input cb-vol-Mo" id="vMo" data-vol="Moderate">
    <label class="cb-pill" for="vMo">Moderate</label>
    <input type="checkbox" class="cb-input cb-vol-B" id="vB" data-vol="Bespoke">
    <label class="cb-pill" for="vB">Bespoke</label>
  </div>

  <div class="divider"></div>

  <div class="control-group">
    <label class="group-label">Min vol/yr</label>
    <div class="slider-group">
      <input type="range" id="volSlider" min="0" max="1500" step="5" value="0">
      <span class="slider-val" id="volVal">0+</span>
    </div>
  </div>

  <div class="divider"></div>

  <div class="control-group">
    <label class="group-label">Max 1+2★</label>
    <div class="slider-group">
      <input type="range" id="badSlider" min="0" max="20" step="0.5" value="20">
      <span class="slider-val" id="badVal">any</span>
    </div>
  </div>

  <div class="divider"></div>

  <div class="control-group">
    <label class="group-label">Sort</label>
    <button class="sort-btn active" id="sortDesc">&#x2193; Reviews</button>
    <button class="sort-btn" id="sortAsc">&#x2191; Reviews</button>
    <button class="sort-btn" id="sortCat">Category</button>
  </div>

  <div class="divider"></div>

  <input type="search" id="search" placeholder="Search name or address…">

  <button class="hidden-toggle" id="hiddenToggle"></button>
  <span class="count" id="count"></span>
</div>

<table>
  <thead>
    <tr>
      <th></th><th>#</th><th>Name</th><th>Rating</th><th>Reviews</th>
      <th>Volume</th><th>Est. Projects/yr</th><th>Star Distribution</th><th>Category</th><th>Address</th>
    </tr>
  </thead>
  <tbody id="tbody"></tbody>
</table>

<script>
const DATA = {json_str};

const CAT_LABELS = {{
  1: "C1 · Tech",
  2: "C2 · Mid-Premium",
  3: "C3 · Boutique",
  4: "C4 · Luxury",
}};
const CAT_FULL = {{
  1: "Category 1 · High-Volume Tech Platforms & Aggregators",
  2: "Category 2 · Organized Mid-to-Large Mid-Premium Players",
  3: "Category 3 · Boutique & Bespoke Studios",
  4: "Category 4 · High-End Custom Luxury Designers",
}};
const CAT_BADGE = {{ 1:"cat-badge-1", 2:"cat-badge-2", 3:"cat-badge-3", 4:"cat-badge-4" }};
const CAT_HDR   = {{ 1:"cat-header-1", 2:"cat-header-2", 3:"cat-header-3", 4:"cat-header-4" }};

const EYE_OPEN = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>`;
const EYE_SHUT = `<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17.94 17.94A10.07 10.07 0 0112 20c-7 0-11-8-11-8a18.45 18.45 0 015.06-5.94M9.9 4.24A9.12 9.12 0 0112 4c7 0 11 8 11 8a18.5 18.5 0 01-2.16 3.19m-6.72-1.07a3 3 0 11-4.24-4.24"/><line x1="1" y1="1" x2="23" y2="23"/></svg>`;

const STORAGE_KEY = 'interiors_shortlist_hidden';
let hidden = new Set(JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]'));
let showHidden = false;
let sortMode = 'desc';
let query = '';
let selectedCats = new Set();
let selectedVols = new Set();
let minVolPyr  = 0;
let maxBadPct  = 20;

function saveHidden() {{
  localStorage.setItem(STORAGE_KEY, JSON.stringify([...hidden]));
}}

function parseEstMin(est) {{
  if (!est) return 0;
  const m = est.replace(/,/g,'').match(/\d+/);
  return m ? parseInt(m[0]) : 0;
}}

function badPct(stars) {{
  if (!stars || stars.length < 5) return 0;
  const total = stars.reduce((a,b) => a+b, 0);
  return total ? (stars[3]+stars[4])/total*100 : 0;
}}

function ratingClass(r) {{
  if (r >= 5)   return 'r5';
  if (r >= 4.9) return 'r49';
  if (r >= 4.8) return 'r48';
  if (r >= 4.7) return 'r47';
  if (r >= 4.6) return 'r46';
  if (r >= 4.5) return 'r45';
  return 'r-low';
}}

function starBar(stars) {{
  if (!stars || stars.length < 5) return '<span style="color:#ccc;font-size:0.72rem">—</span>';
  const total = stars.reduce((a,b) => a+b, 0);
  if (!total) return '';
  const pct = stars.map(s => (s/total*100).toFixed(1));
  const tip = `5★: ${{stars[0].toLocaleString()}}  4★: ${{stars[1].toLocaleString()}}  3★: ${{stars[2].toLocaleString()}}  2★: ${{stars[3].toLocaleString()}}  1★: ${{stars[4].toLocaleString()}}`;
  const p5  = (stars[0]/total*100).toFixed(0);
  const p12 = ((stars[3]+stars[4])/total*100).toFixed(0);
  const pct12 = ((stars[3]+stars[4])/total*100).toFixed(1);
  return `<div class="star-bar" title="${{tip}}">
    <span class="s5" style="width:${{pct[0]}}%"></span>
    <span class="s4" style="width:${{pct[1]}}%"></span>
    <span class="s3" style="width:${{pct[2]}}%"></span>
    <span class="s1" style="width:${{pct12}}%"></span>
  </div>
  <div class="star-counts">5★ ${{p5}}% &nbsp; 1+2★ ${{p12}}%</div>`;
}}

function updateHiddenToggle() {{
  const btn = document.getElementById('hiddenToggle');
  if (hidden.size === 0) {{ btn.classList.remove('visible'); showHidden = false; }}
  else {{
    btn.classList.add('visible');
    btn.textContent = showHidden ? `Hide hidden (${{hidden.size}})` : `Show hidden (${{hidden.size}})`;
  }}
}}

function render() {{
  const q = query.toLowerCase();
  let rows = DATA.filter(e => {{
    if (hidden.has(e.name) && !showHidden) return false;
    if (selectedCats.size > 0 && !selectedCats.has(e.category)) return false;
    if (selectedVols.size > 0 && !selectedVols.has(e.volume)) return false;
    if (minVolPyr > 0 && parseEstMin(e.est) < minVolPyr) return false;
    if (badPct(e.stars) > maxBadPct) return false;
    if (q && !e.name.toLowerCase().includes(q) && !e.address.toLowerCase().includes(q)) return false;
    return true;
  }});

  if (sortMode === 'desc') rows.sort((a,b) => (b.reviews||0)-(a.reviews||0));
  else if (sortMode === 'asc') rows.sort((a,b) => (a.reviews||0)-(b.reviews||0));
  else rows.sort((a,b) => a.category-b.category || (b.reviews||0)-(a.reviews||0));

  const visibleCount = rows.filter(e => !hidden.has(e.name)).length;
  document.getElementById('count').textContent =
    hidden.size > 0 ? `${{visibleCount}} shown · ${{hidden.size}} hidden` : `${{rows.length}} listings`;

  const tbody = document.getElementById('tbody');
  if (rows.length === 0) {{
    tbody.innerHTML = '<tr><td colspan="10" class="empty">No results</td></tr>';
    return;
  }}

  let html = ''; let lastCat = null; let rowNum = 0;
  rows.forEach(e => {{
    if (sortMode === 'cat' && e.category !== lastCat) {{
      lastCat = e.category; rowNum = 0;
      html += `<tr class="cat-header"><td colspan="10" class="${{CAT_HDR[e.category]}}">${{CAT_FULL[e.category]}}</td></tr>`;
    }}
    rowNum++;
    const isHidden = hidden.has(e.name);
    const rLabel  = e.rating.toFixed(1);
    const rc      = ratingClass(e.rating);
    const sponsored = e.sponsored ? '<span class="sponsored">Ad</span>' : '';
    const addr    = e.address || '<span class="no-addr">no address</span>';
    const eyeIcon = isHidden ? EYE_SHUT : EYE_OPEN;
    const eyeClass = isHidden ? 'eye-btn eye-hidden' : 'eye-btn';
    const volKey  = e.volume || '';
    const volClass = 'vol-' + (volKey === 'Bespoke / Low' ? 'Bespoke' : volKey);
    const volLabel = volKey === 'Bespoke' ? 'Bespoke / Low' : volKey;
    html += `<tr class="${{isHidden?'hidden-row':''}}">
      <td class="eye"><button class="${{eyeClass}}" data-name="${{e.name.replace(/"/g,'&quot;')}}" title="${{isHidden?'Restore':'Hide'}}">${{eyeIcon}}</button></td>
      <td class="num">${{rowNum}}</td>
      <td class="name">${{e.name}}${{sponsored}}</td>
      <td class="rating"><span class="rating-pill ${{rc}}">${{rLabel}}</span></td>
      <td class="reviews">${{e.reviews.toLocaleString()}}</td>
      <td class="vol"><span class="vol-badge ${{volClass}}">${{volLabel}}</span></td>
      <td class="est">${{e.est || '—'}}</td>
      <td class="stars">${{starBar(e.stars)}}</td>
      <td class="cat"><span class="cat-badge ${{CAT_BADGE[e.category]}}">${{CAT_LABELS[e.category]}}</span></td>
      <td class="address">${{addr}}</td>
    </tr>`;
  }});
  tbody.innerHTML = html;

  tbody.querySelectorAll('.eye-btn').forEach(btn => {{
    btn.addEventListener('click', () => {{
      const name = btn.dataset.name;
      if (hidden.has(name)) hidden.delete(name); else hidden.add(name);
      saveHidden(); updateHiddenToggle(); render();
    }});
  }});
}}

// Category filters
document.querySelectorAll('.cb-input[id^=cb]').forEach(cb => {{
  cb.addEventListener('change', () => {{
    if (cb.checked) selectedCats.add(parseInt(cb.value));
    else selectedCats.delete(parseInt(cb.value));
    render();
  }});
}});

// Volume filters
document.querySelectorAll('.cb-input[data-vol]').forEach(cb => {{
  cb.addEventListener('change', () => {{
    if (cb.checked) selectedVols.add(cb.dataset.vol);
    else selectedVols.delete(cb.dataset.vol);
    render();
  }});
}});

// Sort
document.getElementById('sortDesc').addEventListener('click', function() {{
  sortMode='desc'; this.classList.add('active');
  document.getElementById('sortAsc').classList.remove('active');
  document.getElementById('sortCat').classList.remove('active');
  render();
}});
document.getElementById('sortAsc').addEventListener('click', function() {{
  sortMode='asc'; this.classList.add('active');
  document.getElementById('sortDesc').classList.remove('active');
  document.getElementById('sortCat').classList.remove('active');
  render();
}});
document.getElementById('sortCat').addEventListener('click', function() {{
  sortMode='cat'; this.classList.add('active');
  document.getElementById('sortDesc').classList.remove('active');
  document.getElementById('sortAsc').classList.remove('active');
  render();
}});

document.getElementById('search').addEventListener('input', e => {{
  query = e.target.value; render();
}});

document.getElementById('hiddenToggle').addEventListener('click', () => {{
  showHidden = !showHidden; updateHiddenToggle(); render();
}});

// Volume/yr slider
document.getElementById('volSlider').addEventListener('input', function() {{
  minVolPyr = parseInt(this.value);
  document.getElementById('volVal').textContent = minVolPyr === 0 ? '0+' : minVolPyr + '+';
  render();
}});

// 1+2★ slider
document.getElementById('badSlider').addEventListener('input', function() {{
  maxBadPct = parseFloat(this.value);
  document.getElementById('badVal').textContent = maxBadPct >= 20 ? 'any' : maxBadPct.toFixed(1) + '%';
  render();
}});

updateHiddenToggle();
render();
</script>
</body>
</html>"""

with open("interiors_shortlist.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"Written {len(entries)} entries to interiors_shortlist.html")

from collections import Counter
vc = Counter(e["volume"] for e in entries)
for k in ["Massive","High","Moderate","Bespoke"]:
    print(f"  {k}: {vc.get(k,0)}")
