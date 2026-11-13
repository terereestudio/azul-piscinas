#!/usr/bin/env python3
"""Genera index.html y páginas internas de Remanso Piscinas.

Proyecto conceptual de Tereré Estudio: marca, datos e imágenes ficticios.
Todos los botones de WhatsApp llevan a Tereré Estudio con el mensaje
"Quiero una página como esta".

Uso: python3 build.py
"""
from urllib.parse import quote
import pathlib

OUT = pathlib.Path(__file__).resolve().parent.parent / "sitio"
MARCA = "Remanso Piscinas"
WA_NUM = ""  # [COMPLETAR: WhatsApp de Tereré Estudio, formato 549XXXXXXXXXX]
WA_TEXTO = "Hola, quiero una página como esta. Vi la demo de Remanso Piscinas."
EMAIL_USER, EMAIL_DOMAIN = "hola", "remanso.example"  # dominio reservado: no existe
GARANTIA = 10  # años (dato de ejemplo)

def wa():
    base = f"https://wa.me/{WA_NUM}" if WA_NUM else "https://wa.me/"
    return f"{base}?text={quote(WA_TEXTO, safe='')}"

WA_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 1.8a8.2 8.2 0 1 1-4.2 15.3l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 0 1 12 3.8z"/>'
           '<path d="M8.6 7.2c.2-.4.4-.4.7-.4h.5c.2 0 .4 0 .6.5l.8 1.9c.1.2.1.4 0 .6l-.4.6c-.1.2-.3.3-.1.6.5.9 1.1 1.6 1.9 2.2.6.5 1.2.8 1.6 1 .3.1.4.1.6-.1l.7-.9c.2-.2.4-.2.6-.1l1.8.9c.3.1.4.2.4.4 0 .3 0 1-.4 1.5-.4.6-1.4 1.1-2.2 1.1-.9 0-2.3-.4-3.9-1.6a11 11 0 0 1-3-3.6c-.6-1.2-.7-2.2-.4-3 .2-.6.5-1 .6-1.1z"/></svg>')

def ico(paths):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{paths}</svg>'

I = {
  "shield": '<path d="M12 3l8 3v6c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
  "factory": '<path d="M3 21V10l5 3V10l5 3V5h4l1 16z"/><path d="M3 21h18"/>',
  "gem": '<path d="M6 3h12l3 6-9 12L3 9z"/><path d="M3 9h18M9 3l3 18 3-18"/>',
  "drop": '<path d="M12 3c4 5 6 8.3 6 11a6 6 0 0 1-12 0c0-2.7 2-6 6-11z"/>',
  "gear": '<circle cx="12" cy="12" r="3.2"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/>',
  "chat": '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9.5h8M8 12.5h5"/>',
  "tools": '<path d="M14.5 5.5a4 4 0 0 0 4.9 4.9L21 12l-9 9-3-3 9-9"/><path d="M3 6l3-3 4 4-3 3z"/>',
  "digger": '<path d="M3 18h11v3H3z"/><path d="M5 18v-5h6l2 5"/><path d="M11 13l4-7 5 3-2 4h-3"/>',
  "tiles": '<rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="8" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/><rect x="13" y="13" width="8" height="8" rx="1"/>',
  "pool": '<path d="M7 17V5a2 2 0 0 1 4 0M13 17V5a2 2 0 0 1 4 0M7 9h6M7 13h6"/><path d="M3 20c1.5 0 1.5-1 3-1s1.5 1 3 1 1.5-1 3-1 1.5 1 3 1 1.5-1 3-1 1.5 1 3 1"/>',
  "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
  "photo": '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M21 16l-5-5-9 8"/>',
  "swipe": '<path d="M4 12h15M15 8l4 4-4 4"/>',
  "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
}

# Modelos de ejemplo: n, largo, ancho, profundidad, escalera, lado, frase
MODELS = [
  (1, 4.50, 2.60, "1,10 m", "Recta", "der", "La más compacta. Entra en patios chicos y el agua se templa rápido."),
  (2, 5.50, 3.00, "1,10 a 1,40 m", "Recta", "izq", "Para empezar en familia, con sector bajo para los chicos."),
  (3, 6.20, 3.20, "1,20 a 1,45 m", "Curva", "der", "Escalera curva para entrar despacio y sentarse al sol."),
  (4, 7.20, 3.30, "1,20 a 1,60 m", "Curva", "der", "Lugar para nadar y para una tarde con amigos."),
  (5, 7.20, 3.30, "1,40 a 1,65 m", "Recta", "izq", "La más profunda de la línea, para los que se tiran de cabeza."),
  (6, 8.80, 3.40, "1,20 a 1,65 m", "Recta", "der", "La más grande, para reuniones largas de verano."),
]

