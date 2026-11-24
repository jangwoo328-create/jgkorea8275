import re
p='/home/claude/draft/build.py';s=open(p).read()
i=s.index("\nCOL8_URL = "); j=s.index("\ndef column8():")+5; k=s.index("\ndef ", j)
e=s[i:k].replace('COL8','COL9').replace('def column8','def column9').replace('column-8.html','column-9.html').replace('column-8-hero.jpg','column-9-hero.jpg')
T7='어깨 힘줄(회전근개) 부분 파열, 수술해야 하나요? 치료방법과 회복기간'
T='허리디스크, 꼭 수술해야 하나요? 치료 기간과 좋아지는 신호'
D='"디스크가 터졌대요." 허리디스크는 대부분 수술 없이 좋아집니다. 수술이 필요한 경우, 디스크의 자연 흡수, 양·한방 치료와 침치료 연구, 치료 기간과 좋아지는 신호까지 정리했습니다.'
assert T7 in e; e=e.replace(T7,T)
d0=e.index("    desc = '"); d1=e.index("\n",d0); e=e[:d0]+f"    desc = '{D}'"+e[d1:]
R=[('"datePublished": "2026-11-21"','"datePublished": "2026-11-23"'),
('"name": "어깨 힘줄(회전근개) 부분 파열, 수술해야 하나요?", "item"','"name": "허리디스크, 꼭 수술해야 하나요?", "item"'),
('content="2026-11-21"','content="2026-11-23"'),
('<span class="chip">칼럼 · 회전근개 파열</span>','<span class="chip">칼럼 · 허리디스크</span>'),
('<time datetime="2026-11-21">2026.11.21</time>','<time datetime="2026-11-23">2026.11.23</time>'),
('https://blog.naver.com/jgkorea8275/224486440105','https://blog.naver.com/jgkorea8275/224488736563'),
("      {chk('회전근개 부분 파열, 수술이 필요한 경우와 아닌 경우')}\n      {chk('치료 기간과 재활운동·침치료·주사치료')}\n      {chk('회복 중 피할 동작과 집에서 하는 단계별 어깨 운동')}",
 "      {chk('허리디스크, 수술이 필요한 경우와 아닌 경우')}\n      {chk('양방 치료와 한방 치료, 침치료는 어떻게 도움이 될까요')}\n      {chk('치료 기간과 좋아지는 신호, 디스크 위치별 저린 곳')}"),
('''      <li><a href="column-3.html">칼럼 · 어깨가 아프면 다 오십견일까요?{ic("chev")}</a></li>
      <li><a href="column-1.html">칼럼 · 삐끗했는데 왜 이렇게 오래 가죠?{ic("chev")}</a></li>
      <li><a href="column-6.html">칼럼 · 침 치료 원리, 과학적으로 쉽게 설명드립니다{ic("chev")}</a></li>
      <li><a href="index.html#area">근육통·관절통 진료 안내{ic("chev")}</a></li>''',
'''      <li><a href="column-6.html">칼럼 · 침 치료 원리, 과학적으로 쉽게 설명드립니다{ic("chev")}</a></li>
      <li><a href="column-5.html">칼럼 · 자고 일어났더니 목이 안 돌아가요{ic("chev")}</a></li>
      <li><a href="essay-4.html">에세이 · 불은 그대로인데 사이렌만 끄고 있지는 않습니까?{ic("chev")}</a></li>
      <li><a href="index.html#area">허리·목디스크 진료 안내{ic("chev")}</a></li>'''),
]
for a,b in R:
    assert a in e,a[:70]; e=e.replace(a,b)
a=e[e.index("    toc = [("):e.index("    chk = lambda")]
e=e.replace(a,"""    toc = [('s1', '허리디스크란?'), ('s2', '수술해야 하나요?'), ('s3', '양방 치료와 한방 치료'), ('s4', '얼마나 치료하면 낫나요?'),
           ('s5', '디스크 위치에 따라 다리 아픈 곳이 다릅니다'), ('s6', '꼭 기억하세요')]
""")
b0=e.index('  <div class="prose" data-size="0">\n')+len('  <div class="prose" data-size="0">\n'); b1=e.index('  </div>\n\n  <aside class="ccta"')
e=e[:b0]+open('/home/claude/tools/column9_body.html').read()+e[b1:]
assert '회전근개' not in e
s=s[:k]+e+s[k:]
a="    open(os.path.join(OUT, 'column-8.html'), 'w').write(v2(column8()))"
assert a in s; s=s.replace(a,a+"\n    open(os.path.join(OUT, 'column-9.html'), 'w').write(v2(column9()))")
a='    <div class="col-list">\n'
assert s.count(a)==1
s=s.replace(a,a+'''    <a class="colcard" href="column-9.html">
      <img src="images/column-9-hero.jpg" alt="허리디스크 · 허리디스크, 꼭 수술해야 하나요?" width="743" height="743" loading="lazy">
      <div class="body">
        <span class="chip">칼럼 · 허리디스크</span>
        <h3>허리디스크, 꼭 수술해야 하나요? 치료 기간과 좋아지는 신호</h3>
        <p>"원장님, 디스크가 터졌대요." 허리디스크는 대부분 수술 없이 좋아집니다. 수술이 필요한 경우와 치료 기간, 좋아지는 신호를 정리했습니다.</p>
        <time datetime="2026-11-23">2026.11.23</time>
      </div>
    </a>
''')
# 허리·목디스크 카드: 칼럼 + 방송 출연분
a="TV_SPINE = [("
assert a in s
s=s.replace(a,"TV_SPINE = [('칼럼', '허리디스크, 꼭 수술해야 하나요? 치료 기간과 좋아지는 신호', 'column-9.html'),\n            (",1)
a="TV_SPINE_SERIES = '[요통과 허리디스크]'"
assert a in s
s=s.replace(a,a+"\nTV_SPINE_TOPIC = {'칼럼': '건강 칼럼', '1부': TV_SPINE_SERIES, '2부': TV_SPINE_SERIES, '3부': TV_SPINE_SERIES, '4부': TV_SPINE_SERIES, '통합본': TV_SPINE_SERIES}")
a='{tv_sheet("tv-spine", "허리·목디스크", TV_SPINE)}'
assert a in s
s=s.replace(a,'{tv_sheet("tv-spine", "허리·목디스크", TV_SPINE, TV_SPINE_TOPIC, "칼럼 · 방송 출연분", "칼럼은 홈페이지에서, 방송 출연분은 네이버 블로그에서 열립니다.")}')
a="'#tv-spine', '방송 출연분 보기', False),"
assert a in s
s=s.replace(a,"'#tv-spine', '칼럼·방송 출연분 보기', False),")
a="POSTS = [  # 최신 글이 위로. 새 칼럼·에세이를 올리면 여기에 한 줄 추가\n"
assert a in s
s=s.replace(a,a+f"""    {{'url': 'column-9.html', 'title': '{T}', 'date': 'Mon, 23 Nov 2026 18:14:00 +0900', 'cat': '칼럼',
     'desc': '{D}',
     'img': 'images/column-9-hero.jpg'}},
""")
s=re.sub(r"^VER = '[0-9a-z]+'","VER = '20261124'",s,flags=re.M)
open(p,'w').write(s); print('ok')
