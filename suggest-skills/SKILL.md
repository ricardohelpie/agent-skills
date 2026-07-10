---
name: suggest-skills
description: Analisa o projeto/tarefa atual e sugere skills instaladas em ~/.claude/skills que podem ser úteis, perguntando ao usuário se deseja ativar alguma delas.
---

# Suggest Skills

Lê o contexto atual (projeto, tarefa em andamento, stack) e cruza com as skills instaladas localmente para sugerir quais podem ser úteis — perguntando ao usuário antes de qualquer ação.

## Comportamento

### Passo 1 — Coletar contexto

Identifique:
- Diretório atual e tipo de projeto (WordPress, React/Next.js, design, etc.)
- Tarefa descrita pelo usuário na sessão atual
- Stack relevante (Elementor, Figma, animações, Obsidian, etc.)

### Passo 2 — Ler skills instaladas

Leia `~/.claude/skills/` para listar as skills disponíveis (nome + descrição do SKILL.md de cada uma).

Referência rápida das skills instaladas (verificar diretório para atualizações):

| Skill | Quando é útil |
|---|---|
| `animate` | Animações CSS/JS (scroll, hover, entrada) |
| `copywriting` | Reescrever ou criar copy de marketing |
| `design-to-html` | Converter design para HTML/CSS |
| `elementor-controls` | Trabalhar com widgets/controles Elementor |
| `figma-code-connect` | Mapear componentes Figma → código |
| `figma-create-design-system-rules` | Criar regras de design system no Figma |
| `figma-generate-design` | Gerar layouts completos no Figma |
| `figma-generate-library` | Construir bibliotecas de componentes no Figma |
| `figma-implement-design` | Implementar design Figma → código produção |
| `find-skills` | Descobrir e instalar novas skills |
| `frontend-design` | Componentes frontend com alta direção estética |
| `insights-digest` | Extrair friction points → Obsidian → Gmail |
| `research-stack` | Pesquisa de stack técnica |
| `save-learnings` | Salvar aprendizados de sessão em Obsidian + CLAUDE.md |
| `svg-animation-engineer` | Animações SVG puras com CSS keyframes |
| `svg-animations` | SVG interativos e ilustrações animadas |
| `ui-ux-pro-max` | Critique e geração de UI premium |
| `wordpress-elementor` | Sites WordPress + Elementor |
| `wp-update` | Atualizações WordPress |

### Passo 3 — Cruzar e filtrar

Selecione apenas skills com match claro ao contexto atual. Não liste skills irrelevantes.

Critérios de match:
- **WordPress/Elementor ativo** → `wordpress-elementor`, `elementor-controls`, `wp-update`
- **Figma aberto ou mencionado** → `figma-*` relevantes
- **Animação mencionada** → `animate`, `svg-animations`, `svg-animation-engineer`
- **Design → código** → `design-to-html`, `figma-implement-design`, `frontend-design`
- **Obsidian/pesquisa** → `research-stack`, `save-learnings`, `insights-digest`
- **Copy/marketing** → `copywriting`

### Passo 4 — Apresentar ao usuário

Mostre apenas as skills com match. Formato:

```
Com base no projeto atual ([nome do projeto/contexto]), estas skills podem ser úteis:

1. **`skill-name`** — [o que faz em 1 linha]
   Usar com: /skill-name

2. **`skill-name`** — [o que faz em 1 linha]
   Usar com: /skill-name

Quer ativar alguma delas agora?
```

Se nenhuma skill tiver match claro, responda:
```
Nenhuma skill instalada parece especialmente relevante para o contexto atual.
Quer que eu procure novas skills? (posso rodar /find-skills)
```

## Regras

- Nunca ative uma skill sem confirmação do usuário
- Nunca liste todas as skills — só as relevantes ao contexto
- Máximo 4 sugestões por vez
- Se o usuário confirmar, invoque a skill com `Skill({ skill: "nome" })`
