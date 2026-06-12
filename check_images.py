# -*- coding: utf-8 -*-
import re, os

base = "E:\\decarli-website"
pages = ['index.html','institucional.html','colecoes.html','lazqa.html','porto-alegre.html','passo-fundo.html']

missing = []
found   = 0

img_pattern = re.compile(r'(?:src|background-image|data-lightbox)\s*[=:]\s*["\']([^"\']*assets/images/[^"\']+)["\']')

for page in pages:
    path = os.path.join(base, page)
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    matches = img_pattern.findall(content)
    for m in matches:
        # strip leading ./
        rel = m.lstrip('./')
        full = os.path.join(base, rel.replace('/', os.sep))
        if os.path.exists(full):
            found += 1
        else:
            missing.append((page, m))

print(f"\nIMAGENS OK: {found}")
print(f"IMAGENS NAO ENCONTRADAS: {len(missing)}\n")

if missing:
    cur_page = None
    for page, src in sorted(missing, key=lambda x: x[0]):
        if page != cur_page:
            print(f"\n[{page}]")
            cur_page = page
        print(f"  FALTANDO: {src}")
else:
    print("Tudo certo! Todas as imagens foram encontradas.")
