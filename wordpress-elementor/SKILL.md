---
name: wordpress-elementor
description: |
  Use this skill for any task involving building, editing, or improving WordPress sites with Elementor Pro — especially when MCP tools are connected (elementor-mcp + WordPress MCP adapter). Trigger when the user wants to: create a new page or section in Elementor, improve an existing site's UX/UI and implement the changes, set up global styles (colors, typography, design system), map or audit an Elementor site, choose the right Elementor widget for a layout pattern, or combine Elementor work with other skills like impeccable or frontend-design. Also trigger when the user mentions: Elementor widgets, Elementor kit, global colors, global typography, containers, Loop Builder, Theme Builder, page builder, or any task that involves making changes to a WordPress/Elementor site — even if they don't say "Elementor" explicitly.
---

# WordPress + Elementor Pro

## Core Principle

Always use native Elementor widgets. The HTML widget breaks the design token chain — values become hardcoded and invisible to the kit system, clients can't edit content, and responsive behavior becomes unpredictable. Use the HTML widget only for third-party embeds that have no native equivalent.

When native Elementor cannot achieve something (complex animations, structural hacks, global behavior), use custom CSS at the element level first, then WP Code snippets for site-wide JS/CSS.

## Standardization Principle

**Before proposing any solution, ask: can Ricardo apply this himself repeatedly without external help?**

A solution that works once but requires remembering CSS variable names, typing internal API values, or running MCP calls is NOT a good solution — it creates dependency and inconsistency.

Prioritize solutions that:
- Use the Elementor editor UI natively (Global Classes dropdown, color picker, etc.)
- Can be applied by selecting a named class or preset from a list
- Don't require knowledge of internal variable names (e.g. `var(--e-global-color-primary)`)
- Are self-documenting: the class name communicates its purpose

If a technically correct solution fails the standardization test, propose an alternative workflow or create the infrastructure (e.g. CSS class in custom CSS) so the repeatable action becomes simple.

---

## Terminology

- **AE** — Atomic Elementor: widgets do editor atômico v4 (prefixo `e-`, integração nativa com global classes, estilo via classes Tailwind-like)
- **EP** — Elementor Pro classic: widgets legados com painel de controles próprio; necessários para funcionalidades sem equivalente AE

---

## AE vs EP — Widget Selection

**Regra geral:** preferir AE. Usar EP apenas quando o widget não tem equivalente AE ou requer customização além do que classes suportam.

| Função | AE (preferir) | EP (fallback) | Nota |
|---|---|---|---|
| Título | `e-heading` | `heading` | AE integra global classes direto |
| Texto | `e-paragraph` | `text-editor` | EP se precisar de editor rico (HTML, listas) |
| Imagem | `e-image` | `image` | AE |
| Botão | `e-button` | `button` | AE — `btn-primary` etc. via classes |
| SVG / ícone standalone | `e-svg` | — | AE com classe `icon-outline` + cor |
| Container de bloco | `e-div-block` | container | AE para componentes internos |
| Número animado | — | `counter` | Sem equivalente AE |
| Ícone + título + texto | — | `icon-box` | Sem equivalente AE direto |
| Accordion / Tabs | — | `accordion`, `tabs` | Sem equivalente AE |
| Formulário | — | `form` | Apenas EP (Pro) |
| Loop / posts dinâmicos | — | `loop-grid` | Apenas EP (Pro) |
| Carrossel | — | `nested-carousel` | Apenas EP |
| Menu de navegação | — | `nav-menu` | Apenas EP (header global) |
| Lista com ícones | — | `icon-list` | Manter EP enquanto AE não tem equivalente |

**Regra de escalada:** se um componente AE exigir customização que classes não cobrem (hover complexo, JS, controles de layout avançados), migrar para EP — nunca hackear AE além do que classes suportam.

---

## AE — Classe System (Tailwind-like)

O editor atômico trabalha com classes utilitárias — similar ao Tailwind. Cada classe tem uma responsabilidade:

- Classes de tipografia: `heading-xl`, `body-text`, etc.
- Classes de cor de texto: `text-primary`, `text-white`, etc.
- Classes de background: `dtb-bg-green`, `dtb-bg-dark`, etc.
- Classes de ícone: `icon-outline` + `dtb-icon-primary` (sempre as duas juntas para e-svg Lucide)

