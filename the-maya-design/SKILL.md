---
name: the-maya-design
description: Evaluate, create, or redesign UX/UI for apps and websites to reach the MAYA sweet spot — Most Advanced Yet Acceptable. Use when analyzing whether a design feels dated or too experimental, creating a new interface from scratch, or redesigning to better resonate with a specific audience. Accepts screenshots, Figma URLs, design system files, project descriptions, or just a brief about who the product is for. Trigger with "analyze this UI", "is this design too advanced for my users?", "create an app for [audience]", "redesign this screen", "does this feel modern enough?", "maya design", "ux ui sweet spot", "design that enchants users", or any request to make a design feel both familiar and innovative.
argument-hint: "<screenshot, Figma URL, design file, project description, or 'create [app/website] for [audience]'>"
---

# /the-maya-design

Evaluate, create, or redesign UX/UI interfaces to reach the **MAYA sweet spot**: the precise point where a design is *advanced enough to captivate* and *familiar enough to be immediately accepted*.

> "The most dangerous design is one that users understand — but forget. The second most dangerous is one they admire — but can't use."

## Usage

```
/the-maya-design $ARGUMENTS
```

---

## What I Need From You

- **The design or idea**: screenshot, Figma URL, design system, code, or a written description
- **The audience**: who will use it? (age range, digital literacy, industry, context of use)
- **The sector**: e-commerce, SaaS, fintech, health, social, gaming, etc.
- **The mode** (optional): analyze / create / redesign

If anything is missing, I will ask the minimum necessary before proceeding.

---

## The MAYA Principle

**Most Advanced Yet Acceptable** — coined by Raymond Loewy — defines the zone where innovation meets acceptance. Applied to UX/UI:

```
Too Familiar ←————————[ MAYA SWEET SPOT ]————————→ Too Advanced
  (forgettable,           (captivating,             (confusing,
   outdated,              trustworthy,               alienating,
   no delight)            delightful)                high drop-off)
```

The sweet spot is **not absolute** — it shifts based on audience, sector, and current design zeitgeist. A MAYA-calibrated design for a 55+ banking audience looks very different from one for a Gen Z gaming app.

---

## Step 1 — Audience Analysis

Before evaluating any axis, I calibrate the MAYA point for the specific audience across 5 dimensions:

### Dimension 1 — Cognitive Profile
- Digital literacy level (novice / intermediate / power user)
- Familiarity with the product category
- Existing mental models (which apps/platforms do they already use daily?)

### Dimension 2 — Usage Context
- Primary device (mobile-first, desktop, tablet, TV)
- Usage mode: quick/recurrent tasks or immersive/exploratory sessions
- Environment: commute, workplace, leisure, healthcare, finance

### Dimension 3 — Emotional Profile
- Tolerance for ambiguity (do they explore or need certainty?)
- Primary motivation: task completion / pleasure / social / status
- Aesthetic demand level (do they notice and care about visual quality?)

### Dimension 4 — Cultural & Regional Context
- Visual metaphors that resonate in this culture
- Reading direction, information density tolerance
- Expected tone: formal, casual, authoritative, friendly

### Dimension 5 — Audience Benchmark
- Which apps/websites does this audience consider "excellent UX"?
- What do they find "too complicated" or "too basic"?
- What is their ceiling of novelty acceptance?

**Output of this step**: an Audience MAYA Profile — a calibrated baseline that defines where the sweet spot sits for this specific group.

---

## Step 2 — The 4 MAYA Axes

Each axis is scored independently from 1–10:

```
1–3   → Too familiar (safe, forgettable, below audience expectations)
4–6   → Acceptable zone (functional but unremarkable)
7–8   → MAYA zone ✦ (sweet spot: innovative yet instantly graspable)
9–10  → Too advanced (innovative but creates friction or confusion)
```

### Axis 1 — Visual Language
Evaluates: typography, color system, spacing, iconography, illustration style, brand expression.

- **Familiar end**: system fonts, 8px grid, semantic color defaults, flat neutral palette
- **Advanced end**: expressive type, broken grid, unexpected color theory, layered depth

Key question: *Does the visual style feel like a step ahead of the category — or like a different universe?*

### Axis 2 — Interaction Architecture
Evaluates: gestures, transitions, microinteractions, feedback states, animation.

