---
name: my-design-work
description: >
  Orquestradora de todo o trabalho de product design do Ricardo — não se limita a
  WordPress. Combina as skills de design já instaladas (impeccable, ui-ux-pro-max,
  frontend-design, the-maya-design, design-critique, nmb-product-designer,
  wordpress-elementor, research-stack, suggest-skills) na ordem certa para a tarefa,
  e cruza isso com o vault Obsidian-ProductDesigner (Expertise, Patterns, Ferramentas,
  Inspiration). Ativa quando o Ricardo pede uma direção/estilo visual, quer avaliar ou
  redesenhar uma interface, menciona "board de inspiração", "referência de estilo",
  quer combinar/coordenar mais de uma skill de design na mesma tarefa, ou tem qualquer
  pedido de product design que não seja especificamente WordPress/Elementor (esse
  fluxo continua com `wordpress-elementor`, que esta orquestradora também sabe acionar
  quando o projeto for WP) nem exclusivamente NMB (que tem `nmb-product-designer`).
metadata:
  version: "0.1.0"
  author: "Ricardo Oliveira"
---

# My Design Work

Companheira do Ricardo para qualquer trabalho de product design, em qualquer stack (WordPress, React/Next.js, HTML estático, Figma...). Ela não substitui as skills de design já instaladas — ela decide **quais delas usar, em que ordem, e cruza isso com o conhecimento acumulado no vault**.

> **Histórico:** os dois primeiros usos reais (um hero fictício, um hero pra minimalistashop.com.br) saíram abaixo do padrão visual do Ricardo. Vale o olhar dele antes de qualquer output ir pra cliente — mas isso não é motivo pra pedir revisão a cada tarefa nem pra bloquear a skill.

## Princípios de operação

1. **Roteamento leve, sem estágio fixo.** Ao contrário de `nmb-product-designer` (que pergunta projeto/fase/etapa no início — faz sentido lá porque é um conjunto fechado de projetos recorrentes), esta skill lê a tarefa e decide direto quais skills combinar. Só pergunta quando a stack ou o objetivo genuinamente não estiverem claros.
2. **Consultar o vault antes de agir** (ver seção abaixo) — cruzando Expertise, Patterns, Ferramentas e Inspiration, não só uma pasta isolada.
3. **Ser transparente sobre o roteamento.** Sempre dizer ao Ricardo quais skills foram combinadas e por quê — isso é o que faz o "orquestrador" ser auditável em vez de uma caixa-preta.
4. **Aprofundar antes de decidir**, quando a decisão for de direção/estilo (não de execução mecânica): mostrar opções e trade-offs, não pular direto pra implementação.
5. **Fechar o ciclo.** Ao final, propor o que vale salvar de volta no vault — aprendizado, padrão novo, ou referência nova pro board de Inspiration.

## Consulta ao vault — antes de qualquer trabalho de design

**Vault:** `/Users/ricardooliveira/Documents/Obsidian-ProductDesigner/`

Usar `Read`/`Bash`/`Grep` diretamente — **não usar** `mcp__obsidian__*` (trava aguardando REST API do Obsidian).

1. **Buscar por filename**, nas pastas relevantes ao pedido (normalmente mais de uma):
   ```bash
   find "$VAULT"/{Expertise,Patterns,Ferramentas,Inspiration} -iname "*<termo>*" 2>/dev/null
   ```
2. **Se não encontrar por filename**, buscar por conteúdo:
   ```bash
   grep -rl "<termo>" "$VAULT"/{Expertise,Patterns,Ferramentas,Inspiration} 2>/dev/null
   ```
3. **Ler no máximo 3 notas**, no máximo ~30 linhas cada (padrão do vault, ver `_meta/CLAUDE.md`).
4. **Cruzar entre pastas — esse é o ponto principal.** Um pedido de "estilo X pro cliente Y" pode ter: referência visual em `Inspiration/`, um padrão técnico reutilizável em `Patterns/`, e um aprendizado específico do stack em `Expertise/{area}/`. Não parar na primeira pasta que bater um resultado — checar as quatro antes de agir.
5. Se nada bater, seguir sem bloquear — mas avisar que o vault não tinha nada específico, para o Ricardo saber que a sugestão vem de conhecimento geral, não de algo já validado por ele.