**Padrão de tokens entre sites:** classes permanecem com o mesmo nome (`btn-primary`, `heading-xl`), mas a aparência muda porque os tokens de cor/tipografia diferem por site. Não criar classes diferentes por site — variar os tokens.

**e-svg com Lucide — padrão obrigatório:**
```
classes: ["icon-outline", "dtb-icon-{cor}", "e-{id}-{hash}"]
```
- `icon-outline` — custom CSS do site: `fill: none !important; stroke: currentColor !important`
- `dtb-icon-{cor}` — global class com `color` prop apontando para token de cor
- Elementor renderiza e-svg com `fill="currentColor"` — sem `icon-outline`, o ícone aparece sólido

**Campo Classes no editor AE:** aceita global classes (aparecem no dropdown) e custom CSS classes (aplicadas mas não aparecem como chip). Não tentar exibir custom classes no dropdown — o fluxo atual funciona bem.

---

## Research Backlog — AE

Tópicos a investigar para evoluir a biblioteca de componentes AE:

1. **Hover states em global classes** — formato da variant com `state: "hover"` via REST API; validar se funciona no editor UI
2. **e-div-block como componente composto** — estrutura canônica: e-svg + e-heading + e-paragraph dentro de e-div-block com global class; testar estabilidade como template
3. **Classe como token — validação cross-site** — confirmar que global class com `color` prop atualiza automaticamente quando o token de cor muda; testar com dois sites de tokens diferentes
4. **Loop Builder + classes condicionais** — se é possível aplicar classes diferentes baseado em campo dinâmico (ex: categoria define classe de cor do componente)

---

## Critical Behavior Rules (MCP)

### Bloqueios — avisar e oferecer alternativas, nunca substituir silenciosamente
Quando uma ação solicitada não pode ser implementada via MCP (controle não existe, API retorna erro, parâmetro inválido), **parar e informar o usuário** com:
1. O que não foi possível e por quê
2. Alternativas disponíveis (editor manual, WPCode, outra abordagem)
Nunca substituir por outra solução sem avisar. Ricardo prefere decidir o caminho.

### Breakpoints — confirmar antes de aplicar
Antes de aplicar padding, margin ou tamanho de fonte, confirmar se é global ou mobile-only.
- Canvas estreito + bordas rosa no editor = visualização mobile → aplicar só no breakpoint correto
- Instrução sem breakpoint explícito → perguntar antes de aplicar
- `add-container` não tem sufixo de breakpoint — valores de padding são globais; ajustes mobile ficam para o editor

### Tipografia em widgets legados — `typography_typography: "custom"` obrigatório
Widgets legados (icon-list, button, text-editor, heading, icon-box, testimonial, accordion) ignoram `typography_font_family` sem `"typography_typography": "custom"` no mesmo update. Sempre incluir os dois juntos.

### `update-page-settings` — NUNCA usar
Sobrescreve todo o `_elementor_page_settings` incluindo CSS personalizado do usuário. Cada operação MCP já persiste automaticamente — não é preciso "salvar".


---

## Vault Consultation — Aprendizados

**Ao iniciar qualquer tarefa**, antes de qualquer chamada MCP:

1. **Extrair 2–3 termos-chave** da tarefa (ex: `carousel`, `tipografia`, `global-classes`, `variables`, `background`, `nested-tabs`)
2. **Buscar por filename** — rápido, cobre a maioria dos casos:
   ```bash
   find /Users/ricardooliveira/Documents/Obsidian-ProductDesigner/Expertise/vibe-wp -name "*<termo>*"
   ```
3. **Se não encontrar por filename**, buscar por conteúdo:
   ```bash
   grep -rl "<termo>" /Users/ricardooliveira/Documents/Obsidian-ProductDesigner/Expertise/vibe-wp/
   ```
4. **Ler só as notas que bateram** — máximo 3 notas, máximo 20 linhas cada:
   ```bash
   head -20 <path>
   ```
5. **Incorporar ao plano** antes de agir — se a nota indicar gotcha ou limitação, ajustar a abordagem antes de chamar qualquer MCP
6. Se nenhuma nota bater → prosseguir sem consulta

