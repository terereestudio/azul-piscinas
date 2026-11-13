#!/usr/bin/env python3
"""Ilustraciones propias de Remanso Piscinas (proyecto conceptual de Tereré Estudio).

Todo se dibuja por código: no hay fotos de terceros ni de clientes.
Salida en WebP calidad 80, sin metadatos, en sitio/img/.
- hero-piscina.webp   1600 × 1000
- modelo-1..6.webp    800 × 420 (casco visto desde arriba, según cada modelo)
- trabajo-1..5.webp   720 × 720
- og-remanso.webp     1200 × 630

Uso: python3 ilustraciones.py
"""
import math, random
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = Path(__file__).resolve().parent.parent / "sitio" / "img"
FONTS = Path("/usr/share/fonts/truetype/google-fonts")
SS = 2  # supersampling para bordes suaves

C = {
    "sky1": (196, 228, 246), "sky2": (238, 248, 252),
    "navy": (16, 42, 76), "blue": (27, 106, 165), "aqua": (63, 176, 217),
    "water1": (88, 196, 232), "water2": (34, 132, 196), "water3": (20, 98, 160),
    "shell": (120, 196, 238), "shell_d": (78, 160, 214), "shell_l": (170, 220, 246), "rim": (232, 244, 251),
    "deck": (236, 229, 214), "deck_l": (246, 241, 230), "deck_line": (220, 210, 190),
    "grass": (146, 196, 120), "grass_d": (112, 170, 96), "tree": (72, 140, 92), "tree_d": (52, 112, 76),
    "wood": (190, 140, 96), "wood_d": (160, 112, 74), "earth": (176, 132, 96), "earth_d": (140, 100, 70),
    "white": (255, 255, 255), "shadow": (0, 0, 0),
}

def canvas(w, h, color=(255, 255, 255)):
    im = Image.new("RGB", (w * SS, h * SS), color)
    return im, ImageDraw.Draw(im, "RGBA")

def s(*v):
    return [x * SS for x in v]

def finish(im, name, w, h, quality=80):
    im = im.resize((w, h), Image.LANCZOS)
    clean = Image.frombytes("RGB", im.size, im.tobytes())  # sin metadatos
    clean.save(OUT / name, "WEBP", quality=quality, method=6)
    return clean

def vgrad(d, box, c1, c2):
    x0, y0, x1, y1 = box
    for y in range(int(y0), int(y1)):
        t = (y - y0) / max(1, (y1 - y0))
        d.line([(x0, y), (x1, y)], fill=tuple(int(a + (b - a) * t) for a, b in zip(c1, c2)))

def blob_tree(d, cx, cy, r, rnd, col=None, dark=None):
    col = col or C["tree"]; dark = dark or C["tree_d"]
    for _ in range(7):
        a = rnd.uniform(0, 2 * math.pi); rr = r * rnd.uniform(.45, .7)
        x, y = cx + math.cos(a) * r * .45, cy + math.sin(a) * r * .35
        d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=dark)
    for _ in range(6):
        a = rnd.uniform(0, 2 * math.pi); rr = r * rnd.uniform(.4, .62)
        x, y = cx + math.cos(a) * r * .38 - r * .08, cy + math.sin(a) * r * .3 - r * .1
        d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=col)

def caustics(d, box, rnd, alpha=60, n=26, width=3):
    x0, y0, x1, y1 = box
    for _ in range(n):
        y = rnd.uniform(y0, y1); amp = rnd.uniform(4, 12) * SS; ph = rnd.uniform(0, 6)
        pts = [(x, y + math.sin(x / (38 * SS) + ph) * amp) for x in range(int(x0), int(x1), 6 * SS)]
        d.line(pts, fill=(255, 255, 255, alpha), width=width * SS)

