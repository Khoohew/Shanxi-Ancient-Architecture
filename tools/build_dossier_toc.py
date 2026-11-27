#!/usr/bin/env python3
"""為含多個點位的研究檔案：(1) 每個點位標題前加 <a id="xx-nnn"> 錨點（使 CSV 中的 #xx-nnn 連結真正可跳轉）；
(2) 在檔案開頭加「本檔景點目錄」。可重複執行。用法：python3 tools/build_dossier_toc.py"""
import glob, re, sys
sys.path.insert(0, 'tools')
from dossier_lib import IDH, HEAD
S, E = '<!-- toc:start -->', '<!-- toc:end -->'
for p in sorted(glob.glob('places/*.md')):
    if p.endswith('README.md'): continue
    t = open(p, encoding='utf-8').read()
    t = re.sub(r'\n*' + re.escape(S) + r'.*?' + re.escape(E) + r'\n*', '\n\n', t, flags=re.S)
    lines = t.split('\n'); out = []; entries = []
    for i, l in enumerate(lines):
        m = IDH.match(l)
        if m:
            sid = m.group(2).lower()
            entries.append((sid, re.split(r'\s*-\s*', m.group(3).strip(), maxsplit=1)[0] or m.group(2)))
            if not (out and out[-1] == f'<a id="{sid}"></a>'): out.append(f'<a id="{sid}"></a>')
        out.append(l)
    if len(entries) >= 2:
        toc = [S, '<details open><summary><b>本檔景點目錄（%d 處）</b></summary>' % len(entries), '']
        toc += [f'- [{sid.upper()}　{nm}](#{sid})' for sid, nm in entries]
        toc += ['', '</details>', E]
        k = next(i for i, l in enumerate(out) if l.startswith('# '))
        out[k+1:k+1] = [''] + toc
    open(p, 'w', encoding='utf-8').write('\n'.join(out))
    print(p, len(entries))