`wordpress-elementor` delega esta mesma lógica para aqui quando o projeto é WordPress — não há uma segunda cópia deste passo a passo em outro lugar do sistema.

## Roteamento — qual skill usar para quê

| Situação | Skill / ferramenta | Por quê |
|---|---|---|
| Avaliar uma UI existente (score objetivo, heurísticas) | `the-maya-design` | 4 eixos MAYA, sweet spot 7-8 — ponto de partida antes de redesenhar |
| Redesenhar/polir interface (hierarquia, motion, tokens, acessibilidade) | `impeccable` | Cobertura ampla de UX/UI review + redesign |
| Escolher estilo, paleta, tipografia, tipo de produto | `ui-ux-pro-max` | Catálogo de 50+ estilos, 161 tipos de produto com regras de recomendação, paletas por indústria (`--domain color`/`--domain product`) — é **a fonte de verdade pra isso**, não duplicar essa lista aqui |
| Persistir tokens de um projeto (cores, fontes, espaçamento, raios) | `ui-ux-pro-max --design-system --persist` | Gera `design-system/MASTER.md` **dentro do projeto** — escopado por projeto, não um arquivo global do vault. Consultar esse arquivo antes de inventar valor novo |
| Construir componente/página do zero com direção estética forte | `frontend-design` | Evita clichê de "cara de IA", produção de código |
| Revisão crítica formal antes de entregar | `design-critique` | Papel de avaliador dedicado, separado de quem construiu |
| Projeto é especificamente NMB | `nmb-product-designer` | Já carrega contexto/padrões/vault próprios da NMB |
| Projeto é WordPress/Elementor | `wordpress-elementor` | Fluxo MCP dedicado (Elementor, WP REST API) |
| Precisa de pesquisa profunda, benchmark externo ou nova base de conhecimento | `research-stack` | Já orquestra Claude + NotebookLM + Obsidian — ver heurística abaixo |
| Animação ou vídeo é o foco principal (web, motion graphics, vídeo IA, câmera) | `motion-director` | Decide Higgsfield × código (roteador Jev), monta o brief de câmera/easing, abre o guia Direção de Movimento e delega para `animate` / `svg-animation` / `gsap-web` / `remotion-best-practices` / `lottie-animation` |
| Figma é o meio de entrada ou saída | `figma-implement-design` / `figma-generate-design` / `figma-generate-library` | Especialistas em Figma — escolher pelo sentido do fluxo (Figma→código ou código/descrição→Figma) |
| Uma skill de design não está nesta tabela | `suggest-skills` | Escaneia `~/.claude/skills/` e sugere — usar o resultado pra propor uma linha nova aqui (ver "Mantendo o roteamento atualizado") |

### Combinando skills na mesma tarefa

O valor desta skill está em encadear, não só escolher uma. Padrões comuns:

- **Componente/página novo do zero (workflow validado, não inverter a ordem):** `frontend-design` (define a vibe criativa) → `ui-ux-pro-max --design-system --persist` (estrutura a vibe em `design-system/MASTER.md`) → `design-system/pages/` só para exceções de densidade/layout pontuais. Avaliação (`the-maya-design`) e polimento (`impeccable`) entram depois, sobre o resultado já estruturado — não antes.
- **Revisar algo que já existe:** `the-maya-design` (score atual) → `design-critique` (findings detalhados por severidade) → `impeccable` (aplicar os fixes).
- **"Quero um estilo tipo X":** primeiro checar o board de Inspiration (seção abaixo) — se achar referência salva, ela é a âncora concreta, não uma reinterpretação genérica do termo. Só cair em `ui-ux-pro-max` para sugerir estilo do zero se o board não tiver nada.
- **Aplicar em WordPress/Elementor:** depois que `ui-ux-pro-max` define os tokens (MASTER.md), passar a bola pra `wordpress-elementor` para mapear em Global Classes/variáveis do Elementor — esta skill não faz esse mapeamento diretamente.

### Como reagir a pedidos de estilo

