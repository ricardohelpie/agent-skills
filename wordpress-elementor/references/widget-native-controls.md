# Widget Native Controls Reference

For each widget: what can be achieved natively in Content / Style / Advanced tabs — before reaching for custom CSS.

---

## Container

**Content tab:**
- Direction: row / column / row-reverse / column-reverse
- Wrap: wrap / nowrap
- Justify content: flex-start / center / flex-end / space-between / space-around / space-evenly
- Align items: flex-start / center / flex-end / stretch
- Gap: row gap + column gap (px/em/rem/%)
- Min height, overflow

**Style tab:**
- Background: solid color / gradient / image / video / slideshow
- Background overlay (color + opacity)
- Border: width, color, style, radius per corner
- Box shadow
- Padding / margin

**Advanced tab:**
- CSS ID and Classes
- Motion effects: entrance animation, scroll effects (parallax, fade, blur, scale)
- Responsive: hide on mobile/tablet/desktop
- Custom CSS (scoped to element)

**Native limits:** Complex multi-layer backgrounds, CSS grid (use flex grid instead), sticky positioning with offset requires custom CSS.

---

## Heading

**Content tab:**
- Title text (supports basic HTML inline: `<strong>`, `<em>`, `<a>`, `<span>`)
- HTML tag: h1–h6, div, span, p
- Link (wraps heading in `<a>`)

**Style tab:**
- Alignment: left / center / right / justify
- Color (links to global color tokens)
- Typography: font family, size, weight, style, decoration, transform, line-height, letter-spacing
- Text shadow
- Blend mode

**Native limits:** Multi-color headings require `<span>` with inline style inside the text field or custom CSS.

---

## Text Editor

**Content tab:**
- Rich text editor (bold, italic, underline, lists, links, inline HTML)

**Style tab:**
- Alignment
- Color
- Typography
- Text shadow
- Columns (multi-column text layout)

**Native limits:** Pull quotes, dropcap, advanced typographic treatments need custom CSS.

---

## Button

**Content tab:**
- Text
- Link (URL, target, nofollow)
- Icon: position (before/after), size, spacing
- Size: xs / sm / md / lg / xl
- Button ID (for JS targeting)

**Style tab:**
- Type: filled / outline / (no background handled via color settings)
- Typography
- Text color + hover color
- Background color + hover color
- Border: width, color, style, radius
- Hover border color
- Box shadow + hover shadow
- Padding (top/right/bottom/left)
- Width: auto / full width

**Native limits:** Gradient background on hover, complex icon animations need custom CSS.

---

## Image

**Content tab:**
- Image source (media library or URL)
- Alt text, title attribute
- Link: none / media file / custom URL / attachment page
- Caption

**Style tab:**
- Width / max width
- Height (auto or fixed)
- Object fit: cover / contain / fill
- Alignment
- Border: radius, style, color
- Box shadow
- CSS filters: blur, brightness, contrast, saturation, hue
- Hover: opacity, CSS filters, box shadow transition

**Native limits:** Image overlay on hover without interaction widget requires custom CSS.

---

## Icon Box

**Content tab:**
- Icon (from icon library or SVG)
- Title (HTML tag selectable: h1–h6, div, span)
- Description (rich text)
- Link (wraps entire widget or just title)
- Icon position: top / left / right

**Style tab:**
- Icon: size, color, hover color, background, padding, border, border-radius, box shadow
- Title: spacing, color, typography
- Description: spacing, color, typography
- Vertical alignment of icon vs text
- Content alignment

**Native limits:** Icon animation on hover (spin, bounce) requires custom CSS or JS.

---

## Icon List

**Content tab:**
- Items: each has icon + text + link
- Layout: inline / stacked

**Style tab:**
- Space between items
- Divider: style, weight, color
- Icon: size, color (global or per-item)
- Text: indent, color, typography

**Native limits:** Per-item background color, complex hover states need custom CSS.

---

## Testimonial

**Content tab:**
- Content (testimonial text)
- Name, title (job title/company)
- Image (avatar)
- Link

**Style tab:**
- Alignment
- Content: color, typography, background, padding, border radius
- Image: size, gap, border, border-radius, box shadow
- Name: color, typography
- Job title: color, typography
- Image position: top / left / right / bottom

