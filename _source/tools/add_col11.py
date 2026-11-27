import re
p='/home/claude/draft/build.py';s=open(p).read()
i=s.index("\nCOL10_URL = "); j=s.index("\ndef column10():")+5; k=s.index("\ndef ", j)
e=s[i:k].replace('COL10','COL11').replace('def column10','def column11').replace('column-10.html','column-11.html').replace('column-10-hero.jpg','column-11-hero.jpg')
T7='요통을 예방하는 습관 3가지 — 오래 앉지 않기, 바른 자세, 체중 관리'
T="허리 삐끗했는데, 왜 다음 날 더 아플까요? — 허리 '뜨끔' 뒤 처음 며칠은 이렇게 흘러갑니다"
D="허리를 삐끗한 다음 날 더 아픈 이유는 염증 반응 때문입니다. 같은 '뜨끔'이라도 경과가 갈리는 이유, 침 치료 경과 세 가지 길, 처음 며칠 집에서 지내는 법을 정리했습니다."
assert T7 in e; e=e.replace(T7,T); e=e.replace("COL11_TITLE = '"+T+"'", 'COL11_TITLE = "'+T+'"')
d0=e.index("    desc = '"); d1=e.index("\n",d0); e=e[:d0]+'    desc = "'+D+'"'+e[d1:]
R=[('"datePublished": "2026-11-25"','"datePublished": "2026-11-26"'),
('"name": "요통을 예방하는 습관 3가지", "item"','"name": "허리 삐끗했는데, 왜 다음 날 더 아플까요?", "item"'),
('content="2026-11-25"','content="2026-11-26"'),
('<span class="chip">칼럼 · 요통 예방</span>','<span class="chip">칼럼 · 급성 요통</span>'),
('<time datetime="2026-11-25">2026.11.25</time>','<time datetime="2026-11-26">2026.11.26</time>'),
('https://blog.naver.com/jgkorea8275/224490703882','https://blog.naver.com/jgkorea8275/224493215411'),
("      {chk('오래 앉아 있으면 허리 디스크에 어떤 일이 생길까요 (505법칙)')}\n      {chk('바른 앉기·물건 들기·머리 감기 자세와 체중 관리')}\n      {chk('허리가 아플 때 쉬는 법과 통증이 가라앉은 뒤 운동하는 법')}",
 "      {chk('허리를 삐끗한 다음 날 더 아픈 이유')}\n      {chk('같은 뜨끔인데 사람마다 경과가 다른 이유와 침 치료 경과 세 가지')}\n      {chk('처음 며칠 집에서 지내는 법과 바로 진료가 필요한 경우')}"),
('''      <li><a href="column-9.html">칼럼 · 허리디스크, 꼭 수술해야 하나요?{ic("chev")}</a></li>
      <li><a href="column-1.html">칼럼 · 삐끗했는데 왜 이렇게 오래 가죠?{ic("chev")}</a></li>
      <li><a href="essay-3.html">에세이 · 몸은 쉬라고 하는데, 삶은 멈출 수 없을 때{ic("chev")}</a></li>
      <li><a href="index.html#area">허리·목디스크 진료 안내{ic("chev")}</a></li>''',
'''      <li><a href="column-10.html">칼럼 · 요통을 예방하는 습관 3가지{ic("chev")}</a></li>
      <li><a href="column-9.html">칼럼 · 허리디스크, 꼭 수술해야 하나요?{ic("chev")}</a></li>
      <li><a href="column-1.html">칼럼 · 삐끗했는데 왜 이렇게 오래 가죠?{ic("chev")}</a></li>
      <li><a href="index.html#area">허리·목디스크 진료 안내{ic("chev")}</a></li>'''),
]
for a,b in R:
    assert a in e,a[:70]; e=e.replace(a,b)
a=e[e.index("    toc = [("):e.index("    chk = lambda")]
e=e.replace(a,"""    toc = [('s1', '같은 허리 통증이라도 회복되는 과정은 제각각입니다'), ('s2', '왜 다음 날 더 아플까요?'), ('s3', "같은 '뜨끔'인데, 왜 사람마다 경과가 다를까요?"),
           ('s4', '그래서 저는 첫날 이 그림을 보여드립니다'), ('s5', '처음 며칠, 집에서는 이렇게 지내세요'), ('s6', '오늘 꼭 기억하실 3가지')]
""")
b0=e.index('  <div class="prose" data-size="0">\n')+len('  <div class="prose" data-size="0">\n'); b1=e.index('  </div>\n\n  <aside class="ccta"')
e=e[:b0]+open('/home/claude/tools/column11_body.html').read()+e[b1:]
assert '505법칙' not in e
s=s[:k]+e+s[k:]
a="    open(os.path.join(OUT, 'column-10.html'), 'w').write(v2(column10()))"
assert a in s; s=s.replace(a,a+"\n    open(os.path.join(OUT, 'column-11.html'), 'w').write(v2(column11()))")
a='    <div class="col-list">\n'
assert s.count(a)==1
s=s.replace(a,a+'''    <a class="colcard" href="column-11.html">
      <img src="images/column-11-hero.jpg" alt="급성 요통 · 허리 삐끗했는데, 왜 다음 날 더 아플까요?" width="743" height="743" loading="lazy">
      <div class="body">
        <span class="chip">칼럼 · 급성 요통</span>
        <h3>허리 삐끗했는데, 왜 다음 날 더 아플까요? — 허리 '뜨끔' 뒤 처음 며칠은 이렇게 흘러갑니다</h3>
        <p>"원장님, 어제 허리를 삐끗했는데 오늘은 더 아파요." 처음 2~3일이 더 아픈 이유와 침 치료 경과, 처음 며칠 집에서 지내는 법을 정리했습니다.</p>
        <time datetime="2026-11-26">2026.11.26</time>
      </div>
    </a>
''')
a="            ('칼럼', '요통을 예방하는 습관 3가지 — 오래 앉지 않기, 바른 자세, 체중 관리', 'column-10.html', '요통예방'),\n"
assert a in s
s=s.replace(a,a+"            ('칼럼', \"허리 삐끗했는데, 왜 다음 날 더 아플까요? — 허리 '뜨끔' 뒤 처음 며칠\", 'column-11.html', '급성요통'),\n")
a="POSTS = [  # 최신 글이 위로. 새 칼럼·에세이를 올리면 여기에 한 줄 추가\n"
assert a in s
s=s.replace(a,a+"    {'url': 'column-11.html', 'title': "+repr(T)+", 'date': 'Thu, 26 Nov 2026 15:51:00 +0900', 'cat': '칼럼',\n     'desc': "+repr(D)+",\n     'img': 'images/column-11-hero.jpg'},\n")

s=re.sub(r"^VER = '[0-9a-z]+'","VER = '20261127'",s,flags=re.M)
open(p,'w').write(s); print('ok')
