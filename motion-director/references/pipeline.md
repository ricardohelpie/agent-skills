# Pipeline de produção (conceitos extraídos do OpenMontage)

OpenMontage (github.com/calesthio/OpenMontage, AGPLv3) NÃO está instalado — decisão de 2026-10-04: só os conceitos.

## Estágios — usar para vídeos com mais de 1 plano
1. **Pesquisa** — referências (vault Inspiration, cliente, concorrentes)
2. **Proposta** — 1 parágrafo: objetivo, formato, tom, recurso (saída do route.py)
3. **Roteiro** — falas/ações com tempo
4. **Plano de cenas** — shot list (references/briefs.md), função de cada cena: abrir → mostrar → provar → chamar
5. **Assets** — imagens de referência / start frames (generate_image), clipes (generate_video), TTS, trilha
6. **Edição** — ordem, cortes, ritmo (cut on the beat), transições
7. **Composição** — Remotion: títulos, legendas, grafismos de marca sobre os clipes; export

Checkpoint de aprovação do Ricardo depois de 2 (proposta) e de 4 (shot list) — antes de gastar créditos.

## Escolha de provedor (dentro do Higgsfield)
Não fixar modelo por memória. Chamar `models_explore` com `action: "recommend"` e uma query com:
o `higgsfield_need` do route.py + entrada (texto puro / imagem de referência / vídeo) + duração + aspect ratio.
Critérios para desempatar: qualidade de movimento, controle de câmera, consistência de identidade, áudio nativo, custo (testar em 720p/draft, finalizar em 1080p).
Gerações independentes: `generate_video_batch` + `jobs_wait` + um único `show_generation_by_ids`.
