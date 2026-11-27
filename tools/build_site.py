#!/usr/bin/env python3
"""繁簡對照表 tools/t2s_map.json 取自 LibreOffice 字元級轉換表（已排除乾、余、祇等易誤轉字）。
由 data/sites.csv 生成 docs/index.html（給人瀏覽）與 data/sites-simple.csv（精簡表）。
用法：python3 tools/build_site.py"""
import csv, json, re, os, html as H, sys
sys.path.insert(0, 'tools')
from dossier_lib import site_sections
R = 'https://github.com/Khoohew/Shanxi-Ancient-Architecture/blob/main/'
rows = list(csv.DictReader(open('data/sites.csv', encoding='utf-8')))
CITY_ORDER = ['太原市','大同市','朔州市','忻州市','呂梁市','晉中市','陽泉市','長治市','晉城市','臨汾市','運城市']

RAW = 'https://github.com/Khoohew/Shanxi-Ancient-Architecture/blob/main/'
def inline(t):
    t = H.escape(t, quote=False)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    def lk(m):
        u = m.group(2)
        if not u.startswith('http'):
            u = RAW + os.path.normpath(os.path.join('places', u)).replace(os.sep, '/')
        return f'<a href="{u}" target="_blank" rel="noopener">{m.group(1)}</a>'
    return re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', lk, t)
def md2html(lines):
    out = []; ul = False; tb = False
    for l in lines:
        s = l.rstrip()
        if ul and not re.match(r'\s*[-*] ', s): out.append('</ul>'); ul = False
        if tb and not s.startswith('|'): out.append('</table>'); tb = False
        if not s.strip(): continue
        m = re.match(r'(#{3,6})\s*(.*)', s)
        if m: out.append(f'<h5>{inline(m.group(2))}</h5>'); continue
        if s.startswith('|'):
            cells = [c.strip() for c in s.strip('|').split('|')]
            if all(re.fullmatch(r':?-+:?', c) for c in cells): continue
            if not tb: out.append('<table>'); tb = True
            out.append('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in cells) + '</tr>'); continue
        if s.startswith('>'): out.append(f'<blockquote>{inline(s.lstrip("> "))}</blockquote>'); continue
        m = re.match(r'\s*[-*] (.*)', s)
        if m:
            if not ul: out.append('<ul>'); ul = True
            out.append(f'<li>{inline(m.group(1))}</li>'); continue
        out.append(f'<p>{inline(s)}</p>')
    if ul: out.append('</ul>')
    if tb: out.append('</table>')
    return ''.join(out)
details = {}
_cache = {}
def detail_for(r):
    p = r['dossier_path']
    if not p: return None
    f, _, a = p.partition('#')
    if f not in _cache: _cache[f] = open(f, encoding='utf-8').read()
    t = _cache[f]
    if a:
        sec = site_sections(t).get(a.lower())
        if not sec: return None
        body = sec[1]
    else:  # 單點專題：整份檔案，去掉標題與目錄
        body = [l for l in t.split('\n')[1:]]
    h = md2html(body)
    return h if len(h) > 80 else None
def clean_notes(s):
    s = re.sub(r'\s*詳細資料見[^；。]*[；。]?', ' ', s)
    s = re.sub(r'開放狀態須另行實時覈查。?', '', s)
    s = re.sub(r'本輪資料初核[^。]*。?', '', s)
    return re.sub(r'\s+', ' ', s).strip()
def split_name(n):
    m = re.split(r'\s*-\s*', n, maxsplit=1)
    return m[0].strip(), (m[1].strip() if len(m) > 1 else '')
sites = []
for r in rows:
    name, loc = split_name(r['name'])
    sites.append(dict(id=r['id'], city=r['city'], name=name, loc=loc,
        era=r['construction_period'], found=r['founding_period'], level=r['heritage_level'],
        status=r['dating_status'], conf=r['source_confidence'], note=clean_notes(r['notes']),
        access=r['access_hint'], map=r['google_maps_search_url'],
        dossier=(R + r['dossier_path']) if r['dossier_path'] else ''))
    d = detail_for(r)
    if d:
        sites[-1]['hd'] = 1
        details.setdefault(r['id'].split('-')[0], {})[r['id']] = d
cities = [c for c in CITY_ORDER if any(s['city'] == c for s in sites)]
with open('data/sites-simple.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['編號','城市','名稱','現存建築年代','文保級別','核實狀態','地圖定位','研究檔案'])
    for s in sites:
        w.writerow([s['id'], s['city'], s['name'], s['era'], s['level'], s['status'], s['map'], s['dossier']])
os.makedirs('docs/d', exist_ok=True)
for k, v in details.items():
    json.dump(v, open(f'docs/d/{k}.json', 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
print('details', sum(len(v) for v in details.values()), 'of', len(sites), '; bytes', sum(os.path.getsize(f'docs/d/{k}.json') for k in details))
html = open('tools/site_template.html', encoding='utf-8').read()
m = json.load(open('tools/t2s_map.json', encoding='utf-8'))
html = html.replace('__TK__', ''.join(m)).replace('__TV__', ''.join(m.values()))
html = html.replace('__DATA__', json.dumps({'cities': cities, 'sites': sites}, ensure_ascii=False).replace('</', '<\\/'))
open('docs/index.html', 'w', encoding='utf-8').write(html)
print(len(sites), 'sites', len(cities), 'cities')
