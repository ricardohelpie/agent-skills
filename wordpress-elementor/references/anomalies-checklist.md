# Anomalies Checklist — Run Before Any Elementor Intervention

Always run this audit in Mode 2 (Improvement) before touching any site. Use `get-global-settings` + Chrome MCP inspection to verify each point.

## The 7 Checks

### 1. Body Typography in Kit
- **Check:** Is `body_typography` defined in kit settings?
- **Problem:** If blank, the effective font depends on the active theme — unpredictable across updates
- **Fix:** Set family + size + line-height in Site Settings → Global Fonts → Body (manual — not available via MCP)

### 2. Parallel Font Systems
- **Check:** Are system typography slots and custom typography slots using different font families?
- **Problem:** Visual inconsistency — e.g., Poppins in system slots, Urbanist in custom slots for body text
- **Fix:** Unify under one family, or explicitly document which slot is used for what purpose

### 3. Missing Responsive Breakpoints on Custom Styles
- **Check:** Do custom typography styles have sizes defined for tablet and mobile?
- **Problem:** Most custom styles only have desktop size — mobile renders at incorrect scale
- **Fix:** Add tablet (768px) and mobile (480px) sizes to the most-used typography styles

### 4. Nearly Identical Color Slots
- **Check:** Are `secondary` and `accent` hex values almost the same?
- **Problem:** Maintenance confusion — accidental swaps, unclear purpose
- **Fix:** Either differentiate them meaningfully or merge into one slot with a clear name

### 5. Missing H1 on Internal Pages
- **Check:** Do internal pages (service, about, contact) have an H1?
- **Problem:** SEO on-page drop — search engines expect one H1 per page
- **Fix:** Add a visible or visually-hidden H1 heading widget to each internal page template

### 6. Legacy Section Templates (pre-Container)
- **Check:** Are there saved templates of type `section` (Elementor v2/v3 style)?
- **Problem:** Reusing them in v4 container-based pages brings incompatible CSS and layout bugs
- **Fix:** Mark them as deprecated in template name, or rebuild as container-based sections

### 7. Token Value Mismatch (Kit vs Resolved)
- **Check:** Does `--e-global-color-primary` resolve to the same hex as the kit definition?
- **Problem:** Theme CSS or external plugins can override global color variables, making kit values misleading
- **How to check:** Inspect the element in Chrome MCP — computed style vs kit value
- **Fix:** Add a CSS override at the Elementor kit level, or remove the conflicting external CSS

---

## Additional Checks for NMB / Event Sites

- External CTA links (Sympla, etc.) — verify they point to the current edition, not a previous one
- Check if `primary` token hex in kit matches actual rendered button color (common override source: theme builder header CSS)
- Remove orphaned color/typography entries left from previous brand configurations