- **Familiar end**: tap/click, vertical scroll, button → loader → success toast
- **Advanced end**: physics-based transitions, contextual drag, multi-step gestures, spatial navigation

Key question: *Can a first-time user discover and execute the core flow without instruction?*

### Axis 3 — Information Structure
Evaluates: navigation paradigm, hierarchy, progressive disclosure, flow design.

- **Familiar end**: top navbar, sidebar, breadcrumb, linear checkout
- **Advanced end**: AI-driven filtering, spatial/non-linear navigation, context-aware menus

Key question: *Does the structure reduce cognitive load — or require the user to learn a new mental map?*

### Axis 4 — Required Mental Model
Evaluates: how much the user needs to "learn" to use the product.

- **Familiar end**: universal metaphors (cart, trash, envelope, toggle)
- **Advanced end**: new paradigms with no known reference

Key question: *Does the interface borrow from what users already know — and elevate it?*

---

## Step 3 — Sweet Spot Diagnostic

For each axis, I apply the 3 universal MAYA criteria:

| Criterion | Diagnostic Question | If NO |
|-----------|--------------------|----|
| **Discoverability** | Is the novel element found without a tutorial? | Too advanced |
| **Schema Transfer** | Does the user connect it to something already known? | Too advanced |
| **Perceived Elevation** | After using it, does everything else feel inferior? | Too familiar |

A design is at the MAYA sweet spot when all three are YES on all axes.

---

## Step 4 — Best-in-Class Benchmark

I compare the design against the leading references for this specific sector and audience, not against universal design conventions alone.

Examples:
- Fintech mobile → Revolut, Robinhood, Nubank
- E-commerce → Shopify storefronts, Nike, Glossier
- SaaS dashboard → Linear, Vercel, Notion
- Health & wellness → Calm, Headspace, Oura
- Social → Bereal, Locket, Daylio

I identify where the design stands relative to best-in-class on each axis — and what the gap is.

---

## Modes of Operation

### Mode A — Analyze
Receive an existing design (screenshot, Figma, description, design system) and return a full MAYA audit: axis scores, audience calibration, benchmark comparison, and priority opportunities.

### Mode B — Create
Receive a brief (audience, sector, product purpose) and generate a UX/UI concept calibrated to the MAYA sweet spot from scratch — including layout direction, interaction principles, visual language guidelines, and component recommendations.

### Mode C — Redesign
Receive an existing design that is too familiar or too advanced. Diagnose the gap, then either:
- Propose specific changes with reasoning, or
- Generate a redesigned version for evaluation

---

## Output Format

```markdown
## MAYA Design Report: [Product Name]

### Audience MAYA Profile
[Who they are, what their baseline is, where the sweet spot sits for them]

### MAYA Axis Scores
| Axis | Score | Status | Key Finding |
|------|-------|--------|-------------|
| Visual Language | X/10 | 🟢 MAYA / 🟡 Too Familiar / 🔴 Too Advanced | [1-line finding] |
| Interaction Architecture | X/10 | ... | ... |
| Information Structure | X/10 | ... | ... |
| Required Mental Model | X/10 | ... | ... |
| **Overall MAYA Score** | **X/10** | | |

### Sweet Spot Diagnostic
[Per axis: which criteria pass/fail and why]

### Best-in-Class Gap Analysis
[How this design compares to leading references in the sector]

### What Enchants (keep and amplify)
- [Observation 1]
- [Observation 2]

### What Holds It Back (priority opportunities)
1. **[Most impactful]** — [Why and how to fix]
2. **[Second priority]** — [Why and how to fix]
3. **[Third priority]** — [Why and how to fix]

### Recommended Direction
[Concrete next step: adjust axis X toward MAYA by doing Y]
```

---

## Design Critique Integration

When deeper structural feedback is needed, I apply the `/design-critique` framework as a sub-layer — specifically for First Impression (2s), Usability, Visual Hierarchy, and Accessibility — then synthesize those findings into the MAYA axis scores.

---

## Tips for Best Results

1. **Share the audience first** — "This is for 40+ professionals in Brazil using mobile" immediately calibrates the entire analysis.
2. **Show references you admire** — "We want the feel of Linear but for healthcare" gives me a benchmark anchor.
3. **Tell me the stage** — early concept gets different guidance than a near-launch product.
4. **Don't over-specify for creation mode** — give me the audience and the purpose; I'll bring the design direction.