**Regras de token:**
- Nunca ler mais de 3 notas por consulta
- Nunca ler uma nota inteira — `head -20` é suficiente para o contexto inicial
- Se a nota for relevante mas incompleta, ler mais 10 linhas com `sed -n '21,30p' <path>`

---

## Two Operating Modes

### Mode 1: CREATION

Building a new page or section from a design system or brand kit.

**Trigger phrases:** "criar página", "build page", "implementar layout", "criar do zero", "montar a home"

**Workflow — always in this order:**

1. **Identify design system source** — Figma file, brand kit document, existing HTML, or disorganized site to extract tokens from
2. **Set up global styles first** — see `references/global-styles.md`
3. **Generate HTML reference** (optional, when client approval needed) — build a static HTML prototype where every component maps 1:1 to an Elementor widget; include HTML comments marking widget boundaries
4. **Build in Elementor via MCP** — sequence: Global Classes (via REST API) → page containers → widgets
5. **Apply classes to widgets** — never use local styles for anything used in 2+ places

**MCP operation sequence for a new page:**
```
1. list-pages → get post_id
2. get-global-settings → confirmar tokens disponíveis
3. INSPECT — get-element-settings em elementos de referência/irmãos antes de criar qualquer paralelo
4. add-container (page-level, flex column) → aplicar imediatamente: flex_gap + padding + padding_mobile + __globals__.background_color
5. add-container (section-level, per block) → aplicar imediatamente settings copiados da referência
6. add-[widget] por elemento de conteúdo → aplicar imediatamente __globals__ de tipografia e cor
7. get-element-settings em cada elemento novo → verificar que styles foram aplicados (não declarar completo antes)
8. batch-update para conteúdo restante (textos, imagens, links)
```

**⚠️ Criar sem estilizar = trabalho incompleto.** Ver "Style Fidelity Protocol" abaixo.

---

### Mode 2: IMPROVEMENT

Analyzing an existing site and implementing UX/UI improvements.

**Trigger phrases:** "melhorar o site", "analisar", "revisar", "o site está desorganizado", "padronizar"

**Workflow:**

1. **Map the site in parallel** — always run both extractions simultaneously:
   - elementor-mcp: `get-global-settings` + `list-pages` + `list-templates` + `get-page-structure` (home)
   - firecrawl: scrape visible pages to capture what the user actually sees
2. **Run anomalies checklist** — see `references/anomalies-checklist.md` — do this before any changes
3. **Invoke impeccable** (if UX/UI diagnosis requested) — pass the firecrawl output as context
4. **Plan interventions** — map each suggestion to the correct Elementor widget or kit setting
5. **Implement in batches** — confirm with Ricardo after each logical group (typography, colors, layout)
6. **Use batch-update** — group related changes into a single MCP call when possible

---

## Style Fidelity Protocol — Obrigatório

**Regra mestra:** Criar estrutura sem aplicar estilos é trabalho incompleto. Cada elemento criado deve ter seus estilos aplicados no mesmo passo — nunca delegar para depois.

### 1. Inspect Before Create

Antes de criar qualquer elemento que tem um paralelo/irmão já existente na página:

```
1. get-element-settings(post_id, ID_DO_ELEMENTO_REFERÊNCIA)
2. Identificar: __globals__ (background_color, typography_typography), flex_gap, padding, padding_mobile, container_type
3. Criar o novo elemento
4. Aplicar os mesmos settings imediatamente com update-element ou update-widget
```

**Quando aplicar:** sempre que o usuário pedir "adicionar seção similar", "replicar em outro idioma", "criar o mesmo padrão", ou qualquer tarefa onde uma estrutura análoga já existe.

---

### 2. Heading Creation Protocol

`add-heading` cria o widget com tipografia padrão do Elementor — não reflete o design system.

**Sequência obrigatória após add-heading:**

```
1. get-element-settings(post_id, ID_HEADING_REFERÊNCIA) → capturar valor __globals__.typography_typography
2. update-widget(post_id, novo_heading_id, { "__globals__": { "typography_typography": "globals/typography?id=XXXX" } })
```

Formato correto:
```json
{ "__globals__": { "typography_typography": "globals/typography?id=c4bd555" } }
```

Nota: `c4bd555` = Title-2 no nm-brasil.com.br. Em outros sites, ler o heading de referência para obter o ID — nunca adivinhar.

---

### 3. Container Section Protocol

