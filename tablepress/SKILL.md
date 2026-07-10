---
name: tablepress
description: |
  Create, import, and embed tables in WordPress using the TablePress plugin.
  Use when managing schedules, grids, pricing tables, or any tabular content
  in WordPress/Elementor sites. Triggers: "create a TablePress table", "embed
  [table id=N]", "import CSV/JSON into TablePress", "configure table
  sorting/pagination", "add a table to an Elementor page", "create a schedule
  table in WordPress". Covers: creating tables via WP Admin session or script,
  embedding via shortcode or Elementor widget, CSS styling, DataTables config,
  and programmatic import without REST API (free plan compatible).
---

# TablePress

Plugin WordPress para gerenciar tabelas. Cada tabela tem um ID numérico e é embutida via shortcode ou bloco Gutenberg.

## Embed em posts/páginas

```
[table id=1 /]
```

No Elementor: usar widget **Shortcode** ou **HTML** — não o bloco Gutenberg.

Para tabelas estáticas (grade de evento, lista de preços sem interatividade):

```
[table id=1 use_datatables=false alternating_row_colors=false /]
```

`use_datatables=false` desativa sort/filter/pagination — reduz JS carregado e evita comportamento inesperado.

Para estilização custom, adicionar classe via `extra_css_classes=minha-classe` e estilizar no Elementor Custom CSS ou WPCode.

Para referência completa de parâmetros: [references/shortcode-params.md](references/shortcode-params.md)

## Criar tabela via script (sem REST API)

Usar `scripts/wp_tablepress_import.py` — funciona com o plano gratuito do TablePress.

Fluxo: login com cookie → busca nonce `tablepress_import` na página de import → POST com JSON/CSV → captura table ID no redirect.

```bash
python3 scripts/wp_tablepress_import.py \
  --url https://seusite.com.br \
  --user admin --pass "senha" \
  --data '[["Horário","Parceiro","Tema"],["10h","TikTok","Como usar Live"]]' \
  --name "Grade Oficinas"
```

Retorna o table ID criado, pronto para usar no shortcode.

## Formato JSON de import

Array 2D de strings — primeira linha é o cabeçalho:

```json
[
  ["Horário", "Parceiro", "Tema"],
  ["10h", "TikTok Shop", "Live na prática"],
  ["13h", "Nós Somos Moda", "Estratégia de comunicação"]
]
```

Para importar/exportar formatos e fontes suportadas: [references/import-export.md](references/import-export.md)

## CSS útil para tabelas de evento

```css
/* Remover zebra striping e hover em tabelas estáticas */
.tablepress td, .tablepress th { background: transparent !important; }
.tablepress tbody tr:hover td { background: transparent !important; }

/* Alinhar primeira coluna (horário) centralizado */
.tablepress td:first-child { text-align: center; font-weight: bold; }
```

## Gotchas críticos

- O ID da tabela no WP Admin pode não ser sequencial — sempre verificar na tela "All Tables"
- `cache_table_output=false` necessário se a tabela tiver shortcodes ou conteúdo dinâmico nas células
- TablePress carrega DataTables JS em toda página que tiver a tabela — usar `use_datatables=false` quando não precisar de interatividade
- Import via "form-field" aceita JSON puro (array 2D) ou CSV — o plugin detecta automaticamente
- REST API (`/wp-json/tablepress/v1/tables`) só existe no plano **Max** (pago); o script usa o form de import do WP Admin que funciona no plano gratuito
