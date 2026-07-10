---
name: save-learnings
description: Persist session findings to Obsidian-ProductDesigner vault (filesystem, no MCP)
---

## Vault

- **Path:** `/Users/ricardooliveira/Documents/Obsidian-ProductDesigner/`
- Usar `Write`/`Read`/`Edit`/`Bash` diretamente — **não usar** `mcp__obsidian__*` (trava aguardando REST API)

## Quando invocar

Invocar ao fim de sessões que contenham:
- Problema resolvido de forma não óbvia
- Padrão de design/código validado na prática
- Ferramenta ou skill usada com sucesso pela primeira vez
- Decisão de produto/design com raciocínio relevante

Não invocar para tarefas rotineiras ou edições simples.

## Processo

1. **Avaliar a sessão:** houve aprendizado concreto e reusável?
2. **Verificar duplicata:** `Bash("grep -rl '<termo-chave>' /Users/ricardooliveira/Documents/Obsidian-ProductDesigner/Expertise/ 2>/dev/null")`
3. **Criar nota** em `Expertise/<area>/YYYY-MM-DD-slug.md` com frontmatter:
   ```yaml
   ---
   type: aprendizado
   area: vibe-wp | vibe-react | design-system | ux-ui | animacao | ferramentas
   clientes: [nmb, treeid, tribemd, grupobipp, ...]
   reusavel_em: [wordpress, elementor, nextjs, react, figma, tailwind, ...]
   confianca: alto | medio | baixo
   updated: YYYY-MM-DD
   tags: []
   ---
   ```
   **Área correta:**
   - `vibe-wp` → WordPress, Elementor, REST API, plugins, LiteSpeed, MCP
   - `vibe-react` → React, Next.js, TypeScript, Tailwind, shadcn
   - `design-system` → tokens, atomic design, kit, documentação de DS
   - `ux-ui` → padrões UX, layout, contraste, interação visual
   - `animacao` → WebGL, GSAP, SVG, Remotion, CSS animations
   - `ferramentas` → MCPs, Claude Code, Python, devtools, regras de processo
4. **Se for padrão recorrente:** criar também em `Patterns/`
5. **Atualizar Dashboard** em `_meta/Dashboard.md`:
   - Localizar a seção da área pelo cabeçalho (ex: `## Vibe Coding — WordPress / Elementor`)
   - Inserir nova linha logo após `|---|---|---|` dessa seção (mais recente primeiro):
     `| YYYY-MM-DD | [[Expertise/<area>/slug\|Título da nota]] | cliente1, cliente2 |`
   - Atualizar o contador `**N notas**` na linha abaixo do cabeçalho (incrementar N em 1)
   - Atualizar `**N aprendizados**` na linha de resumo no topo do arquivo

   **Mapa área → cabeçalho de seção no Dashboard:**
   - `vibe-wp`       → `## Vibe Coding — WordPress / Elementor`
   - `vibe-react`    → `## Vibe Coding — React / Next.js`
   - `design-system` → `## Design System`
   - `ux-ui`         → `## UX / UI`
   - `animacao`      → `## Animação`
   - `ferramentas`   → `## Ferramentas & Processo`

## Regras

- Máximo 30 linhas por nota
- Não duplicar — verificar antes de criar
- Dashboard: atualizar só os campos que mudaram (cabeçalho da seção + contador + linha nova)
- Datas absolutas (YYYY-MM-DD) — nunca relativas
