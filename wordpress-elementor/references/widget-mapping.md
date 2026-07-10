# Widget Mapping — HTML Patterns → Elementor Widgets

## Text & Typography

| HTML Pattern | Elementor Widget | MCP Tool | Notes |
|---|---|---|---|
| `<h1>`–`<h6>` | Heading | `add-heading` | Set `header_size`: h1–h6, div, span, p |
| `<p>` body text | Text Editor | `add-text-editor` | Supports rich text, links, inline HTML |
| `<blockquote>` | Blockquote (Pro) | `add-blockquote` | With citation and style options |
| Curved/path text | Text Path (Pro) | `add-text-path` | Requires SVG path |
| Animated headline | Animated Headline (Pro) | `add-animated-headline` | Rotating/typing/highlight effects |

## Media

| HTML Pattern | Elementor Widget | MCP Tool | Notes |
|---|---|---|---|
| `<img>` standalone | Image | `add-image` | Set `image`, `alt`, `caption`, link |
| `<img>` + title + text | Image Box | `add-image-box` | Single widget — don't use 3 separate ones |
| `<video>` or YouTube embed | Video | `add-video` | YouTube, Vimeo, HTML5 |
| Lottie animation | Lottie (Pro) | `add-lottie` | JSON animation file |
| Image carousel / slider | Image Carousel | `add-image-carousel` | Auto or manual navigation |
| Media carousel | Media Carousel (Pro) | `add-media-carousel` | Mixed image/video |

## Layout & Structure

| HTML Pattern | Elementor Widget | MCP Tool | Notes |
|---|---|---|---|
| Flexbox container | Container | `add-container` | Use for all structural grouping |
| `<hr>` divider | Divider | `add-divider` | Styled horizontal rule |
| Blank vertical space | Spacer | `add-spacer` | Better than padding hacks |
| Anchor target | Menu Anchor | `add-menu-anchor` | Invisible, for one-page nav |

## Navigation & Interaction

| HTML Pattern | Elementor Widget | MCP Tool | Notes |
|---|---|---|---|
| `<a>` CTA button | Button | `add-button` | Size, style, icon, link, hover |
| `<nav>` menu | Nav Menu | `add-nav-menu` | Uses WordPress nav menus |
| Tab panels | Tabs / Nested Tabs (Pro) | `add-tabs` / `add-nested-tabs` | Nested Tabs supports container content |
| Accordion / FAQ | Accordion / Nested Accordion (Pro) | `add-accordion` / `add-nested-accordion` | Nested supports container content |
| Off-canvas sidebar | Off Canvas (Pro) | `add-off-canvas` | Slide-in panel triggered by button |
| Search bar | Search (Pro) | `add-search` | Site search integration |

## Icons & Lists

| HTML Pattern | Elementor Widget | MCP Tool | Notes |
|---|---|---|---|
| Standalone icon | Icon | `add-icon` | From icon libraries |
| Icon + title + description | Icon Box | `add-icon-box` | Three-in-one widget |
| Bullet list with icons | Icon List | `add-icon-list` | Feature lists, checklists |
| Social media icons | Social Icons | `add-social-icons` | Pre-styled with brand colors |
| Star rating display | Star Rating | `add-star-rating` | Static display |
| Animated counter | Counter | `add-counter` | Number animation on scroll |
| Progress bar | Progress | `add-progress` | Animated fill bar |

## Cards & Composite Patterns

| HTML Pattern | Elementor Widget | MCP Tool | Notes |
|---|---|---|---|
| Testimonial card | Testimonial | `add-testimonial` | Quote + name + image + company |
| Testimonial slider | Testimonial Carousel (Pro) | `add-testimonial-carousel` | Multiple testimonials rotating |
| Flip card (front/back) | Flip Box (Pro) | `add-flip-box` | CSS flip animation |
| CTA section with button | Call To Action (Pro) | `add-call-to-action` | Image + text + button |
| Hotspot on image | Hotspot (Pro) | `add-hotspot` | Interactive image markers |
| Author bio | Author Box (Pro) | `add-author-box` | Gravatar + name + bio |

## Dynamic & Posts

| HTML Pattern | Elementor Widget | MCP Tool | Notes |
|---|---|---|---|
| Post grid / blog grid | Loop Grid (Pro) | `add-loop-grid` | For any CPT, use Loop Builder |
| Post carousel | Loop Carousel (Pro) | `add-loop-carousel` | Carousel version of Loop Grid |
| Portfolio grid | Portfolio (Pro) | `add-portfolio` | With filter categories |
| Table of contents | Table of Contents (Pro) | `add-table-of-contents` | Auto-generated from headings |

## Forms & Conversion

| HTML Pattern | Elementor Widget | MCP Tool | Notes |
|---|---|---|---|
| Contact / lead form | Form (Pro) | `add-form` | Full field builder, submissions |
| Login form | Login (Pro) | `add-login` | WP user login with redirect |
| Social share | Share Buttons (Pro) | `add-share-buttons` | Multiple platforms |
| Countdown timer | Countdown (Pro) | `add-countdown` | Date-based or evergreen |
| Popup trigger | — | `create-popup` | Set conditions with `set-popup-settings` |

## Pricing & Commercial

| HTML Pattern | Elementor Widget | MCP Tool | Notes |
|---|---|---|---|
| Pricing card | Price Table (Pro) | `add-price-table` | Header, price, features list, button |
| Menu / price list | Price List (Pro) | `add-price-list` | Restaurant/service menus |

## Embeds & Code (use sparingly)

| HTML Pattern | Elementor Widget | MCP Tool | Notes |
|---|---|---|---|
| WP shortcode | Shortcode | `add-shortcode` | Only for plugins with no native widget |
| Third-party embed (no widget) | HTML | `add-html` | Last resort only |
| Code sample display | Code Highlight (Pro) | `add-code-highlight` | Syntax-highlighted code blocks |
| Google Maps | Google Maps | `add-google-maps` | Embedded map with marker |

---

## Decision Tree: When to Use Custom CSS

1. Does a native Elementor widget exist for this pattern? → Use it
2. Can the visual be achieved via the widget's Style tab settings? → Use Style tab
3. Is a Global Class appropriate (used in 2+ places)? → Create Global Class
4. Is this element-specific and non-repeating? → Use element-level custom CSS via `add-custom-css`
5. Is this a site-wide behavior or animation? → Use WP Code snippet via `add-code-snippet`
6. Does this require JavaScript? → Use `add-code-snippet` with JS, or `add-custom-js` at element level
