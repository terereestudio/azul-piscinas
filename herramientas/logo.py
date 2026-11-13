#!/usr/bin/env python3
"""Logotipo tipográfico de Remanso Piscinas (marca ficticia de demostración).

Genera dos SVG con el texto convertido en trazos (no dependen de fuentes):
- img/logo-remanso.svg        fondo transparente (header)
- img/logo-remanso-claro.svg  con fondo claro (footer oscuro)
Mantiene la proporción 360 × 198 del espacio de logo de la plantilla.

Uso: python3 logo.py RUTA_FUENTES_TTF
"""
import sys
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen

FONTS = Path(sys.argv[1] if len(sys.argv) > 1 else "/usr/share/fonts/truetype/google-fonts")
OUT = Path(__file__).resolve().parent.parent / "sitio" / "img"
W, H = 360, 198
NAVY, BLUE, BG = "#102a4c", "#1b6aa5", "#f2f9fc"

def text_path(font_file, text, size, tracking=0.0):
    """Devuelve (d, ancho, alto_mayúscula) del texto en unidades de pantalla."""
    font = TTFont(font_file)
    gs, cmap = font.getGlyphSet(), font.getBestCmap()
    upm = font["head"].unitsPerEm
    scale = size / upm
    pen = SVGPathPen(gs)
    x = 0.0
    for ch in text:
        name = cmap[ord(ch)]
        tp = TransformPen(pen, (scale, 0, 0, -scale, x, 0))
        gs[name].draw(tp)
        x += gs[name].width * scale + tracking
    width = x - tracking
    bp = BoundsPen(gs)
    gs[cmap[ord("H")]].draw(bp)
    cap = bp.bounds[3] * scale
    return pen.getCommands(), width, cap

def build(background):
    d1, w1, c1 = text_path(FONTS / "Poppins-Bold.ttf", "Remanso", 68, tracking=-1.8)
    d2, w2, c2 = text_path(FONTS / "Poppins-Medium.ttf", "PISCINAS", 21, tracking=8.2)
    gap = 20
    total = c1 + gap + c2
    top = (H - total) / 2
    x1, y1 = (W - w1) / 2, top + c1
    x2, y2 = (W - w2) / 2, y1 + gap + c2
    bg = f'<rect width="{W}" height="{H}" rx="22" fill="{BG}"/>' if background else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Remanso Piscinas">'
            f'{bg}'
            f'<path fill="{NAVY}" transform="translate({x1:.1f} {y1:.1f})" d="{d1}"/>'
            f'<path fill="{BLUE}" transform="translate({x2:.1f} {y2:.1f})" d="{d2}"/>'
            f'</svg>\n')

OUT.mkdir(parents=True, exist_ok=True)
(OUT / "logo-remanso.svg").write_text(build(False), encoding="utf-8")
(OUT / "logo-remanso-claro.svg").write_text(build(True), encoding="utf-8")
print("logo listo")
