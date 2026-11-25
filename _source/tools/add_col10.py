import re
p='/home/claude/draft/build.py';s=open(p).read()
i=s.index("\nCOL9_URL = "); j=s.index("\ndef column9():")+5; k=s.index("\ndef ", j)
e=s[i:k].replace('COL9','COL10').replace('def column9','def column10').replace('column-9.html','column-10.html').replace('column-9-hero.jpg','column-10-hero.jpg')
T7='허리디스크, 꼭 수술해야 하나요? 치료 기간과 좋아지는 신호'
T='요통을 예방하는 습관 3가지 — 오래 앉지 않기, 바른 자세, 체중 관리'
D='"허리 안 아프려면 뭘 조심해야 하나요?" 오래 앉지 않기(505법칙), 바른 앉기·물건 들기 자세, 체중 관리, 그리고 운동은 안 아플 때. 요통을 예방하는 습관을 정리했습니다.'
assert T7 in e; e=e.replace(T7,T)
d0=e.index("    desc = '"); d1=e.index("\n",d0); e=e[:d0]+f"    desc = '{D}'"+e[d1:]
R=[('"datePublished": "2026-11-23"','"datePublished": "2026-11-25"'),
('"name": "허리디스크, 꼭 수술해야 하나요?", "item"','"name": "요통을 예방하는 습관 3가지", "item"'),
('content="2026-11-23"','content="2026-11-25"'),
('<span class="chip">칼럼 · 허리디스크</span>','<span class="chip">칼럼 · 요통 예방</span>'),
('<time datetime="2026-11-23">2026.11.23</time>','<time datetime="2026-11-25">2026.11.25</time>'),
('https://blog.naver.com/jgkorea8275/224488736563','https://blog.naver.com/jgkorea8275/224490703882'),
("      {chk('허리디스크, 수술이 필요한 경우와 아닌 경우')}\n      {chk('양방 치료와 한방 치료, 침치료는 어떻게 도움이 될까요')}\n      {chk('치료 기간과 좋아지는 신호, 디스크 위치별 저린 곳')}",
 "      {chk('오래 앉아 있으면 허리 디스크에 어떤 일이 생길까요 (505법칙)')}\n      {chk('바른 앉기·물건 들기·머리 감기 자세와 체중 관리')}\n      {chk('허리가 아플 때 쉬는 법과 통증이 가라앉은 뒤 운동하는 법')}"),
('''      <li><a href="column-6.html">칼럼 · 침 치료 원리, 과학적으로 쉽게 설명드립니다{ic("chev")}</a></li>
      <li><a href="column-5.html">칼럼 · 자고 일어났더니 목이 안 돌아가요{ic("chev")}</a></li>
      <li><a href="essay-4.html">에세이 · 불은 그대로인데 사이렌만 끄고 있지는 않습니까?{ic("chev")}</a></li>
      <li><a href="index.html#area">허리·목디스크 진료 안내{ic("chev")}</a></li>''',
'''      <li><a href="column-9.html">칼럼 · 허리디스크, 꼭 수술해야 하나요?{ic("chev")}</a></li>
      <li><a href="column-1.html">칼럼 · 삐끗했는데 왜 이렇게 오래 가죠?{ic("chev")}</a></li>
      <li><a href="essay-3.html">에세이 · 몸은 쉬라고 하는데, 삶은 멈출 수 없을 때{ic("chev")}</a></li>
      <li><a href="index.html#area">허리·목디스크 진료 안내{ic("chev")}</a></li>'''),
]
for a,b in R:
    assert a in e,a[:70]; e=e.replace(a,b)
a=e[e.index("    toc = [("):e.index("    chk = lambda")]
e=e.replace(a,"""    toc = [('s1', '오래 앉아 있지 마세요'), ('s2', '일상생활 자세, 이렇게 바꿔 주세요'), ('s3', '체중 관리, 허리의 짐을 가볍게 해 주세요'),
           ('s4', "허리 운동은 '안 아플 때' 하는 것입니다"), ('s5', '오늘 꼭 기억하실 3가지 습관 + 하나 더')]
""")
b0=e.index('  <div class="prose" data-size="0">\n')+len('  <div class="prose" data-size="0">\n'); b1=e.index('  </div>\n\n  <aside class="ccta"')
e=e[:b0]+open('/home/claude/tools/column10_body.html').read()+e[b1:]
assert '마미증후군' not in e
s=s[:k]+e+s[k:]
a="    open(os.path.join(OUT, 'column-9.html'), 'w').write(v2(column9()))"
assert a in s; s=s.replace(a,a+"\n    open(os.path.join(OUT, 'column-10.html'), 'w').write(v2(column10()))")
a='    <div class="col-list">\n'
assert s.count(a)==1
s=s.replace(a,a+'''    <a class="colcard" href="column-10.html">
      <img src="images/column-10-hero.jpg" alt="요통 예방 · 요통을 예방하는 습관 3가지" width="743" height="743" loading="lazy">
      <div class="body">
        <span class="chip">칼럼 · 요통 예방</span>
        <h3>요통을 예방하는 습관 3가지 — 오래 앉지 않기, 바른 자세, 체중 관리</h3>
        <p>"원장님, 허리 안 아프려면 뭘 조심해야 하나요?" 진료실에서 늘 하는 단골 잔소리, 505법칙과 바른 자세, 체중 관리, 운동하는 때를 정리했습니다.</p>
        <time datetime="2026-11-25">2026.11.25</time>
      </div>
    </a>
''')
a="TV_SPINE = [('칼럼', '허리디스크, 꼭 수술해야 하나요? 치료 기간과 좋아지는 신호', 'column-9.html'),\n"
assert a in s
s=s.replace(a,a+"            ('칼럼', '요통을 예방하는 습관 3가지 — 오래 앉지 않기, 바른 자세, 체중 관리', 'column-10.html'),\n")
a="POSTS = [  # 최신 글이 위로. 새 칼럼·에세이를 올리면 여기에 한 줄 추가\n"
assert a in s
s=s.replace(a,a+f"""    {{'url': 'column-10.html', 'title': '{T}', 'date': 'Wed, 25 Nov 2026 01:13:00 +0900', 'cat': '칼럼',
     'desc': '{D}',
     'img': 'images/column-10-hero.jpg'}},
""")
s=re.sub(r"^VER = '[0-9a-z]+'","VER = '20261125'",s,flags=re.M)
open(p,'w').write(s); print('ok')
