# Briefs de direção

Preencher antes de gerar. Campo vazio = perguntar ao Ricardo ou propor default explícito, nunca inventar em silêncio.

## Vídeo (Higgsfield ou híbrido) — shot list

| # | Duração | Plano | Ângulo | Movimento | Lente/óptica | Ação | Luz | Áudio |
|---|---|---|---|---|---|---|---|---|
| 1 | 4s | medium shot | eye-level | slow push in | 85mm, shallow DoF | … | golden hour | ambience: … |

Cabeçalho do projeto (uma vez):
- **Objetivo / onde publica:** (Reels, site, evento…) → define aspect ratio, fps, duração
- **Gancho (0–3s):**
- **Estilo + cor:** (ex: product commercial, warm palette) — checar board de Inspiration
- **Continuidade:** imagem de referência do personagem/produto? start/end frame?
- **Negativo:** substantivos (text, watermark, extra fingers…)
- **Áudio:** nativo ligado/desligado (trilha vem depois?)

Montagem do prompt (inglês, um movimento por plano):
`[plano + ângulo] of [assunto concreto] [ação] in [cena, hora, clima]. [movimento], [lente]. [luz], [estilo + cor], [tempo]. Audio: … Negative: …`

## Animação em código (Remotion / GSAP / CSS / SVG / Lottie)

| Elemento | Gatilho | De → para | Duração | Easing | Stagger | Repetição |
|---|---|---|---|---|---|---|
| título (palavras) | load | y+12px, opacity 0 → 0, 1 | 500ms | ease-out | 80ms | 1x |

- **Coreografia:** ordem de entrada (ex: título → subtítulo → CTA → imagem)
- **Reduced-motion:** fallback (aparecer sem deslocamento)
- **Tipografia:** escala usada (ratio) e fonte da marca
- **Saída:** página web, MP4 (Remotion/huashu-design), GIF, Lottie JSON
