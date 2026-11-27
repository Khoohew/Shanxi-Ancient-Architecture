"""研究檔案解析：找出各點位的小節。供 build_site.py 與 build_dossier_toc.py 使用。"""
import re
HEAD = re.compile(r'^(#{1,6})\s*(.*)$')
IDH = re.compile(r'^(#{2,4})\s*([A-Za-z]{2}-\d{3})[｜\s]*(.*)$')

def site_sections(text):
    """回傳 {小寫編號: (標題名稱, 內文行列表)}；小節止於下一個同級或更高級標題。"""
    lines = text.split('\n'); out = {}; i = 0
    while i < len(lines):
        m = IDH.match(lines[i])
        if m:
            lvl = len(m.group(1)); j = i + 1
            while j < len(lines):
                h = HEAD.match(lines[j])
                if h and len(h.group(1)) <= lvl: break
                j += 1
            body = [l for l in lines[i+1:j] if not l.startswith('<a id=')]
            out[m.group(2).lower()] = (m.group(3).strip(), body)
            i = j
        else:
            i += 1
    return out
