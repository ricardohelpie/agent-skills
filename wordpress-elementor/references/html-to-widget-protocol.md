# HTML-to-Widget Protocol

## Purpose

When generating HTML prototypes, every component must mirror an Elementor widget — not generic HTML. This makes the prototype directly translatable to Elementor without interpretation gaps.

---

## HTML Generation Rules

### 1. Mark every component with a widget annotation

Every block must open with a comment declaring the widget it maps to:

```html
<!-- [Widget: add-heading | header_size: h2 | align: center] -->
<h2 class="el-heading">Título da Seção</h2>

<!-- [Widget: add-icon-box | icon: fas fa-check | position: top] -->
<div class="el-icon-box">
  <i class="fas fa-check"></i>
  <h3>Feature Title</h3>
  <p>Feature description text goes here.</p>
</div>
```

### 2. Use semantic class names that map to widget tabs

Class naming convention: `el-{widget-name}` for the wrapper, `el-{widget}___{part}` for internals.

```html
<!-- [Widget: add-button | size: md | type: filled | icon: fas fa-arrow-right | icon_align: right] -->
<a href="#" class="el-button el-button--primary el-button--md">
  Saiba Mais <i class="fas fa-arrow-right"></i>
</a>

<!-- [Widget: add-counter | starting_number: 0 | ending_number: 5000 | suffix: +] -->
<div class="el-counter">
  <span class="el-counter___number">5.000+</span>
  <span class="el-counter___title">Visitantes qualificados</span>
</div>
```

### 3. Mark containers with layout intent

```html
<!-- [Container: flex | direction: row | justify: space-between | gap: 32px] -->
<div class="el-container el-container--row el-container--gap-md">
  <!-- children here -->
</div>

<!-- [Container: flex | direction: column | align: center] -->
<section class="el-section el-section--center">
  <!-- children here -->
</section>
```

### 4. Mark global token usage

When a color or font maps to a global token, note it explicitly:

```html
<!-- [Widget: add-heading | color: var(--color-primary) → global: primary] -->
<h1 class="el-heading el-heading--xl" style="color: var(--color-primary)">
  Headline Text
</h1>
```

### 5. Mark what requires custom CSS

If a visual effect cannot be achieved natively, flag it:

```html
<!-- [Widget: add-container | NATIVE-LIMIT: gradient border requires custom CSS] -->
<div class="el-card el-card--gradient-border">
  ...
</div>
```

---

## HTML Section Template (Homepage)

Use this structure as the base for homepage HTML prototypes:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Client] — Prototype</title>
  <!-- Design tokens — map to Elementor Global Colors + Typography -->
  <style>
    :root {
      --color-primary: #HEX;       /* → Elementor system: primary */
      --color-secondary: #HEX;     /* → Elementor system: secondary */
      --color-text: #HEX;          /* → Elementor system: text */
      --color-accent: #HEX;        /* → Elementor system: accent */
      --font-heading: 'FontName';  /* → Elementor system typography: primary */
      --font-body: 'FontName';     /* → Elementor system typography: text */
      --space-section: 80px;       /* → Elementor container padding */
      --space-gap: 32px;           /* → Elementor container gap */
      --radius-btn: 6px;           /* → Button widget border-radius */
      --radius-card: 12px;         /* → Container border-radius */
    }
  </style>
</head>
<body>

  <!-- ═══════════════════════════════════════════
       HERO
       [Container: flex | direction: row | min-height: 100vh]
       ═══════════════════════════════════════════ -->
  <section class="el-section el-section--hero">

    <!-- [Widget: add-heading | header_size: h1] -->
    <h1 class="el-heading el-heading--xl">Headline Principal</h1>

    <!-- [Widget: add-text-editor] -->
    <p class="el-text">Subtítulo ou descrição do hero.</p>

    <!-- [Widget: add-button | size: lg | type: filled] -->
    <a href="#" class="el-button el-button--primary el-button--lg">CTA Principal</a>

    <!-- [Widget: add-image | link: none] -->
    <img src="hero-image.jpg" alt="Hero" class="el-image">

  </section>

  <!-- ═══════════════════════════════════════════
       FEATURES / BENEFITS
       [Container: flex | direction: row | wrap: wrap | gap: 32px]
       ═══════════════════════════════════════════ -->
  <section class="el-section">

    <!-- [Widget: add-heading | header_size: h2 | align: center] -->
    <h2 class="el-heading el-heading--lg el-heading--center">Por que escolher</h2>

    <div class="el-container el-container--row el-container--wrap">

      <!-- Repeat per feature: [Widget: add-icon-box | position: top | icon: fas fa-star] -->
      <div class="el-icon-box">
        <i class="fas fa-star"></i>
        <h3>Feature Title</h3>
        <p>Feature description.</p>
      </div>

    </div>
  </section>

  <!-- ═══════════════════════════════════════════
       TESTIMONIALS
       [Widget: add-testimonial-carousel]
       ═══════════════════════════════════════════ -->
  <section class="el-section">
    <div class="el-testimonial-carousel">

      <!-- [Widget: add-testimonial | name: "Nome" | title: "Cargo, Empresa"] -->
      <div class="el-testimonial">
        <p class="el-testimonial___content">"Depoimento do cliente aqui."</p>
        <span class="el-testimonial___name">Nome Sobrenome</span>
        <span class="el-testimonial___title">Cargo, Empresa</span>
      </div>

    </div>
  </section>

  <!-- ═══════════════════════════════════════════
       CTA FINAL
       [Container: flex | direction: column | align: center | background: primary]
       ═══════════════════════════════════════════ -->
  <section class="el-section el-section--bg-primary">

    <!-- [Widget: add-heading | header_size: h2 | color: white] -->
    <h2 class="el-heading el-heading--lg el-heading--white">Pronto para começar?</h2>

    <!-- [Widget: add-button | size: lg | type: outline | color: white] -->
    <a href="#" class="el-button el-button--outline-white el-button--lg">Falar com especialista</a>

  </section>

</body>
</html>
```

---

## HTML → Elementor Translation Checklist

When implementing HTML in Elementor via MCP, go element by element in this order:

1. **Read structure** — `get-page-structure` if updating existing, or plan containers fresh
2. **Create outer containers** — one per `<section>` (flex column, full width)
3. **Create inner containers** — per row/grid inside each section
4. **Add widgets** — follow the `[Widget: ...]` annotations exactly
5. **Apply content** — text, images, links from the HTML
6. **Apply styling** — use Style tab properties (see `widget-native-controls.md`); only use `add-custom-css` for effects marked `NATIVE-LIMIT`
7. **Apply global tokens** — link colors/fonts to global slots, never hardcode hex values
8. **Batch-update** — group typography and color updates into `batch-update` calls
