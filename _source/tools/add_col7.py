p='/home/claude/draft/build.py';s=open(p).read()
i=s.index("\nCOL6_URL = "); j=s.index("\ndef column6():")+5; k=s.index("\ndef ", j)
e=s[i:k].replace('COL6','COL7').replace('def column6','def column7').replace('column-6.html','column-7.html').replace('column-6-hero.jpg','column-7-hero.jpg')
T5='침 치료 원리, 과학적으로 쉽게 설명드립니다 (관문조절설, 엔도르핀, 전침)'
T='얼굴이 떨리고 저릴 때, 걱정해야 할까요? (눈꺼풀 떨림, 안면경련, 구안와사, 뇌졸중 신호)'
D='눈꺼풀 떨림부터 반측성 안면경련, 구안와사, 삼차신경통, 대상포진, 뇌졸중 신호까지. 걱정하지 않아도 될 떨림과 바로 119를 불러야 할 신호를 구분해 정리했습니다.'
e=e.replace(T5,T)
d0=e.index("    desc = '"); d1=e.index("\n",d0); e=e[:d0]+f"    desc = '{D}'"+e[d1:]
R=[('"datePublished": "2026-11-17"','"datePublished": "2026-11-19"'),
('"name": "침 치료 원리, 과학적으로 쉽게 설명드립니다", "item"','"name": "얼굴이 떨리고 저릴 때, 걱정해야 할까요?", "item"'),
('content="2026-11-17"','content="2026-11-19"'),
('<span class="chip">칼럼 · 침 치료 원리</span>','<span class="chip">칼럼 · 얼굴 떨림·저림</span>'),
('<time datetime="2026-11-17">2026.11.17</time>','<time datetime="2026-11-19">2026.11.19</time>'),
('https://blog.naver.com/jgkorea8275/224480664949','https://blog.naver.com/jgkorea8275/224483198255'),
("      {chk('경락과 경혈, 현대 과학은 어떻게 보고 있을까요')}\n      {chk('침이 통증을 줄이는 네 가지 원리')}\n      {chk('침은 몸이 스스로 진통제를 만들도록 깨우는 치료')}",
 "      {chk('걱정하지 않아도 되는 떨림과 진료가 필요한 떨림')}\n      {chk('저리고 아플 때 원인을 알려 주는 단서')}\n      {chk('바로 119를 불러야 하는 뇌졸중 신호')}"),
('''      <li><a href="column-2.html">칼럼 · 근육통 회복 속도를 결정하는 네가지 요인{ic("chev")}</a></li>
      <li><a href="column-5.html">칼럼 · 자고 일어났더니 목이 안 돌아가요{ic("chev")}</a></li>
      <li><a href="essay-4.html">에세이 · 불은 그대로인데 사이렌만 끄고 있지는 않습니까?{ic("chev")}</a></li>
      <li><a href="index.html#treatment">치료 방법 · 침과 전침{ic("chev")}</a></li>''',
'''      <li><a href="column-6.html">칼럼 · 침 치료 원리, 과학적으로 쉽게 설명드립니다{ic("chev")}</a></li>
      <li><a href="column-5.html">칼럼 · 자고 일어났더니 목이 안 돌아가요{ic("chev")}</a></li>
      <li><a href="column-4.html">칼럼 · 자다가 종아리에 쥐가 나요{ic("chev")}</a></li>
      <li><a href="index.html#treatment">치료 방법 · 침과 전침{ic("chev")}</a></li>'''),
]
for a,b in R:
    assert a in e,a[:70]; e=e.replace(a,b)
a=e[e.index("    toc = [("):e.index("    chk = lambda")]
e=e.replace(a,"""    toc = [('s1', '먼저 결론부터'), ('s2', "얼굴에는 두 종류의 '전깃줄'이 있습니다"), ('s3', '떨릴 때'), ('s4', '얼굴 한쪽이 굳을 때'),
           ('s5', '저리거나 아플 때'), ('s6', '실제로 떨리는 것과 떨리는 느낌만 있는 것은 다릅니다'), ('s7', '이럴 땐 망설이지 마세요'),
           ('s8', '한의학에서는 어떻게 볼까요'), ('s9', '집에서 해 볼 수 있는 것'), ('s10', '한눈에 정리'), ('s11', '마치며')]
""")
b0=e.index('  <div class="prose" data-size="0">\n')+len('  <div class="prose" data-size="0">\n'); b1=e.index('  </div>\n\n  <aside class="ccta"')
e=e[:b0]+open('/home/claude/tools/column7_body.html').read()+e[b1:]
assert '관문조절설' not in e
s=s[:k]+e+s[k:]
a="    open(os.path.join(OUT, 'column-6.html'), 'w').write(v2(column6()))"
assert a in s; s=s.replace(a,a+"\n    open(os.path.join(OUT, 'column-7.html'), 'w').write(v2(column7()))")
a='    <div class="col-list">\n'
assert s.count(a)==1
s=s.replace(a,a+'''    <a class="colcard" href="column-7.html">
      <img src="images/column-7-hero.jpg" alt="얼굴 떨림·저림 · 얼굴이 떨리고 저릴 때" width="743" height="743" loading="lazy">
      <div class="body">
        <span class="chip">칼럼 · 얼굴 떨림·저림</span>
        <h3>얼굴이 떨리고 저릴 때, 걱정해야 할까요? (눈꺼풀 떨림, 안면경련, 구안와사, 뇌졸중 신호)</h3>
        <p>대부분은 피곤해서 생기는 떨림이지만, 서둘러야 할 신호도 있습니다. 걱정하지 않아도 될 떨림과 바로 119를 불러야 할 신호를 구분해 정리했습니다.</p>
        <time datetime="2026-11-19">2026.11.19</time>
      </div>
    </a>
''')
a="POSTS = [  # 최신 글이 위로. 새 칼럼·에세이를 올리면 여기에 한 줄 추가\n"
assert a in s
s=s.replace(a,a+f"""    {{'url': 'column-7.html', 'title': '{T}', 'date': 'Thu, 19 Nov 2026 11:38:00 +0900', 'cat': '칼럼',
     'desc': '{D}',
     'img': 'images/column-7-hero.jpg'}},
""")
import re
s=re.sub(r"^VER = '[0-9a-z]+'","VER = '20261120'",s,flags=re.M)
open(p,'w').write(s); print('ok')