def num(x):
    return f"{x:.2f}".replace(".", ",")

def plan_svg(n, L, A, esc, lado):
    """Plano en planta dibujado a escala común: 10 unidades = 1 metro."""
    s = 10
    x0, y0 = 2, 2
    w, h = L * s, A * s
    parts = [f'<rect class="plan-pool" x="{x0}" y="{y0 + (34 - h)/2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="1.6"/>']
    top = y0 + (34 - h) / 2
    bot = top + h
    for k in range(1, 4):
        off = k * 3.6
        x = x0 + w - off if lado == "der" else x0 + off
        if esc == "Recta":
            parts.append(f'<line class="plan-step" x1="{x:.1f}" y1="{top + .8:.1f}" x2="{x:.1f}" y2="{bot - .8:.1f}"/>')
        else:
            bend = -3 if lado == "der" else 3
            parts.append(f'<path class="plan-step" d="M{x:.1f} {top + .8:.1f} Q{x + bend:.1f} {(top + bot)/2:.1f} {x:.1f} {bot - .8:.1f}"/>')
    ry = 40  # regla 0 a 9 m
    parts.append(f'<line class="plan-ruler" x1="{x0}" y1="{ry}" x2="{x0 + 90}" y2="{ry}"/>')
    for m in range(0, 10):
        x = x0 + m * s
        tick = 2 if m % 2 == 0 else 1.2
        parts.append(f'<line class="plan-ruler" x1="{x}" y1="{ry - tick}" x2="{x}" y2="{ry}"/>')
        if m % 2 == 0:
            parts.append(f'<text class="plan-label" x="{x}" y="{ry + 4}" text-anchor="middle">{m}</text>')
    parts.append(f'<text class="plan-label" x="{x0 + 90}" y="{ry + 4}" text-anchor="end">m</text>')
    title = f"Plano en planta del Modelo {n}: {num(L)} por {num(A)} metros, escalera {esc.lower()}"
    return (f'<svg viewBox="0 0 96 46" role="img" aria-label="{title}">' + "".join(parts) + "</svg>")

def model_card(m):
    n, L, A, prof, esc, lado, claim = m
    return f'''
        <li class="model" id="modelo-{n}">
          <article class="model-card" aria-labelledby="m{n}-t">
            <div class="model-photo">
              <img src="img/modelo-{n}.webp" width="800" height="420" loading="lazy" decoding="async" alt="Ilustración del Modelo {n}: casco de fibra de vidrio visto desde arriba, con escalera {esc.lower()}">
              <span class="model-tag">Modelo {n}</span>
            </div>
            <div class="model-head">
              <h3 class="model-size" id="m{n}-t"><span class="visually-hidden">Modelo {n}: </span>{num(L)} × {num(A)} m</h3>
              <p class="model-claim">{claim}</p>
            </div>
            <div class="model-body">
              <dl class="model-specs">
                <div><dt>Largo</dt><dd>{num(L)} m</dd></div>
                <div><dt>Ancho</dt><dd>{num(A)} m</dd></div>
                <div><dt>Profundidad</dt><dd>{prof}</dd></div>
                <div><dt>Escalera</dt><dd>{esc}</dd></div>
              </dl>
              <figure class="model-plan">
                {plan_svg(n, L, A, esc, lado)}
                <figcaption>Vista desde arriba, a la misma escala que los otros modelos.</figcaption>
              </figure>
            </div>
            <a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener noreferrer"><span class="wa-dot">{WA_ICON}</span>Consultá el Modelo {n}</a>
          </article>
        </li>'''

def head(title, desc, extra=""):
    # noindex: proyecto conceptual, no debe aparecer en Google como negocio real
    return f'''<!doctype html>
<html lang="es-AR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="theme-color" content="#bfe3f4">
<link rel="preload" href="/fonts/poppins-700.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="/css/styles.css">
{extra}</head>'''

