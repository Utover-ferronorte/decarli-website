# -*- coding: utf-8 -*-
import re

# YouTube embed helpers
def yt_autoplay(vid_id):
    return (f'<iframe src="https://www.youtube.com/embed/{vid_id}'
            f'?autoplay=1&mute=1&loop=1&playlist={vid_id}&controls=0&playsinline=1&rel=0" '
            f'frameborder="0" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen '
            f'style="position:absolute;inset:0;width:100%;height:100%;border:none;"></iframe>')

def yt_normal(vid_id):
    return (f'<iframe src="https://www.youtube.com/embed/{vid_id}?rel=0" '
            f'frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; '
            f'gyroscope; picture-in-picture" allowfullscreen '
            f'style="position:absolute;inset:0;width:100%;height:100%;border:none;"></iframe>')

# Pattern: remove entire <video ...>...</video> block and replace with iframe
def replace_video(content, src_fragment, iframe_html):
    # Match <video ...> block containing a <source> with src_fragment
    pattern = r'<video[^>]*>[\s\S]*?<source[^>]*' + re.escape(src_fragment) + r'[^>]*>[\s\S]*?</video>'
    new_content = re.sub(pattern, iframe_html, content)
    if new_content == content:
        print(f'  AVISO: nao encontrado -> {src_fragment}')
    else:
        print(f'  OK: substituido -> {src_fragment}')
    return new_content

# ── porto-alegre.html ──────────────────────────────────────────────────────
print('\n[porto-alegre.html]')
with open('porto-alegre.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Banner autoplay
html = replace_video(html, 'tour pela loja de Porto Alegre', yt_autoplay('y2lUm2JAZGw'))
# Galeria carousel 1
html = replace_video(html, 'DJI_0011_stabilized', yt_normal('uskIX4JZa0g'))
# Galeria carousel 2
html = replace_video(html, 'DJI_0012_stabilized', yt_normal('LjgDOnR6VV4'))
# Essencia
html = replace_video(html, 'DJI_0022_stabilized', yt_normal('LvIDNXuePzc'))

with open('porto-alegre.html', 'w', encoding='utf-8') as f:
    f.write(html)

# ── institucional.html ─────────────────────────────────────────────────────
print('\n[institucional.html]')
with open('institucional.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Manifesto
html = replace_video(html, 'Manifesto', yt_normal('6RTAYhjnAoQ'))
# Fabrica POA
html = replace_video(html, 'fabrica - POA', yt_normal('narlgXb0OU8'))
# Fabrica PF
html = replace_video(html, 'PF Atualizado', yt_normal('mNeLFBBvSyI'))

with open('institucional.html', 'w', encoding='utf-8') as f:
    f.write(html)

# ── passo-fundo.html ───────────────────────────────────────────────────────
print('\n[passo-fundo.html]')
with open('passo-fundo.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Banner autoplay
html = replace_video(html, 'tour pela loja de Passo Fundo', yt_autoplay('NjmPUo-Kllo'))
# Galeria carousel
html = replace_video(html, 'DJI_20260417091027_0003', yt_normal('iwLkVbd0_sE'))
html = replace_video(html, 'IMG_2531', yt_normal('NcZoDlsT5yM'))
html = replace_video(html, 'DJI_20260417090922_0002', yt_normal('fpGvVVnBU3A'))
html = replace_video(html, 'DJI_20260417091415_0006', yt_normal('EGPWukk88eU'))
# Fabrica PF
html = replace_video(html, 'PF Atualizado', yt_normal('mNeLFBBvSyI'))

with open('passo-fundo.html', 'w', encoding='utf-8') as f:
    f.write(html)

# ── lazqa.html ─────────────────────────────────────────────────────────────
print('\n[lazqa.html]')
with open('lazqa.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = replace_video(html, 'Lazqa - 4K', yt_normal('389ND4PW2oo'))

with open('lazqa.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('\nConcluido!')
