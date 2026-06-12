# -*- coding: utf-8 -*-
"""Substitui embeds YouTube por <video> local."""
import re

V = {
    'manifesto': 'assets/video/Manifesto.mp4',
    'essencia': 'assets/video/Espaço_Essência/espacoEssencia.mp4',
    'fab_estrutura': 'assets/video/Estrutura_Fábrica/EstruturaFábrica.mp4',
    'fab_fachada': 'assets/video/Estrutura_Fábrica/FaixadaFábrica.mp4',
    'lazqa': 'assets/video/Lazqa/Lazqa.mp4',
    'tour_pf': 'assets/video/PassoFundo/TourLojaPassoFundo.mp4',
    'tour_poa': 'assets/video/PortoAlegre/TourLojaPortoAlegre.mp4',
    'gal_pf1': 'assets/video/GaleriaLoja/galeriaLoja1.mp4',
    'gal_pf2': 'assets/video/GaleriaLoja/galeriaLoja2.mp4',
    'gal_pf3': 'assets/video/GaleriaLoja/galeriaLoja3.mp4',
    'gal_pf4': 'assets/video/GaleriaLoja/galeriaLoja4.mp4',
    'gal_poa1': 'assets/video/PortoAlegre/galeria1.mp4',
    'gal_poa2': 'assets/video/PortoAlegre/galeria2.mp4',
}

PLAY_BTN = (
    '<button type="button" class="video-play-overlay" aria-label="Reproduzir vídeo">'
    '<span class="video-play-btn"><svg width="28" height="28" viewBox="0 0 24 24" fill="white">'
    '<path d="M8 5v14l11-7z"/></svg></span></button>'
)

def video_src(path):
    return f'<source src="{path}" type="video/mp4">'

def banner(path):
    return (
        f'<div class="video-banner" style="height:calc(100vh - var(--nav-h));min-height:520px;">\n'
        f'    <video autoplay muted loop playsinline preload="metadata">\n'
        f'      {video_src(path)}\n'
        f'    </video>\n'
        f'  </div>'
    )

def gallery_card(path, label, title, flex_style):
    return f'''        <div class="video-gallery-wrap" style="{flex_style}">
          <video controls playsinline preload="metadata">
            {video_src(path)}
          </video>
          <div style="position:absolute;bottom:0;left:0;right:0;background:linear-gradient(to top,rgba(0,0,0,0.7),transparent);padding:24px 28px;pointer-events:none;z-index:2;">
            <span style="font-size:0.6rem;letter-spacing:0.2em;text-transform:uppercase;color:var(--gold);">{label}</span>
            <div style="font-family:var(--font-serif);font-size:1.1rem;color:var(--white);margin-top:4px;">{title}</div>
          </div>
        </div>'''

def video_wrap_controls(path, extra_style=''):
    style = f' style="{extra_style}"' if extra_style else ''
    return (
        f'<div class="video-wrap{style}">\n'
        f'      <video controls playsinline preload="metadata">\n'
        f'        {video_src(path)}\n'
        f'      </video>\n'
        f'    </div>'
    )

def video_inline_manifesto(path):
    return (
        f'    <div class="video-wrap reveal" style="max-width:960px;margin:0 auto;">\n'
        f'      <div class="video-inline">\n'
        f'        <video playsinline preload="metadata">\n'
        f'          {video_src(path)}\n'
        f'        </video>\n'
        f'        {PLAY_BTN}\n'
        f'      </div>\n'
        f'    </div>'
    )

FLEX = 'flex:0 0 calc(66.666% - 3px);min-width:0;aspect-ratio:16/9;'

# ── passo-fundo.html ──
with open('passo-fundo.html', 'r', encoding='utf-8') as f:
    pf = f.read()

pf = re.sub(
    r'  <link rel="preconnect" href="https://www\.youtube-nocookie\.com">\n'
    r'  <link rel="preconnect" href="https://www\.youtube\.com">\n',
    '', pf)

pf = re.sub(
    r'<div class="yt-banner-section"[^>]*>[\s\S]*?</div>',
    banner(V['tour_pf']), pf, count=1)

