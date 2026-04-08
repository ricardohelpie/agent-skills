---
name: ui-ux-pro-max
description: Generates and critiques UI components and design systems to a premium standard. Combines A) real-time critique with WCAG/visual rhythm/micro-interaction analysis and B) premium component generation referencing Linear, Stripe, Vercel, and Radix as quality benchmarks. Use when building design systems, component libraries, landing pages, dashboards, or any UI that needs to exceed "good enough" and reach "delightful and trusted". Trigger with "build this component", "improve this UI", "critique this design", "generate a design system section", "make this look premium", "elevate this interface", or any request involving UI generation or design quality feedback.
argument-hint: "<component description, code snippet, screenshot, or 'critique: [existing UI description]'>"
---

# /ui-ux-pro-max

Generate and critique UI with the precision of a senior product designer at a best-in-class company. Every output should feel like it belongs in Linear, Stripe, or Vercel — not a template.

> "Good design is invisible. Premium design is unforgettable."

## Usage

```
/ui-ux-pro-max $ARGUMENTS
```

---

## Two Modes — Always Combined

This skill operates in two modes simultaneously: **Generate** and **Critique**. You never just generate without critiquing, and you never just critique without proposing improvements.

---

## Mode A — Premium Component Generation

When creating any UI component, apply these standards before delivering:

### The 5 Non-Negotiables

**1. Spacing with intention**
- Use an 8px base grid. No arbitrary values.
- Generous internal padding on interactive elements (min 12px vertical, 16px horizontal for buttons).
- Distinct density levels: compact (for tables/lists), default (for cards), spacious (for landing sections).

**2. Type hierarchy that guides the eye**
- Maximum 3 type sizes per component.
- Weight contrast over size contrast when possible (500→700 reads cleaner than 14px→22px).
- Line-height: 1.4–1.6 for body, 1.1–1.25 for headings.
- Letter-spacing: slightly negative for large headings (−0.02em at 2xl+), normal for body.

**3. Color with restraint**
- Primary color used for 1 focal action per view. Never 2.
- Secondary/accent reserved for supporting information (badges, highlights, icons).
- Neutrals do the heavy lifting: 80% of the UI should be grays/whites with color as punctuation.
- Use opacity variants for backgrounds: `primary/8` for soft fills, `primary/16` for hover.

**4. Interaction states — all of them**
- Every interactive element needs: default, hover, active/pressed, focus-visible, disabled.
- Hover: subtle background shift or opacity change — never jarring.
- Focus: visible ring, 2px offset, uses primary color at 50% opacity.
- Transitions: 150ms ease for micro (hover/focus), 250ms ease-out for layout changes.

**5. Shadow as depth signal**
- No decorative shadows. Only functional (floating elements, modals, dropdowns).
- Prefer subtle shadows with low opacity: `0 1px 3px rgba(0,0,0,0.08), 0 1px 2px rgba(0,0,0,0.04)`.
- Cards: 1-layer shadow. Modals: 2-layer shadow. Tooltips: 1-layer sharp.

### Reference Benchmarks by Component Type

| Component | Reference Standard | Key Pattern to Borrow |
|-----------|-------------------|----------------------|
| Buttons | Linear | Tight radius (6px), weight 500, letter-spacing 0, icon gap 6px |
| Cards | Stripe | Clean border (1px neutral-200), no shadow by default, shadow on hover |
| Inputs | Vercel | 1px border, 6px radius, placeholder at neutral-400, clear focus ring |
| Badges | GitHub | Pill shape, soft background (color/12), text at color-700 |
| Tables | Notion | Sticky header, row hover, border only horizontal |
| Navigation | Linear | Dense, 36px row height, icon+label, active state with soft bg |
| Data display | Stripe Dashboard | Label above value, subtle dividers, monospace for numbers |
| Modals | Radix UI | Overlay at neutral/60, center card, ESC dismissable, focus-trapped |
| Toasts | Sonner | Bottom-right, auto-dismiss, stacked, minimal border |
| Empty states | Vercel | Icon + heading + short copy + 1 CTA only |

