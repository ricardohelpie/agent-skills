#!/usr/bin/env python3
"""Roteador da motion-director via TypeSafe Jev.

Uso:  python3 route.py "pedido de animação em linguagem natural"
Saída (stdout, JSON): route, confidence, distribution, higgsfield_need, ask_user
Exit 3 = Jev indisponível (sem chave/rede) -> Claude decide pelo próprio julgamento.
"""
import json, os, sys, urllib.request

THRESHOLD = 0.70  # abaixo disso: perguntar ao Ricardo antes de executar

ROUTES = {
    "higgsfield": "Video gerado por IA: filmagem fotorrealista, pessoas, animais, fisica (fumaca, agua, tecido), produto em cena",
    "remotion": "Video por codigo em React: tipografia de marca, dados, legendas, narracao, timing exato, exporta MP4",
    "gsap_css_web": "Animacao dentro de pagina web: entrada de texto, scroll, hover, transicoes de interface",
    "svg": "Animacao vetorial de logo ou icone: tracado se desenhando, morph, caminho",
    "lottie": "Animacao vetorial vinda do After Effects para web ou app",
    "hybrid": "Clipes gerados por IA compostos em codigo com titulos, legendas ou grafismos de marca por cima",
}
HF_NEEDS = {
    "cinematic_control": "Controle fino de camera, lente, luz, genero e pacing",
    "reference_identity": "Manter identidade de pessoa ou produto a partir de imagens de referencia",
    "multi_shot": "Varios planos numa mesma geracao",
    "motion_transfer": "Copiar o movimento de um video de referencia para outro sujeito",
    "edit_existing": "Editar, estender ou trocar objetos num video que ja existe",
    "animate_image": "Animar uma imagem estatica (image-to-video simples)",
}


def main():
    if len(sys.argv) < 2:
        sys.exit("uso: route.py \"pedido\"")
    key = os.environ.get("TYPESAFE_API_KEY")
    if not key:
        print(json.dumps({"error": "JEV_UNAVAILABLE", "reason": "TYPESAFE_API_KEY ausente"}))
        sys.exit(3)
    body = {
        "state": {"request": sys.argv[1]},
        "model": "jev-latest",
        "questions": {
            "route": {"type": "choice", "instructions": "Qual o melhor recurso para produzir `request`?", "criteria": ROUTES},
            "hf_need": {"type": "choice", "instructions": "Supondo que a parte filmada/cinematografica de `request` seja gerada por um modelo de video de IA, qual a necessidade principal dessa geracao?", "criteria": HF_NEEDS},
        },
    }
    req = urllib.request.Request(
        "https://api.typesafe.ai/v1/systemone", data=json.dumps(body).encode(), method="POST",
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            out = json.load(r)
    except Exception as e:  # rede, 401, timeout
        print(json.dumps({"error": "JEV_UNAVAILABLE", "reason": str(e)[:200]}))
        sys.exit(3)
    a, h = out["answers"]["route"], out["answers"]["hf_need"]
    print(json.dumps({
        "route": a["choice"],
        "confidence": round(a["confidence"], 2),
        "distribution": {k: round(v, 2) for k, v in sorted(a.get("probabilities", {}).items(), key=lambda x: -x[1])[:3]},
        "higgsfield_need": h["choice"] if a["choice"] in ("higgsfield", "hybrid") else None,
        "ask_user": a["confidence"] < THRESHOLD,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
