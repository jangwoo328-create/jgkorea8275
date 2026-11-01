from playwright.sync_api import sync_playwright
svg=open('map_v4.svg').read()
html='<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;background:#fff}svg{display:block}</style></head><body>'+svg+'</body></html>'
with sync_playwright() as p:
    b=p.chromium.launch(); t=b.new_page(viewport={'width':1250,'height':960},device_scale_factor=2)
    t.set_content(html); t.wait_for_timeout(500)
    t.screenshot(path='map_v4.png',clip={'x':0,'y':0,'width':1250,'height':960})
    t2=b.new_page(viewport={'width':350,'height':269}); t2.set_content(html.replace('width="1250" height="960"','width="350" height="269"')); t2.wait_for_timeout(300); t2.screenshot(path='map_v4_small.png')
    b.close()