`add-container` cria com valores padrão do Elementor: `flex_gap` 20px, padding 0, background transparente.

**Sequência obrigatória após add-container:**

```
1. get-element-settings(post_id, ID_CONTAINER_REFERÊNCIA)
2. update-element(post_id, novo_container_id, { ...settings_copiados })
```

Settings típicos para seções NMB (referência: PT calendário post_id 13512):
```json
{
  "flex_direction": "column",
  "background_background": "classic",
  "__globals__": { "background_color": "globals/colors?id=ffb04f2" },
  "padding": { "unit": "px", "top": "112", "right": "0", "bottom": "80", "left": "0", "isLinked": false },
  "padding_mobile": { "unit": "px", "top": "56", "right": "16", "bottom": "56", "left": "16", "isLinked": false },
  "flex_gap": { "column": "56", "row": "56", "isLinked": true, "unit": "px", "size": 56 }
}
```

**`padding_mobile` é suportado via MCP** — aplicar junto com o desktop no mesmo `update-element`.

---

### 4. Post-Creation Verification

Após qualquer criação estrutural, verificar antes de declarar completo:

```
get-element-settings(post_id, novo_elemento_id) → confirmar que __globals__, flex_gap e padding foram aplicados
```

Se flex_gap ainda for 20px, padding for 0 ou __globals__ ausente → reaplicar. Nunca reportar sucesso sem verificação.

---

### 5. UX/UI Checklist — O que Não Pode Ser Ignorado

| Elemento | Propriedade obrigatória | Risco se ignorado |
|---|---|---|
| Heading | `__globals__.typography_typography` | Fonte padrão Elementor, não o design system |
| Container de seção | `flex_gap` | Gap padrão 20px vs 56px — densidade visual errada |
| Container de seção | `padding` desktop | Seção sem respiro visual |
| Container de seção | `padding_mobile` | Mobile sem margem lateral |
| Container de seção | `__globals__.background_color` | Fundo transparente, sem identidade visual |
| Grid container | `container_type: "grid"` | Layout em linha em vez de grade |
| Widget oculto | `hide_desktop/tablet/mobile` via `update-element` | Usar valores device-specific `"hidden-desktop"` — **nunca** `batch-update` para containers |

---

## Known Limitations — O que MCP Não Consegue Fazer

Quando uma dessas limitações aparecer: **parar, informar o usuário, propor alternativa manual**. Nunca fingir que foi feito.

| Limitação | Causa | Alternativa |
|---|---|---|
| `add-container` no nível raiz da página (`parent_id=post_id`) | API retorna "Parent element not found" | Duplicar container existente do mesmo nível → limpar filhos → reposicionar com `reorder-elements` |
| Alterar colunas do grid por breakpoint (ex: 3 desktop → 1 mobile) | `grid_template_columns` responsivo não exposto via MCP | Editor manual: selecionar container → Advanced → Grid, ajustar por breakpoint |
| Hover CSS states | Nenhum campo settings corresponde ao state hover | Custom CSS com `[id]:hover` via `add-custom-css` no elemento |
| Animações de scroll nativas do Elementor | Motion Effects API não exposta via MCP | Editor manual: Advanced → Motion Effects |
| Criar/editar Global Classes | Requer REST API (`PUT /elementor/v1/global-classes`), não está no MCP | `curl` direto ou editor de Global Classes do Elementor |
| Slots do sistema de cor (primary, secondary) via `update-global-colors` | MCP só escreve em `custom_colors`, não nos 4 slots do sistema | REST API: `POST /wp-json/elementor/v1/globals/colors/{slot}` |
| Cache LiteSpeed/Cloudflare após qualquer update | MCP escreve corretamente, mas cache serve HTML antigo | Purge All no WP Admin → LiteSpeed Cache → Purge All (obrigatório após toda sessão de edição) |

---

## Widget Selection Rules

Read `references/widget-mapping.md` for the full HTML-to-widget mapping table.

