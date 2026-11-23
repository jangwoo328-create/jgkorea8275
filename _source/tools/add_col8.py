import re
p='/home/claude/draft/build.py';s=open(p).read()
i=s.index("\nCOL7_URL = "); j=s.index("\ndef column7():")+5; k=s.index("\ndef ", j)
e=s[i:k].replace('COL7','COL8').replace('def column7','def column8').replace('column-7.html','column-8.html').replace('column-7-hero.jpg','column-8-hero.jpg')
T7='얼굴이 떨리고 저릴 때, 걱정해야 할까요? (눈꺼풀 떨림, 안면경련, 구안와사, 뇌졸중 신호)'
T='어깨 힘줄(회전근개) 부분 파열, 수술해야 하나요? 치료방법과 회복기간'
D='회전근개 부분 파열은 수술 없이 좋아지는 경우가 많습니다. 수술이 필요한 경우, 치료 기간, 재활운동·침치료·주사치료, 집에서 하는 단계별 어깨 운동까지 정리했습니다.'
assert T7 in e; e=e.replace(T7,T)
d0=e.index("    desc = '"); d1=e.index("\n",d0); e=e[:d0]+f"    desc = '{D}'"+e[d1:]
R=[('"datePublished": "2026-11-19"','"datePublished": "2026-11-21"'),
('"name": "얼굴이 떨리고 저릴 때, 걱정해야 할까요?", "item"','"name": "어깨 힘줄(회전근개) 부분 파열, 수술해야 하나요?", "item"'),
('content="2026-11-19"','content="2026-11-21"'),
('<span class="chip">칼럼 · 얼굴 떨림·저림</span>','<span class="chip">칼럼 · 회전근개 파열</span>'),
('<time datetime="2026-11-19">2026.11.19</time>','<time datetime="2026-11-21">2026.11.21</time>'),
('https://blog.naver.com/jgkorea8275/224483198255','https://blog.naver.com/jgkorea8275/224486440105'),
("      {chk('걱정하지 않아도 되는 떨림과 진료가 필요한 떨림')}\n      {chk('저리고 아플 때 원인을 알려 주는 단서')}\n      {chk('바로 119를 불러야 하는 뇌졸중 신호')}",
 "      {chk('회전근개 부분 파열, 수술이 필요한 경우와 아닌 경우')}\n      {chk('치료 기간과 재활운동·침치료·주사치료')}\n      {chk('회복 중 피할 동작과 집에서 하는 단계별 어깨 운동')}"),
('''      <li><a href="column-6.html">칼럼 · 침 치료 원리, 과학적으로 쉽게 설명드립니다{ic("chev")}</a></li>
      <li><a href="column-5.html">칼럼 · 자고 일어났더니 목이 안 돌아가요{ic("chev")}</a></li>
      <li><a href="column-4.html">칼럼 · 자다가 종아리에 쥐가 나요{ic("chev")}</a></li>
      <li><a href="index.html#treatment">치료 방법 · 침과 전침{ic("chev")}</a></li>''',
'''      <li><a href="column-3.html">칼럼 · 어깨가 아프면 다 오십견일까요?{ic("chev")}</a></li>
      <li><a href="column-1.html">칼럼 · 삐끗했는데 왜 이렇게 오래 가죠?{ic("chev")}</a></li>
      <li><a href="column-6.html">칼럼 · 침 치료 원리, 과학적으로 쉽게 설명드립니다{ic("chev")}</a></li>
      <li><a href="index.html#area">근육통·관절통 진료 안내{ic("chev")}</a></li>'''),
]
for a,b in R:
    assert a in e,a[:70]; e=e.replace(a,b)
a=e[e.index("    toc = [("):e.index("    chk = lambda")]
e=e.replace(a,"""    toc = [('s1', '회전근개 부분 파열이란'), ('s2', '수술해야 하나요?'), ('s3', '얼마나 치료 받아야 하나요?'), ('s4', '치료는 어떻게 하나요?'),
           ('s5', '회복 중에는 이런 동작을 피하세요'), ('s6', '집에서 하는 어깨 재활운동'), ('s7', '꼭 기억하세요')]
""")
b0=e.index('  <div class="prose" data-size="0">\n')+len('  <div class="prose" data-size="0">\n'); b1=e.index('  </div>\n\n  <aside class="ccta"')
e=e[:b0]+open('/home/claude/tools/column8_body.html').read()+e[b1:]
assert '뇌졸중' not in e
s=s[:k]+e+s[k:]
a="    open(os.path.join(OUT, 'column-7.html'), 'w').write(v2(column7()))"
assert a in s; s=s.replace(a,a+"\n    open(os.path.join(OUT, 'column-8.html'), 'w').write(v2(column8()))")
a='    <div class="col-list">\n'
assert s.count(a)==1
s=s.replace(a,a+'''    <a class="colcard" href="column-8.html">
      <img src="images/column-8-hero.jpg" alt="회전근개 파열 · 어깨 힘줄이 찢어졌대요" width="743" height="743" loading="lazy">
      <div class="body">
        <span class="chip">칼럼 · 회전근개 파열</span>
        <h3>어깨 힘줄(회전근개) 부분 파열, 수술해야 하나요? 치료방법과 회복기간</h3>
        <p>"원장님, 꼭 수술해야 하나요?" 회전근개 부분 파열의 수술 여부와 치료 기간, 재활운동과 침치료, 집에서 하는 단계별 어깨 운동을 정리했습니다.</p>
        <time datetime="2026-11-21">2026.11.21</time>
      </div>
    </a>
''')
a="""              ('4', '어깨가 아프면 다 오십견일까요? (오십견의 특징과 운동법)', 'column-3.html')]
COL_MUSCLE_TOPIC = {'1': '근육·인대·힘줄', '2': '근육통', '3': '야간 다리 경련', '4': '오십견·어깨 통증'}"""
assert a in s
s=s.replace(a,"""              ('4', '어깨가 아프면 다 오십견일까요? (오십견의 특징과 운동법)', 'column-3.html'),
              ('5', '어깨 힘줄(회전근개) 부분 파열, 수술해야 하나요? 치료방법과 회복기간', 'column-8.html')]
COL_MUSCLE_TOPIC = {'1': '근육·인대·힘줄', '2': '근육통', '3': '야간 다리 경련', '4': '오십견·어깨 통증', '5': '회전근개 파열'}""")
a="POSTS = [  # 최신 글이 위로. 새 칼럼·에세이를 올리면 여기에 한 줄 추가\n"
assert a in s
s=s.replace(a,a+f"""    {{'url': 'column-8.html', 'title': '{T}', 'date': 'Sat, 21 Nov 2026 23:22:00 +0900', 'cat': '칼럼',
     'desc': '{D}',
     'img': 'images/column-8-hero.jpg'}},
""")
s=re.sub(r"^VER = '[0-9a-z]+'","VER = '20261123'",s,flags=re.M)
open(p,'w').write(s); print('ok')
