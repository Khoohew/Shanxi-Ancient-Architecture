#!/usr/bin/env python3
"""由 data/sites.csv 的 dossier_path 生成 places/README.md。用法：python3 tools/build_places_index.py"""
import csv, re, collections
rows = list(csv.DictReader(open('data/sites.csv', encoding='utf-8')))
CITIES = ['太原市','大同市','朔州市','忻州市','呂梁市','晉中市','陽泉市','長治市','晉城市','臨汾市','運城市']
byfile = collections.defaultdict(list)
for r in rows:
    if r['dossier_path']:
        byfile[r['dossier_path'].split('/')[-1].split('#')[0]].append(r)
FEATURED = [  # (組名, [(顯示名, 檔名)])
 ('唐代及早期木構', [('佛光寺東大殿','foguangsi-east-hall.md'),('南禪寺大殿','nanchansi-main-hall.md'),('芮城廣仁王廟','guangrenwang-temple.md')]),
 ('五代、宋、遼金建築', [('平順天台庵','pingshun-tiantai-an.md'),('平順大雲院','pingshun-dayun-temple.md'),('平順龍門寺','pingshun-longmen-temple.md'),('平遙鎮國寺','zhenguo-temple.md'),('高平開化寺','gaoping-kaihua-temple.md'),('太原晉祠','jinci-temple.md'),('大同華嚴寺','huayan-temple.md'),('應縣木塔','yingxian-wooden-pagoda.md'),('渾源懸空寺','xuankong-temple.md'),('朔州崇福寺','chongfu-temple.md')]),
 ('石窟、壁畫及彩塑', [('天龍山石窟','tianlongshan-grottoes.md'),('雲岡石窟','yungang-grottoes.md'),('府城玉皇廟','fucheng-yuhuang-temple.md'),('洪洞廣勝寺','guangsheng-temple.md'),('芮城永樂宮','yongle-palace.md'),('隰縣小西天','xiaoxitian.md'),('平遙雙林寺','shuanglin-temple.md')]),
]
featured_files = {f for _, g in FEATURED for _, f in g}
FCITY = {'foguangsi-east-hall.md':'忻州市','nanchansi-main-hall.md':'忻州市','guangrenwang-temple.md':'運城市',
 'pingshun-tiantai-an.md':'長治市','pingshun-dayun-temple.md':'長治市','pingshun-longmen-temple.md':'長治市','zhenguo-temple.md':'晉中市',
 'gaoping-kaihua-temple.md':'晉城市','jinci-temple.md':'太原市','huayan-temple.md':'大同市','yingxian-wooden-pagoda.md':'朔州市',
 'xuankong-temple.md':'大同市','chongfu-temple.md':'朔州市','tianlongshan-grottoes.md':'太原市','yungang-grottoes.md':'大同市',
 'fucheng-yuhuang-temple.md':'晉城市','guangsheng-temple.md':'臨汾市','yongle-palace.md':'運城市','xiaoxitian.md':'臨汾市','shuanglin-temple.md':'晉中市'}
def rng(rs):
    ids = sorted(r['id'] for r in rs)
    return ids[0] if len(ids) == 1 else f'{ids[0]}—{ids[-1]}'
def key(f):
    m = re.search(r'batch-(\d+)(?:-part-(\d+))?', f)
    return (int(m.group(1)), int(m.group(2) or 0)) if m else (999, 0)
L = ['# 古建研究檔案索引', '',
 '這裡是**逐點的詳細研究**（建築形制、年代爭議、來源），適合想深入讀某一處的人。只想瀏覽、搜尋或在地圖定位，請用[首頁的瀏覽頁面](../README.md)。', '',
 '本頁分兩種找法：', '',
 '- **按城市找** → 第一部分。每個城市列出它的研究檔案。', '- **按著名建築／朝代找** → 第二部分。約 20 處重點建築各有獨立專文。', '',
 '研究檔案內每個點位是一節，標題為「編號｜名稱」（如 `CZ-001`）；編號與 `data/sites.csv` 一致。', '',
 '## 第一部分：按城市找', '']
for c in CITIES:
    fs = sorted([f for f in byfile if any(r['city'] == c for r in byfile[f])], key=key)
    n = sum(1 for r in rows if r['city'] == c)
    L += [f'### {c}（{n} 處）', '']
    batch = [f for f in fs if f not in featured_files]
    for f in batch:
        rs = [r for r in byfile[f] if r['city'] == c]
        L.append(f'- [{rng(rs)}]({f})')
    sp = [(nm, f) for _, g in FEATURED for nm, f in g if FCITY[f] == c]
    if sp: L.append('- 重點專題：' + '、'.join(f'[{nm}]({f})' for nm, f in sp))
    L.append('')
L += ['## 第二部分：按著名建築／朝代找', '']
cityof = {f: byfile[f][0]['city'] for f in byfile}
for g, items in FEATURED:
    L += [f'### {g}', '']
    for nm, f in items:
        L.append(f'- [{nm}]({f})｜{FCITY[f]}')
    L.append('')
L += ['## 檔案維護說明', '',
 '- 每批按原始 CSV 順序研究，保留原始名稱及座標。',
 '- 寺院創建、現存建築、碑刻、造像、壁畫及維修年代分開判斷。',
 '- 來源存在矛盾時保留不同說法，不把推測寫成定論。',
 '- 桌面研究不等於現場踏查；開放狀態、入口及進入權限須另行核查。',
 '- 新增檔案後，於 `data/sites.csv` 填好 `dossier_path`，再執行 `python3 tools/build_places_index.py` 更新本頁。', '']
open('places/README.md', 'w', encoding='utf-8').write('\n'.join(L))
import os
missing = [f for f in os.listdir('places') if f.endswith('.md') and f != 'README.md' and f not in byfile]
print('files not referenced by CSV:', missing)
bad=[f for f in byfile if f in FCITY and any(r['city']!=FCITY[f] for r in byfile[f][:1])]
print('city mismatch:', bad)