**Native limits:** Star rating inside testimonial, complex card layout needs Icon Box + Text Editor combo or custom CSS.

---

## Testimonial Carousel (Pro)

Same content fields as Testimonial × multiple items, plus:

**Content tab:**
- Navigation: arrows, dots, both, none
- Autoplay: on/off, speed, pause on hover
- Loop, infinite scroll

**Style tab:**
- Arrow: size, color, background, border, position
- Dots: size, color, active color, gap

---

## Accordion / Nested Accordion (Pro)

**Content tab:**
- Items: each has title + content (Nested Accordion uses Container for content — supports any widget inside)
- Default open item

**Style tab:**
- Border: width, color, radius
- Title: background color, typography, color, padding, active state colors
- Content: background, typography, color, padding
- Icon: open/close icons, size, color, position (left/right)

**Native limits:** Smooth animation height (CSS `height: auto` transition) sometimes needs custom CSS for exact easing.

---

## Tabs / Nested Tabs (Pro)

**Content tab:**
- Items: each has title + content (Nested Tabs uses Container — supports any widget inside)
- Active tab on load

**Style tab:**
- Tab layout: horizontal / vertical
- Tab alignment
- Title: typography, color, background, padding, border, active state, hover state
- Content: background, padding, border

**Native limits:** Animated tab transitions (slide, fade between panels) need custom CSS/JS.

---

## Counter

**Content tab:**
- Starting number, ending number
- Duration (seconds)
- Number prefix / suffix
- Title (label below number)

**Style tab:**
- Number: typography, color (two separate layers: `typography_*` for number, `title_typography_*` for title)
- Title: typography, color
- Gap between number and title

**Note:** Always set both `typography_*` and `title_typography_*` in the same `update-widget` call.

---

## Form (Pro)

**Content tab:**
- Fields: text, email, tel, number, textarea, select, checkbox, radio, date, time, file upload, hidden, HTML
- Each field: label, placeholder, required, width (%), column break
- Submit button: text, size, alignment
- Actions after submit: email, redirect, webhook, MailChimp, etc.

**Style tab:**
- Labels: typography, color, spacing
- Fields: typography, text color, background, border, border-radius, padding, focus state
- Buttons: same as Button widget
- Messages: success / error color and typography

**Native limits:** Multi-step forms, conditional field logic need plugins (e.g., Fluent Forms) or custom JS.

---

## Price Table (Pro)

**Content tab:**
- Heading: plan name
- Sub heading (supports `<del>` for strikethrough old price)
- Price, currency symbol, period
- Features list: each item has icon + text + line-through toggle
- CTA button text + link
- Ribbon: text, position (top-right / top-left)

**Style tab:**
- Header: background, typography, color, padding
- Price: typography, color, period typography
- Features: divider, item typography, item icon color
- Footer: background, padding
- Button: full Button widget style controls

**Native limits:** Toggle between pricing tiers (monthly/annual) needs custom JS.

---

## Image Box

**Content tab:**
- Image
- Title, description
- Link

**Style tab:**
- Image: width, spacing, border, hover effects
- Title: typography, color, spacing
- Description: typography, color
- Content alignment, vertical alignment

---

## Loop Grid (Pro)

**Content tab:**
- Post type, filters (taxonomy, status, author)
- Template: select a Loop Item template
- Columns per breakpoint
- Pagination: none / numbers / load more / infinite scroll

**Style tab:**
- Column gap, row gap
- Pagination: typography, color, border, active state

**Note:** Design the card appearance in the Loop Item template (Theme Builder), not here.

---

## When to Use Custom CSS

Only reach for `add-custom-css` or WP Code snippets when the native Style tab genuinely cannot achieve the effect. Common legitimate cases:

| Effect | Why native fails | Solution |
|---|---|---|
| Gradient border | No native gradient border control | Custom CSS `border-image` or pseudo-element |
| Icon spin on hover | No animation control in Style tab | Custom CSS `@keyframes` |
| Glassmorphism card | No `backdrop-filter` control | Custom CSS |
| Sticky header with offset | Advanced stacking context | Custom CSS + JS |
| Monthly/annual price toggle | No native conditional display | WP Code JS snippet |
| Multi-color heading text | No per-word color control | Inline `<span style>` in title field |
| Scroll-triggered number counter delay | Motion effects don't chain | Custom JS via WP Code |
