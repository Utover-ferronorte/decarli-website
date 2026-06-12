# -*- coding: utf-8 -*-
import re, os

base = "E:\\decarli-website"
pages = ['index.html','institucional.html','colecoes.html','lazqa.html','porto-alegre.html','passo-fundo.html']

def fix_extensions(content):
    # 1. Dentro de caminhos assets/images/..., troca todas as extensoes por .jpg
    def replace_ext(m):
        path = m.group(0)
        # Substitui extensao por .jpg (case-insensitive)
        return re.sub(r'\.(png|PNG|jpeg|JPEG|JPG|webp|WEBP|avif|AVIF|gif|GIF|bmp|BMP|heic|HEIC)(?=["\'\s]|$)',
                      '.jpg', path)
    content = re.sub(r'assets/images/[^"\')\s]+', replace_ext, content)
    return content

def fix_specific_names(content):
    # calacata-nobile-decolores (1).jpg -> calacata-nobile-decolores.jpg
    content = content.replace('calacata-nobile-decolores (1).jpg', 'calacata-nobile-decolores.jpg')
    # calacata-nobile-decolores (2).jpg -> calacata-nobile-decolores.jpg (remove duplicates)
    content = content.replace('calacata-nobile-decolores (2).jpg', 'calacata-nobile-decolores.jpg')
    # AURORA GOLD.png na colecoes.html (já trocado pela extensao, mas o nome tinha (1) nos mármores)
    # Remover suffix (1) de calacata-ouro também
    content = content.replace('calacata-ouro-decolores (1).jpg', 'calacata-ouro-decolores.jpg')
    return content

total_changes = 0

for page in pages:
    path = os.path.join(base, page)
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()

    updated = fix_extensions(original)
    updated = fix_specific_names(updated)

    if updated != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(updated)
        # count changes
        diff = sum(1 for a, b in zip(original.split('\n'), updated.split('\n')) if a != b)
        print(f"[{page}] {diff} linhas atualizadas")
        total_changes += diff
    else:
        print(f"[{page}] sem alteracoes")

print(f"\nTotal: {total_changes} linhas corrigidas")