FIRMA = '''<div class="firma-te">
  <a href="https://terereestudio.com.ar" rel="noopener">
    <span>Desarrollado por</span>
    <img src="/img/firma-terereestudio.webp" width="360" height="120" alt="Tereré Estudio" loading="lazy" decoding="async">
  </a>
</div>'''

def footer():
    return f'''<footer class="site-footer">
  <div class="wrap">
    <div class="footer-brand">
      <img src="/img/logo-remanso-claro.svg" width="360" height="198" alt="{MARCA}" loading="lazy" decoding="async">
      <p>Fabricamos e instalamos piscinas de fibra de vidrio con {GARANTIA} años de garantía.</p>
    </div>
    <ul class="footer-links">
      <li><a href="/#modelos">Modelos</a></li>
      <li><a href="/#garantia">Garantía</a></li>
      <li><a href="/#trabajos">Obras</a></li>
      <li><a href="/#contacto">Contacto</a></li>
      <li><a href="/privacidad/">Política de privacidad</a></li>
    </ul>
    <p class="footer-legal">© <span data-year>2026</span> {MARCA}.</p>
    <p class="footer-demo">Proyecto conceptual de Tereré Estudio. Marca y datos ficticios.</p>
  </div>
</footer>'''

def index():
    og = f'''<meta property="og:type" content="website">
<meta property="og:locale" content="es_AR">
<meta property="og:site_name" content="{MARCA}">
<meta property="og:title" content="{MARCA} | Piscinas de fibra de vidrio">
<meta property="og:description" content="Proyecto conceptual de Tereré Estudio: landing para una fábrica de piscinas de fibra con 6 modelos y planos a escala.">
<meta property="og:image" content="/img/og-remanso.webp">
<meta property="og:image:type" content="image/webp">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="/img/hero-piscina.webp" as="image" type="image/webp">
'''
    cards = "".join(model_card(m) for m in MODELS)
    works = [
      ("trabajo-1", "Ilustración de una piscina terminada en un patio con cerco de madera, vista desde arriba"),
      ("trabajo-2", "Ilustración de un casco de fibra bajando con una grúa hacia la excavación"),
      ("trabajo-3", "Ilustración del equipo de filtrado: filtro, bomba y caños"),
      ("trabajo-4", "Ilustración de la escalera curva de una piscina llena, vista desde el borde"),
      ("trabajo-5", "Ilustración de una piscina en un jardín grande con árboles, vista desde arriba"),
    ]
    works_html = "".join(
      f'<li><img src="img/{f}.webp" width="720" height="720" loading="lazy" decoding="async" alt="{alt}"></li>' for f, alt in works)
    return head(
      f"Piscinas de fibra de vidrio | {MARCA}",
      "Proyecto conceptual de Tereré Estudio: landing para una fábrica de piscinas de fibra de vidrio con 6 modelos, planos a escala y presupuesto por WhatsApp.",
      og) + f'''
<body>
<a class="skip-link" href="#contenido">Saltar al contenido</a>

<!-- ============ HEADER ============ -->
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="#inicio" aria-label="{MARCA}, ir al inicio">
      <img src="img/logo-remanso.svg" width="360" height="198" loading="eager" decoding="async" alt="{MARCA}">
    </a>
    <nav class="nav" aria-label="Secciones">
      <a href="#modelos">Modelos</a>
      <a href="#garantia">Garantía</a>
      <a href="#servicios">Servicios</a>
      <a href="#trabajos">Obras</a>
      <a href="#contacto">Contacto</a>
    </nav>
    <a class="btn btn-wa header-cta" href="{wa()}" target="_blank" rel="noopener noreferrer"><span class="wa-dot">{WA_ICON}</span>Presupuesto</a>
  </div>
</header>

<main id="contenido">

<!-- ============ HERO ============ -->
<section class="hero" id="inicio" aria-labelledby="hero-title">
  <div class="wrap">
    <div class="hero-copy">
      <span class="hero-kicker">Fábrica de piscinas de fibra de vidrio</span>
      <h1 id="hero-title">¿Ya te estás preparando para <em>el verano</em>?</h1>
      <p class="hero-sub">Fabricamos e instalamos tu piscina de fibra de vidrio, con {GARANTIA} años de garantía. Elegí tu modelo y pedí el presupuesto sin cargo por WhatsApp.</p>
      <div class="hero-actions">
        <a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener noreferrer"><span class="wa-dot">{WA_ICON}</span>Pedí tu presupuesto</a>
        <a class="btn btn-ghost" href="#modelos">Ver los 6 modelos</a>
      </div>
      <ul class="trust" aria-label="Por qué elegirnos">
        <li>{ico(I["check"])}{GARANTIA} años de garantía</li>
        <li>{ico(I["check"])}Fabricación propia</li>
        <li>{ico(I["check"])}Presupuesto sin cargo</li>
      </ul>
    </div>
    <div class="hero-media">
      <img src="img/hero-piscina.webp" width="1600" height="1000" loading="eager" decoding="async" fetchpriority="high" alt="Ilustración de una piscina celeste en un jardín soleado, con reposera, sombrilla y salvavidas">
      <svg class="hero-waves" viewBox="0 0 1200 100" preserveAspectRatio="none" aria-hidden="true">
        <g class="w"><path class="wave-a" d="M0 55 C150 20 300 90 600 55 S1050 20 1200 55 C1350 20 1500 90 1800 55 S2250 20 2400 55 V100 H0Z"/></g>
        <g class="w w2"><path class="wave-b" d="M0 75 C200 45 400 100 600 75 S1000 45 1200 75 C1400 45 1600 100 1800 75 S2200 45 2400 75 V100 H0Z"/></g>
      </svg>
      <div class="hero-badge">{ico(I["shield"])}<strong>{GARANTIA}</strong><span>años de<br>garantía</span></div>
    </div>
  </div>
</section>

<!-- ============ MODELOS ============ -->
<svg class="wave-divider" viewBox="0 0 1200 48" preserveAspectRatio="none" aria-hidden="true"><path d="M0 30 C200 0 400 48 600 26 S1000 6 1200 30 V48 H0Z"/></svg>
<section class="section models" id="modelos" aria-labelledby="modelos-title">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Nuestros modelos</span>
      <h2 class="section-title" id="modelos-title">Elegí el tamaño de tu verano</h2>
      <p class="lead">Seis piscinas de fibra de vidrio, de 4,50 a 8,80 metros. Los planos están a la misma escala, así comparás de un vistazo cuál entra en tu patio.</p>
    </div>
    <p class="models-hint">{ico(I["swipe"])}Deslizá para ver los 6 modelos</p>
    <ul class="model-list">{cards}
    </ul>
    <div class="models-more">
      <p>¿No sabés cuál te conviene o buscás otra medida? Contanos el espacio que tenés y te asesoramos.</p>
      <a class="btn btn-ghost" href="{wa()}" target="_blank" rel="noopener noreferrer">Consultá otras medidas</a>
    </div>
  </div>
</section>

<!-- ============ GARANTÍA / DIFERENCIALES ============ -->
<section class="section warranty" id="garantia" aria-labelledby="garantia-title">
  <div class="wrap">
    <svg class="shield" viewBox="0 0 160 184" role="img" aria-label="{GARANTIA} años de garantía">
      <path class="s-out" d="M80 6 L150 30 V88 C150 132 120 164 80 178 C40 164 10 132 10 88 V30 Z"/>
      <text class="s-num" x="80" y="98" text-anchor="middle">{GARANTIA}</text>
      <text class="s-txt" x="80" y="122" text-anchor="middle">AÑOS DE</text>
      <text class="s-txt" x="80" y="140" text-anchor="middle">GARANTÍA</text>
    </svg>
    <div class="warranty-body">
      <div class="section-head">
        <span class="eyebrow">Hecha para durar</span>
        <h2 class="section-title" id="garantia-title">Una piscina que se disfruta muchos veranos</h2>
        <p class="lead">Cada piscina sale de nuestra planta con {GARANTIA} años de garantía. Si la fabricamos nosotros, respondemos nosotros.</p>
      </div>
      <ul class="perks">
        <li><span class="ico">{ico(I["gem"])}</span><div><h3>Fibra reforzada</h3><p>Capas de fibra de vidrio y terminación con protección UV.</p></div></li>
        <li><span class="ico">{ico(I["drop"])}</span><div><h3>Superficie lisa</h3><p>Cuesta que se peguen las algas y se limpia en minutos.</p></div></li>
        <li><span class="ico">{ico(I["factory"])}</span><div><h3>Hecha en nuestra planta</h3><p>Cada casco pasa un control antes de salir del taller.</p></div></li>
        <li><span class="ico">{ico(I["chat"])}</span><div><h3>Te acompañamos después</h3><p>Te enseñamos a cuidar el agua y volvemos si nos necesitás.</p></div></li>
      </ul>
    </div>
  </div>
</section>

<!-- ============ SERVICIOS ============ -->
<section class="section services" id="servicios" aria-labelledby="servicios-title">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Todo en un solo lugar</span>
      <h2 class="section-title" id="servicios-title">De la excavación al primer chapuzón</h2>
      <p class="lead">Nos encargamos de cada etapa, para que no tengas que coordinar con nadie más.</p>
    </div>
    <ul class="services-grid">
      <li class="service">{ico(I["factory"])}<h3>Fabricación</h3><p>Cascos de fibra hechos en nuestros moldes.</p></li>
      <li class="service">{ico(I["pool"])}<h3>Instalación</h3><p>Dejamos la piscina nivelada y lista para llenar.</p></li>
      <li class="service">{ico(I["digger"])}<h3>Excavación</h3><p>Hacemos el pozo y preparamos la base.</p></li>
      <li class="service">{ico(I["tiles"])}<h3>Solados y bordes</h3><p>Piso atérmico alrededor de la piscina.</p></li>
      <li class="service">{ico(I["tools"])}<h3>Puesta a punto</h3><p>Limpieza y revisión antes de cada temporada.</p></li>
      <li class="service">{ico(I["gear"])}<h3>Equipos</h3><p>Bombas, filtros, luces y accesorios.</p></li>
    </ul>
  </div>
</section>

<!-- ============ PROCESO ============ -->
<section class="section process" id="proceso" aria-labelledby="proceso-title">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Cómo trabajamos</span>
      <h2 class="section-title" id="proceso-title">Tu piscina en 4 pasos</h2>
    </div>
    <ol class="steps">
      <li class="step"><div><h3>Elegís el modelo</h3><p>Mirá las medidas y escribinos por WhatsApp con el que te guste.</p></div></li>
      <li class="step"><div><h3>Te pasamos el presupuesto</h3><p>Te asesoramos según tu espacio. El presupuesto es sin cargo.</p></div></li>
      <li class="step"><div><h3>Excavamos e instalamos</h3><p>Hacemos el pozo y colocamos tu piscina.</p></div></li>
      <li class="step"><div><h3>A disfrutar</h3><p>Sumá solados y equipos, y empezá la temporada.</p></div></li>
    </ol>
  </div>
</section>

<!-- ============ OBRAS (galería local, sin embeds) ============ -->
<section class="section works" id="trabajos" aria-labelledby="trabajos-title">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Obras</span>
      <h2 class="section-title" id="trabajos-title">Así quedan nuestras piscinas</h2>
      <p class="lead">De la grúa al primer día de pileta: así es cada instalación.</p>
    </div>
    <ul class="works-grid">{works_html}
      <li class="ig-tile"><a href="{wa()}" target="_blank" rel="noopener noreferrer">{ico(I["photo"])}Pedí más fotos de obras<small>Te las mandamos por WhatsApp</small></a></li>
    </ul>
  </div>
</section>

<!-- ============ PREGUNTAS FRECUENTES ============ -->
<section class="section faq" id="preguntas" aria-labelledby="faq-title">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Preguntas frecuentes</span>
      <h2 class="section-title" id="faq-title">Lo que más nos consultan</h2>
    </div>
    <div class="faq-list">
      <details><summary>¿De qué material son las piscinas?</summary><p>De fibra de vidrio reforzada, hechas en nuestra planta. Resisten el sol, el cloro y el clima, y son fáciles de mantener.</p></details>
      <details><summary>¿Qué garantía tienen?</summary><p>Todas tienen {GARANTIA} años de garantía de fábrica.</p></details>
      <details><summary>¿Ustedes hacen la excavación?</summary><p>Sí. Hacemos el pozo, la base y la instalación completa.</p></details>
      <details><summary>¿Cuánto tarda la instalación?</summary><p>Con la excavación lista, la colocación lleva entre 2 y 3 días.</p></details>
      <details><summary>¿En qué zonas trabajan?</summary><p>Instalamos hasta 80 km de la planta. Para distancias mayores, consultanos.</p></details>
      <details><summary>¿El presupuesto tiene costo?</summary><p>No, es sin cargo. Escribinos por WhatsApp con el modelo que te interesa y tu localidad.</p></details>
    </div>
  </div>
</section>

<!-- ============ CTA FINAL ============ -->
<section class="section cta-final" aria-labelledby="cta-title">
  <div class="wrap">
    <h2 id="cta-title">Que el verano te encuentre adentro del agua</h2>
    <p>Mandanos el modelo que te gustó y te respondemos con el presupuesto. Rápido y sin compromiso.</p>
    <a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener noreferrer"><span class="wa-dot">{WA_ICON}</span>Quiero mi piscina</a>
  </div>
</section>

<!-- ============ CONTACTO ============ -->
<section class="section contact" id="contacto" aria-labelledby="contacto-title">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Contacto</span>
      <h2 class="section-title" id="contacto-title">Estamos para asesorarte</h2>
      <p class="lead">Atención directa y respuesta rápida. Elegí el canal que te quede más cómodo.</p>
    </div>
    <div class="grid">
      <div>
        <ul class="channels">
          <li><a class="channel" href="{wa()}" target="_blank" rel="noopener noreferrer"><span class="ico wa">{WA_ICON}</span><div><span>WhatsApp</span><strong>Escribinos</strong></div></a></li>
          <li><a class="channel" href="#contacto" data-mail-user="{EMAIL_USER}" data-mail-domain="{EMAIL_DOMAIN}"><span class="ico">{ico(I["mail"])}</span><div><span>Email</span><strong data-mail-label>Usá el formulario o WhatsApp</strong></div></a></li>
        </ul>
        <div class="contact-info">
          <p><strong>Zona:</strong> hasta 80 km de la planta.</p>
          <p><strong>Horarios:</strong> lunes a viernes de 8 a 18 y sábados de 9 a 13.</p>
        </div>
      </div>

      <form class="form" id="form-contacto" name="contacto" method="POST" action="/gracias/" data-netlify="true" netlify-honeypot="bot-field">
        <h3>Pedí tu presupuesto</h3>
        <input type="hidden" name="form-name" value="contacto">
        <p class="hp" aria-hidden="true"><label for="bot-field">No completar</label><input id="bot-field" name="bot-field" tabindex="-1" autocomplete="off"></p>
        <div class="form-row">
          <div class="field"><label for="f-nombre">Nombre</label><input id="f-nombre" name="nombre" type="text" required maxlength="80" autocomplete="name"></div>
          <div class="field"><label for="f-tel">WhatsApp o teléfono</label><input id="f-tel" name="telefono" type="tel" required maxlength="25" pattern="[0-9 +()-]{{8,25}}" autocomplete="tel" inputmode="tel"></div>
        </div>
        <div class="form-row">
          <div class="field"><label for="f-localidad">Localidad</label><input id="f-localidad" name="localidad" type="text" required maxlength="60" autocomplete="address-level2"></div>
          <div class="field"><label for="f-modelo">Modelo que te interesa</label>
            <select id="f-modelo" name="modelo">
              <option value="No sé todavía">No sé todavía</option>
              {"".join(f'<option value="Modelo {m[0]}">Modelo {m[0]} ({num(m[1])} × {num(m[2])} m)</option>' for m in MODELS)}
              <option value="Otra medida">Otra medida</option>
            </select>
          </div>
        </div>
        <div class="field"><label for="f-mensaje">Mensaje (opcional)</label><textarea id="f-mensaje" name="mensaje" maxlength="800"></textarea></div>
        <label class="consent" for="f-consent"><input id="f-consent" name="consentimiento" type="checkbox" value="si" required><span>Acepto que se usen estos datos para responder mi consulta, según la <a href="/privacidad/">Política de privacidad</a>.</span></label>
        <p class="form-msg" role="status" aria-live="polite"></p>
        <button class="btn btn-wa btn-block" type="submit">Enviar consulta</button>
      </form>
    </div>
  </div>
</section>

</main>

<a class="wa-float" href="{wa()}" target="_blank" rel="noopener noreferrer" aria-label="Escribinos por WhatsApp">{WA_ICON}</a>
{footer()}
{FIRMA}
<script src="js/main.js" defer></script>
</body>
</html>
'''

