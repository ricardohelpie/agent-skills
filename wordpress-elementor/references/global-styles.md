# Global Styles Setup Workflow

## When to use this reference
- Setting up a new site from a brand kit or design system
- Standardizing a disorganized site's styles
- Migrating from one brand to another

---

## MCP Limitation Map

| What you want to set | MCP tool | Works? | Alternative |
|---|---|---|---|
| Custom colors (extra palette) | `update-global-colors` | ✅ Yes | — |
| System colors (primary/secondary/text/accent) | `update-global-colors` | ❌ No | REST API (see below) |
| Custom typography styles | `update-global-typography` | ✅ Yes | — |
| System typography (primary/secondary/text/accent) | `update-global-typography` | ❌ No | REST API (see below) |
| Container width | `update-page-settings` on kit | ❌ No | Manual: Site Settings → Layout |
| Body typography | any MCP tool | ❌ No | Manual: Site Settings → Global Fonts → Body |

---

## Step 1: System Slots via REST API

Set the 4 system color slots before anything else:

```bash
AUTH="Basic $(echo -n 'username:password' | base64)"
BASE="https://yoursite.com/wp-json/elementor/v1"

# Colors
for SLOT in primary secondary text accent; do
  curl -s -X POST \
    -H "Authorization: $AUTH" \
    -H "Content-Type: application/json" \
    -d "{\"id\":\"$SLOT\",\"title\":\"$(echo $SLOT | sed 's/./\u&/')\",\"value\":\"#HEX\"}" \
    "$BASE/globals/colors/$SLOT"
done

# Typography
curl -s -X POST -H "Authorization: $AUTH" -H "Content-Type: application/json" \
  -d '{"id":"primary","title":"Primary","value":{"font_family":"Inter","font_weight":"700"}}' \
  "$BASE/globals/typography/primary"
```

---

## Step 2: Custom Colors via MCP

After system slots are set, add brand-specific palette entries:

```
update-global-colors with:
[
  {"name": "Brand Primary 500", "color_hex": "#HEX", "id": "brand-p500"},
  {"name": "Brand Primary 300", "color_hex": "#HEX", "id": "brand-p300"},
  {"name": "Brand Neutral 900", "color_hex": "#HEX", "id": "brand-n900"}
]
```

### Always generate dark/light variants for primary, secondary, and accent

Whenever the token set includes `primary`, `secondary`, or `accent`, generate a `-dark` and `-light` variant for each alongside the base color — never leave them as a single flat value. These variants are what make hover states, tints/backgrounds, and badges possible without inventing ad hoc hex values later.

Formula (blend toward black/white, not HSL lightness shift — keeps hue stable):
```python
def darken(hex, pct):   # pct ~0.20 for -dark
    r,g,b = ...channels of hex...
    return [int(c * (1 - pct)) for c in (r,g,b)]

def lighten(hex, pct):  # pct ~0.25 for -light
    r,g,b = ...channels of hex...
    return [int(c + (255 - c) * pct) for c in (r,g,b)]
```

Naming: `{token}-dark`, `{token}-light` (add `{token}-lighter` at ~0.45 only if the design needs a third tint tier, e.g. a very light background wash). Save all variants as custom colors in the same `update-global-colors` call as the base tokens.

Typical use: `-dark` for hover/active states on buttons and links; `-light`/`-lighter` for tinted backgrounds, badges, and borders that need to read as "brand color" without full saturation.

---

## Step 3: Manual Settings (must be done in editor)

Open Site Settings in Elementor editor and configure:
- **Layout → Container Width** — typically 1200px or 1440px
- **Global Fonts → Body** — base font family, size, line-height
- **Global Fonts → Accent** — secondary font if using two typefaces

---

## Step 4: Global Classes (Atomic Editor v4 only — REQUIRES the Atomic Editor toggle to be ON)

After tokens are set, create reusable classes via REST API before building any page.

**⚠️ Hard dependency confirmed on Elementor 4.1.5 (2026-07):** the moment the Atomic Editor is disabled in the site (Ricardo may turn it off deliberately — see note below), `/wp-json/elementor/v1/global-classes` returns `404 rest_no_route` on **every** method, including GET. There is no MCP tool that creates or edits Class Manager entries — `list-global-classes` is read-only and just resolves `g-` IDs already on elements. Classes created before the toggle was switched off keep working (frozen, still resolve via `list-global-classes`), but you cannot add or modify any. If you hit this 404, stop trying REST/MCP routes for global classes and fall back to the classic-Elementor pattern instead: a **WP Code / kit custom-CSS snippet** defining `.btn-primary { background: var(--e-global-color-primary); ... }` style rules (same approach documented for DTB in its DESIGN.md §8), applied to widgets via the **Advanced → CSS Classes** field — never via `add-custom-css` on the kit itself (destroys `custom_colors`/`custom_typography`, see Known Limitations table in the main SKILL.md).

