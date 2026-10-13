# Regras de motion para interface (código)

Síntese própria, extraída em 2026-10-04 de skills do catálogo ui-skills.com (não instaladas):
12-principles-of-animation e to-spring-or-not-to-spring (raphaelsalaja), fixing-motion-performance (ibelick),
web-animation-design / "Easing Blueprint" (vercel-labs/open-agents), animation-vocabulary (emilkowalski).
Usar ao montar o brief de código e ao revisar uma animação antes de entregar.

## 1. Escolher o mecanismo de tempo
| Tipo de movimento | Usar | Por quê |
|---|---|---|
| Dirigido pelo usuário (arrastar, gesto, pode ser interrompido) | spring | preserva velocidade, sobrevive à interrupção |
| Dirigido pelo sistema (entrar, sair, mudar estado) | easing | início e fim previsíveis |
| Representa tempo (progresso, loading, marquee) | linear | 1:1 entre tempo e progresso |
| Alta frequência (digitar, toggles rápidos, navegação por teclado, menu de contexto) | nenhuma animação | animar só deixa mais lento |

## 2. Easing
- Entrada: ease-out (padrão `cubic-bezier(.16,1,.3,1)`). Saída: ease-in. Elemento já na tela indo de A→B: ease-in-out.
- Hover / troca de cor: `ease` 150ms.
- Linear só para tempo/progresso. Nunca linear em deslocamento de UI.
- Elementos pareados (overlay + modal) usam a mesma curva e duração.

## 3. Duração
- Micro (press, toggle): 100–150ms · UI padrão (tooltip, dropdown): 150–250ms · modal, drawer: 200–300ms.
- Interface de produto: teto de 300ms. Marketing, hero, vídeo: pode passar disso.
- Saída ~20% mais rápida que a entrada. Distância maior e elemento maior = duração maior.
- Se parece lento, encurte a duração antes de mexer na curva.
- Frequência: ação usada 100+ vezes/dia → sem animação; ocasional → padrão; rara/primeira vez → pode encantar.

## 4. Física e encenação
- Escala de entrada parte de 0,85–0,95, nunca de 0. Deformações sutis (squash ≤ ~5%).
- Estado ativo (press): `scale(.97)` imediato.
- Overshoot só com spring/back, não com ease comum.
- Stagger: 30–80ms por item, total da cascata curto (não deixar o último item esperando > ~400ms).
- Um ponto focal por vez; fundo escurece/recua quando um modal entra; hierarquia de z-index coerente.
- Popover/menu cresce a partir do gatilho (transform-origin no botão), não do centro.

## 5. Performance (ordem de custo)
- Composite (barato): `transform`, `opacity` → padrão para movimento.
- Paint (médio): cor, borda, gradiente, máscara, filtro, blur → só em superfícies pequenas ou efeito único.
- Layout (caro): width, height, top/left, margin, grid → evitar contínuo; usar FLIP (medir uma vez, animar com transform).
- Nunca: alternar leitura e escrita de layout no mesmo frame; animar a partir de eventos de scroll/`scrollY` (usar ScrollTrigger, `animation-timeline: view()` ou IntersectionObserver); loop de rAF sem condição de parada; dois sistemas de animação mexendo no mesmo elemento.
- `will-change` só durante a animação, não permanente. Blur grande e animado custa caro: reduzir raio ou área.
- Prefira rebaixar a técnica a remover o movimento.

## 6. Acessibilidade
- Sempre `prefers-reduced-motion`: trocar deslocamento/escala por fade simples (não apenas desligar tudo).
- Nada essencial pode depender só de hover.
- Loop contínuo chamativo: oferecer pausa ou manter sutil.

## Checklist de revisão (antes de entregar)
[ ] mecanismo certo (spring/easing/linear/nenhum) · [ ] curva certa para entrada/saída · [ ] durações dentro da faixa
[ ] só transform/opacity no que se repete · [ ] reduced-motion implementado · [ ] um ponto focal · [ ] origem no gatilho