**Quick rules:**
- `<h1>`–`<h6>` → `add-heading` (set `header_size`)
- `<p>` body text → `add-text-editor`
- CTA button → `add-button`
- Icon + title + description → `add-icon-box` (not three separate widgets)
- Testimonial quote → `add-testimonial` or `add-testimonial-carousel`
- Checklist / feature list → `add-icon-list`
- Collapsible FAQ → `add-accordion` or `add-nested-accordion`
- Tab panels → `add-tabs` or `add-nested-tabs`
- Animated number → `add-counter`
- Dynamic posts grid → `add-loop-grid` (not `add-posts-grid` for custom post types)
- Pricing → `add-price-table`
- Gallery → `add-gallery` (Pro) — never a grid of image HTML
- Navigation → `add-nav-menu`
- Contact form → `add-form`

**Never use `add-html` for:** headings, paragraphs, buttons, icons, images, cards, grids, or any layout that has a native widget equivalent.

---

## Global Styles — Critical MCP Limitation

The MCP `update-global-colors` only writes to `custom_colors`, NOT to the 4 system slots (primary, secondary, text, accent). To update system slots, use REST API directly:

```bash
AUTH="Basic <base64-user:pass>"
BASE="https://<site>/wp-json/elementor/v1"

# System color slot (primary | secondary | text | accent)
curl -s -X POST -H "Authorization: $AUTH" -H "Content-Type: application/json" \
  -d '{"id":"primary","title":"Brand Primary","value":"#HEX"}' \
  "$BASE/globals/colors/primary"

# System typography slot
curl -s -X POST -H "Authorization: $AUTH" -H "Content-Type: application/json" \
  -d '{"id":"primary","title":"Primary","value":{"font_family":"Inter","font_weight":"700"}}' \
  "$BASE/globals/typography/primary"
```

Similarly, `container_width` and `body_typography` are in `_elementor_kit_settings` and must be set manually: Site Settings → Layout and Site Settings → Global Fonts.

Full global styles workflow in `references/global-styles.md`.

---

## Typography Format for update-widget

Always use this exact structure — `sizes: []` is required or the field may be silently ignored:

```json
{
  "typography_typography": "custom",
  "typography_font_family": "Inter",
  "typography_font_weight": "600",
  "typography_font_size": { "unit": "px", "size": 32, "sizes": [] },
  "typography_line_height": { "unit": "em", "size": 1.3, "sizes": [] }
}
```

For the Counter widget, two separate layers exist:
- `typography_*` → the animated number
- `title_typography_*` → the label below the number

Both must be defined in the same `update-widget` call.

---

## Atomic Editor v4 — System-First Workflow

When working on a site with Elementor v4 (atomic editor) enabled:

**Hierarchy:**
```
Variables (POST /elementor/v1/variables/create → IDs e-gv-xxxxxxx)
  └── Global Classes (PUT /elementor/v1/global-classes — refs IDs via $$type)
        └── Widgets (classic: _css_classes | atomic: classes $$type)
```

**Practical rules:**
- Create a Global Class whenever a style is used in 2+ places
- Apply to classic widgets via `_css_classes: "class-name"` in update-widget
- Apply to atomic widgets via `"classes": {"$$type": "classes", "value": ["class-name", "e-id-7hex"]}`
- `padding` is NOT supported in Global Class props — set directly on element via update-element
- Outline/transparent button classes MUST include explicit `background: transparent`
- Do NOT confuse `/globals/colors` (legacy Global Colors panel) with `/variables/create` (atomic Variables panel)

**Variables API — `POST /elementor/v1/variables/create`:**
```json
{"label": "dtb-orange", "value": "#f88c00", "type": "global-color-variable"}
{"label": "kallisto-bold", "value": "Kallisto",  "type": "global-font-variable"}
{"label": "text-xl",  "value": "1.25rem", "type": "global-size-variable"}
{"label": "spacing-4", "value": "1rem",   "type": "global-size-variable"}
{"label": "rounded-lg", "value": "0.5rem", "type": "global-size-variable"}
```
Returns `{"id": "e-gv-xxxxxxx"}`. Save all IDs before creating classes.
Standard set per project: 11 colors + 2 fonts + 10 text sizes + 12 spacings + 8 border-radius = **43 variables**.

**Global Classes — 3 groups, each with different prop format:**

Group 1 — Typography (font + size + color, refs variable ID directly):
```json
"props": {
  "font-family": {"$$type": "global-font-variable",  "value": "e-gv-XXXXXXX"},
  "font-size":   {"$$type": "global-size-variable",  "value": "e-gv-XXXXXXX"},
  "color":       {"$$type": "global-color-variable", "value": "e-gv-XXXXXXX"}
}
```