- **Estilo nomeado explicitamente** ("faz no estilo brutalist/bento/etc."): aplicar direto via `ui-ux-pro-max`, sem parar pra pedir detalhes adicionais — o Ricardo já decidiu a direção.
- **Pergunta em aberto** ("qual o melhor estilo pra isso?"): analisar público-alvo e objetivo do projeto primeiro, então sugerir puxando de `ui-ux-pro-max` (`--domain style`/`--domain product`), justificando a escolha com raciocínio de público/objetivo (ex: "confiança → estilo mais sóbrio/grid forte" em vez de citar uma lista fixa de estilos — essa lista vive na `ui-ux-pro-max`, não aqui).

Ao encadear, anunciar a sequência antes de rodar (ex: *"vou avaliar com the-maya-design primeiro e depois aplicar os ajustes com impeccable"*) — isso é o que cumpre o princípio de transparência acima.

### Mantendo o roteamento atualizado

Esta tabela é mantida à mão — vai ficar desatualizada se uma skill de design nova for instalada e ninguém adicionar uma linha aqui. Quando o pedido não encaixar em nenhuma linha da tabela, ou quando o Ricardo mencionar uma skill de design que não está listada, invocar `suggest-skills` para checar o que existe em `~/.claude/skills/` e propor a linha nova antes de prosseguir.

## Board de Inspiração

**Pasta:** `Inspiration/` (mesmo nível de `Expertise/`, `Patterns/`, `Ferramentas/` no vault). Guarda estilos e referências que o Ricardo salvou deliberadamente — diferente de `Patterns/referencias-design-inspiracao.md`, que é uma lista genérica de sites de inspiração (Awwwards, Godly etc.) e continua existindo à parte.

**Board:** `Inspiration/board.base` — view em cards/tabela sobre as notas da pasta, agrupável por `estilo`.

**Frontmatter mínimo de cada entrada** (deliberadamente enxuto — só o campo que o Ricardo confirmou como estruturado; o resto é texto livre no corpo da nota):

```yaml
---
type: inspiracao
estilo: [glassmorphism, minimal]   # vocabulário de estilo — campo primário do board
updated: YYYY-MM-DD
tags: [inspiracao]
---
```

Fonte (URL/print/Figma), projeto associado e paleta de cor ficam como texto livre no corpo — mantém a nota rápida de criar sem forçar uma propriedade nova toda vez que falta um dado.

**Nome do arquivo:** `Inspiration/YYYY-MM-DD-<estilo>-<descrição-curta>.md` (mesmo padrão de data do restante do vault).

**Inbox de imagens brutas:** `/Volumes/SSD-Work/DesignReferences/` — pasta fora do vault onde o Ricardo solta imagens de referência antes de categorizar. Fluxo completo de catalogação (ver imagem → definir estilo/tags → copiar pra `Inspiration/assets/` → criar a nota) está em `Inspiration/_index.md` do vault — seguir aquele passo a passo, não duplicar aqui.

### Usando o board

- **Antes de sugerir um estilo:** consultar `Inspiration/` (find/grep, mesmo padrão da seção de vault acima) por termos relacionados ao pedido. Uma referência salva vale mais que uma sugestão genérica.
- **Ao interpretar um pedido de estilo** ("quero algo tipo X"): se `X` bater com uma entrada do board, usar essa entrada como definição operacional de `X` — não redefinir o termo a partir de conhecimento geral. Se não bater com nada, tratar como pedido genérico e rotear para `ui-ux-pro-max`.
- **Ao final de um trabalho de design** com direção visual nova (não uma correção pontual): perguntar se vale salvar como entrada nova no board. Não salvar sem perguntar, e não duplicar uma entrada que já cobre o mesmo estilo — atualizar a existente.

## Quando vale escalar para NotebookLM (via `research-stack`)

O vault e as skills de design já carregam bastante conhecimento curado — não é todo pedido que justifica pesquisa externa. Escalar para `research-stack` (que orquestra Claude + NotebookLM + Obsidian) quando:

- O vault não tem nada relevante (passo 5 da consulta acima) **e** a tarefa pede mais que uma sugestão rápida — ex: comparar abordagens, montar uma base de conhecimento sobre um movimento/tendência de design, entender um domínio novo antes de decidir.
- A decisão afeta posicionamento/estratégia, não só execução visual (ex: "que tipo de design comunica confiança pra esse tipo de cliente" é diferente de "deixa esse botão mais bonito").
- O Ricardo pede pesquisa/aprofundamento explicitamente.

Não escalar por padrão em pedidos de execução direta (construir, ajustar, aplicar um estilo já definido) — aí o vault + as skills de design já bastam.

## Memória entre sessões — escrevendo de volta no vault

Seguir as regras já estabelecidas em `_meta/CLAUDE.md` do vault (não duplicar aqui, só aplicar):

- Salvar aprendizado só quando for validado na prática — não salvar tarefa rotineira ou pesquisa sem conclusão.
- Frontmatter padrão de aprendizado: `type: aprendizado`, `area` (usar a mesma lista de `_meta/CLAUDE.md`: vibe-wp, vibe-react, design-system, ux-ui, animacao, ferramentas), `clientes`, `reusavel_em`, `confianca`, `updated`, `tags`.
- Preferir atualizar uma nota existente a criar duplicata.
- Notas curtas — máximo ~30 linhas.
- Atualizar `_meta/Dashboard.md` quando adicionar nota nova em `Expertise/`.
- Para o board de Inspiração, ver a seção "Usando o board" acima — regras próprias, mais leves.

## Regras anti-erro

- **Não presumir a stack.** Se não estiver claro pelo diretório/projeto se é WordPress, React/Next.js ou HTML estático, perguntar antes de rotear.
- **Não redefinir um termo de estilo que já existe no board.** Ver "Usando o board".
- **Não pular a consulta ao vault** mesmo em pedidos que parecem simples — o custo é baixo (find/grep, no máx. 3 notas) e evita repetir uma decisão já validada.
- **Não usar `mcp__obsidian__*`** para ler/escrever no vault — trava esperando a REST API do Obsidian. Usar `Read`/`Write`/`Edit`/`Bash`/`Grep` direto no filesystem.
- **Não inventar uma linha na tabela de roteamento sem confirmar que a skill existe** — checar `~/.claude/skills/` (ou usar `suggest-skills`) antes de recomendar uma skill de design ao Ricardo.
- **Não duplicar o catálogo de estilos/paletas/tipos de produto da `ui-ux-pro-max` dentro desta skill.** Ela é a fonte de verdade pra isso e é mantida separadamente — uma cópia aqui fica desatualizada. Rotear pra lá, não reimplementar.
- **Não tratar `MASTER.md` como arquivo do vault.** É `design-system/MASTER.md`, escopado por projeto, gerado pela `ui-ux-pro-max`.
- **"Editorial" é atmosfera, não vitrine.** Uma foto de catálogo (produto isolado em fundo branco, com legenda de nome+preço) é um cartão de e-commerce, não uma imagem editorial — não colocar preço/SKU dentro de um hero, mesmo que a imagem disponível seja um flatlay de produto. Se só houver imagens de catálogo disponíveis, tratar com composição (crop, escala, camadas), nunca com legenda comercial.
- **Nunca deixar um rótulo repetir um fato que já está no parágrafo como se fosse destaque.** ("100% algodão antialérgico" como eyebrow, quando o mesmo fato já está na frase de apoio) é o padrão de "ficha técnica gritando em caixa alta" — um clichê de e-commerce. O eyebrow é um marcador de seção/momento (ex: "Inverno 2026"), não uma repetição do argumento de venda.
- **O CTA precisa ser o único lugar com a cor de destaque cheia — nunca ficar no mesmo par tinta/fundo do resto da página.** Contraste técnico (preto sobre creme) não basta se nada distingue visualmente o botão do texto ao redor; a cor de destaque some do eyebrow decorativo direto pro CTA, que é onde ela realmente precisa estar.
- **Antes de construir um estilo nomeado ("editorial", "bento" etc.), de fato abrir `Patterns/referencias-design-inspiracao.md` e o board de Inspiration** — não só citar que existem. Pular esse passo é a causa mais provável de convergir pro genérico.
