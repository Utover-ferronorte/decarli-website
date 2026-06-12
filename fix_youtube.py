# -*- coding: utf-8 -*-
import re

base = "E:\\decarli-website"
pages = ['index.html','institucional.html','colecoes.html','lazqa.html','porto-alegre.html','passo-fundo.html']

# IDs de galeria (usuario pode ver controles, mas sem acesso ao YouTube)
GALLERY_IDS = {
    'uskIX4JZa0g', 'LjgDOnR6VV4',           # galeria POA
    'iwLkVbd0_sE', 'fpGvVVnBU3A',            # galeria PF
    'EGPWukk88eU', 'NcZoDlsT5yM',            # galeria PF
    '389ND4PW2oo',                            # lazqa
}

# IDs de autoplay/background (sem controles, sem info)
AUTOPLAY_IDS = {
    'y2lUm2JAZGw', 'NjmPUo-Kllo',
}

def new_url(vid_id, original_url):
    if vid_id in AUTOPLAY_IDS:
        # Banner de sessao: autoplay, mudo, loop, sem controles, sem info
        return (f"https://www.youtube-nocookie.com/embed/{vid_id}"
                f"?autoplay=1&mute=1&controls=0&modestbranding=1&rel=0"
                f"&showinfo=0&iv_load_policy=3&disablekb=1&playsinline=1"
                f"&fs=0&cc_load_policy=0")
    else:
        # Sessão / galeria: sem controles, sem branding YouTube
        return (f"https://www.youtube-nocookie.com/embed/{vid_id}"
                f"?controls=0&modestbranding=1&rel=0"
                f"&showinfo=0&iv_load_policy=3&disablekb=1"
                f"&playsinline=1&fs=0&cc_load_policy=0")

def replace_yt_urls(content):
    def replacer(m):
        full_url = m.group(1)
        vid_match = re.search(r'/embed/([A-Za-z0-9_-]{11})', full_url)
        if vid_match:
            vid_id = vid_match.group(1)
            return m.group(0).replace(full_url, new_url(vid_id, full_url))
        return m.group(0)
    return re.sub(r'src="(https://www\.youtube(?:-nocookie)?\.com/embed/[^"]+)"', replacer, content)

for page in pages:
    path = f"{base}\\{page}"
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    updated = replace_yt_urls(content)
    if updated != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f"[{page}] URLs atualizadas")
    else:
        print(f"[{page}] sem YouTube embeds")

print("\nConcluido!")