Group 2 — Background classes (refs variable via CSS var string):
```json
"props": {
  "background": {"$$type": "background", "value": {"color": {"$$type": "color", "value": "var(--e-gv-XXXXXXX)"}}}
}
```
Note: gradient backgrounds are NOT supported in class props — apply via `update-element` directly.

Group 3 — Text color overrides (refs variable via CSS var string):
```json
"props": {
  "color": {"$$type": "color", "value": "var(--e-gv-XXXXXXX)"}
}
```

**PUT /elementor/v1/global-classes rules:**
- HTTP 204 = success (no body)
- `order` array MUST include ALL existing class IDs on the site, not just the new ones
- Hover state: second variant with `"meta": {"breakpoint": "desktop", "state": "hover"}`

---

## Chrome MCP Requirement

Before writing any custom CSS — inspect with Chrome MCP first. Never guess selectors. The resolved value of a token (e.g., `--e-global-color-primary`) may differ from the kit value due to theme overrides or external CSS. Always verify.

---

## Combining with Other Skills

- **impeccable**: invoke in Mode 2 after site mapping, pass the firecrawl/structure output as context for UX diagnosis
- **frontend-design**: invoke in Mode 1 when creating the HTML reference prototype before Elementor implementation
- **elementor-controls**: invoke when a widget customization requires PHP (custom widget controls, not CSS)

---

## HTML Generation Rules

When generating HTML prototypes, the HTML must mirror Elementor widget structure — not be generic HTML. Read `references/html-to-widget-protocol.md` before generating any HTML.

Key rules:
- Every block opens with `<!-- [Widget: add-xxx | property: value] -->` annotation
- Class names follow `el-{widget}` convention
- CSS custom properties in `:root` map explicitly to Elementor global slots
- Effects that native controls cannot achieve are flagged with `NATIVE-LIMIT`
- The HTML structure directly predicts the MCP call sequence for implementation

---

## Nested Carousel — Regras Obrigatórias

O widget `nested-carousel` mantém **dois arrays separados** que precisam estar sempre em sync:
- `elements[]` — os containers filhos reais (slides)
- `carousel_items[]` — array de metadata no settings do widget (IDs + títulos)

O Elementor só mantém isso em sync quando o slide é criado pelo editor nativo. Qualquer inserção via MCP quebra o vínculo → slides fantasmas ou em branco ao final do carousel.

### Antes de qualquer edição estrutural

```
1. get-page-structure (post_id) → coletar IDs reais dos containers filhos do nested-carousel
2. get-element-settings (carousel widget_id) → checar carousel_items[]
3. Comparar: se _ids no carousel_items ≠ _ids dos containers reais → está dessincronizado
```

### Ao adicionar slides (duplicate-element ou add-container)

```
1. duplicate-element ou add-container dentro do carousel
2. get-page-structure → capturar o novo ID do container criado
3. update-widget no carousel → adicionar o novo _id ao carousel_items[]
   (nunca pular este passo — é o que causa slides em branco)
```

### Fix para carousel dessincronizado

```
1. get-page-structure → listar todos os IDs reais dos containers filhos
2. update-widget (carousel widget_id) com:
   carousel_items: [{ "_id": "ID_REAL", "slide_title": "Nome" }, ...]
   — um item por container, na mesma ordem
```

### Verificação após qualquer mudança

`len(carousel_items)` deve ser igual a `len(elements filhos diretos do widget)`. Se divergir → corrigir antes de continuar.

---

## Reference Files

- `references/html-to-widget-protocol.md` — How to generate HTML that mirrors Elementor widgets; HTML→MCP translation checklist (read before generating HTML or implementing)
- `references/widget-native-controls.md` — What each widget achieves natively in Content/Style/Advanced tabs (read before deciding to use custom CSS)
- `references/widget-mapping.md` — HTML patterns → correct Elementor widget (read when choosing widgets)
- `references/global-styles.md` — Full global styles setup workflow (read when setting up or auditing kit)
- `references/anomalies-checklist.md` — 7 recurring anomalies to check before any intervention (read in Mode 2)
- `references/json-workflow.md` — Legacy JSON export/import workflow (read when MCP is not available or for backup)
