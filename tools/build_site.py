#!/usr/bin/env python3
"""繁簡對照表 tools/t2s_map.json 取自 LibreOffice 字元級轉換表（已排除乾、余、祇等易誤轉字）。
由 data/sites.csv 生成 docs/index.html（給人瀏覽）與 data/sites-simple.csv（精簡表）。
用法：python3 tools/build_site.py"""
import csv, json, re
R = 'https://github.com/Khoohew/Shanxi-Ancient-Architecture/blob/main/'
rows = list(csv.DictReader(open('data/sites.csv', encoding='utf-8')))
CITY_ORDER = ['太原市','大同市','朔州市','忻州市','呂梁市','晉中市','陽泉市','長治市','晉城市','臨汾市','運城市']
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
cities = [c for c in CITY_ORDER if any(s['city'] == c for s in sites)]
with open('data/sites-simple.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['編號','城市','名稱','現存建築年代','文保級別','核實狀態','地圖定位','研究檔案'])
    for s in sites:
        w.writerow([s['id'], s['city'], s['name'], s['era'], s['level'], s['status'], s['map'], s['dossier']])
html = open('tools/site_template.html', encoding='utf-8').read()
m = json.load(open('tools/t2s_map.json', encoding='utf-8'))
html = html.replace('__TK__', ''.join(m)).replace('__TV__', ''.join(m.values()))
html = html.replace('__DATA__', json.dumps({'cities': cities, 'sites': sites}, ensure_ascii=False).replace('</', '<\\/'))
open('docs/index.html', 'w', encoding='utf-8').write(html)
print(len(sites), 'sites', len(cities), 'cities')