**Concrete fallback mechanism (confirmed working, Biobank 2026-07):** the emcp-tools MCP exposes `add-code-snippet` — creates a site-wide Elementor Pro Custom Code snippet (injects into `<head>`/`body_start`/`body_end` on every page, `status:"publish"` activates immediately). This is the right tool for utility CSS classes that need to exist site-wide when Global Classes is unavailable — e.g. the DTB-style `.icon-outline` / `.icon-outline-{color}` pattern (SVG `fill: none !important; stroke: <color> !important`, plus a `.elementor-icon-list-icon svg` override since Elementor's icon-list widget generates fill with higher specificity). Wrap the CSS in `<style>...</style>` tags in the `code` param. This is distinct from `add-custom-css` (element/page-scoped) and from kit `custom_css` (forbidden) — it's the closest equivalent to a real global stylesheet available via MCP.

### Create via REST API (only when Atomic Editor is ON)

```bash
AUTH="Basic <base64-user:pass>"
PUT https://site.com/wp-json/elementor/v1/global-classes
Content-Type: application/json
```

Body structure — **note the discriminator key is `$$type` (double dollar), not `$type`**. A single `$` was tested on Elementor 4.1.5 and every prop came back `invalid_value`; switching to `$$type` returned `204` and the class resolved correctly via `list-global-classes` right after:
```json
{
  "changes": {"added": ["btn-primary"], "deleted": [], "modified": []},
  "items": {
    "btn-primary": {
      "id": "btn-primary", "type": "class", "label": "btn-primary",
      "variants": [
        {
          "meta": {"breakpoint": "desktop", "state": null},
          "props": {
            "background": {"$$type": "background", "value": {"color": {"$$type": "color", "value": "#E00029"}}},
            "color": {"$$type": "color", "value": "#FFFFFF"},
            "border-color": {"$$type": "color", "value": "#E00029"},
            "border-width": {"$$type": "size", "value": {"size": 1, "unit": "px"}},
            "border-style": {"$$type": "string", "value": "solid"},
            "border-radius": {"$$type": "size", "value": {"size": 99, "unit": "px"}},
            "font-family": {"$$type": "string", "value": "NMText"},
            "font-weight": {"$$type": "string", "value": "500"}
          }
        },
        {
          "meta": {"breakpoint": "desktop", "state": "hover"},
          "props": {
            "background": {"$$type": "background", "value": {"color": {"$$type": "color", "value": "#F30694"}}},
            "border-color": {"$$type": "color", "value": "#F30694"}
          }
        }
      ]
    }
  },
  "order": ["btn-primary"]
}
```
You do **not** need a Variables ID for this — plain hex/string literals inside `$$type` props work fine (the double-dollar variable-reference form with `var(--e-gv-...)` shown elsewhere in this skill is only required when the prop should track a live Variable, not a fixed value).

**Supported `$$type` values:**
| CSS property | `$$type` | `value` format |
|---|---|---|
| `color`, `border-color` | `"color"` | `"#HEX"` |
| `background` | `"background"` | `{"color": {"$$type":"color","value":"#HEX"}}` |
| `border-radius`, `font-size`, `letter-spacing`, `border-width` | `"size"` | `{"size": N, "unit": "px"}` |
| `font-family`, `font-weight`, `border-style`, `text-decoration` | `"string"` | `"value"` |

**Critical rules:**
- `padding` is NOT supported via API — falls back to Kit's global button padding
- Outline/white classes MUST include explicit `background: transparent` or widget inherits Elementor default bg
- For updating: use `"modified": ["class-name"]` in `changes`, send the complete class with all variants
- `order` must include every existing class ID on the site, not just the ones you're touching, or the PUT can drop others from the visible order

### Apply to widget

```json
"_css_classes": "icon-outline btn-primary"
```

Multiple classes space-separated. Kit-level CSS classes (from `custom_css`) coexist with Global Classes.

### Variables panel (Elementor 4.1.1 — BLOCKED)

`POST /elementor/v1/variables/create` rejects all `type` values with `rest_invalid_param`. The batch endpoint crashes with PHP 500. **Create Variables manually** in editor: Sistema de design → Variáveis → "+". Do not confuse with `/globals/colors` (those are Global Colors, not Variables).

---

## Step 5: Cleanup After Brand Migration

After updating a site from a previous brand:
- Remove orphaned entries from `custom_colors` and `custom_typography` in Site Settings
- Search for hardcoded hex values in widget settings using `find-element` with settings filter
- Check Theme Builder templates (header/footer) for outdated brand colors

---

## Design System Source Mapping

| Source | How to extract tokens |
|---|---|
| Figma file | Read Variables panel + Styles panel; map to Elementor slot names |
| Brand kit PDF/doc | Extract hex codes, font names, font weights; confirm web font availability on Google Fonts |
| Existing disorganized site | Run `get-global-settings` + Chrome MCP inspection; document current state before standardizing |
| HTML design system file | Parse CSS custom properties (`:root` vars); map `--color-primary` → `primary` slot |