def simple(title, desc, body):
    return head(title, desc) + f'''
<body>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="/" aria-label="{MARCA}, volver al inicio"><img src="/img/logo-remanso.svg" width="360" height="198" loading="eager" decoding="async" fetchpriority="high" alt="{MARCA}"></a>
    <a class="btn btn-wa header-cta" href="{wa()}" target="_blank" rel="noopener noreferrer"><span class="wa-dot">{WA_ICON}</span>WhatsApp</a>
  </div>
</header>
<main class="page-simple"><div class="wrap">
{body}
</div></main>
{footer()}
{FIRMA}
<script src="/js/main.js" defer></script>
</body>
</html>
'''

GRACIAS = f'''<h1>¡Gracias! Recibimos tu consulta</h1>
<p>Te vamos a responder lo antes posible al teléfono que nos dejaste. Si querés adelantar, escribinos por WhatsApp.</p>
<p><a class="btn btn-wa" href="{wa()}" target="_blank" rel="noopener noreferrer"><span class="wa-dot">{WA_ICON}</span>Escribir por WhatsApp</a></p>
<p><a href="/">Volver al inicio</a></p>'''

PRIVACIDAD = f'''<h1>Política de privacidad</h1>
<p>Esta es una política de ejemplo de un proyecto conceptual de Tereré Estudio. {MARCA} es una marca ficticia.</p>
<h2>Responsable de los datos</h2>
<p>En un sitio real acá figuran el nombre o la razón social, el CUIT, el domicilio y un contacto para temas de datos personales del responsable de la base de datos.</p>
<h2>Qué datos pedimos y para qué</h2>
<p>Cuando completás el formulario pedimos nombre, teléfono o WhatsApp, localidad, el modelo que te interesa y un mensaje opcional. Se usan solo para responder la consulta. No se venden ni se ceden a terceros con fines comerciales.</p>
<h2>Dónde se guardan</h2>
<p>El formulario se procesa con Netlify Forms, el servicio de alojamiento del sitio. Si escribís por WhatsApp, la conversación sigue por esa aplicación, que pertenece a Meta Platforms y tiene su propia política de privacidad.</p>
<h2>Cookies y estadísticas</h2>
<p>Este sitio no usa cookies de seguimiento ni herramientas de publicidad. Las fuentes y las imágenes se sirven desde el propio sitio.</p>
<h2>Tus derechos</h2>
<p>Podés pedir el acceso, la rectificación, la actualización o la supresión de tus datos. El titular de los datos personales tiene la facultad de ejercer el derecho de acceso a los mismos en forma gratuita a intervalos no inferiores a seis meses, salvo que se acredite un interés legítimo al efecto, conforme lo establecido en el artículo 14, inciso 3 de la Ley N° 25.326.</p>
<p>La Agencia de Acceso a la Información Pública, en su carácter de Órgano de Control de la Ley N° 25.326, tiene la atribución de atender las denuncias y reclamos que interpongan quienes resulten afectados en sus derechos por incumplimiento de las normas vigentes en materia de protección de datos personales.</p>
<h2>Plazo de conservación</h2>
<p>Los datos se guardan solo el tiempo necesario para responder la consulta y hacer el seguimiento del presupuesto.</p>
<p><a href="/">Volver al inicio</a></p>'''

NOTFOUND = '''<h1>No encontramos esta página</h1>
<p>Puede que el enlace esté mal escrito o que la página ya no exista.</p>
<p><a class="btn btn-ghost" href="/">Ir al inicio</a></p>'''

html = index()
for a, b in [('="/img/', '="img/'), ('="/css/', '="css/'), ('="/fonts/', '="fonts/'), ('="/js/', '="js/'), ('href="/#', 'href="#')]:
    html = html.replace(a, b)
(OUT / "index.html").write_text(html, encoding="utf-8")
(OUT / "gracias/index.html").write_text(simple(f"Gracias | {MARCA}", "Recibimos tu consulta.", GRACIAS), encoding="utf-8")
(OUT / "privacidad/index.html").write_text(simple(f"Política de privacidad | {MARCA}", "Política de privacidad de ejemplo.", PRIVACIDAD), encoding="utf-8")
(OUT / "404.html").write_text(simple(f"Página no encontrada | {MARCA}", "Página no encontrada.", NOTFOUND), encoding="utf-8")
print("ok")