---

## Mode B — Critique & Refinement

After generating (or when reviewing existing UI), apply this 6-point critique before finalizing:

### Critique Framework

**B1 — Contrast Audit**
- Text on background: WCAG AA minimum (4.5:1 for body, 3:1 for large text).
- Interactive element contrast against surrounding background: ≥3:1.
- Flag any gray-on-gray text combinations.
- Tool: mentally check if the element is readable at arm's length on a laptop screen in daylight.

**B2 — Visual Rhythm Check**
- Do spacing values follow the 8px grid? Flag any odd values (7px, 11px, 13px).
- Is there visual breathing room between sections? (min 32px between distinct content blocks)
- Is related content grouped with less space than unrelated content? (proximity law)

**B3 — Hierarchy Clarity**
- Can you identify the primary action in < 2 seconds without reading?
- Is there clear distinction between primary, secondary, and tertiary actions?
- Is the heading/body contrast sufficient to guide reading order?

**B4 — Micro-interaction Quality**
- Are all hover/focus states defined?
- Do transitions feel snappy (≤200ms) or sluggish (>300ms)?
- Is there a loading/skeleton state for async data?

**B5 — Consistency Check**
- Do all buttons of the same variant have identical padding, radius, and weight?
- Do icons have consistent size (stick to 16px or 20px, not both)?
- Is border-radius consistent across the same component type?

**B6 — Density Appropriateness**
- Is the information density right for the use context (mobile vs desktop, quick task vs analysis)?
- Are there elements that compete for attention unnecessarily?
- Is whitespace used to create emphasis, or is everything equally spaced?

---

## Output Format

### For Generate mode:
```
## [Component Name]

**Benchmark reference:** [Which design system inspired this, and why]
**Key decisions:** [3 specific choices made and the reasoning]

[CODE]

**Self-critique:**
- ✅ [What's strong about this implementation]
- ⚠️ [One thing to watch as the design evolves]
```

### For Critique mode:
```
## Critique: [Component/Screen Name]

### What's Working
- [Specific observation + why it works]

### Priority Fixes (ordered by impact)
1. **[Issue]** — [Why it matters] → [Exact fix]
2. **[Issue]** — [Why it matters] → [Exact fix]
3. **[Issue]** — [Why it matters] → [Exact fix]

### Contrast Scores
| Element | Ratio | WCAG | Status |
|---------|-------|------|--------|
| Body text | X.X:1 | AA (4.5:1) | ✅/❌ |

### Revised Version
[CODE with fixes applied]
```

---

## Design System Context Awareness

When working on a **multi-brand design system** (like NMB Vitrines):

- Treat CSS custom properties (`--ds-primary`, `--ds-font-display`) as sacred — never hardcode brand colors.
- Validate every component across all themes before signing off (a button that looks great in green might look wrong in a warm brown palette).
- Typography choice must match brand personality:
  - Elegant/beauty → serif display (Cormorant, Playfair, DM Serif)
  - Clinical/pharma → clean geometric sans (Inter, Plus Jakarta Sans)
  - Friendly/pet → rounded humanist (Nunito, Poppins, Quicksand)
  - Corporate/events → versatile grotesque (Roboto, DM Sans, Geist)
- Spacing and grid are always shared across themes — do not compromise them per brand.

---

## Tips for Best Results

1. **For generation:** Describe the component's context — "a card used in a fair exhibitor listing for a beauty trade show" gets better output than "a card".
2. **For critique:** Share the full component code + which theme/brand it belongs to.
3. **For design systems:** State which section you're working on (Colors / Typography / Spacing / Components) so I apply the right benchmark focus.
4. **Iterate quickly:** Accept the first pass, then use "refine: [specific issue]" to drill down — don't discard, improve.
