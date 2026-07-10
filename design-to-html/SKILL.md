# design-to-html

Converts a Figma frame or component into a production-ready HTML page with scroll animations, then verifies visually via Chrome MCP and saves decisions to Obsidian.

## Trigger

User says: "implement this Figma frame", "convert to HTML", "build this page from Figma", or similar.

## Required inputs

Before starting, confirm:
1. Figma file ID and node ID (or URL — extract IDs from it)
2. Target HTML file path (new file or existing)
3. Design system context: which theme/brand? (bfshow, cosmetique, pharma, petsa, petvet)
4. Animation intent: confirm exact type per section (slide-in, fade, parallax, clip-path) — do NOT assume

## Workflow

### Phase 1 — Extract tokens from Figma

Use Figma MCP to read the target node:
- Extract color tokens (fills, strokes) → map to CSS custom properties
- Extract typography (font family, size, weight, line-height) → CSS vars or inline styles
- Extract spacing (padding, gap, margin) → exact pixel values
- Extract effects (shadows, blur, gradients) → CSS equivalents
- Note any components referenced but not yet extracted

Do NOT improvise values. If a token is unclear, ask before proceeding.

### Phase 2 — Scaffold the HTML

- Use inline CSS (not Tailwind, not external stylesheet) — this project's convention
- Structure: semantic HTML5 sections matching Figma frame hierarchy
- Apply extracted tokens as CSS custom properties at `:root` level
- Mobile-first, with breakpoints mirroring the Figma frames (mobile/tablet/desktop)
- Do NOT add copy, placeholder text, or icons not present in the Figma frame

### Phase 3 — Apply scroll animations

Confirm animation type per section with the user before coding. Never substitute:
- `slide-in-from-right` ≠ `clip-path reveal` ≠ `fade-in`
- Parallax intensity must be confirmed (subtle / medium / strong)

Use `IntersectionObserver` for scroll-triggered animations. Inline the JS in a `<script>` tag at the bottom. Match timing and easing to design system defaults unless overridden.

### Phase 4 — Visual verification via Chrome MCP

1. Open the HTML file in Chrome via Chrome MCP (`navigate` to `file://` path)
2. Screenshot at three viewports: 375px (mobile), 768px (tablet), 1440px (desktop)
3. Compare against Figma frame visually — call out discrepancies
4. Fix any spacing, color, or layout issues found
5. Re-screenshot after fixes to confirm
6. Do NOT loop more than 3 fix rounds — if issues persist, flag for manual review

### Phase 5 — Save to Obsidian

Use the Obsidian MCP to create or update a note at:
`Design Decisions / [project-name] / [page-name].md`

Record:
- Figma file ID + node ID used
- Design tokens extracted (color palette, type scale)
- Animation types applied per section
- Any deviations from Figma (with reason)
- Known issues or follow-up items

## Error handling

- If Figma MCP returns no data: stop, report the node ID used, ask user to verify
- If Chrome MCP can't screenshot: note it, continue and report at end
- If Obsidian MCP fails: output the note content in the chat so user can save manually
- Never retry a failed step more than 2 times

## Output

At the end, summarize:
- HTML file path written
- Tokens extracted (count)
- Animations applied (list)
- Screenshots taken (viewports)
- Obsidian note path saved
- Any open issues