# galeria PF - replace each yt-gallery-wrap block
gal_pf = [
    (V['gal_pf1'], 'Galeria', 'Tour pela Galeria I'),
    (V['gal_pf2'], 'Galeria', 'Tour pela Galeria II'),
    (V['gal_pf3'], 'Galeria', 'Tour pela Galeria III'),
    (V['gal_pf4'], 'Galeria', 'Tour pela Galeria IV'),
]
for i, (path, label, title) in enumerate(gal_pf):
    pf = re.sub(
        r'<div class="yt-gallery-wrap" style="flex:0 0 calc\(66\.666% - 3px\);min-width:0;aspect-ratio:16/9;">[\s\S]*?</div>\s*\n',
        gallery_card(path, label, title, FLEX) + '\n\n',
        pf, count=1)

pf = re.sub(
    r'<div class="yt-section-video yt-cinematic reveal" style="margin-top:80px;">[\s\S]*?</div>',
    video_wrap_controls(V['fab_estrutura'], 'margin-top:80px;') + '\n',
    pf, count=1)

with open('passo-fundo.html', 'w', encoding='utf-8') as f:
    f.write(pf)
print('passo-fundo.html OK')

# ── porto-alegre.html ──
with open('porto-alegre.html', 'r', encoding='utf-8') as f:
    poa = f.read()

poa = re.sub(
    r'  <link rel="preconnect" href="https://www\.youtube-nocookie\.com">\n'
    r'  <link rel="preconnect" href="https://www\.youtube\.com">\n',
    '', poa)

poa = re.sub(
    r'<div class="yt-banner-section"[^>]*>[\s\S]*?</div>',
    banner(V['tour_poa']), poa, count=1)

gal_poa = [
    (V['essencia'], 'Essência', 'Tour pelo Espaço I'),
    (V['gal_poa1'], 'Essência', 'Tour pelo Espaço II'),
    (V['gal_poa2'], 'Essência', 'Tour pelo Espaço III'),
]
for path, label, title in gal_poa:
    poa = re.sub(
        r'<div class="yt-gallery-wrap" style="flex:0 0 calc\(66\.666% - 3px\);min-width:0;aspect-ratio:16/9;">[\s\S]*?</div>\s*\n',
        gallery_card(path, label, title, FLEX) + '\n\n',
        poa, count=1)

with open('porto-alegre.html', 'w', encoding='utf-8') as f:
    f.write(poa)
print('porto-alegre.html OK')

# ── institucional.html ──
with open('institucional.html', 'r', encoding='utf-8') as f:
    inst = f.read()

inst = re.sub(
    r'<div class="yt-inline"[\s\S]*?</div>\s*</div>',
    video_inline_manifesto(V['manifesto']).strip() + '\n',
    inst, count=1)

inst = re.sub(
    r'<div class="yt-section-video yt-cinematic" style="min-height:360px;height:50vh;">[\s\S]*?</div>',
    video_wrap_controls(V['fab_estrutura'], 'min-height:360px;height:50vh;'),
    inst, count=1)

inst = re.sub(
    r'<div class="yt-section-video yt-cinematic" style="min-height:360px;height:50vh;">[\s\S]*?</div>',
    video_wrap_controls(V['fab_fachada'], 'min-height:360px;height:50vh;'),
    inst, count=1)

with open('institucional.html', 'w', encoding='utf-8') as f:
    f.write(inst)
print('institucional.html OK')

# ── lazqa.html ──
with open('lazqa.html', 'r', encoding='utf-8') as f:
    laz = f.read()

laz = re.sub(
    r'  </div>\n  <div class="yt-section-video yt-cinematic reveal">[\s\S]*?</div>\n</section>',
    '  </div>\n  <div class="container">\n' +
    video_wrap_controls(V['lazqa'], 'max-width:960px;margin:0 auto;') +
    '\n  </div>\n</section>',
    laz, count=1)

with open('lazqa.html', 'w', encoding='utf-8') as f:
    f.write(laz)
print('lazqa.html OK')

print('Concluido!')