def pavers(d, box, size, rnd, base=None, line=None):
    base = base or C["deck"]; line = line or C["deck_line"]
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=base)
    y = y0; row = 0
    while y < y1:
        x = x0 - (size // 2 if row % 2 else 0)
        while x < x1:
            v = rnd.randint(-6, 6)
            d.rectangle([x + SS, y + SS, x + size - SS, y + size // 2 - SS], fill=tuple(min(255, c + v) for c in base))
            x += size
        d.line([(x0, y), (x1, y)], fill=line, width=SS)
        y += size // 2; row += 1

# ---------------------------------------------------------------- HERO
def hero():
    W, H = 1600, 1000
    rnd = random.Random(7)
    im, d = canvas(W, H)
    vgrad(d, s(0, 0, W, 430), C["sky1"], C["sky2"])
    # sol
    d.ellipse(s(1250, 70, 1410, 230), fill=(255, 246, 214))
    for r, a in [(130, 40), (170, 22)]:
        d.ellipse(s(1330 - r, 150 - r, 1330 + r, 150 + r), fill=(255, 244, 200, a))
    # árboles del fondo
    for i in range(14):
        x = i * 125 + rnd.randint(-30, 30); r = rnd.randint(70, 120)
        blob_tree(d, x * SS, (400 - r * .2) * SS, r * SS, rnd)
    # pasto y deck
    d.rectangle(s(0, 400, W, H), fill=C["grass"])
    pav = [(260, 470), (1340, 470), (1600, 1000), (0, 1000)]
    d.polygon([(x * SS, y * SS) for x, y in pav], fill=C["deck"])
    for k in range(1, 12):  # juntas en perspectiva
        t = k / 12
        y = 470 + (1000 - 470) * (t ** 1.4)
        xl = 260 + (0 - 260) * ((y - 470) / 530); xr = 1340 + (1600 - 1340) * ((y - 470) / 530)
        d.line(s(xl, y, xr, y), fill=C["deck_line"], width=2 * SS)
    for k in range(-8, 9):
        d.line(s(800 + k * 68, 470, 800 + k * 160, 1000), fill=C["deck_line"], width=2 * SS)
    # piscina en perspectiva
    outer = [(380, 520), (1220, 520), (1420, 930), (180, 930)]
    d.polygon([(x * SS, y * SS) for x, y in outer], fill=C["rim"])
    inner = [(410, 538), (1190, 538), (1380, 905), (220, 905)]
    d.polygon([(x * SS, y * SS) for x, y in inner], fill=C["water2"])
    # agua con degradé: capa clara arriba
    water = Image.new("RGBA", im.size, (0, 0, 0, 0)); wd = ImageDraw.Draw(water)
    for y in range(538, 905):
        t = (y - 538) / 367
        col = tuple(int(a + (b - a) * t) for a, b in zip(C["water3"], C["water1"]))
        wd.line(s(0, y, W, y), fill=col + (255,), width=SS)
    mask = Image.new("L", im.size, 0); ImageDraw.Draw(mask).polygon([(x * SS, y * SS) for x, y in inner], fill=255)
    im.paste(water, (0, 0), mask)
    d = ImageDraw.Draw(im, "RGBA")
    # escalones (lado derecho)
    for k, a in enumerate([70, 50, 30]):
        x_off = 60 + k * 55
        d.polygon(s(1190 - x_off, 538, 1190 - x_off + 55, 538, 1380 - x_off * 1.15 + 63, 905, 1380 - x_off * 1.15, 905), fill=(255, 255, 255, a))
    # brillos
    layer = Image.new("RGBA", im.size, (0, 0, 0, 0)); ld = ImageDraw.Draw(layer)
    caustics(ld, s(220, 560, 1380, 900), rnd, alpha=55, n=30)
    im.paste(layer, (0, 0), Image.composite(layer.split()[3], Image.new("L", im.size, 0), mask))
    d = ImageDraw.Draw(im, "RGBA")
    # salvavidas
    cx, cy = 640, 760
    d.ellipse(s(cx - 70, cy - 36, cx + 70, cy + 36), fill=(0, 0, 0, 40))
    d.ellipse(s(cx - 68, cy - 42, cx + 68, cy + 30), fill=(255, 255, 255))
    for a0 in range(0, 360, 90):
        d.pieslice(s(cx - 68, cy - 42, cx + 68, cy + 30), a0, a0 + 45, fill=(240, 120, 96))
    d.ellipse(s(cx - 34, cy - 22, cx + 34, cy + 10), fill=C["water2"])
    # reposera
    d.polygon(s(90, 640, 330, 600, 350, 640, 110, 690), fill=(0, 0, 0, 35))
    d.polygon(s(80, 610, 300, 572, 318, 600, 98, 642), fill=(255, 255, 255))
    d.polygon(s(80, 610, 40, 520, 64, 512, 108, 600), fill=(250, 250, 250))
    for x in range(110, 300, 26):
        d.line(s(x, 604 - (x - 80) * .17, x + 14, 632 - (x - 80) * .17), fill=C["aqua"], width=6 * SS)
    # sombrilla
    d.line(s(250, 610, 262, 330), fill=(120, 110, 100), width=8 * SS)
    d.pieslice(s(110, 260, 410, 420), 180, 360, fill=C["navy"])
    for k in range(4):
        d.pieslice(s(110, 260, 410, 420), 180 + k * 45, 180 + k * 45 + 22, fill=C["aqua"])
    # maceta con planta
    d.polygon(s(1420, 640, 1500, 640, 1488, 720, 1432, 720), fill=(214, 196, 170))
    for a in range(-70, 80, 22):
        r = math.radians(a - 90)
        d.ellipse(s(1460 + math.cos(r) * 70 - 22, 600 + math.sin(r) * 80 - 12, 1460 + math.cos(r) * 70 + 22, 600 + math.sin(r) * 80 + 12), fill=C["tree"])
    finish(im, "hero-piscina.webp", W, H)

# ---------------------------------------------------------------- MODELOS
MODELOS = {  # n: (largo, ancho, escalera, lado, prof_rel)
    1: (4.5, 2.6, "recta", "der", .45), 2: (5.5, 3.0, "recta", "izq", .55), 3: (6.2, 3.2, "curva", "der", .6),
    4: (7.2, 3.3, "curva", "der", .75), 5: (7.2, 3.3, "recta", "izq", .95), 6: (8.8, 3.4, "recta", "der", .8),
}

def modelo(n):
    L, A, esc, lado, prof = MODELOS[n]
    W, H = 800, 420
    rnd = random.Random(n)
    im, d = canvas(W, H)
    pavers(d, s(0, 0, W, H), 64 * SS, rnd)
    # tamaño del casco: proporción real, entra en el cuadro
    sc = min(700 / L, 330 / A)
    w, h = L * sc, A * sc
    x0, y0 = (W - w) / 2, (H - h) / 2
    x1, y1 = x0 + w, y0 + h
    # sombra
    sh = Image.new("RGBA", im.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle(s(x0 + 10, y0 + 14, x1 + 10, y1 + 18), 18 * SS, fill=(0, 0, 0, 70))
    im.paste(sh.filter(ImageFilter.GaussianBlur(10 * SS)), (0, 0), sh.filter(ImageFilter.GaussianBlur(10 * SS)))
    d = ImageDraw.Draw(im, "RGBA")
    d.rounded_rectangle(s(x0, y0, x1, y1), 16 * SS, fill=C["rim"])
    b = 12  # borde
    ix0, iy0, ix1, iy1 = x0 + b, y0 + b, x1 - b, y1 - b
    wall = 18 + 10 * prof  # paredes más anchas = más profunda
    fx0, fy0, fx1, fy1 = ix0 + wall * .8, iy0 + wall * .6, ix1 - wall, iy1 - wall * 1.1
    # paredes (luz desde arriba a la izquierda)
    d.polygon(s(ix0, iy0, ix1, iy0, fx1, fy0, fx0, fy0), fill=C["shell_d"])          # arriba
    d.polygon(s(ix0, iy0, fx0, fy0, fx0, fy1, ix0, iy1), fill=C["shell_d"])          # izquierda
    d.polygon(s(ix1, iy0, ix1, iy1, fx1, fy1, fx1, fy0), fill=C["shell_l"])          # derecha
    d.polygon(s(ix0, iy1, fx0, fy1, fx1, fy1, ix1, iy1), fill=C["shell_l"])          # abajo
    # piso con degradé hacia el lado hondo
    floor = Image.new("RGBA", im.size, (0, 0, 0, 0)); fd = ImageDraw.Draw(floor)
    for x in range(int(fx0), int(fx1) + 1):
        t = (x - fx0) / (fx1 - fx0)
        t = 1 - t if lado == "izq" else t
        c = tuple(int(a + (b2 - a) * (1 - t) * prof * .6) for a, b2 in zip(C["shell"], C["shell_d"]))
        fd.line(s(x, fy0, x, fy1), fill=c + (255,), width=SS + 1)
    im.paste(floor, (0, 0), floor)
    d = ImageDraw.Draw(im, "RGBA")
    # escalones
    step = max(26, w * .07)
    for k in (2, 1, 0):  # del más interno al del borde, para que no se tapen
        col = (214 - k * 22, 238 - k * 12, 252 - k * 4, 255)  # cada escalón más claro que el piso
        if lado == "der":
            sx1 = ix1 - k * step; sx0 = sx1 - step
        else:
            sx0 = ix0 + k * step; sx1 = sx0 + step
        if esc == "recta":
            d.rectangle(s(sx0, iy0, sx1, iy1), fill=col)
            edge = sx0 if lado == "der" else sx1
            d.line(s(edge, iy0, edge, iy1), fill=C["shell_d"], width=3 * SS)
        else:
            bend = step * 1.3 * (-1 if lado == "der" else 1)
            pts = []
            for i in range(0, 41):
                t = i / 40; yy = iy0 + (iy1 - iy0) * t
                off = math.sin(t * math.pi) * bend
                pts.append((sx0 + off, yy) if lado == "der" else (sx1 + off, yy))
            outer_edge = ix1 if lado == "der" else ix0
            poly = pts + [(outer_edge, iy1), (outer_edge, iy0)]
            d.polygon([(x * SS, y * SS) for x, y in poly], fill=col)
            d.line([(x * SS, y * SS) for x, y in pts], fill=C["shell_d"], width=3 * SS)
    # boquillas
    for k in range(3):
        bx = ix0 + (ix1 - ix0) * (.25 + k * .22)
        d.ellipse(s(bx - 5, iy0 + 4, bx + 5, iy0 + 12), fill=(200, 210, 220))
    # brillo del gelcoat
    d.line(s(fx0 + 30, fy0 + 20, fx0 + (fx1 - fx0) * .35, fy0 + 20), fill=(255, 255, 255, 110), width=6 * SS)
    finish(im, f"modelo-{n}.webp", W, H)

# ---------------------------------------------------------------- OBRAS
def obra_patio():  # piscina terminada con cerco de madera (vista aérea)
    W = H = 720; rnd = random.Random(11)
    im, d = canvas(W, H, C["grass"])
    for _ in range(140):
        x, y = rnd.randint(0, W), rnd.randint(0, H)
        d.line(s(x, y, x + 3, y - 8), fill=C["grass_d"], width=2 * SS)
    d.rectangle(s(0, 0, W, 70), fill=C["wood"])
    for x in range(0, W, 36):
        d.line(s(x, 0, x, 70), fill=C["wood_d"], width=3 * SS)
    pavers(d, s(110, 170, 610, 560), 56 * SS, rnd)
    d.rounded_rectangle(s(150, 210, 570, 520), 18 * SS, fill=C["rim"])
    d.rounded_rectangle(s(164, 224, 556, 506), 14 * SS, fill=C["water2"])
    vgrad(d, s(170, 230, 550, 500), C["water1"], C["water2"])
    for k in range(3):
        d.rectangle(s(500 - k * 22, 230, 522 - k * 22, 500), fill=(255, 255, 255, 50 + k * 15))
    caustics(d, s(170, 240, 490, 495), rnd, alpha=70, n=14)
    blob_tree(d, 640 * SS, 640 * SS, 90 * SS, rnd)
    blob_tree(d, 70 * SS, 150 * SS, 70 * SS, rnd)
    finish(im, "trabajo-1.webp", W, H)

def obra_instalacion():  # casco bajando al pozo
    W = H = 720; rnd = random.Random(12)
    im, d = canvas(W, H)
    vgrad(d, s(0, 0, W, 330), C["sky1"], C["sky2"])
    d.rectangle(s(0, 330, W, H), fill=C["earth"])
    for _ in range(90):
        x, y = rnd.randint(0, W), rnd.randint(340, H)
        d.ellipse(s(x, y, x + 6, y + 4), fill=C["earth_d"])
    d.polygon(s(120, 470, 600, 470, 640, 620, 80, 620), fill=(118, 84, 60))      # pozo
    d.polygon(s(140, 485, 580, 485, 612, 605, 108, 605), fill=(96, 68, 48))
    # grúa
    d.polygon(s(600, 330, 640, 330, 640, 120, 610, 120), fill=(244, 190, 60))
    d.line(s(625, 130, 300, 60), fill=(244, 190, 60), width=16 * SS)
    for t in [.2, .4, .6, .8]:
        x = 625 + (300 - 625) * t; y = 130 + (60 - 130) * t
        d.line(s(x, y - 6, x - 30, y + 2), fill=(214, 160, 40), width=4 * SS)
    d.line(s(300, 60, 300, 200), fill=(70, 70, 70), width=3 * SS)
    d.line(s(300, 200, 180, 290), fill=(70, 70, 70), width=3 * SS)
    d.line(s(300, 200, 470, 300), fill=(70, 70, 70), width=3 * SS)
    # casco inclinado
    shell = [(160, 290), (490, 300), (520, 390), (140, 380)]
    d.polygon([(x * SS, y * SS) for x, y in shell], fill=C["shell_d"])
    d.polygon(s(176, 300, 476, 309, 498, 376, 158, 368), fill=C["shell"])
    d.line(s(160, 290, 490, 300), fill=C["rim"], width=8 * SS)
    for k in range(3):
        d.line(s(440 - k * 22, 306, 462 - k * 22, 374), fill=C["shell_l"], width=5 * SS)
    finish(im, "trabajo-2.webp", W, H)

def obra_equipo():  # bomba y filtro
    W = H = 720; rnd = random.Random(13)
    im, d = canvas(W, H, (226, 232, 238))
    for y in range(0, H, 60):
        d.line(s(0, y, W, y), fill=(212, 219, 226), width=2 * SS)
    d.rectangle(s(0, 560, W, H), fill=(196, 202, 208))
    # filtro
    d.rounded_rectangle(s(110, 220, 300, 560), 90 * SS, fill=C["navy"])
    d.rounded_rectangle(s(130, 240, 190, 520), 30 * SS, fill=(40, 72, 112))
    d.ellipse(s(160, 170, 250, 240), fill=(70, 74, 82))
    d.rectangle(s(195, 140, 215, 180), fill=(90, 94, 102))
    d.ellipse(s(180, 120, 230, 150), fill=(200, 60, 50))
    # bomba
    d.rounded_rectangle(s(380, 420, 600, 540), 26 * SS, fill=(70, 120, 170))
    d.rounded_rectangle(s(560, 430, 660, 530), 20 * SS, fill=(60, 64, 72))
    for y in range(440, 530, 14):
        d.line(s(570, y, 650, y), fill=(84, 88, 96), width=4 * SS)
    d.ellipse(s(330, 410, 430, 510), fill=(90, 150, 200))
    d.ellipse(s(352, 432, 408, 488), fill=(220, 236, 248, 200))
    d.rectangle(s(380, 540, 640, 560), fill=(150, 156, 164))
    # caños
    pipe = (238, 240, 242)
    d.line(s(300, 470, 330, 470), fill=pipe, width=26 * SS)
    d.line(s(205, 220, 205, 90), fill=pipe, width=26 * SS)
    d.line(s(192, 90, 720, 90), fill=pipe, width=26 * SS)
    d.line(s(470, 420, 470, 300), fill=pipe, width=26 * SS)
    d.line(s(458, 300, 720, 300), fill=pipe, width=26 * SS)
    for x in (205, 470):
        d.rectangle(s(x - 18, 300 if x == 470 else 90, x + 18, (300 if x == 470 else 90) + 12), fill=(210, 214, 218))
    finish(im, "trabajo-3.webp", W, H)

def obra_escalera():  # esquina con escalones bajo el agua
    W = H = 720; rnd = random.Random(14)
    im, d = canvas(W, H)
    pavers(d, s(0, 0, W, H), 72 * SS, rnd)
    d.rounded_rectangle(s(120, 120, W + 40, H + 40), 20 * SS, fill=C["rim"])
    d.rounded_rectangle(s(140, 140, W + 40, H + 40), 16 * SS, fill=C["water2"])
    vgrad(d, s(146, 146, W, H), C["water1"], C["water3"])
    for k in range(3):
        r = 300 - k * 80
        d.pieslice(s(140 - r, 140 - r, 140 + r, 140 + r), 0, 90, fill=(255, 255, 255, 40 + k * 22))
        d.arc(s(140 - r, 140 - r, 140 + r, 140 + r), 0, 90, fill=(255, 255, 255, 150), width=4 * SS)
    caustics(d, s(150, 150, W, H), rnd, alpha=55, n=22)
    # toalla
    d.rounded_rectangle(s(20, 300, 100, 520), 10 * SS, fill=(250, 250, 250))
    for y in range(320, 520, 40):
        d.rectangle(s(20, y, 100, y + 16), fill=C["aqua"])
    finish(im, "trabajo-4.webp", W, H)

def obra_jardin():  # terreno grande con árboles (vista aérea)
    W = H = 720; rnd = random.Random(15)
    im, d = canvas(W, H, C["grass"])
    for _ in range(200):
        x, y = rnd.randint(0, W), rnd.randint(0, H)
        d.line(s(x, y, x + 3, y - 8), fill=C["grass_d"], width=2 * SS)
    d.line(s(0, 600, 300, 440, 420, 420), fill=C["deck_l"], width=34 * SS, joint="curve")
    pavers(d, s(300, 250, 660, 520), 48 * SS, rnd)
    d.rounded_rectangle(s(330, 290, 630, 480), 16 * SS, fill=C["rim"])
    d.rounded_rectangle(s(342, 302, 618, 468), 12 * SS, fill=C["water2"])
    vgrad(d, s(348, 308, 612, 462), C["water1"], C["water2"])
    for k in range(3):
        d.rectangle(s(352 + k * 18, 308, 370 + k * 18, 462), fill=(255, 255, 255, 70 - k * 15))
    caustics(d, s(400, 316, 610, 458), rnd, alpha=70, n=10)
    for cx, cy, r in [(110, 110, 110), (300, 80, 80), (560, 100, 95), (120, 380, 85), (660, 640, 90), (80, 640, 70)]:
        blob_tree(d, cx * SS, cy * SS, r * SS, rnd)
    finish(im, "trabajo-5.webp", W, H)

# ---------------------------------------------------------------- OPEN GRAPH
def og():
    hero_img = Image.open(OUT / "hero-piscina.webp").convert("RGB")
    W, H = 1200, 630
    im = hero_img.resize((1200, 750), Image.LANCZOS).crop((0, 80, 1200, 710))
    d = ImageDraw.Draw(im, "RGBA")
    d.rounded_rectangle([60, 60, 600, 260], 24, fill=(242, 249, 252, 235))
    f1 = ImageFont.truetype(str(FONTS / "Poppins-Bold.ttf"), 84)
    f2 = ImageFont.truetype(str(FONTS / "Poppins-Medium.ttf"), 30)
    d.text((100, 78), "Remanso", font=f1, fill=C["navy"])
    d.text((104, 192), "P I S C I N A S   D E   F I B R A", font=f2, fill=C["blue"])
    clean = Image.frombytes("RGB", im.size, im.tobytes())
    clean.save(OUT / "og-remanso.webp", "WEBP", quality=80, method=6)

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    hero()
    for n in MODELOS:
        modelo(n)
    obra_patio(); obra_instalacion(); obra_equipo(); obra_escalera(); obra_jardin()
    og()
    print("ilustraciones listas")
