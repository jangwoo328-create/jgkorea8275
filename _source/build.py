#!/usr/bin/env python3
"""정관고려한의원 리뉴얼 시안 — index.html, column-1.html 생성"""
import json, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site')

TEL = '051-727-8275'
TEL_HREF = 'tel:0517278275'
ADDR = '부산시 기장군 정관읍 정관4로 37 2층'
KMAP = 'https://map.kakao.com/link/search/%EC%A0%95%EA%B4%80%EA%B3%A0%EB%A0%A4%ED%95%9C%EC%9D%98%EC%9B%90'
KAKAO_EMBED = '''<div class="kmap" id="kmap" aria-label="카카오맵 – 손가락으로 움직이고 확대할 수 있습니다">
          <script charset="UTF-8" class="daum_roughmap_loader_script" src="https://t1.kakaocdn.net/kakaomapweb/roughmap/loader/prod/roughmapLoader.js"></script>
          <script charset="UTF-8">
            (function () {
              var wrap = document.getElementById('kmap');
              var w = Math.round(wrap.clientWidth || 640);
              var m = (window.innerWidth || w) < 768;
              var code = m ? { ts: '1792999950938', key: '3wwyy3xqi6p' } : { ts: '1792999388607', key: '3wwmuaipsyb' };
              var h = m ? Math.max(260, Math.round(w * 0.78)) : Math.max(300, Math.min(380, Math.round(w * 0.66)));
              var box = document.createElement('div');
              box.id = 'daumRoughmapContainer' + code.ts;
              box.className = 'root_daum_roughmap root_daum_roughmap_landing';
              wrap.appendChild(box);
              try {
                new daum.roughmap.Lander({ "timestamp": code.ts, "key": code.key, "mapWidth": String(w), "mapHeight": String(h) }).render();
              } catch (e) { wrap.classList.add('kmap-off'); }
            })();
          </script>
        </div>'''
BLOG = 'https://blog.naver.com/jgkorea8275'
VER = '20261124'

# ---------------------------------------------------------------- icons
SPRITE = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true">
<symbol id="i-phone" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></symbol>
<symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9.5"/><path d="M12 7v5l3.5 2"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24"><path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></symbol>
<symbol id="i-park" viewBox="0 0 24 24"><rect width="18" height="18" x="3" y="3" rx="3"/><path d="M9.5 17V7h3.5a3 3 0 0 1 0 6H9.5"/></symbol>
<symbol id="i-chev" viewBox="0 0 24 24"><path d="m9 18 6-6-6-6"/></symbol>
<symbol id="i-chev-l" viewBox="0 0 24 24"><path d="m15 18-6-6 6-6"/></symbol>
<symbol id="i-down" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></symbol>
<symbol id="i-up" viewBox="0 0 24 24"><path d="m18 15-6-6-6 6"/></symbol>
<symbol id="i-back" viewBox="0 0 24 24"><path d="m12 19-7-7 7-7"/><path d="M19 12H5"/></symbol>
<symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></symbol>
<symbol id="i-x" viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12"/></symbol>
<symbol id="i-plus" viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></symbol>
<symbol id="i-check" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9.5"/><path d="m8.5 12 2.5 2.5 4.5-5"/></symbol>
<symbol id="i-nav" viewBox="0 0 24 24"><path d="M3 11 22 2l-9 19-2-8-8-2Z"/></symbol>
<symbol id="i-share" viewBox="0 0 24 24"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="m8.6 13.5 6.8 4M15.4 6.5l-6.8 4"/></symbol>
<symbol id="i-ext" viewBox="0 0 24 24"><path d="M15 3h6v6M10 14 21 3M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/></symbol>
<symbol id="i-alert" viewBox="0 0 24 24"><path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4M12 17h.01"/></symbol>
<symbol id="i-award" viewBox="0 0 24 24"><circle cx="12" cy="8" r="6"/><path d="M15.48 12.89 17 22l-5-3-5 3 1.52-9.11"/></symbol>
<symbol id="i-heart" viewBox="0 0 24 24"><path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z"/></symbol>
<symbol id="i-home" viewBox="0 0 24 24"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/></symbol>
<symbol id="i-wallet" viewBox="0 0 24 24"><path d="M19 7V4a1 1 0 0 0-1-1H5a2 2 0 0 0 0 4h15a1 1 0 0 1 1 1v4h-3a2 2 0 0 0 0 4h3a1 1 0 0 0 1-1v-2a1 1 0 0 0-1-1"/><path d="M3 5v14a2 2 0 0 0 2 2h15a1 1 0 0 0 1-1v-4"/></symbol>
<symbol id="i-door" viewBox="0 0 24 24"><path d="M3 21h18M6 21V4a1 1 0 0 1 1-1h10a1 1 0 0 1 1 1v17"/><path d="M14 12h.01"/></symbol>
<!-- 진료 분야 그림 아이콘 (48 그리드) -->
<symbol id="a-car" viewBox="0 0 48 48"><path d="M37 33h3.5c.9 0 1.5-.6 1.5-1.5V26c0-1.4-1-2.6-2.3-2.9-3.6-.9-8.7-2-8.7-2s-2.4-2.6-4.1-4.2c-.9-.8-2-1.3-3.3-1.3H11c-1.1 0-2.1.7-2.6 1.7l-2.6 5.4C5.3 23.6 5 24.6 5 25.6V31.5c0 .9.6 1.5 1.5 1.5H10"/><circle cx="14" cy="33" r="3.6"/><circle cx="33" cy="33" r="3.6"/><path d="M17.6 33h11.8"/><path d="M9 21h15"/><path d="M40 9l-3 4.5M44.5 15l-4.5 1.5M33.5 8l.5 4.5"/></symbol>
<symbol id="a-spine" viewBox="0 0 48 48"><rect x="18" y="4" width="11" height="6" rx="2.2"/><rect x="17" y="12.5" width="11" height="6" rx="2.2"/><rect x="16.5" y="21" width="11" height="6" rx="2.2"/><rect x="17" y="29.5" width="11" height="6" rx="2.2"/><rect x="18.5" y="38" width="11" height="6" rx="2.2"/><path d="M29 7h4M28 15.5h4.5M27.5 24h5M28 32.5h4.5M29.5 41h4"/><ellipse class="hot" cx="22" cy="28.2" rx="9" ry="3"/></symbol>
<symbol id="a-knee" viewBox="0 0 48 48"><path d="M17 3v14c0 3.6 3 6 7 6s7-2.4 7-6V3"/><path d="M17 45V32c0-2.2 3-3.6 7-3.6s7 1.4 7 3.6v13"/><ellipse cx="35.5" cy="25.5" rx="3.2" ry="4.2"/><path d="M20 39h0M28 39h0"/><circle class="hot" cx="24" cy="25.7" r="6"/></symbol>
<symbol id="a-neck" viewBox="0 0 48 48"><circle cx="24" cy="10.5" r="6.5"/><path d="M20.5 17v4.5M27.5 17v4.5"/><path d="M6 40c.6-8 4-13.5 10.5-16.2 1.6-.7 3-1.6 4-2.3M42 40c-.6-8-4-13.5-10.5-16.2-1.6-.7-3-1.6-4-2.3"/><circle class="hot" cx="32" cy="26.5" r="5"/><path d="M38.5 19l2-2M40 26.5h2.8M38.5 33.5l2 2"/></symbol>
<symbol id="a-bowl" viewBox="0 0 48 48"><path d="M7 25h34c0 9.4-7.6 16-17 16S7 34.4 7 25Z"/><path d="M17.5 41l-1.5 3.5h16L30.5 41"/><path d="M17 20c-2-2.7 2-4.6 0-7.6M24 20c-2-2.7 2-4.6 0-7.6M31 20c-2-2.7 2-4.6 0-7.6"/><path class="hot" d="M10 28h28c-1.3 5.6-7 9.5-14 9.5S11.3 33.6 10 28Z"/></symbol>
<symbol id="a-needle" viewBox="0 0 48 48"><path d="M12 36 33 15"/><path d="m31 11 6 6M33.5 8.5l6 6M36 6l6 6"/><path d="M6 42c4-2.5 8-2.5 12 0s8 2.5 12 0"/><circle class="hot" cx="11" cy="37" r="4.5"/></symbol>
</svg>'''

def ic(name, cls='ic'):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'

def ill(name):
    return f'<svg class="ill" aria-hidden="true"><use href="#a-{name}"/></svg>'

FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&amp;family=Noto+Serif+KR:wght@500&amp;display=swap">'''

ANALYTICS = '''<!-- ANALYTICS:START -->
<!-- Naver Analytics -->
<script type="text/javascript" src="//wcs.pstatic.net/wcslog.js"></script>
<script type="text/javascript">
if(!wcs_add) var wcs_add = {};
wcs_add["wa"] = "1cb7cfbebf4c3b0";
if(window.wcs) {
  wcs_do();
}
</script>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-R9LK4PG3RZ"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-R9LK4PG3RZ');
</script>
<!-- ANALYTICS:END -->'''

NAV = [('#area', '주요 진료 분야'), ('#about', '한의원 소개'), ('#doctor', '원장 소개'), ('#treatment', '치료 방법'),
       ('#column', '칼럼 및 에세이'), ('#media', '방송 출연'), ('#faq', '자주 묻는 질문'), ('#hours', '진료 시간'), ('#visit', '오시는 길')]

def header(prefix=''):
    links = ''.join(f'<a href="{prefix}{h}">{t}</a>' for h, t in NAV)
    dlinks = ''.join(f'<li><a href="{prefix}{h}">{t}{ic("chev")}</a></li>' for h, t in NAV)
    return f'''<header class="hd">
  <div class="wrap hd-in">
    <a class="brand" href="{prefix or '#top'}" aria-label="정관고려한의원 홈"><img src="images/2e68b0b4.png" alt="정관고려한의원" width="1359" height="200"></a>
    <nav class="nav" aria-label="주 메뉴">{links}</nav>
    <a class="hd-call" href="{TEL_HREF}">{ic("phone")}{TEL}</a>
    <button class="menu-btn" type="button" aria-label="메뉴 열기" aria-expanded="false" aria-controls="drawer">{ic("menu","ic bars")}{ic("x","ic x")}</button>
  </div>
  <div class="drawer" id="drawer">
    <div class="wrap">
      <ul>{dlinks}</ul>
      <a class="btn-gold" href="{TEL_HREF}">{ic("phone")}전화 문의 {TEL}</a>
    </div>
  </div>
</header>'''

def footer():
    return f'''<footer class="ft">
  <div class="wrap">
    <img src="images/2e68b0b4.png" alt="정관고려한의원" width="1359" height="200" loading="lazy">
    <div class="row"><span>{ADDR} 정관고려한의원</span></div>
    <div class="row"><span>대표원장 박장우</span><span>전화 <a href="{TEL_HREF}">{TEL}</a></span></div>
    <div class="row"><span>평일 09:00–19:00 (점심 13:00–14:00) · 토요일 09:00–13:00 · 일요일·공휴일 휴진</span></div>
    <div class="row"><a href="{BLOG}" target="_blank" rel="noopener">공식 네이버 블로그</a></div>
    <p class="copy">© since 2010 정관고려한의원</p>
  </div>
</footer>'''

def dock(prefix=''):
    return f'''<div class="dock" role="navigation" aria-label="빠른 연락">
  <a class="dock-call" href="{TEL_HREF}"><i>{ic("phone")}</i><span><small>전화 바로 연결</small><b>{TEL}</b></span></a>
  <a class="dock-btn" href="{prefix}#hours">{ic("clock")}진료시간</a>
  <a class="dock-btn" href="{KMAP}" target="_blank" rel="noopener">{ic("nav")}길찾기</a>
</div>
<div class="fab" id="fab" hidden>
  <nav class="fab-menu" id="fab-menu" aria-label="빠른 메뉴" hidden>
    <p class="fab-title">바로 가기</p>
    <ul>{''.join(f'<li><a href="{prefix}{h}">{t}</a></li>' for h, t in NAV)}</ul>
    <button type="button" class="fab-top" data-totop>{ic("up")}맨 위로</button>
  </nav>
  <button type="button" class="fab-btn" aria-expanded="false" aria-controls="fab-menu">{ic("menu","ic m")}{ic("x","ic x")}<span>메뉴</span></button>
</div>'''

# ---------------------------------------------------------------- index
TV_SPINE = [('칼럼', '허리디스크, 꼭 수술해야 하나요? 치료 기간과 좋아지는 신호', 'column-9.html'),
            ('방송1부', '허리디스크의 진단', 'https://blog.naver.com/jgkorea8275/223447810095'),
            ('방송2부', '허리디스크 수술해야 하나?', 'https://blog.naver.com/jgkorea8275/223450860463'),
            ('방송3부', '허리디스크의 비수술적 치료', 'https://blog.naver.com/jgkorea8275/223450870734'),
            ('방송4부', '허리디스크의 한방치료', 'https://blog.naver.com/jgkorea8275/223450881863'),
            ('방송통합본', '1~4부 한 번에 보기', 'https://blog.naver.com/jgkorea8275/221188934176')]
TV_SPINE_SERIES = '[요통과 허리디스크]'
TV_SPINE_TOPIC = {'칼럼': '건강 칼럼', '방송1부': TV_SPINE_SERIES, '방송2부': TV_SPINE_SERIES, '방송3부': TV_SPINE_SERIES, '방송4부': TV_SPINE_SERIES, '방송통합본': TV_SPINE_SERIES}
TV_BOYAK = [('방송1부', '오해의 종류와 녹용', 'https://blog.naver.com/jgkorea8275/223459097458'),
            ('방송2부', '노년보약, 여름보약', 'https://blog.naver.com/jgkorea8275/223459148340'),
            ('방송3부', '금기식? 먹고 살찌는 거 아닌가?', 'https://blog.naver.com/jgkorea8275/223459164071'),
            ('방송4부', '한약과 간(肝)', 'https://blog.naver.com/jgkorea8275/223459177910'),
            ('방송통합본', '1~4부 한 번에 보기', 'https://blog.naver.com/jgkorea8275/221188922757')]
TV_BOYAK_SERIES = '[한약에 대한 오해와 진실]'
def tv_sheet(sid, title, items, series=TV_SPINE_SERIES, kicker='방송 출연분', note='네이버 블로그에서 영상이 열립니다.'):
    def li(n, t, u):
        sm = series if isinstance(series, str) else series[n]
        ext = u.startswith('http')
        tgt = ' target="_blank" rel="noopener"' if ext else ''
        return f'<li><a href="{u}"{tgt}><span class="n{' num' if n.isdigit() else ''}">{n}</span><span class="t"><small>{sm}</small>{t}</span>{ic("ext" if ext else "chev")}</a></li>'
    lis = ''.join(li(n, t, u) for n, t, u in items)
    return (f'    <dialog class="sheet" id="{sid}" aria-labelledby="{sid}-h"><div class="sheet-in">'
            f'<div class="sheet-hd"><p class="sheet-k">{kicker}</p><h3 id="{sid}-h">{title}</h3>'
            f'<button type="button" class="sheet-x" aria-label="닫기">{ic("x")}</button></div>'
            f'<ol class="sheet-list">{lis}</ol><p class="sheet-note">{note}</p></div></dialog>\n')
COL_MUSCLE = [('1', '삐끗했는데 왜 이렇게 오래 가죠? 근육·인대·힘줄 손상의 회복 이야기', 'column-1.html'),
              ('2', '"침 한방에 낫게 해주소~" 근육통 회복 속도를 결정하는 네가지 요인', 'column-2.html'),
              ('3', '자다가 종아리에 쥐가 나요 (야간 하지 경련의 원인과 대처법)', 'column-4.html'),
              ('4', '어깨가 아프면 다 오십견일까요? (오십견의 특징과 운동법)', 'column-3.html'),
              ('5', '어깨 힘줄(회전근개) 부분 파열, 수술해야 하나요? 치료방법과 회복기간', 'column-8.html')]
COL_MUSCLE_TOPIC = {'1': '근육·인대·힘줄', '2': '근육통', '3': '야간 다리 경련', '4': '오십견·어깨 통증', '5': '회전근개 파열'}
CLINIC_LD = {"@context": "https://schema.org", "@type": "MedicalClinic", "name": "정관고려한의원", "url": "https://jgkorea8275.co.kr/", "telephone": "+82-51-727-8275", "image": "https://jgkorea8275.co.kr/og-image-2.jpg", "logo": "https://jgkorea8275.co.kr/images/c9de5ada.png", "description": "부산 기장군 정관읍 정관고려한의원. 한의학박사·한방재활의학과 전문의가 직접 진료합니다. 교통사고 후유증, 허리·목디스크, 근육통·관절통, 담결림, 보약. 예약 없이 방문 가능. 051-727-8275", "medicalSpecialty": "Physiatry", "address": {"@type": "PostalAddress", "streetAddress": "정관4로 37 2층", "addressLocality": "기장군 정관읍", "addressRegion": "부산광역시", "addressCountry": "KR"}, "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "13:00"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "14:00", "closes": "19:00"}, {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "09:00", "closes": "13:00"}], "founder": {"@type": "Person", "name": "박장우", "jobTitle": "대표원장"}, "foundingDate": "2010", "sameAs": ["https://blog.naver.com/jgkorea8275"]}

FAQS = [
    ('예약 없이 가도 진료받을 수 있나요?', '네, 예약 없이 언제든 방문하셔서 진료받으실 수 있습니다.'),
    ('교통사고 후유증도 진료하나요?', '네, 전국의 모든 한의원에서 교통사고 후유증을 치료합니다. 하지만 교통사고 후유증을 전문적으로 보는 한방과는 한방재활의학과입니다. 정관고려한의원은 한방재활의학과 전문의로서 교통사고 후유증을 좀 더 세심하게 진료합니다.'),
    ('침이 많이 아프지 않나요?', '초등학생들도 잘 맞고 갈 정도로 아프지 않게 침을 놓습니다. 침에 대한 공포감이 있는 분들은 미리 말씀하시면 더 신경 써서 아프지 않게 자침합니다. 반대로 강한 자극을 원하는 분들도 미리 말씀 주시면 자극량을 알맞게 조절합니다.'),
    ('피 뽑는 부항도 하나요?', '네, 이를 \'습식부항\'이라고 합니다. 한의사 선생님에 따라 선호하는 분도 있고 그렇지 않은 분도 계신데, 정관고려한의원은 습식부항을 많이 활용하는 편입니다.'),
    ('추나요법도 하나요?', '네, 물론입니다. 자동차보험으로 치료받으시는 분들은 본인 부담이 없어 부담 없이 추나치료를 시행합니다. 의료보험으로 치료받으시는 분들은 비용이 발생할 수 있으므로, 본인이 원하시고 원장님이 꼭 필요하다고 판단하는 경우에 시행합니다.'),
    ('약침과 봉침도 하나요?', '네, 약침은 어혈약침과 재생약침(PDRN약침) 두 가지가 있습니다. 봉침은 알러지 부작용이 없게 나온 봉침을 활용하고 있습니다.'),
    ('침 맞고 샤워나 목욕해도 되나요?', '침이 워낙 가늘어서 바로 하셔도 괜찮습니다. 다만 습식부항(사혈하는 부항)을 한 경우에는 3~4시간 뒤에 하시는 것이 좋습니다.'),
]
FAQ_LD = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}

TREAT = [
    ('추나요법', '손으로 틀어진 척추와 관절을 바로잡아 통증을 줄이는 치료입니다.'),
    ('침과 전침', '통증 부위와 경혈에 침을 놓고, 필요하면 전기 자극을 더해 치료합니다.', ('column-6.html', '칼럼 · 침 치료 원리, 과학적으로 쉽게 설명드립니다')),
    ('전자뜸', '연기와 화상 부담 없이 환부에 온열 자극을 줍니다.'),
    ('왕뜸', '복부를 깊이 데워 순환을 돕는 전통 뜸 치료입니다. 무연뜸이라 냄새가 밸 염려가 없습니다.'),
    ('부항요법', '건식부항과 습식부항(피 뽑는 부항)을 상태에 맞게 번갈아 시행합니다.'),
    ('약침', '어혈약침과 재생약침(PDRN약침)을 환자 상태에 맞게 사용합니다.'),
    ('봉침', '알러지 부작용이 없게 나온 봉침을 활용합니다.'),
    ('물리치료', '한방 치료와 함께 통증과 근육 긴장을 풀어 주는 물리치료를 병행합니다.'),
    ('한약', '체질과 상태에 맞춰 원장님이 원내에서 직접 조제하고 달입니다.'),
]

GALLERY = [
    ('33607c6a.jpg', '한의원 외관'),
    ('40ad143c.jpg', '한의원 입구'),
    ('74aee4ac.jpg', '접수·안내 데스크'),
    ('c4706834.jpg', '대기 공간'),
    ('018db94f.jpg', '진료실'),
    ('ac1642a0.jpg', '추나 치료 테이블'),
    ('d9bffc92.jpg', '치료실'),
    ('physio.jpg', '물리치료실'),
]

def spin(items, label, ratio, cls='', extra=''):
    """예전 홈페이지의 원통형 회전 사진. items: [(파일, 설명)], ratio: 사진 세로/가로"""
    imgs = ''.join(f'<img src="images/{f}" alt="{c}" data-cap="{c}" loading="lazy">' for f, c in items)
    return (f'<div class="spin {cls}" data-ratio="{ratio}"{extra} role="region" aria-roledescription="회전 사진" aria-label="{label}" tabindex="0">'
            f'<div class="spin-stage" aria-hidden="true"></div><div class="spin-src">{imgs}</div></div>')

def index():
    areas = [
        ('car', '교통사고 후유증', '사고 이후 남은 통증과 불편을 전문적으로 진료', 'traffic-accident.html', '안내 보기', True),
        ('spine', '허리·목디스크', '허리통증·다리 저림<br>목통증·팔 저림', '#tv-spine', '칼럼·방송 출연분 보기', False),
        ('knee', '근육통·관절통', '어깨·팔꿈치·손목 통증<br>고관절·무릎·발목 통증', '#tv-muscle', '칼럼 보기', False),
        ('neck', '담결림', '목과 등의 담을 사혈부항과 침, 약침 등을 이용해 치료', 'column-5.html', '칼럼 보기', False),
        ('bowl', '보약 처방', '체질과 상태에 따른 보약을 원장이 직접 조제', '#tv-boyak', '방송 출연분 보기', False),
    ]
    cards = ''
    for icon, t, d, href, go, badge in areas:
        b = '<span class="badge">전문의</span>' if badge else ''
        inner = f'{ill(icon)}<div class="txt"><h3>{t}</h3><p>{d}</p>' + (f'<span class="go">{go}{ic("chev")}</span>' if go else '') + '</div>'
        if href.startswith('#tv-') if href else False:
            cards += f'<button type="button" class="area" data-sheet="{href[1:]}" aria-haspopup="dialog">{b}{inner}</button>'
        elif href:
            ext = ' target="_blank" rel="noopener"' if href.startswith('http') else ''
            cards += f'<a class="area" href="{href}"{ext}>{b}{inner}</a>'
        else:
            cards += f'<div class="area">{inner}</div>'
    cards += f'<a class="area area-dark" href="#treatment">{ill("needle")}<div class="txt"><h3>치료 방법 9가지</h3><p>추나, 침·전침, 뜸, 부항, 약침, 봉침, 물리치료, 한약</p><span class="go">자세히 보기{ic("chev")}</span></div></a>'

    gal = spin(GALLERY, '한의원 사진', 640/960, 'spin-light', ' data-wide-vis="116"')

    def _tx(i, t, d, more=None):
        lk = f'<a class="tx-more" href="{more[0]}">{more[1]}{ic("chev")}</a>' if more else ''
        return f'<details><summary><span class="n">{i:02d}</span><span class="t">{t}</span>{ic("plus","ic pl")}</summary><p{" class=\"w500\"" if t == "약침" else ""}>{d}</p>{lk}</details>'
    tx = ''.join(_tx(i, *row) for i, row in enumerate(TREAT, 1))

    faq = ''.join(f'<details><summary><span class="q">Q.</span><span>{q}</span>{ic("down")}</summary><p>{a}</p></details>' for q, a in FAQS)

    def mcard_photos(items, label, src, title, desc):
        return f'<article class="mcard">{spin(items, label, 0.75, "spin-dark")}<div class="meta"><span class="src">{src}</span><h3>{title}</h3><p>{desc}</p></div></article>'

    def mcard_video(poster, video, alt, src, title, desc):
        return f'<article class="mcard"><video controls playsinline preload="none" poster="images/{poster}" aria-label="{alt}"><source src="videos/{video}" type="video/mp4"></video><div class="meta"><span class="src">{src}</span><h3>{title}</h3><p>{desc}</p></div></article>'

    media = (
        mcard_video('8625f57f.jpg', '13cf83f4.mp4', '요통과 허리디스크 방송 영상', '부산불교방송 BBS · 2015.03.10', '부산경남 라디오830 · 한의학상담', '요통과 허리디스크')
        + mcard_video('dd6fa96a.jpg', '0dcc02bc.mp4', '한약에 대한 오해와 진실 방송 영상', '부산불교방송 BBS · 2015.05.19', '부산경남 라디오830 · 한의학상담', '한약에 대한 오해와 진실')
        + mcard_photos([('01673539.jpg', '박장우 원장 인터뷰 화면'), ('33bd2a12.jpg', '추나요법 설명 장면'), ('3195d9d6.jpg', '봉침 설명 장면')],
                       '자생한방병원 근무 시 방송 출연 화면', '2009 · 자생한방병원 근무 시 출연', '추나요법과 봉침 설명', '추나요법과 봉침에 관한 설명 과정')
        + mcard_photos([('cd46677c.jpg', '박장우 원장 인터뷰'), ('9dc87954.jpg', '잘못된 한방상식을 잡아라 O·X 퀴즈'), ('6f4c92c2.jpg', '체질은 약으로 바꿀 수 있다 O·X'), ('93cbc5ae.jpg', '오후 6시 이후 먹으면 살찐다 O·X'), ('b90f632d.jpg', 'O·X 퀴즈 진행 장면'), ('ca7a6942.jpg', '오후 6시 이후 먹으면 살찐다 정답 X')],
                       'tbs 무료 한방검진 현장 방송 화면', '서울교통방송 tbs · 2008', 'tbs 개국 18주년 무료 한방검진 현장', '잘못된 한방상식을 잡아라 O·X')
    )

    head = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>정관고려한의원 | 부산 기장군 정관읍 한방재활의학과 전문의</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="정관고려한의원. 한의학박사·한방재활의학과 전문의 진료. 교통사고 후유증, 허리·목디스크, 근육통·관절통, 담결림, 보약. 예약 없이 방문 가능.">
<meta name="google-site-verification" content="j5edXme60Dbx0P52GLduuovIJlDX7XBwTngunqrttzU" />
<meta name="naver-site-verification" content="7645e75f9b64aa19ec814efb47641c5b23b4a674" />
<meta name="theme-color" content="#171511">
<link rel="canonical" href="https://jgkorea8275.co.kr/">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="alternate" type="application/rss+xml" title="정관고려한의원 칼럼·에세이" href="https://jgkorea8275.co.kr/rss.xml">
<meta property="og:type" content="website">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="정관고려한의원">
<meta property="og:title" content="정관고려한의원 | 부산 기장군 정관읍">
<meta property="og:description" content="정관고려한의원. 한의학박사·한방재활의학과 전문의 진료. 교통사고 후유증, 허리·목디스크, 근육통·관절통, 담결림, 보약. 예약 없이 방문 가능.">
<meta property="og:url" content="https://jgkorea8275.co.kr/">
<meta property="og:image" content="https://jgkorea8275.co.kr/og-image-2.jpg">
<meta property="og:image:secure_url" content="https://jgkorea8275.co.kr/og-image-2.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="정관고려한의원 입구 금색 간판">
<meta name="twitter:image" content="https://jgkorea8275.co.kr/og-image-2.jpg">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json.dumps(CLINIC_LD, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(FAQ_LD, ensure_ascii=False)}</script>
{FONTS}
<link rel="stylesheet" href="assets/site.css?v={VER}">
</head>'''

    body = f'''<body class="has-dock" id="top">
{SPRITE}
{header()}
<main>
<section class="hero" aria-label="정관고려한의원 소개">
  <div class="wrap hero-grid">
    <div class="hero-txt">
      <p class="eyebrow-d">정관고려한의원 · SINCE 2010</p>
      <h1>편하게 찾는<br>우리 동네 한의원,<br><em>전문의의 정확한 진료</em></h1>
      <p class="hero-sub"><b>한의학박사·한방재활의학과 전문의</b>가 직접 진료합니다.<br>예약 없이 편한 시간에 들러 주세요.</p>
      <div class="hero-cta">
        <a class="btn-gold" href="{TEL_HREF}">{ic("phone")}전화 문의하기{ic("chev","ic chev")}</a>
        <a class="btn-line" href="#hours">진료시간 · 오시는 길</a>
      </div>
    </div>
    <div class="hero-photo">
      <picture><source media="(min-width:1000px)" srcset="images/33607c6a.jpg" width="960" height="640"><img src="images/hero-sign.jpg" alt="정관고려한의원 2층 간판" width="480" height="500" fetchpriority="high"></picture>
    </div>
  </div>
  <div class="hero-info">
    <div class="wrap">
      <ul>
        <li><a href="#hours">{ic("clock")}<span><b>진료시간</b></span></a></li>
        <li><a href="#visit">{ic("pin")}<span><b>오시는 길</b></span></a></li>
        <li><a href="#parking">{ic("park")}<span><b>주차 안내</b></span></a></li>
      </ul>
    </div>
  </div>
</section>

<section class="sec" id="area">
  <div class="wrap">
    <p class="eyebrow">01. 어떤 증상으로 오셨나요?</p>
    <h2>주요 진료 분야</h2>
    <p class="lead"><b class="lead-em">한방재활의학과 전문의</b>가 통증이 생긴 원인부터 살펴 진료합니다. 특히 교통사고 후유증을 전문적으로 봅니다.</p>
    <div class="areas">{cards}</div>
{tv_sheet("tv-spine", "허리·목디스크", TV_SPINE, TV_SPINE_TOPIC, "칼럼 · 방송 출연분", "칼럼은 홈페이지에서, 방송 출연분은 네이버 블로그에서 열립니다.")}{tv_sheet("tv-boyak", "보약 처방", TV_BOYAK, TV_BOYAK_SERIES)}{tv_sheet("tv-muscle", "근육통·관절통", COL_MUSCLE, COL_MUSCLE_TOPIC, "건강 칼럼", "원장이 직접 쓴 칼럼으로 이동합니다.")}
  </div>
</section>

<section class="sec" id="about">
  <div class="wrap">
    <div class="about">
      <div>
        <p class="eyebrow">02. 한의원 소개</p>
        <h2>오래된 이웃같은<br>동네 한의원입니다</h2>
        <p class="lead">2010년 정관 최초로 개원해 오랜 시간 정관 주민의 건강을 지켜 왔습니다. 오래된 이웃처럼 편하게 들르실 수 있는 한의원을 지향합니다.</p>
        <a class="btn-dark" href="#doctor">원장 소개 보기{ic("chev")}</a>
      </div>
      <figure class="about-fig">
        <img src="images/74aee4ac.jpg" alt="정관고려한의원 접수 데스크와 대기실" width="960" height="640">
        <figcaption>2010년부터 같은 자리에서</figcaption>
      </figure>
    </div>
    <ul class="reasons">
      <li>{ic("door")}<b>예약 없이 언제든</b><p>전화 예약 없이 편한 시간에 들러 진료받으세요.</p></li>
      <li>{ic("heart")}<b>안 아프게 놓는 침</b><p>침이 무서운 분도 걱정 마세요. 미리 말씀하시면 더 안 아프게 시술합니다.</p></li>
      <li>{ic("home")}<b>2010년부터 함께한 한의원</b><p>정관 최초의 한의원으로 오랜 시간 정관 주민과 함께해 왔습니다.</p></li>
      <li>{ic("wallet")}<b>합리적인 비용</b><p>오래된 이웃 같은 한의원을 표방하므로, 치료 비용이 부담스럽지 않게 신경 씁니다.</p></li>
    </ul>
    <div class="gallery">
      <div class="gal-head">
        <div><h3>한의원 둘러보기</h3><p>사진을 좌우로 밀어서 직접 돌려 보세요</p></div>
        <div class="gal-btns"><button type="button" data-spin="prev" aria-label="이전 사진">{ic("chev-l")}</button><button type="button" data-spin="next" aria-label="다음 사진">{ic("chev")}</button></div>
      </div>
      {gal}
      <p class="spin-cap" aria-hidden="true"></p>
    </div>
  </div>
</section>

<section class="sec" id="doctor">
  <div class="wrap">
    <div class="doc">
      <header class="doc-head">
        <p class="eyebrow">03. 원장 소개</p>
        <h2 class="doc-title"><small>대표원장</small>박장우</h2>
        <ul class="doc-creds">
          <li>{ic("award")}한의학박사</li>
          <li>{ic("award")}한방재활의학과 전문의</li>
        </ul>
      </header>
      <div class="doc-photo"><img src="images/director-portrait.jpg" alt="정관고려한의원 대표원장 박장우 한의학박사" width="900" height="878" loading="lazy"></div>
      <div class="doc-body">
        <h3 class="doc-sub">약력</h3>
        <ul class="career">
          <li>대전대 한의학과 및 동대학원 졸업 (<em>한의학박사</em> 취득)</li>
          <li>대전대 부속 대전한방병원 일반수련의 및 전문수련의 (<em>한방재활의학과 전문의</em> 취득)</li>
          <li class="w500"><span class="gold">한의사 전문의 국가고시 전국 차석</span><small>한방재활의학과</small></li>
          <li>前) 자생한방병원 일산분원 척추디스크센터 및 관절센터 진료원장</li>
          <li class="now">現) 정관고려한의원 대표원장</li>
        </ul>
        <div class="socs">
          <h3 class="doc-sub">학회 활동</h3>
          <ul><li>한방재활의학과학회 평생회원</li><li>척추신경추나학회 정회원</li><li>대한약침학회 정회원</li><li>한의통증제형학회 정회원</li><li>한국 시리악스 학회 정회원</li></ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="treatment">
  <div class="wrap">
    <p class="eyebrow">04. 치료 방법</p>
    <h2>상태에 맞춰 함께 쓰는 치료</h2>
    <p class="lead">한 가지 치료만 고집하지 않고, 통증의 원인과 회복 단계에 맞춰 필요한 치료를 골라 함께 씁니다.</p>
    <div class="tx">{tx}</div>
  </div>
</section>

<section class="sec" id="column">
  <div class="wrap colwrap">
    <div>
      <p class="eyebrow">05. 칼럼 및 에세이</p>
      <h2>진료실에서 나눈 이야기를<br>칼럼과 에세이로 씁니다</h2>
      <p class="lead">어렵게 느껴지는 통증 이야기는 그림과 표로 쉽게 정리한 칼럼으로, 진료하며 품어 온 생각은 에세이로 전합니다.</p>
      <a class="btn-dark" href="{BLOG}" target="_blank" rel="noopener" style="margin-top:22px">블로그에서 더 보기{ic("chev")}</a>
    </div>
    <div class="col-list">
    <a class="colcard" href="column-9.html">
      <img src="images/column-9-hero.jpg" alt="허리디스크 · 허리디스크, 꼭 수술해야 하나요?" width="743" height="743" loading="lazy">
      <div class="body">
        <span class="chip">칼럼 · 허리디스크</span>
        <h3>허리디스크, 꼭 수술해야 하나요? 치료 기간과 좋아지는 신호</h3>
        <p>"원장님, 디스크가 터졌대요." 허리디스크는 대부분 수술 없이 좋아집니다. 수술이 필요한 경우와 치료 기간, 좋아지는 신호를 정리했습니다.</p>
        <time datetime="2026-11-23">2026.11.23</time>
      </div>
    </a>
    <a class="colcard" href="column-8.html">
      <img src="images/column-8-hero.jpg" alt="회전근개 파열 · 어깨 힘줄이 찢어졌대요" width="743" height="743" loading="lazy">
      <div class="body">
        <span class="chip">칼럼 · 회전근개 파열</span>
        <h3>어깨 힘줄(회전근개) 부분 파열, 수술해야 하나요? 치료방법과 회복기간</h3>
        <p>"원장님, 꼭 수술해야 하나요?" 회전근개 부분 파열의 수술 여부와 치료 기간, 재활운동과 침치료, 집에서 하는 단계별 어깨 운동을 정리했습니다.</p>
        <time datetime="2026-11-21">2026.11.21</time>
      </div>
    </a>
    <a class="colcard" href="column-7.html">
      <img src="images/column-7-hero.jpg" alt="얼굴 떨림·저림 · 얼굴이 떨리고 저릴 때" width="743" height="743" loading="lazy">
      <div class="body">
        <span class="chip">칼럼 · 얼굴 떨림·저림</span>
        <h3>얼굴이 떨리고 저릴 때, 걱정해야 할까요? (눈꺼풀 떨림, 안면경련, 구안와사, 뇌졸중 신호)</h3>
        <p>대부분은 피곤해서 생기는 떨림이지만, 서둘러야 할 신호도 있습니다. 걱정하지 않아도 될 떨림과 바로 119를 불러야 할 신호를 구분해 정리했습니다.</p>
        <time datetime="2026-11-19">2026.11.19</time>
      </div>
    </a>
    <a class="colcard" href="column-6.html">
      <img src="images/column-6-hero.jpg" alt="침 치료 원리 · 침은 어떻게 통증을 줄일까요?" width="743" height="743" loading="lazy">
      <div class="body">
        <span class="chip">칼럼 · 침 치료 원리</span>
        <h3>침 치료 원리, 과학적으로 쉽게 설명드립니다 (관문조절설, 엔도르핀, 전침)</h3>
        <p>"원장님, 침은 어떻게 해서 낫는 거예요?" 고교생 환자의 질문에서 시작해, 침이 통증을 줄이는 네 가지 원리를 쉽게 풀었습니다.</p>
        <time datetime="2026-11-17">2026.11.17</time>
      </div>
    </a>
    <a class="colcard" href="column-5.html">
      <img src="images/column-5-hero.jpg" alt="목 담결림 · 자고 일어났더니 목이 안 돌아가요" width="743" height="743" loading="lazy">
      <div class="body">
        <span class="chip">칼럼 · 목 담결림</span>
        <h3>자고 일어났더니 목이 안 돌아가요 (목 담결림·낙침)</h3>
        <p>목 담결림이 생기는 네 가지 이유, 그냥 둘 때와 침치료를 받을 때의 경과, 빨리 회복하는 법과 바로 진료가 필요한 경우를 정리했습니다.</p>
        <time datetime="2026-11-10">2026.11.10</time>
      </div>
    </a>
    <a class="colcard" href="column-4.html">
      <img src="images/column-4-hero.jpg" alt="야간 다리 경련 · 자다가 종아리에 쥐가 나요" width="743" height="743" loading="lazy">
      <div class="body">
        <span class="chip">칼럼 · 야간 다리 경련</span>
        <h3>자다가 종아리에 쥐가 나요 (야간 하지 경련의 원인과 대처법)</h3>
        <p>밤에 종아리에 쥐가 나는 이유와 잘 생기는 조건, 중풍과 구별하는 법, 쥐가 났을 때 대처법 4가지와 예방 스트레칭을 정리했습니다.</p>
        <time datetime="2026-11-08">2026.11.08</time>
      </div>
    </a>
    <a class="colcard" href="column-3.html">
      <img src="images/column-3-hero.jpg" alt="오십견·어깨 통증 · 어깨가 아프면 다 오십견일까요?" width="743" height="743" loading="lazy">
      <div class="body">
        <span class="chip">칼럼 · 오십견·어깨 통증</span>
        <h3>어깨가 아프면 다 오십견일까요? (오십견의 특징과 운동법)</h3>
        <p>어깨가 아프다고 다 오십견은 아닙니다. 혼동하기 쉬운 질환과 자가감별법, 경과와 치료, 집에서 하는 운동 6가지를 정리했습니다.</p>
        <time datetime="2026-11-04">2026.11.04</time>
      </div>
    </a>
    <a class="colcard" href="column-2.html">
      <img src="images/column-2-hero.jpg" alt="원장 칼럼 · 침 한방에 낫게 해주소~ · 근육통, 회복 속도를 결정하는 4가지 요인" width="743" height="743" loading="lazy">
      <div class="body">
        <span class="chip">칼럼 · 근육통</span>
        <h3>"침 한방에 낫게 <span class="nw">해주소~"</span> 근육통 회복 속도를 결정하는 네가지 요인</h3>
        <p>같은 치료를 받아도 빨리 낫는 분과 더디 낫는 분이 있습니다. 그 차이를 만드는 네 가지 요인을 쉽게 풀었습니다.</p>
        <time datetime="2026-11-01">2026.11.01</time>
      </div>
    </a>
    <a class="colcard" href="essay-4.html">
      <img src="images/essay-4-hero.jpg" alt="에세이 04 · 불은 그대로인데 사이렌만 끄고 있지는 않습니까?" width="743" height="743" loading="lazy">
      <div class="body">
        <span class="chip chip-essay">에세이</span>
        <h3>불은 그대로인데 사이렌만 끄고 있지는 않습니까?</h3>
        <p>통증주사에 익숙해진 시대, 침을 놓는 한의사의 마음. 통증이 사라졌다고 손상된 조직까지 다 나은 것은 아닙니다.</p>
        <time datetime="2026-10-31">2026.10.31</time>
      </div>
    </a>
    <a class="colcard" href="essay-3.html">
      <img src="images/essay-3-hero.jpg" alt="에세이 · 몸은 쉬라고 하는데, 삶은 멈출 수 없을 때" width="743" height="743" loading="lazy">
      <div class="body">
        <span class="chip chip-essay">에세이</span>
        <h3>몸은 쉬라고 하는데, 삶은 멈출 수 없을 때</h3>
        <p>"원장님, 일을 좀 쉬면 나을까요?" 아픔을 참아가며 일하는 분들을 위한 과사용 증후군 이야기입니다.</p>
        <time datetime="2026-10-30">2026.10.30</time>
      </div>
    </a>
    <a class="colcard" href="essay-2.html">
      <img src="images/essay-2-hero.jpg" alt="에세이 02 · 내 몸 안의 의사를 믿는다는 것" width="743" height="743" loading="lazy">
      <div class="body">
        <span class="chip chip-essay">에세이</span>
        <h3>내 몸 안의 의사를 믿는다는 것</h3>
        <p>허리가 아파도, 어깨가 아파도 진통제. 우리는 왜 통증을 없애는 데만 익숙해졌을까요? 통증은 몸이 보내는 편지입니다.</p>
        <time datetime="2026-10-28">2026.10.28</time>
      </div>
    </a>
    <a class="colcard" href="column-1.html">
      <img src="images/column-1-hero.jpg" alt="삐끗했는데 왜 이렇게 오래 가죠? 근육 1~4주, 인대 2~8주, 힘줄 6주~3개월" width="800" height="800" loading="lazy">
      <div class="body">
        <span class="chip">칼럼 · 근육·인대·힘줄</span>
        <h3>삐끗했는데 왜 이렇게 오래 가죠? 근육·인대·힘줄 손상의 회복 이야기</h3>
        <p>똑같이 "삐끗했다"고 오셨는데 어떤 분은 1~2주 만에, 어떤 분은 석 달이 지나도 아픕니다. 차이는 어느 조직을 다쳤느냐에 있습니다.</p>
        <time datetime="2026-10-24">2026.10.24</time>
      </div>
    </a>
    </div>
  </div>
</section>

<section class="sec" id="media">
  <div class="wrap">
    <p class="eyebrow">06. 방송 출연</p>
    <h2>방송으로 전한 한의학 이야기</h2>
    <div class="media">{media}</div>
  </div>
</section>

<section class="sec" id="faq">
  <div class="wrap faqgrid">
    <div>
      <p class="eyebrow">07. 자주 묻는 질문</p>
      <h2>처음 오시는 분들이<br>많이 물어보세요</h2>
      <p class="lead">궁금한 점이 더 있으시면 편하게 전화 주세요.</p>
    </div>
    <div class="faq">{faq}</div>
  </div>
</section>

<section class="sec hrs-sec" id="time">
  <div class="wrap">
    <p class="eyebrow">08. 진료시간</p>
    <h2>진료시간 안내</h2>
    <p class="lead">예약 없이 진료시간 안에 편하게 오시면 됩니다.</p>
    <div class="hrs-grid">
      <div class="hrs-card" id="hours">
        <dl class="hrs">
          <div class="hrs-row main"><dt>평일 <small>월 – 금</small></dt><dd class="big"><span class="ap">오전</span><b>9:00</b><span class="tl">~</span><span class="ap">오후</span><b>7:00</b></dd></div>
          <div class="hrs-row sub"><dt>점심시간</dt><dd>오후 1:00 – 2:00</dd></div>
          <div class="hrs-row main"><dt>토요일</dt><dd class="big"><span class="ap">오전</span><b>9:00</b><span class="tl">~</span><span class="ap">오후</span><b>1:00</b></dd></div>
          <div class="hrs-row off"><dt>일요일 · 공휴일</dt><dd>휴진</dd></div>
        </dl>
      </div>
      <div class="hrs-side">
        <ul class="hrs-notes">
          <li>예약 없이 오셔도 진료받으실 수 있습니다.</li>
          <li>점심시간(오후 1시 – 2시)에는 진료하지 않습니다.</li>
          <li>토요일은 오후 1시까지 진료합니다.</li>
        </ul>
        <a class="more" href="https://blog.naver.com/jgkorea8275/223272913722" target="_blank" rel="noopener">진료시간 안내 자세히 보기{ic("chev")}</a>
      </div>
    </div>
  </div>
</section>

<section class="sec" id="visit">
  <div class="wrap">
    <p class="eyebrow">09. 오시는 길</p>
    <h2>예약 없이, 편하게 오세요</h2>
    <div class="visit">
      <div class="vmap-wrap">
        <p class="map-cap">{ic("pin")}약도</p>
        <a class="vmap is-map" href="{KMAP}" target="_blank" rel="noopener" aria-label="정관고려한의원 약도 – 카카오맵에서 크게 보기">
          <img src="images/map.png" alt="정관고려한의원 약도: 정관4로 37, 제일프라자 파리바게뜨 건물 2층. 정관로와 정관4로 교차로 동쪽, 정관 주민자치회관 건너편이며 한의원 앞에 버스정류장이 있습니다." width="1600" height="1229" loading="lazy">
        </a>
        <a class="vmap-open" href="{KMAP}" target="_blank" rel="noopener">카카오맵 바로보기{ic("ext")}</a>
        {KAKAO_EMBED}
      </div>
      <ul class="vinfo">
        <li id="parking">{ic("park")}<div><h3>주차</h3>
          <p>한의원 건물에 지하주차장이 있습니다. 자리가 없을 때는 정관성당 맞은편 블록 끝 무료 주차장을 이용해 주세요.</p>
          <details class="park"><summary>주차장 위치 사진 보기{ic("down")}</summary><img src="images/parking.jpg" alt="주차장 안내: 주차장1 한의원 건물 지하1층, 주차장2 정관성당 건너편 무료 공영주차장 위치와 사진" width="800" height="1453" loading="lazy"></details>
        </div></li>
        <li>{ic("pin")}<div><h3>주소</h3><p>{ADDR} 정관고려한의원</p></div></li>
        <li>{ic("phone")}<div><h3>전화</h3><a class="tel" href="{TEL_HREF}">{TEL}</a></div></li>
      </ul>
    </div>
  </div>
</section>

<section class="blog-sec">
  <div class="wrap">
    <a class="blog" href="{BLOG}" target="_blank" rel="noopener">
      <div><small>OFFICIAL BLOG</small><b>정관고려한의원 공식 블로그</b><p>진료 이야기와 건강 정보, 방송 출연 소식을 더 자세히 만나 보세요.</p></div>
      <span class="btn-gold">블로그 바로가기{ic("ext")}</span>
    </a>
  </div>
</section>
</main>
{footer()}
{dock()}
<script src="assets/site.js?v={VER}"></script>
{ANALYTICS}
</body>
</html>
'''
    return head + '\n' + body

# ---------------------------------------------------------------- column 1
ART_LD = {"@context": "https://schema.org", "@type": "Article", "headline": "삐끗했는데 왜 이렇게 오래 가죠? 근육·인대·힘줄 손상의 회복 이야기", "datePublished": "2026-10-24", "image": ["https://jgkorea8275.co.kr/images/column-1-hero.jpg"], "mainEntityOfPage": "https://jgkorea8275.co.kr/column-1.html", "author": {"@type": "Organization", "name": "정관고려한의원", "url": "https://jgkorea8275.co.kr/"}, "publisher": {"@type": "Organization", "name": "정관고려한의원", "logo": {"@type": "ImageObject", "url": "https://jgkorea8275.co.kr/favicon.png"}}}
CRUMB_LD = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "정관고려한의원", "item": "https://jgkorea8275.co.kr/"},
    {"@type": "ListItem", "position": 2, "name": "건강 칼럼", "item": "https://jgkorea8275.co.kr/#column"},
    {"@type": "ListItem", "position": 3, "name": "삐끗했는데 왜 이렇게 오래 가죠?", "item": "https://jgkorea8275.co.kr/column-1.html"}]}

def column1():
    desc = '삐끗한 뒤 회복 기간은 근육 1~4주, 인대 2~8주, 힘줄 6주~3개월. 다친 조직에 따라 다른 이유를 정관고려한의원이 정리했습니다.'
    title = '삐끗했는데 왜 이렇게 오래 가죠? 근육·인대·힘줄 손상의 회복 이야기'
    chk = lambda s: f'<li>{ic("check")}<span>{s}</span></li>'
    toc = [('s1', "같은 '삐끗'인데 회복 기간은 왜 다를까요?"), ('s2', '근육·인대·힘줄은 어떻게 다를까요?'), ('s3', '회복 속도, 한눈에 비교하기'),
           ('s4', '1. 근육 손상'), ('s5', '2. 인대 손상'), ('s6', '3. 힘줄 손상'), ('s7', '통증이 사라졌다고 다 나은 것은 아닙니다'), ('s8', '마치며')]
    toc_html = ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    head = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} | 정관고려한의원</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<meta name="theme-color" content="#171511">
<link rel="canonical" href="https://jgkorea8275.co.kr/column-1.html">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="alternate" type="application/rss+xml" title="정관고려한의원 칼럼·에세이" href="https://jgkorea8275.co.kr/rss.xml">
<meta property="og:type" content="article">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="정관고려한의원">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://jgkorea8275.co.kr/column-1.html">
<meta property="og:image" content="https://jgkorea8275.co.kr/images/column-1-hero.jpg">
<meta property="og:image:width" content="800">
<meta property="og:image:height" content="800">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://jgkorea8275.co.kr/images/column-1-hero.jpg">
<meta property="article:published_time" content="2026-10-24">
<script type="application/ld+json">{json.dumps(ART_LD, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(CRUMB_LD, ensure_ascii=False)}</script>
{FONTS}
<link rel="stylesheet" href="assets/site.css?v={VER}">
</head>'''

    body = f'''<body class="has-dock">
{SPRITE}
{header('index.html')}
<div class="cbanner">
  <img src="images/column-banner.jpg" alt="" width="1600" height="900">
  <div class="wrap"><p class="ttl">건강 칼럼</p><p>진료실에서 자주 받는 질문을 쉽게 풀어 씁니다.</p></div>
</div>
<main class="art">
  <a class="back" href="index.html#column">{ic("back")}목록으로</a>
  <header class="art-head">
    <span class="chip">근육·인대·힘줄</span>
    <h1>{title}</h1>
    <p class="art-meta"><span><time datetime="2026-10-24">2026.10.24</time></span><span>정관고려한의원 건강 칼럼</span></p>
  </header>

  <section class="sum" aria-labelledby="sum-h">
    <h2 id="sum-h">이 글에서 알 수 있는 내용</h2>
    <ul>
      {chk('근육·인대·힘줄의 회복 기간이 서로 다른 이유')}
      {chk('조직별로 진료실에서 자주 보는 질환')}
      {chk('통증이 사라진 뒤에도 지켜야 할 생활 수칙')}
      {chk('바로 영상 검사를 받아야 하는 위험 신호')}
    </ul>
    <details class="toc"><summary>목차 보기{ic("down")}</summary><ol>{toc_html}</ol></details>
  </section>

  <div class="prose" data-size="0">
    <figure><img src="images/column-1-hero.jpg" alt="삐끗했는데 왜 이렇게 오래 가죠? 다친 곳에 따라 회복 기간이 다른 이유 - 근육 1~4주, 인대 2~8주, 힘줄 6주~3개월" width="800" height="800"></figure>

    <h2 id="s1">같은 '삐끗'인데 회복 기간은 왜 다를까요?</h2>
    <p>똑같이 "삐끗했다"고 오셨는데, 어떤 분은 1~2주 만에 털고 일어나고 어떤 분은 석 달이 지나도 아프다고 하십니다. 차이는 대부분 <b>어느 조직을 다쳤느냐</b>에 있습니다.</p>
    <p>우리 몸을 움직이는 연부조직은 크게 <b>근육, 인대, 힘줄(건)</b> 세 가지입니다. 이 셋은 피가 도는 정도와 사용되는 방식이 달라서 회복 속도도 크게 다릅니다.</p>
    <p>오늘은 각 조직이 왜 다르게 낫는지, 진료실에서 자주 보는 질환은 무엇인지 그림과 표로 정리해 보겠습니다.</p>

    <h2 id="s2">근육·인대·힘줄은 어떻게 다를까요?</h2>
    <figure><img src="images/column-1-structure.jpg" alt="근육, 인대, 힘줄 구조 비교" width="1080" height="2325" loading="lazy"><figcaption>근육·인대·힘줄의 구조와 혈액 공급 비교</figcaption></figure>
    <p>조직이 회복하려면 피를 통해 산소와 영양분이 공급되어야 합니다. 혈관이 풍부한 근육은 빨리 낫고, 혈관이 적은 인대와 힘줄은 오래 걸립니다.</p>
    <p>인대와 힘줄의 혈액 공급은 비슷하지만, <b><u>힘줄은 반복 사용으로 조금씩 상하고 일상에서 계속 쓰게 되어 가장 오래 갑니다.</u></b></p>

    <h2 id="s3">회복 속도, 한눈에 비교하기</h2>
    <figure><img src="images/column-1-curve.jpg" alt="근육, 인대, 힘줄 회복 곡선" width="1080" height="1680" loading="lazy"><figcaption>다친 뒤 시간에 따른 조직별 회복 정도</figcaption></figure>
    <p>위 그래프는 다친 뒤 시간이 지나면서 조직이 얼마나 회복되는지를 보여줍니다. 근육은 한 달이면 거의 회복되지만, 힘줄은 넉 달이 지나도 곡선이 계속 올라가는 중입니다.</p>
    <figure><img src="images/column-1-compare.jpg" alt="근육·인대·힘줄 한눈에 비교. 근육: 몸을 움직임, 혈액 공급 풍부, 회복 1~4주(심하면 2개월), 대표 질환 담 결림·허리 근육 염좌·종아리·햄스트링 손상. 인대: 뼈와 뼈를 이어 관절을 잡아줌, 혈액 공급 적음, 회복 2~8주(파열 시 3개월 이상), 대표 질환 발목 염좌·무릎 내측측부인대 손상·손목·손가락 염좌. 힘줄: 근육을 뼈에 붙임, 혈액 공급 적음, 회복 6주~3개월(만성은 6개월 이상), 대표 질환 테니스엘보·회전근개 건병증·아킬레스건염·슬개건염." width="1080" height="2292" loading="lazy"></figure>
    <p>표처럼 <b>테니스엘보</b>와 <b>아킬레스건염</b>은 힘줄의 문제이기 때문에, 부위가 작고 단순해 보여도 가장 오래가는 질환입니다.</p>

    <h2 id="s4"><span class="num">1. 근육 손상</span>: 가장 빨리 낫지만, 방심하면 다시 다칩니다</h2>
    <p>근육은 혈관이 촘촘하게 들어차 있어 세 조직 중 가장 빨리 회복됩니다. 가벼운 손상은 대개 1~4주, 근섬유가 일부 찢어진 경우에도 보통 <b>2개월 안</b>에 일상으로 돌아옵니다.</p>
    <p>진료실에서 자주 보는 근육 손상은 다음과 같습니다.</p>
    <figure><img src="images/column-1-muscle.jpg" alt="근육 손상의 흔한 예: 담 결림, 허리 근육 염좌, 종아리 근육 손상, 햄스트링 손상" width="1080" height="1530" loading="lazy"><figcaption>담 결림, 허리 근육 염좌, 종아리 근육 손상, 햄스트링 손상</figcaption></figure>
    <p>주의할 점은 <b>재발</b>입니다. 통증이 빨리 줄다 보니 예전처럼 운동하다가 같은 자리를 다시 다치는 경우가 많습니다. 특히 햄스트링은 재손상이 잦은 부위로 알려져 있어, 통증이 없어진 뒤에도 스트레칭과 근력 운동으로 마무리하는 것이 중요합니다.</p>

    <h2 id="s5"><span class="num">2. 인대 손상</span>: 통증은 몇 주, 튼튼해지기까지는 몇 달</h2>
    <p>인대는 뼈와 뼈를 이어 관절이 엉뚱한 방향으로 꺾이지 않게 잡아 주는 끈입니다. 근육보다 혈액 공급이 적어서, 붓기와 통증은 몇 주면 가라앉아도 인대가 원래의 튼튼함을 되찾기까지는 <b>수개월</b>이 걸립니다.</p>
    <p>인대 손상은 정도에 따라 세 단계로 나눕니다.</p>
    <figure><img src="images/column-1-ligament.jpg" alt="인대 손상 단계별 회복 기간: 1도 1~3주, 2도 3~8주, 3도 3개월 이상" width="1080" height="1330" loading="lazy"><figcaption>인대 손상 단계별 회복 기간 · 1도 1~3주, 2도 3~8주, 3도 3개월 이상</figcaption></figure>
    <p>진료실에서 자주 보는 인대 손상은 이렇습니다.</p>
    <ul class="checks">
      <li>{ic("check")}<span><b>발목 염좌</b> · 계단이나 길에서 발목이 안쪽으로 꺾이며 바깥쪽 인대가 다칩니다. 가장 흔한 인대 손상입니다.</span></li>
      <li>{ic("check")}<span><b>무릎 내측측부인대 손상</b> · 운동 중 무릎이 바깥쪽으로 꺾일 때 무릎 안쪽에 통증이 생깁니다.</span></li>
      <li>{ic("check")}<span><b>손목·손가락 염좌</b> · 넘어지며 손을 짚거나, 공에 손가락이 부딪혀 생깁니다.</span></li>
    </ul>
    <p>발목 염좌는 "그냥 삔 것"으로 여겨 대충 넘기기 쉽습니다. 하지만 충분히 회복되지 않으면 같은 발목을 반복해서 삐는 <b>만성 발목 불안정성</b>으로 이어질 수 있습니다. 초기에는 보호하고, 붓기가 빠진 뒤에는 균형 운동과 발목 근력 운동을 해야 합니다.</p>

    <h2 id="s6"><span class="num">3. 힘줄 손상</span>: 셋 중 회복이 가장 느립니다.</h2>
    <p>힘줄은 근육 끝이 뼈에 붙는 단단한 끈입니다.<br><b>인대처럼 혈액 공급이 적은 데다, 일상 생활에서 계속 부하를 받게 됩니다.</b><br>그래서 회복이 가장 느려 보통 <b>6주~3개월</b>, 오래 끌어 만성이 된 경우는 <b>6개월 이상</b> 걸리기도 합니다.</p>
    <p>힘줄 문제는 한 번에 크게 다치기보다 <b>같은 동작을 반복</b>하며 조금씩 상하는 경우가 대부분입니다.<br>염증보다 힘줄 조직이 약해지는 변성(건병증)이 중심이라, <b><u>원인 동작을 계속하는 한 잘 낫지 않습니다.</u></b></p>
    <figure><img src="images/column-1-tendon2.jpg" alt="진료실에서 자주 보는 힘줄 질환: 테니스엘보(외측상과염, 팔꿈치 바깥쪽), 골프엘보(내측상과염, 팔꿈치 안쪽), 회전근개 건병증(어깨), 아킬레스건염(발뒤꿈치 위), 슬개건염(점퍼스 니, 무릎 앞쪽)" width="1080" height="1746" loading="lazy"><figcaption>테니스엘보, 골프엘보, 회전근개 건병증, 아킬레스건염, 슬개건염</figcaption></figure>
    <p>힘줄은 무조건 쉬게 하면 오히려 약해집니다. 통증이 심한 시기를 넘기면 <b>아프지 않은 범위에서 조금씩 부하</b>를 늘리는 운동이 회복을 돕습니다. <b>원인이 된 반복 동작을 줄이는 것</b>도 치료만큼 중요합니다.</p>

    <h2 id="s7">통증이 사라졌다고 다 나은 것은 아닙니다</h2>
    <p>세 조직 모두 <b>통증이 먼저 줄고, 조직의 회복은 그 뒤에도 계속</b>됩니다. 위 그래프에서 인대와 힘줄의 곡선이 한참 뒤에야 100%에 가까워지는 이유입니다. "이제 안 아프니 됐다" 하고 치료를 멈추거나 무리하면 재발이나 만성화로 이어지기 쉽습니다.</p>
    <p>회복을 돕는 생활 수칙입니다.</p>
    <ol class="steps">
      <li><b>초기 2~3일은 보호하기</b><br>붓고 열감이 있으면 무리하지 말고, 아픈 동작을 피합니다.</li>
      <li><b>통증이 가라앉으면 조금씩 움직이기</b><br>완전히 쉬는 기간이 길수록 근력과 관절 움직임이 떨어집니다.</li>
      <li><b>원인 동작 줄이기</b><br>특히 힘줄 질환은 반복 동작을 줄이지 않으면 잘 낫지 않습니다.</li>
      <li><b>마무리 운동</b><br>통증이 없어진 뒤에도 스트레칭, 근력, 균형 운동으로 재발을 막습니다.</li>
    </ol>
    <p>한의원에서는 손상 조직과 회복 단계에 맞춰 <b>침, 약침, 부항, 뜸, 물리치료</b> 등을 병행해 통증을 줄이고 회복을 돕습니다. 손상 부위와 정도에 따라 치료 횟수와 기간이 달라지므로, 진료 때 안내드린 일정을 지켜 주시는 것이 가장 중요합니다.</p>

    <h2 id="s8">마치며</h2>
    <p>정리하면 <b>근육은 빠르게, 인대는 중간, 힘줄은 가장 느리게</b> 회복됩니다. 같은 "삐끗"이라도 어디를 다쳤는지에 따라 치료 계획이 달라지니, 통증이 1~2주 넘게 이어지거나 붓기·멍이 심하면 꼭 진료를 받아 보시길 권합니다.</p>
    <div class="warn" role="note">{ic("alert")}<p><b>이럴 때는 영상 검사를 먼저 받으세요.</b> 관절이 흔들리거나, 체중을 전혀 싣지 못하거나, "뚝" 소리와 함께 힘이 빠졌다면 골절이나 완전 파열일 수 있습니다.</p></div>
    <p class="tags"><span>#정관한의원</span><span>#정관고려한의원</span><span>#정관인대</span><span>#정관근육통</span><span>#정관발목</span><span>#정관테니스엘보</span><span>#정관회전근개</span><span>#인대힘줄발목</span></p>
  </div>

  <aside class="ccta" aria-label="진료 안내">
    <div class="ccta-top"><img src="images/c9de5ada.png" alt="" width="220" height="220"><div><b>정관고려한의원 진료 안내</b><p>예약 없이 방문하세요. {ADDR}</p></div></div>
    <div class="acts"><a class="btn-gold" href="{TEL_HREF}">{ic("phone")}전화 문의 {TEL}</a><a class="btn-line" href="index.html#hours">진료시간</a></div>
  </aside>

  <p class="src-link"><a href="https://blog.naver.com/jgkorea8275/224452067401" target="_blank" rel="noopener">네이버 블로그에서 원문 보기{ic("ext")}</a></p>

  <div class="tools">
    <a class="back" href="index.html#column">{ic("back")}목록으로</a>
    <div class="r">
      <button type="button" data-share>{ic("share")}공유하기</button>
      <button type="button" data-font aria-label="글자 크기: 보통"><span class="ga" aria-hidden="true">가</span>글자 크기</button>
    </div>
  </div>

  <nav class="related" aria-label="진료 분야 바로가기">
    <h2>관련 진료 분야</h2>
    <ul>
      <li><a href="column-2.html">칼럼 · 근육통 회복 속도를 결정하는 네가지 요인{ic("chev")}</a></li>
      <li><a href="index.html#area">근육통·관절통{ic("chev")}</a></li>
      <li><a href="index.html#area">담결림{ic("chev")}</a></li>
      <li><a href="index.html#treatment">약침·부항·뜸{ic("chev")}</a></li>
      <li><a href="index.html#doctor">원장 소개{ic("chev")}</a></li>
    </ul>
  </nav>
</main>
{footer()}
{dock('index.html')}
<script src="assets/site.js?v={VER}"></script>
{ANALYTICS}
</body>
</html>
'''
    return head + '\n' + body

ESSAY2_URL = 'https://jgkorea8275.co.kr/essay-2.html'
ESSAY2_TITLE = '내 몸 안의 의사를 믿는다는 것'
ESSAY2_LD = {"@context": "https://schema.org", "@type": "Article", "headline": "내 몸 안의 의사를 믿는다는 것 — 우리는 왜 통증을 없애는 데만 익숙해졌을까요", "datePublished": "2026-10-28", "image": ["https://jgkorea8275.co.kr/images/essay-2-hero.jpg"], "mainEntityOfPage": "https://jgkorea8275.co.kr/essay-2.html", "author": {"@type": "Person", "name": "박장우", "jobTitle": "한방재활의학과 전문의, 한의학박사"}, "publisher": {"@type": "Organization", "name": "정관고려한의원", "logo": {"@type": "ImageObject", "url": "https://jgkorea8275.co.kr/favicon.png"}}}
ESSAY2_CRUMB = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "정관고려한의원", "item": "https://jgkorea8275.co.kr/"},
    {"@type": "ListItem", "position": 2, "name": "칼럼 및 에세이", "item": "https://jgkorea8275.co.kr/#column"},
    {"@type": "ListItem", "position": 3, "name": "내 몸 안의 의사를 믿는다는 것", "item": "https://jgkorea8275.co.kr/essay-2.html"}]}

def essay2():
    title = ESSAY2_TITLE
    desc = '우리는 왜 통증을 없애는 데만 익숙해졌을까요? 통증은 몸이 보내는 편지입니다. 한방재활의학과 전문의 박장우 원장의 에세이.'
    toc = [('e1', '우리는 왜 통증을 없애는 데만 익숙해졌을까요?'), ('e2', '감기에 걸리면 저는 일찍 잠자리에 듭니다'), ('e3', '통증은 몸이 보내는 편지입니다'),
           ('e4', '자연 치유력이라는 오케스트라'), ('e5', '저는 현대의학의 놀라운 발전을 존중합니다'), ('e6', '몸을 믿는다는 것')]
    toc_html = ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    head = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} | 에세이 | 정관고려한의원</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<meta name="theme-color" content="#171511">
<link rel="canonical" href="{ESSAY2_URL}">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="alternate" type="application/rss+xml" title="정관고려한의원 칼럼·에세이" href="https://jgkorea8275.co.kr/rss.xml">
<meta property="og:type" content="article">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="정관고려한의원">
<meta property="og:title" content="{title} | 정관고려한의원 에세이">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{ESSAY2_URL}">
<meta property="og:image" content="https://jgkorea8275.co.kr/images/essay-2-hero.jpg">
<meta property="og:image:width" content="743">
<meta property="og:image:height" content="743">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://jgkorea8275.co.kr/images/essay-2-hero.jpg">
<meta property="article:published_time" content="2026-10-28">
<script type="application/ld+json">{json.dumps(ESSAY2_LD, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(ESSAY2_CRUMB, ensure_ascii=False)}</script>
{FONTS}
<link rel="stylesheet" href="assets/site.css?v={VER}">
</head>'''

    body = f'''<body class="has-dock">
{SPRITE}
{header('index.html')}
<div class="cbanner">
  <img src="images/column-banner.jpg" alt="" width="1600" height="900">
  <div class="wrap"><p class="ttl">에세이</p><p>진료실에서 품어 온 생각을 씁니다.</p></div>
</div>
<main class="art essay">
  <a class="back" href="index.html#column">{ic("back")}목록으로</a>
  <header class="art-head">
    <span class="chip">에세이 02</span>
    <h1>{title}</h1>
    <p class="art-sub">우리는 왜 통증을 없애는 데만 익숙해졌을까요?</p>
    <p class="art-meta"><span><time datetime="2026-10-28">2026.10.28</time></span><span>한방재활의학과 전문의 · 한의학박사 박장우</span></p>
  </header>

  <details class="toc toc-solo"><summary>목차 보기{ic("down")}</summary><ol>{toc_html}</ol></details>

  <div class="prose" data-size="0">
    <figure><img src="images/essay-2-hero.jpg" alt="에세이 02 · 내 몸 안의 의사를 믿는다는 것 · 우리는 왜 통증을 없애는 데만 익숙해졌을까요?" width="743" height="743"></figure>

    <h2 id="e1">우리는 왜 통증을 없애는 데만 익숙해졌을까요?</h2>
    <p>진료를 하다 보면 마음 한편이 안타까울 때가 있습니다.<br>허리가 아파도 진통제, 어깨가 아파도 진통제, 무릎이 아파도 진통제.<br>몸 어딘가에 통증이 생기면 우선 약을 먹어 없애야 한다고 생각하는 분들이 많습니다.</p>
    <p>물론 아픈 것을 참는 일은 괴롭습니다. 당장 일을 해야 하고, 가족을 돌봐야 하고, 밤에는 잠도 자야 합니다. 그런 분들에게 진통제가 얼마나 고마운 존재인지 저 역시 잘 알고 있습니다.</p>
    <p>하지만 한의사로서 오랫동안 환자를 진료하면서 제 마음속에 떠나지 않는 질문이 하나 있습니다.<br><b>우리 몸은 왜 통증을 만들어 내는 것일까요? 그 통증은 정말 무조건 없애야 할 적일까요?</b><br>우리는 통증을 없애는 일에 너무 익숙해진 나머지, 정작 몸이 통증을 통해 전하려는 이야기를 듣지 못하고 있는 것은 아닐까요?</p>

    <h2 id="e2">감기에 걸리면 저는 일찍 잠자리에 듭니다</h2>
    <p>저는 지금까지 살아오면서 감기 때문에 양약을 먹어본 적이 학생 때 말고는 없습니다.<br>감기에 걸리면 몸을 따뜻하고 편안하게 하고, 평소보다 일찍 잠자리에 듭니다. 가능하면 충분히 쉬고 많이 잡니다.<br>제 몸의 면역체계가 바이러스에 대응할 수 있도록 시간을 주는 것입니다.</p>
    <p>실제로 저는 감기에 자주 걸리지 않는 편이고, 몇 년에 한 번 감기에 걸리더라도 대개 하루나 며칠 정도 쉬면 회복되곤 했습니다.<br>물론 이것은 어디까지나 제 자신의 경험입니다. 감기의 경과는 사람마다 다르고, 충분한 휴식만으로 해결되지 않는 감염도 있습니다.</p>
    <p>그럼에도 제가 감기에 걸렸을 때 가장 먼저 하는 일은 약을 찾는 것이 아니라, <b>내 몸이 회복에 집중할 수 있는 환경을 만들어 주는 것</b>입니다.<br>우리 몸에는 수많은 면역세포가 있고, 감염을 감지하고 대응하며 손상된 조직을 복구하는 정교한 체계가 있습니다.<br>우리가 잠든 사이에도 그 체계는 쉬지 않고 일합니다.<br>저는 그 놀라운 생명력을 신뢰합니다.</p>

    <h2 id="e3">통증은 몸이 보내는 편지입니다</h2>
    <p>발목을 접질렀다고 생각해 보겠습니다.<br>발목이 붓고 아프면 우리는 본능적으로 절뚝거리며 걷습니다. 아픈 발에 체중을 덜 싣고, 무리하게 뛰지 않으려고 합니다.<br>왜 그럴까요?<br><b>손상된 조직을 더 다치지 않도록 보호하려는 반응</b>이기 때문입니다.</p>
    <p>염증도 마찬가지입니다.<br>우리 몸에 손상이 생기면 면역세포들이 모여 손상된 조직을 정리하고, 회복에 필요한 여러 신호를 주고 받습니다. <b>염증은 단순히 나쁜 것이 아니라 조직 치유 과정의 중요한 일부</b>입니다.<br>물론 염증이 지나치거나 오래 지속되면 오히려 조직을 손상시킬 수 있습니다.<br>통증 역시 언제나 실제 손상 정도를 정확하게 알려주는 것은 아닙니다.</p>
    <p>하지만 적어도 한 가지는 분명합니다.<br><b>통증과 염증은 이유 없이 생겨나는 불필요한 현상만은 아니라는 것입니다.</b></p>
    <p>저는 통증을 몸이 보내는 한 통의 편지라고 생각합니다.</p>
    <blockquote class="letter"><p>'지금은 조금 쉬어 주세요.'</p><p>'이 부위에 무리가 가고 있습니다.'</p><p>'회복할 시간이 필요합니다.'</p></blockquote>
    <p>그런데 우리는 편지의 내용을 읽기도 전에, 그 편지를 없애는 데만 급급한 것은 아닐까요?</p>

    <h2 id="e4">자연 치유력이라는 오케스트라</h2>
    <p>우리 몸의 회복 과정을 생각할 때마다 저는 한 편의 오케스트라를 떠올립니다.</p>
    <p>면역세포는 제 역할을 하고, 혈관은 필요한 물질을 운반하며, 손상된 조직에서는 새로운 세포와 단백질이 만들어집니다.<br>신경계와 호르몬계는 그 모든 과정에 관여합니다.<br>수많은 생리적 반응이 서로 영향을 주고받으며 생명이라는 음악을 연주하고 있는 것입니다.<br>저는 이것이 <b>신이 우리에게 선물한 경이로운 자연치유력</b>이라고 생각합니다.</p>
    <p>그래서 제 몸에 약물을 넣는 일에는 유난히 신중합니다.<br>특히 몸이 스스로 회복하려는 과정에 약물이 불필요하게 개입하는 것은, 정교하게 연주되는 오케스트라에 뜻하지 않은 불협화음을 더하는 것처럼 느껴질 때가 있습니다.</p>
    <p>근골격계 통증이 생겼을 때도 저는 소염진통제를 복용하기보다 침과 부항, 습식부항 등의 방법으로 관리해 왔습니다.<br>이것은 제 몸을 대하는 저만의 신념이자 선택입니다.</p>
    <p>그렇다고 모든 약물이 자연치유를 방해한다는 뜻은 아닙니다. 약물은 때로 생명을 구하고, 지나친 염증을 조절하며, 심한 통증으로 잠조차 이루지 못하는 환자에게 회복할 여유를 만들어 줍니다.<br>저는 약 자체를 부정하는 것이 아닙니다.</p>
    <p><b>다만 약을 쓰기 전에 우리 몸이 스스로 회복할 수 있는 가능성을 먼저 살펴보자는 것입니다.</b></p>

    <h2 id="e5">저는 현대의학의 놀라운 발전을 존중합니다</h2>
    <p>여기까지 읽으신 분들은 제가 현대의학이나 약물을 무조건 반대한다고 생각하실지도 모르겠습니다.<br>그렇지는 않습니다.</p>
    <p>현대의학이 이룩한 성과는 참으로 놀랍습니다.<br>심각한 골절을 수술로 고정하고, 파열된 조직을 봉합하고, 신경을 압박하는 병변을 제거하는 수술은 수많은 사람의 삶을 바꾸어 놓았습니다.<br>과거라면 평생 장애를 안고 살아야 했을 환자가 수술을 통해 다시 걷고 일상으로 돌아가는 모습을 보면 현대에 살고 있다는 것이 얼마나 큰 축복인지 느낍니다.</p>
    <p>저 역시 수술이 꼭 필요한 환자에게는 적절한 진료를 받도록 안내합니다.<br>약물치료가 꼭 필요한 상황도 분명히 있습니다.<br>다만 제가 아쉬워하는 것은 현대의학 자체가 아니라, <b>어떤 질환이든 약이나 수술부터 떠올리고 다른 가능성은 충분히 살펴보지 않는 우리의 익숙한 태도</b>입니다.</p>
    <p>수술이 필요한 병이 있고, 약물이 꼭 필요한 병이 있습니다.<br>반대로 수술 없이도 회복할 수 있는 질환이 있고, 약물을 사용하지 않거나 최소한으로 사용하면서 관리할 수 있는 통증도 있습니다.</p>
    <p>중요한 것은 어느 의학이 더 우월한가를 따지는 것이 아닙니다.<br>환자에게 지금 무엇이 가장 필요하고, 무엇이 가장 안전하며, 장기적으로 어떤 치료가 도움이 되는지를 판단하는 것입니다.</p>

    <h2 id="e6">몸을 믿는다는 것</h2>
    <p>저는 우리 몸을 하나의 기계라고 생각하지 않습니다.<br>어느 부품이 고장 나면 교체하고, 이상 신호가 울리면 소리만 꺼 버리면 되는 기계 말입니다.</p>
    <p>우리 몸은 끊임없이 변화하고, 적응하고, 회복하려는 살아 있는 존재입니다.<br>상처가 나면 새살이 돋고, 부러진 뼈는 다시 붙으며, 적절한 운동을 반복하면 근육과 뼈는 더 큰 부하를 견딜 수 있도록 적응합니다.<br>그 놀라운 능력을 생각할 때마다 저는 생명에 대한 경외감을 느낍니다.</p>
    <p>물론 자연치유력에도 한계는 있습니다. 모든 병이 저절로 낫는 것은 아니며, 때로는 적극적인 의학적 개입이 반드시 필요합니다.<br>그러나 그 한계를 인정하는 것과 우리 몸의 능력을 처음부터 과소평가하는 것은 전혀 다른 이야기입니다.</p>
    <p>저는 환자들이 자신의 몸을 조금 더 신뢰했으면 좋겠습니다.<br>통증이 생겼을 때 무조건 두려워하거나 없애려고 하기보다, 내 몸에 어떤 부담이 쌓였는지, 무엇이 부족했는지, 어떻게 해야 회복할 수 있을지 한 번쯤 생각해 보았으면 합니다.</p>
    <p><b>우리 몸 안에는 이미 훌륭한 치유의 능력이 있습니다.</b></p>
    <p><b>의료의 역할은 때로 그 능력을 대신하는 것이 아니라, 그 능력이 충분히 발휘될 수 있도록 돕는 것이라고 저는 믿습니다.</b></p>
    <p>그것이 제가 침을 놓는 이유이며, 오늘도 환자를 진료하는 마음입니다.</p>
    <p class="sign">한방재활의학과 전문의 · 한의학박사 <b>박장우</b></p>
  </div>

  <aside class="ccta" aria-label="진료 안내">
    <div class="ccta-top"><img src="images/c9de5ada.png" alt="" width="220" height="220"><div><b>정관고려한의원 진료 안내</b><p>예약 없이 방문하세요. {ADDR}</p></div></div>
    <div class="acts"><a class="btn-gold" href="{TEL_HREF}">{ic("phone")}전화 문의 {TEL}</a><a class="btn-line" href="index.html#hours">진료시간</a></div>
  </aside>

  <p class="src-link"><a href="https://blog.naver.com/jgkorea8275/224456800912" target="_blank" rel="noopener">네이버 블로그에서 원문 보기{ic("ext")}</a></p>

  <div class="tools">
    <a class="back" href="index.html#column">{ic("back")}목록으로</a>
    <div class="r">
      <button type="button" data-share>{ic("share")}공유하기</button>
      <button type="button" data-font aria-label="글자 크기: 보통"><span class="ga" aria-hidden="true">가</span>글자 크기</button>
    </div>
  </div>

  <nav class="related" aria-label="함께 보기">
    <h2>함께 보기</h2>
    <ul>
      <li><a href="essay-4.html">에세이 · 불은 그대로인데 사이렌만 끄고 있지는 않습니까?{ic("chev")}</a></li>
      <li><a href="essay-3.html">에세이 · 몸은 쉬라고 하는데, 삶은 멈출 수 없을 때{ic("chev")}</a></li>
      <li><a href="column-1.html">칼럼 · 삐끗했는데 왜 이렇게 오래 가죠?{ic("chev")}</a></li>
      <li><a href="index.html#treatment">치료 방법 · 침·약침·부항{ic("chev")}</a></li>
      <li><a href="index.html#doctor">원장 소개{ic("chev")}</a></li>
    </ul>
  </nav>
</main>
{footer()}
{dock('index.html')}
<script src="assets/site.js?v={VER}"></script>
{ANALYTICS}
</body>
</html>
'''
    return head + '\n' + body

ESSAY3_URL = 'https://jgkorea8275.co.kr/essay-3.html'
ESSAY3_TITLE = '몸은 쉬라고 하는데, 삶은 멈출 수 없을 때'
ESSAY3_LD = {"@context": "https://schema.org", "@type": "Article", "headline": "몸은 쉬라고 하는데, 삶은 멈출 수 없을 때 — 아픔을 참아가며 일하는 사람들을 위한 과사용 증후군 이야기", "datePublished": "2026-10-30", "image": ["https://jgkorea8275.co.kr/images/essay-3-hero.jpg"], "mainEntityOfPage": "https://jgkorea8275.co.kr/essay-3.html", "author": {"@type": "Person", "name": "박장우", "jobTitle": "한방재활의학과 전문의, 한의학박사"}, "publisher": {"@type": "Organization", "name": "정관고려한의원", "logo": {"@type": "ImageObject", "url": "https://jgkorea8275.co.kr/favicon.png"}}}
ESSAY3_CRUMB = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "정관고려한의원", "item": "https://jgkorea8275.co.kr/"},
    {"@type": "ListItem", "position": 2, "name": "칼럼 및 에세이", "item": "https://jgkorea8275.co.kr/#column"},
    {"@type": "ListItem", "position": 3, "name": "몸은 쉬라고 하는데, 삶은 멈출 수 없을 때", "item": "https://jgkorea8275.co.kr/essay-3.html"}]}

def essay3():
    title = ESSAY3_TITLE
    desc = '일을 쉴 수 없는 분들의 근육·힘줄 통증, 과사용 증후군 이야기. 한방재활의학과 전문의 박장우 원장의 에세이.'
    toc = [('e1', '늘 하던 일인데, 왜 갑자기 아플까요'), ('e2', '통증이 사라지는 것은 치료의 끝이 아닙니다'), ('e3', '일을 줄일 수 없다면, 몸의 능력을 키워야 합니다'),
           ('e4', '제가 침을 놓는 이유, 그리고 치료실 밖의 치료'), ('e5', '쉬라는 말 대신 해주고 싶은 말')]
    toc_html = ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    head = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} | 에세이 | 정관고려한의원</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<meta name="theme-color" content="#171511">
<link rel="canonical" href="{ESSAY3_URL}">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="alternate" type="application/rss+xml" title="정관고려한의원 칼럼·에세이" href="https://jgkorea8275.co.kr/rss.xml">
<meta property="og:type" content="article">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="정관고려한의원">
<meta property="og:title" content="{title} | 정관고려한의원 에세이">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{ESSAY3_URL}">
<meta property="og:image" content="https://jgkorea8275.co.kr/images/essay-3-hero.jpg">
<meta property="og:image:width" content="743">
<meta property="og:image:height" content="743">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://jgkorea8275.co.kr/images/essay-3-hero.jpg">
<meta property="article:published_time" content="2026-10-30">
<script type="application/ld+json">{json.dumps(ESSAY3_LD, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(ESSAY3_CRUMB, ensure_ascii=False)}</script>
{FONTS}
<link rel="stylesheet" href="assets/site.css?v={VER}">
</head>'''

    body = f'''<body class="has-dock">
{SPRITE}
{header('index.html')}
<div class="cbanner">
  <img src="images/column-banner.jpg" alt="" width="1600" height="900">
  <div class="wrap"><p class="ttl">에세이</p><p>진료실에서 품어 온 생각을 씁니다.</p></div>
</div>
<main class="art essay">
  <a class="back" href="index.html#column">{ic("back")}목록으로</a>
  <header class="art-head">
    <span class="chip">에세이 03</span>
    <h1>{title}</h1>
    <p class="art-sub">아픔을 참아가며 일하는 사람들을 위한, 과사용 증후군 이야기</p>
    <p class="art-meta"><span><time datetime="2026-10-30">2026.10.30</time></span><span>한방재활의학과 전문의 · 한의학박사 박장우</span></p>
  </header>

  <details class="toc toc-solo"><summary>목차 보기{ic("down")}</summary><ol>{toc_html}</ol></details>

  <div class="prose" data-size="0">
    <figure><img src="images/essay-3-hero.jpg" alt="에세이 · 몸은 쉬라고 하는데, 삶은 멈출 수 없을 때 · 아픔을 참아가며 일하는 사람들을 위한, 과사용 증후군 이야기" width="743" height="743"></figure>

    <p class="lead-quote">"원장님, 일을 좀 쉬면 나을까요?"</p>
    <p>진료실에서 자주 듣는 질문입니다. 팔꿈치가 아픈 식당 사장님, 하루 종일 서서 일하는 미용사, 무거운 짐을 나르는 택배기사, 손목이 아픈 주부까지. 크게 다친 적은 없는데 근육과 힘줄, 관절에 통증이 생긴 분들이 많습니다.</p>
    <p>그런 분들께 제가 "당분간은 일을 좀 줄이셔야겠습니다"라고 말씀드리면, 돌아오는 대답은 대개 비슷합니다.<br>"쉬면 좋죠. 그런데 일을 안 하면 먹고살 수가 없잖아요."</p>
    <p>저는 의학적으로 무엇이 필요한지 알고 있습니다. 하지만 환자가 처한 현실도 알고 있습니다.<br><b>몸은 쉬어야 낫는데, 삶은 그 사람에게 쉴 시간을 허락하지 않습니다.</b></p>

    <h2 id="e1">늘 하던 일인데, 왜 갑자기 아플까요</h2>
    <p>"제가 이 일을 하루 이틀 한 것도 아닌데 왜 이제 와서 아픈 걸까요?"</p>
    <p>20년 동안 식당 일을 하신 분, 30년 넘게 농사를 지으신 분도 같은 질문을 하십니다.<br>이때 설명이 되는 개념이 '<b>과사용 증후군</b>'입니다.</p>
    <p>우리 몸의 근육과 힘줄, 관절은 매일 일정한 부하를 견딥니다. 적절하게 사용하면 그 자극에 적응하고, 충분히 쉬면 다음 활동을 준비합니다. 운동을 꾸준히 하면 근육이 강해지고 뼈가 부하에 맞게 구조를 바꾸는 것이 그 예입니다.<br>문제는 사용량이 지나치거나 회복할 시간이 부족할 때 생깁니다.</p>
    <p><b>과사용 증후군은 조직에 가해지는 부하와 그것을 감당하고 회복하는 능력 사이의 균형이 무너진 상태입니다.</b></p>
    <p>그래서 일의 양이 같아도 어느 날부터 아플 수 있습니다.<br>나이가 들며 근력이 줄고, 잠이 부족하고, 회복 능력이 떨어지면 <b>예전에는 거뜬했던 일이 버거워집니다</b>. 일은 그대로인데 몸이 감당할 수 있는 능력이 줄어든 것입니다.</p>

    <h2 id="e2">통증이 사라지는 것은 치료의 끝이 아닙니다</h2>
    <p>통증은 몸이 보내는 경고입니다.<br>"이제 조금 쉬어야겠습니다", "지금 너무 무리하고 있습니다"라는 신호입니다.</p>
    <p>하지만 생계를 책임지는 분들에게 이 신호는 따르기 쉬운 조언이 아닙니다.<br>팔꿈치가 아프다고 식당 문을 닫을 수 없으니, 하루를 버티고 또 하루를 버팁니다.<br>처음엔 일할 때만 아프던 것이 쉴 때도 아프고, 밤에 잠을 설칠 정도가 되어서야 병원을 찾으십니다.</p>
    <p>저는 이런 환자분들을 볼 때마다 안타깝습니다.<br>건강을 소홀히 해서 아픈 것이 아니라, <b>살아가기 위해 몸을 쓰다가 그 몸이 아파진 분들이기 때문입니다.</b></p>
    <p>이분들에게 진통제는 참 고마운 약입니다.<br>심한 통증은 수면과 활동, 회복운동까지 방해하니 필요할 때는 약의 도움을 받는 것이 합리적입니다.<br>다만 통증이 줄었다고 손상된 조직이 회복된 것은 아닙니다. 힘줄이 감당하기 어려운 부하를 계속 받는 상황에서 통증만 가려진다면 근본 문제는 그대로 남습니다.</p>
    <p>제가 안타까운 것은 진통제가 아니라, <b>통증이 사라지는 것을 치료의 끝이라고 여기는 태도입니다.</b> 왜 아파졌는지, 같은 일을 계속하려면 몸을 어떻게 회복시켜야 하는지가 빠져 있으면 통증은 다시 찾아옵니다.</p>

    <h2 id="e3">일을 줄일 수 없다면, 몸의 능력을 키워야 합니다</h2>
    <p>과사용 증후군을 다루는 방법은 두 가지입니다.<br>하나는 몸에 <b>가해지는 부담을 줄이는 것</b>이고,<br>다른 하나는 몸이 그 부담을 <b>감당하는 능력을 높이는 것</b>입니다.</p>
    <p>둘을 함께 하는 것이 가장 좋지만, 일을 줄이기 어려운 분에게는 두 번째가 더 중요해집니다.<br>저는 이것을 위해 두 가지를 강조합니다.</p>
    <p>첫째는 <b>잠</b>입니다.<br>수면 중에 우리 몸은 낮 동안 지친 기능을 조절하고, 면역과 호르몬의 균형을 맞추고, 손상된 조직을 복구합니다. 그런데 몸을 많이 쓰는 분일수록 일찍 출근하고 늦게 퇴근하느라 잠이 부족합니다. 그래서 저는 다른 무엇보다 잠자는 시간을 먼저 확보하시라고 말씀드립니다.</p>
    <p>둘째는 <b>지친 몸의 회복을 돕는 것</b>으로, 한의학에서는 <b>보약</b>이 이 역할을 해 왔습니다.<br>과로로 허약해진 몸을 살필 때 보기(補氣), 보혈(補血), 보간신(補肝腎)의 원리를 활용합니다.</p>
    <ul class="dl">
      <li><b>보기(補氣)</b> 지친 기운을 북돋우는 것입니다. 일을 하는 데도, 회복하는 데도 에너지가 필요합니다.</li>
      <li><b>보혈(補血)</b> 몸을 충분히 영양하는 것입니다. 손상된 조직이 회복되려면 산소와 영양, 새로운 단백질을 만드는 과정이 필요합니다.</li>
      <li><b>보간신(補肝腎)</b> 근육과 힘줄, 뼈의 건강을 돌보는 것입니다. 이 조직들은 끊임없이 합성과 분해를 거치며 손상을 복구하고 새로운 부하에 적응합니다.</li>
    </ul>
    <p>물론 이 개념들이 현대 생리학의 특정 기능과 정확히 일치한다는 뜻은 아닙니다. 다만 한의학이 오래 중시해 온 기력과 근골의 건강을 오늘의 생리학 관점에서 다시 생각해 볼 수 있다는 이야기입니다.</p>
    <p>낮에는 어쩔 수 없이 몸을 써도, <b>밤에는 충분히 쉬게 하고 지친 몸을 돌보는 것</b>.<br>일을 줄일 수 없는 분께는 이것이 가장 현실적인 회복의 출발점입니다.</p>

    <h2 id="e4">제가 침을 놓는 이유, 그리고 치료실 밖의 치료</h2>
    <p>저는 이런 환자분들께 침치료와 적절한 약침치료를 합니다.<br>단순히 통증을 없애려는 것만은 아닙니다. 아파서 움직이지 못하던 분이 조금 더 편안하게 움직일 수 있어야 적절한 운동을 시작할 수 있고, 근육과 힘줄이 다시 부하에 적응할 기회도 생기기 때문입니다. 그런 의미에서 침치료는 적절한 재활과 결합될 때 회복을 돕는 유용한 도구가 된다고 생각합니다.</p>
    <p>하지만, <b>침을 맞는 시간은 길어야 수십 분</b>이고<br><b>일터에서 몸을 쓰는 시간은 여덟 시간, 열 시간, 때로는 그 이상</b>입니다.<br>그래서 일상에서 할 수 있는 작은 변화를 실천하는 것도 치료의 일부라고 생각합니다.</p>
    <ul class="checks">
      <li>{ic("check")}<span>같은 동작을 오랫동안 반복한다면 <b>중간중간 잠깐씩 쉬기</b></span></li>
      <li>{ic("check")}<span>무거운 물건을 들 때 몸 전체의 힘을 효율적으로 쓰기</span></li>
      <li>{ic("check")}<span>그리고 무엇보다 <b>충분히 자고, 몸이 회복할 시간을 마련하기</b></span></li>
    </ul>
    <p>거창하지 않지만 이런 변화가 쌓이면 몸의 부담이 줄고 회복이 빨라집니다.<br>어떤 환자분께는 한 번의 침치료보다 이런 습관이 장기적으로 더 중요하기도 합니다.</p>
    <p>제가 바라는 것은 침을 맞는 동안만 덜 아픈 몸이 아니라, 치료가 끝난 뒤에도 일상을 견뎌내는 몸입니다.</p>

    <h2 id="e5">쉬라는 말 대신 해주고 싶은 말</h2>
    <p>진료실에서 "쉬셔야 합니다"라고 말하기는 어렵지 않습니다.<br>어려운 것은 그분이 왜 쉴 수 없는지를 이해하는 일입니다.</p>
    <p>자녀의 학비를 벌어야 하는 분, 가족의 생활비를 책임지는 분, 하루만 문을 닫아도 그날 수입이 사라지는 분께 무조건 일을 그만두라고 할 수는 없습니다.<br>그렇다고 몸의 신호를 계속 무시하라고 할 수도 없습니다.</p>
    <p>같은 팔꿈치 통증도 취미로 테니스를 치는 사람과 하루 종일 무거운 프라이팬을 드는 사람에게는 그 의미가 다릅니다.<br>병은 같아도 그 병을 안고 사는 삶이 다르기 때문입니다.</p>
    <p>저는 의학이 병을 치료하는 기술이면서 아픈 사람의 삶을 이해하는 일이기도 하다고 믿습니다.</p>
    <p>그래서 저는 환자와 함께 현실적인 방법을 찾으려 합니다.</p>
    <p><b>가능한 만큼 부담을 줄이고, 통증을 조절하고, 약해진 부분을 조금씩 회복시키는 것.</b></p>
    <p>당장 모든 일을 멈출 수 없더라도 몸이 회복할 기회를 조금씩 만들어 가는 것입니다.</p>
    <p>기계는 오래 쓰면 닳아 없어지지만, <b>우리 몸은 적절한 휴식과 영양과 시간이 주어지면 스스로를 유지하고 복구하는 능력이 있습니다.</b></p>
    <p>환자분들이 그 능력을 믿고 자신의 몸을 조금 더 아끼셨으면 합니다.<br>일하는 것도, 가족을 돌보는 것도, 삶을 즐기는 것도 결국 그 몸이 있어야 가능하니까요.</p>
    <p>그래서 저는 오늘도 침을 놓습니다.</p>
    <p><b>아픈 곳을 조금이라도 편안하게 해 드리고,<br>언젠가는 아픔을 참아가며 일하지 않아도 되는 날이 오기를 바라면서요.</b></p>
    <p class="sign">한방재활의학과 전문의 · 한의학박사 <b>박장우</b></p>
  </div>

  <aside class="ccta" aria-label="진료 안내">
    <div class="ccta-top"><img src="images/c9de5ada.png" alt="" width="220" height="220"><div><b>정관고려한의원 진료 안내</b><p>예약 없이 방문하세요. {ADDR}</p></div></div>
    <div class="acts"><a class="btn-gold" href="{TEL_HREF}">{ic("phone")}전화 문의 {TEL}</a><a class="btn-line" href="index.html#hours">진료시간</a></div>
  </aside>

  <p class="src-link"><a href="https://blog.naver.com/jgkorea8275/224458443750" target="_blank" rel="noopener">네이버 블로그에서 원문 보기{ic("ext")}</a></p>

  <div class="tools">
    <a class="back" href="index.html#column">{ic("back")}목록으로</a>
    <div class="r">
      <button type="button" data-share>{ic("share")}공유하기</button>
      <button type="button" data-font aria-label="글자 크기: 보통"><span class="ga" aria-hidden="true">가</span>글자 크기</button>
    </div>
  </div>

  <nav class="related" aria-label="함께 보기">
    <h2>함께 보기</h2>
    <ul>
      <li><a href="essay-4.html">에세이 · 불은 그대로인데 사이렌만 끄고 있지는 않습니까?{ic("chev")}</a></li>
      <li><a href="essay-2.html">에세이 · 내 몸 안의 의사를 믿는다는 것{ic("chev")}</a></li>
      <li><a href="column-1.html">칼럼 · 삐끗했는데 왜 이렇게 오래 가죠?{ic("chev")}</a></li>
      <li><a href="index.html#treatment">치료 방법 · 침·약침·부항{ic("chev")}</a></li>
      <li><a href="index.html#doctor">원장 소개{ic("chev")}</a></li>
    </ul>
  </nav>
</main>
{footer()}
{dock('index.html')}
<script src="assets/site.js?v={VER}"></script>
{ANALYTICS}
</body>
</html>
'''
    return head + '\n' + body

ESSAY4_URL = 'https://jgkorea8275.co.kr/essay-4.html'
ESSAY4_TITLE = '불은 그대로인데 사이렌만 끄고 있지는 않습니까?'
ESSAY4_LD = {"@context": "https://schema.org", "@type": "Article", "headline": "불은 그대로인데 사이렌만 끄고 있지는 않습니까? — 통증주사에 익숙해진 시대, 침을 놓는 한의사의 마음", "datePublished": "2026-10-31", "image": ["https://jgkorea8275.co.kr/images/essay-4-hero.jpg"], "mainEntityOfPage": "https://jgkorea8275.co.kr/essay-4.html", "author": {"@type": "Person", "name": "박장우", "jobTitle": "한방재활의학과 전문의, 한의학박사"}, "publisher": {"@type": "Organization", "name": "정관고려한의원", "logo": {"@type": "ImageObject", "url": "https://jgkorea8275.co.kr/favicon.png"}}}
ESSAY4_CRUMB = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "정관고려한의원", "item": "https://jgkorea8275.co.kr/"},
    {"@type": "ListItem", "position": 2, "name": "칼럼 및 에세이", "item": "https://jgkorea8275.co.kr/#column"},
    {"@type": "ListItem", "position": 3, "name": "불은 그대로인데 사이렌만 끄고 있지는 않습니까?", "item": "https://jgkorea8275.co.kr/essay-4.html"}]}

def essay4():
    title = ESSAY4_TITLE
    desc = '통증주사에 익숙해진 시대, 통증이 사라져도 몸의 회복은 계속됩니다. 한방재활의학과 전문의 박장우 원장의 에세이.'
    toc = [('e1', '불이 났는데 사이렌만 끄고 있지는 않습니까?'), ('e2', '20여 년 전 진료실의 풍경'), ('e3', '주사를 바라보는 시선도 달라졌습니다'),
           ('e4', '침을 대하는 태도도 변했습니다'), ('e5', '침은 더디지만, 몸이 스스로 회복하도록 돕습니다'), ('e6', '사이렌이 아니라, 불이 꺼졌는지를')]
    toc_html = ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    head = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title} | 에세이 | 정관고려한의원</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<meta name="theme-color" content="#171511">
<link rel="canonical" href="{ESSAY4_URL}">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="alternate" type="application/rss+xml" title="정관고려한의원 칼럼·에세이" href="https://jgkorea8275.co.kr/rss.xml">
<meta property="og:type" content="article">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="정관고려한의원">
<meta property="og:title" content="{title} | 정관고려한의원 에세이">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{ESSAY4_URL}">
<meta property="og:image" content="https://jgkorea8275.co.kr/images/essay-4-hero.jpg">
<meta property="og:image:width" content="743">
<meta property="og:image:height" content="743">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://jgkorea8275.co.kr/images/essay-4-hero.jpg">
<meta property="article:published_time" content="2026-10-31">
<script type="application/ld+json">{json.dumps(ESSAY4_LD, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(ESSAY4_CRUMB, ensure_ascii=False)}</script>
{FONTS}
<link rel="stylesheet" href="assets/site.css?v={VER}">
</head>'''

    body = f'''<body class="has-dock">
{SPRITE}
{header('index.html')}
<div class="cbanner">
  <img src="images/column-banner.jpg" alt="" width="1600" height="900">
  <div class="wrap"><p class="ttl">에세이</p><p>진료실에서 품어 온 생각을 씁니다.</p></div>
</div>
<main class="art essay">
  <a class="back" href="index.html#column">{ic("back")}목록으로</a>
  <header class="art-head">
    <span class="chip">에세이 04</span>
    <h1>{title}</h1>
    <p class="art-sub">통증주사에 익숙해진 시대, 침을 놓는 한의사의 마음</p>
    <p class="art-meta"><span><time datetime="2026-10-31">2026.10.31</time></span><span>한방재활의학과 전문의 · 한의학박사 박장우</span></p>
  </header>

  <details class="toc toc-solo"><summary>목차 보기{ic("down")}</summary><ol>{toc_html}</ol></details>

  <div class="prose" data-size="0">
    <figure><img src="images/essay-4-hero.jpg" alt="에세이 04 · 불은 그대로인데 사이렌만 끄고 있지는 않습니까? · 통증주사에 익숙해진 시대, 침을 놓는 한의사의 마음" width="743" height="743"></figure>

    <p>제가 22년 동안 진료하면서 서서히 느끼고 있는 환자분들의 변화가 하나 있습니다.<br>바로, 통증클리닉에서 주사치료를 받고 오시는 분들이 많아졌다는 것입니다.<br>예전에는 그리 자주 듣지 못했던 이야기를 이제는 진료실에서 자연스럽게 듣게 됩니다.</p>
    <p class="lead-quote">"원장님, 통증클리닉에서 주사 한 대 맞으니까 바로 안 아프던데요."<br>"침은 여러 번 맞아야 하잖아요. 주사 한 방이면 금방 괜찮아지는데요."</p>
    <p>바쁜 현대인들에게 통증을 빠르게 줄여주는 주사가 얼마나 매력적이겠습니까.<br>아픈 몸을 이끌고 여러 번 치료받으러 다니는 것보다 주사 한 번 맞고 일상으로 돌아갈 수 있다면 누구라도 그쪽에 마음이 끌릴 것입니다.</p>
    <p>저 역시 통증이 심한 환자에게 적절한 주사치료가 도움이 될 수 있다는 사실을 잘 알고 있고, 필요할 때는 권하기도 합니다.</p>
    <p>하지만 그런 이야기를 들을 때면 한편으로는 걱정스러운 마음이 듭니다.<br><b>통증이 사라졌다고 해서, 통증을 일으킨 손상 조직까지 모두 회복된 것은 아닐 텐데 하는 걱정입니다.</b></p>

    <h2 id="e1">불이 났는데 사이렌만 끄고 있지는 않습니까?</h2>
    <p>어느 건물에서 불이 났다고 생각해 보겠습니다.<br>불이 나자 화재경보기가 요란하게 울립니다.<br>그런데 누군가 경보음이 너무 시끄럽다며 사이렌부터 부숴버렸습니다.<br>이제 조용해졌습니다.<br>하지만 불은 여전히 타고 있습니다.</p>
    <p>저는 때때로 통증을 대하는 우리의 태도에서 이런 모습을 떠올립니다.</p>
    <p>통증은 우리 몸이 보내는 경고 신호일 수 있습니다.<br><b>몸을 지나치게 사용하고 있으니 이제 좀 쉬라</b>는 신호일 수도 있고, <b>손상된 조직이 더 이상 다치지 않도록 조심하라</b>는 신호일 수도 있습니다.</p>
    <p>그런데 통증의 원인을 충분히 살펴보지 않은 채 당장 아프지 않게 만드는 데만 집중한다면, 사이렌은 꺼졌지만 문제는 그대로 남아 있을 수 있습니다.</p>
    <p>물론 모든 통증주사가 이런 것은 아닙니다.<br>주사의 종류에 따라 염증을 조절하거나 통증의 원인이 되는 신경 자극을 완화할 수 있고, 심한 통증을 줄여 환자가 잠을 자고 재활운동을 시작하도록 돕기도 합니다.</p>
    <p>제가 우려하는 것은 주사라는 치료법 자체가 아닙니다.<br><b>통증이 사라졌다는 이유만으로 몸이 다 나았다고 생각하는 것입니다.</b></p>
    <p>사이렌을 조용하게 만드는 것도 때로는 필요합니다.<br>하지만 사이렌이 멈췄다고 해서 불까지 꺼진 것은 아닙니다.<br>통증이 줄어든 뒤에도 손상된 조직이 충분히 회복되었는지 살펴야 하는 이유입니다.</p>

    <h2 id="e2">20여 년 전 진료실의 풍경</h2>
    <p>제가 한의사 생활을 시작한 것은 20여 년 전입니다.<br>그때와 지금의 진료실을 떠올려 보면 환자들의 모습이 참 많이 달라졌다는 생각이 듭니다.</p>
    <p>당시에는 허리나 어깨, 무릎이 아프면 꾸준히 침을 맞으러 오시는 분들이 많았습니다.<br>일주일에 두세 번씩 오시는 분들도 있었고, 통증이 심하면 매일같이 찾아오시는 분들도 있었습니다.</p>
    <p>그분들은 하루아침에 모든 통증이 사라지기를 기대하기보다는, 치료받고 쉬고 다시 치료받으면서 조금씩 좋아지는 과정을 비교적 자연스럽게 받아들이셨습니다.</p>
    <blockquote class="letter"><p>"원장님, 어제보다 조금 덜 아픕니다."</p><p>"이제 팔이 전보다 좀 올라갑니다."</p></blockquote>
    <p>그런 이야기를 나누며 회복의 경과를 함께 지켜보곤 했습니다.</p>
    <p>그 시절을 떠올리면 분명히 느껴지는 차이가 하나 있습니다.<br><b>예전에는 몸이 회복하는 데 시간이 필요하다는 사실을 지금보다 더 자연스럽게 받아들이는 환자들이 많았던 것 같습니다.</b></p>
    <p>요즘은 모든 것이 빨라졌습니다.<br>음식도 빨리 나오고, 물건도 하루 만에 배송되며, 원하는 정보는 몇 초 만에 찾아볼 수 있습니다.<br>그러다 보니 치료에서도 빠른 결과를 기대하는 마음이 커진 것은 아닐까요.</p>
    <p>"오늘 침 맞으면 내일 낫습니까?"<br>"한 번에 끝나는 치료는 없습니까?"</p>
    <p>이런 질문을 들을 때면 저는 가끔 생각합니다.<br><b>세상의 속도는 빨라졌지만, 우리 몸이 회복하는 데 필요한 시간까지 그만큼 빨라진 것은 아니라고 말입니다.</b></p>

    <h2 id="e3">주사를 바라보는 시선도 달라졌습니다</h2>
    <p>20여 년 전에는 주사에 대한 환자들의 인식도 지금과는 조금 달랐습니다.<br>제가 약침치료를 권하면 이런 질문을 하는 분들이 종종 있었습니다.</p>
    <p>"원장님, 그 주사 몸에 해롭지 않아요?"<br>"주사는 되도록 안 맞는 게 좋은 것 아닙니까?"</p>
    <p>당시 제 진료실에서는 주사라는 치료 행위 자체를 조심스럽게 생각하는 환자들을 적지 않게 만날 수 있었습니다.</p>
    <p>그런데 세월이 흐르면서 분위기가 달라졌습니다.<br>요즘은 통증클리닉에서 주사를 맞는 일을 상당히 익숙하고 편안하게 받아들이는 분들이 많습니다.<br>오히려 주사치료를 받지 않으면 제대로 치료받지 않은 것처럼 느끼는 분들도 있는 듯합니다.</p>
    <p>주사치료 기술이 발전하고, 실제로 도움을 받은 경험이 쌓였으니 그럴 만도 합니다.</p>
    <p>하지만 저는 가끔 이런 생각을 합니다.<br><b>우리가 치료의 효과를 판단할 때 너무 빠른 통증 감소에만 높은 점수를 주고 있는 것은 아닐까요?</b></p>
    <p>주사를 맞고 한 시간 만에 통증이 줄어드는 것과, 손상된 힘줄이나 관절이 회복되는 것은 서로 다른 이야기입니다.</p>
    <p>빠른 진통 효과는 분명 가치가 있습니다.<br>그러나 그 효과가 얼마나 지속되는지, 환자가 이전보다 더 건강하게 움직일 수 있는지, 같은 일을 해도 재발하지 않는지가 함께 중요합니다.</p>

    <h2 id="e4">침을 대하는 태도도 변했습니다</h2>
    <p>침치료에 대한 환자들의 반응 역시 많이 달라졌습니다.<br>예전에는 비교적 굵은 침으로 강한 자극을 주어도 잘 견디는 환자들이 많았습니다.<br>특히 연세가 많은 분들 가운데는 일부러 강한 침 자극을 원하시는 분들도 있었습니다.</p>
    <p>"원장님, 침이 좀 묵직하게 들어와야 맞은 것 같지요~~"<br>그런 말씀을 하시는 분들도 계셨습니다.</p>
    <p>그런데 요즘은 침을 무서워하는 환자들이 많아졌다는 것을 느낍니다.</p>
    <p><b>"침 많이 아픈가요?"</b><br><b>"살살 놔주세요."</b></p>
    <p>저 역시 환자들의 이러한 변화를 느끼면서 점차 가늘고 작은 침을 주로 사용하게 되었습니다.<br>환자가 편안하게 치료받을 수 있도록 하는 것도 의료인의 중요한 역할이기 때문입니다.</p>
    <p>사실 침 자극은 무조건 강하다고 좋은 것만은 아닙니다.<br>강한 자극이 모든 질환에서 더 나은 효과를 보인다는 근거도 충분하지 않습니다.<br>환자의 건강 상태와 치료 부위, 통증 민감도에 따라 적절한 자극을 선택해야 합니다.</p>
    <p>그럼에도 제 마음 한편에는 작은 걱정이 있습니다.<br>침이 아플 것이라는 막연한 두려움 때문에, 침치료를 경험해 보기도 전에 포기하는 분들이 점점 늘어나는 것은 아닐까 하는 걱정입니다.</p>
    <p>침술은 오랜 세월에 걸쳐 발전해 온 동양의 소중한 의학적 유산입니다.<br>저는 그 치료법이 단지 오래되었다는 이유로 존중받아야 한다고 생각하지는 않습니다.<br>실제로 환자에게 도움이 되는 부분이 무엇인지 끊임없이 검증하고 발전시켜야 한다고 생각합니다.</p>
    <p>하지만 충분히 알아보지도 않고, 경험해 보지도 않은 채 외면하기에는 아까운 치료법이라고 믿습니다.</p>

    <h2 id="e5">침은 더디지만, 몸이 스스로 회복하도록 돕습니다</h2>
    <p>침은 맞을 때 따끔하고 뻐근할 수 있습니다.<br>한 번에 끝나지도 않고, 여러 번 오셔야 합니다. 번거로우시겠지요.</p>
    <p>그래도 꾸준히 맞으시면 굳은 근육이 풀리고 혈액순환이 좋아져 움직임이 한결 편해지는 경우가 많습니다.<br>몸이 편해지면 적절한 운동과 재활도 시작할 수 있고, 몸은 그 시간 동안 스스로 회복할 기회를 얻게 됩니다.</p>
    <p>무엇보다 침은 약물에 기대지 않고도 회복을 도울 수 있습니다.</p>
    <p>그러니 꼭 주사나 약물이 필요한 상황이 아니라면, 침치료를 받으며 몸이 낫는 시간을 조금 기다려 주셨으면 합니다.<br>한 번에 끝나지 않는다는 이유로 그 과정의 가치를 작게 여기지는 않으셨으면 합니다.</p>

    <h2 id="e6">사이렌이 아니라, 불이 꺼졌는지를</h2>
    <p>다시 처음의 사이렌 이야기로 돌아가 보겠습니다.</p>
    <p><b>통증이 사라졌다고 불까지 꺼진 것은 아닙니다.</b></p>
    <p>설령 불이 꺼졌다 해도, 타 버린 자리를 다시 세우는 데는 시간이 걸립니다.<br>그을린 벽을 걷어내고, 기둥을 다시 세우고, 사람이 살 수 있는 집으로 되돌리는 시간 말입니다.</p>
    <p>다친 근육과 힘줄도 그렇습니다.<br>통증이 멈춘 뒤에도 몸 안에서는 상한 조직을 걷어내고 새로 채우는 일이 몇 주, 길게는 몇 달 동안 이어집니다.</p>
    <p>침이 그 공사를 대신해 드릴 수는 없습니다.<br>다만 몸이 그 일을 잘 해낼 수 있도록 곁에서 거들 수는 있습니다.</p>
    <p><b>통증을 빨리 없애려는 마음이 앞서, 몸이 다시 집을 짓는 시간까지 놓치지는 않으셨으면 합니다.</b></p>
    <p>저는 그 시간을 환자분과 함께 지키는 한의사이고 싶습니다.</p>
    <p class="sign">한방재활의학과 전문의 · 한의학박사 <b>박장우</b></p>
  </div>

  <aside class="ccta" aria-label="진료 안내">
    <div class="ccta-top"><img src="images/c9de5ada.png" alt="" width="220" height="220"><div><b>정관고려한의원 진료 안내</b><p>예약 없이 방문하세요. {ADDR}</p></div></div>
    <div class="acts"><a class="btn-gold" href="{TEL_HREF}">{ic("phone")}전화 문의 {TEL}</a><a class="btn-line" href="index.html#hours">진료시간</a></div>
  </aside>

  <p class="src-link"><a href="https://blog.naver.com/jgkorea8275/224459662972" target="_blank" rel="noopener">네이버 블로그에서 원문 보기{ic("ext")}</a></p>

  <div class="tools">
    <a class="back" href="index.html#column">{ic("back")}목록으로</a>
    <div class="r">
      <button type="button" data-share>{ic("share")}공유하기</button>
      <button type="button" data-font aria-label="글자 크기: 보통"><span class="ga" aria-hidden="true">가</span>글자 크기</button>
    </div>
  </div>

  <nav class="related" aria-label="함께 보기">
    <h2>함께 보기</h2>
    <ul>
      <li><a href="essay-3.html">에세이 · 몸은 쉬라고 하는데, 삶은 멈출 수 없을 때{ic("chev")}</a></li>
      <li><a href="essay-2.html">에세이 · 내 몸 안의 의사를 믿는다는 것{ic("chev")}</a></li>
      <li><a href="column-1.html">칼럼 · 삐끗했는데 왜 이렇게 오래 가죠?{ic("chev")}</a></li>
      <li><a href="index.html#treatment">치료 방법 · 침·약침·부항{ic("chev")}</a></li>
      <li><a href="index.html#doctor">원장 소개{ic("chev")}</a></li>
    </ul>
  </nav>
</main>
{footer()}
{dock('index.html')}
<script src="assets/site.js?v={VER}"></script>
{ANALYTICS}
</body>
</html>
'''
    return head + '\n' + body

COL2_URL = 'https://jgkorea8275.co.kr/column-2.html'
COL2_TITLE = '"침 한방에 낫게 해주소~" 근육통 회복 속도를 결정하는 네가지 요인'
COL2_LD = {"@context": "https://schema.org", "@type": "Article", "headline": "침 한방에 낫게 해주소~ 근육통 회복 속도를 결정하는 네가지 요인", "datePublished": "2026-11-01", "image": ["https://jgkorea8275.co.kr/images/column-2-hero.jpg"], "mainEntityOfPage": "https://jgkorea8275.co.kr/column-2.html", "author": {"@type": "Person", "name": "박장우", "jobTitle": "한의학박사, 한방재활의학과 전문의"}, "publisher": {"@type": "Organization", "name": "정관고려한의원", "logo": {"@type": "ImageObject", "url": "https://jgkorea8275.co.kr/favicon.png"}}}
COL2_CRUMB = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "정관고려한의원", "item": "https://jgkorea8275.co.kr/"},
    {"@type": "ListItem", "position": 2, "name": "칼럼 및 에세이", "item": "https://jgkorea8275.co.kr/#column"},
    {"@type": "ListItem", "position": 3, "name": "침 한방에 낫게 해주소~ 근육통 회복 속도를 결정하는 네가지 요인", "item": "https://jgkorea8275.co.kr/column-2.html"}]}

def column2():
    title = COL2_TITLE.replace('"', '&quot;')
    title_plain = title
    title_attr = title
    desc = '같은 근육통도 회복 속도는 다릅니다. 다친 정도, 일상 관리, 몸의 회복력, 한의사의 역할까지 네 가지 요인을 정리했습니다.'
    toc = [('s1', '기계 수리와 몸의 치료, 무엇이 다를까요?'), ('s2', '피부 상처로 생각해 볼게요'), ('s3', '근육통이 낫는 속도는 무엇이 결정할까요?'),
           ('s4', '근육통을 빨리 낫게 하려면 이렇게 합시다.'), ('s5', '정리하며')]
    chk = lambda t: f'<li>{ic("check")}<span>{t}</span></li>'
    toc_html = ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    head = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title_plain} | 칼럼 | 정관고려한의원</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<meta name="theme-color" content="#171511">
<link rel="canonical" href="{COL2_URL}">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="alternate" type="application/rss+xml" title="정관고려한의원 칼럼·에세이" href="https://jgkorea8275.co.kr/rss.xml">
<meta property="og:type" content="article">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="정관고려한의원">
<meta property="og:title" content="{title_attr} | 정관고려한의원 칼럼">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{COL2_URL}">
<meta property="og:image" content="https://jgkorea8275.co.kr/images/column-2-hero.jpg">
<meta property="og:image:width" content="743">
<meta property="og:image:height" content="743">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://jgkorea8275.co.kr/images/column-2-hero.jpg">
<meta property="article:published_time" content="2026-11-01">
<script type="application/ld+json">{json.dumps(COL2_LD, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(COL2_CRUMB, ensure_ascii=False)}</script>
{FONTS}
<link rel="stylesheet" href="assets/site.css?v={VER}">
</head>'''

    body = f'''<body class="has-dock">
{SPRITE}
{header('index.html')}
<div class="cbanner">
  <img src="images/column-banner.jpg" alt="" width="1600" height="900">
  <div class="wrap"><p class="ttl">건강 칼럼</p><p>진료실에서 자주 받는 질문을 쉽게 풀어 씁니다.</p></div>
</div>
<main class="art column">
  <a class="back" href="index.html#column">{ic("back")}목록으로</a>
  <header class="art-head">
    <span class="chip">칼럼 · 근육통</span>
    <h1>{title}</h1>
    
    <p class="art-meta"><span><time datetime="2026-11-01">2026.11.01</time></span><span>정관고려한의원 건강 칼럼</span></p>
  </header>

  <section class="sum" aria-labelledby="sum-h">
    <h2 id="sum-h">이 글에서 알 수 있는 내용</h2>
    <ul>
      {chk('치료와 치유는 어떻게 다를까요')}
      {chk('근육통 회복 속도를 결정하는 네 가지 요인')}
      {chk('빨리 낫기 위해 환자와 한의사가 함께 할 일')}
    </ul>
    <details class="toc"><summary>목차 보기{ic("down")}</summary><ol>{toc_html}</ol></details>
  </section>

  <div class="prose" data-size="0">
    <figure><img src="images/column-2-hero.jpg" alt="원장 칼럼 · 원장님, 침 한방에 낫게 해주소~ · 근육통, 회복 속도를 결정하는 4가지 요인 · 낫는 데 필요한 것: 치료 + 회복 시간 = 치유" width="743" height="743"></figure>

    <p>안녕하세요~ 정관고려한의원 원장 박장우 입니다.</p>
    <p>진료실에서 가끔 환자분들께 듣는 말이 있습니다.</p>
    <p class="lead-quote">"원장님, 빨리 낫게 해주소~"<br>"원장님, 침 한방에 낫게 해주소~"</p>
    <p>그러면 저는 웃으면서 이렇게 대답합니다.</p>
    <p><b>"아이고, 사람 치료하는 게 어디 기계 고치는 거랑 같나요.<br>뚝딱뚝딱 손본다고 바로 낫는 게 아입니더~~^^"</b></p>
    <p>오늘은 제가 진료실에서 환자분들께 자주 드리는 이야기를 쉬운 글로 풀어봤습니다.</p>
    <figure><img src="images/column-2-coach.jpg" alt="침을 맞는 환자(아~ 시원하다)와 옆에서 손을 든 한의사(저는 낫는 환경을 만들께요, 우리 같이 노력해봅시다~)" width="743" height="483" loading="lazy"><figcaption>치료는 의사와 환자가 함께 합니다.</figcaption></figure>

    <h2 id="s1">기계 수리와 몸의 치료, 무엇이 다를까요?</h2>
    <p>고장난 기계는 수리가 끝나면 그걸로 끝입니다.</p>
    <p>하지만 우리 몸이 나으려면 두 가지가 필요합니다.<br>바로 <b>치료</b>(수리)와 <b>회복 시간</b>입니다.</p>
    <p>또 하나 다른 점이 있습니다.<br>기계는 누가 고쳐 주지 않으면 스스로 고쳐지지 않습니다.<br>그런데 우리 몸에는 스스로 낫는 힘, <b>자연치유력</b>이 있습니다.</p>
    <p>그렇다면 가만히 두면 낫는데 치료는 왜 받을까요?<br>치료는 <b>몸이 스스로 낫는 힘을 잘 발휘하도록 돕고</b>, 회복을 앞당겨 주기 때문입니다.</p>

    <h2 id="s2">피부 상처로 생각해 볼게요</h2>
    <p>기계에 흠집이 나면 수리하는 그 자리에서 바로 매끈해집니다.<br>하지만 손에 상처가 나면, 치료를 받았다고 그 자리에서 마술처럼 싹 아물지는 않죠.</p>
    <p>상처를 소독하고 꿰매는 것은 <b>치료</b>입니다.<br>그 뒤에 새 살이 차오르며 아무는 것은 <b>치유</b>입니다.</p>
    <p>같은 상처라도 살성이 좋은 분은 금방 아물고, 그렇지 못한 분은 더디 아물죠.</p>
    <p>간단히 요약하면,</p>
    <p><b>치료는 낫는 길을 열어 드리는 것이고, 그 길을 걸어 낫는 것은 환자분의 몸입니다.</b></p>

    <h2 id="s3">근육통이 낫는 속도는 무엇이 결정할까요?</h2>
    <p>근육통도 마찬가지입니다.<br>같은 치료를 받아도 빨리 나으시는 분이 있고, 조금 더디 나으시는 분이 있습니다.<br>그 차이를 만드는 것은 크게 네 가지입니다.</p>

    <h3 class="factor"><span class="n">1</span><span>우선, <b>다친 정도</b>입니다.</span></h3>
    <ul class="checks">
      <li>{ic("check")}<span>잠깐 무리한 뒤 생긴 가벼운 근육통인지,</span></li>
      <li>{ic("check")}<span>근육이 파열된 것인지(대표적으로 종아리 근파열),</span></li>
      <li>{ic("check")}<span>같은 부위에 부담이 반복되면서 통증이 오래 이어진 것인지</span></li>
    </ul>
    <p>에 따라 회복 속도는 달라집니다.<br>그리고 허리의 경우, 디스크나 협착증 때문에 생긴 허리근육통은 더 오래 갑니다.</p>

    <h3 class="factor"><span class="n">2</span><span>두 번째, <b>일상에서 얼마나 조심하느냐</b> 입니다.</span></h3>
    <p>치료받는 시간은 길어야 <b>1시간</b>입니다.<br>나머지 <b>23시간</b>은 환자분의 일상입니다.</p>
    <p>치료받고 나서 무거운 짐을 들거나, 한 자세로 오래 앉아 있거나, 아픈데도 무리해서 운동하시면 회복되던 근육을 다시 혹사시키는 셈이 됩니다.</p>
    <p>상처에 밴드를 붙이고 가만히 두면 빨리 나을 것을, 자꾸 건드리고 흙 묻히고 하면 상처가 오래가고 덧나겠죠?<br>근육도 똑같습니다.</p>

    <h3 class="factor"><span class="n">3</span><span>세 번째, <b>몸의 회복력</b>입니다.</span></h3>
    <p>상처가 아무는 속도가 사람마다 다르듯, 근육이 회복되는 속도도 사람마다 다릅니다.<br>나이, 체질, 평소 건강 상태, 당뇨 같은 지병에 따라 회복이 빠르기도 하고 더디기도 합니다.</p>

    <h3 class="factor"><span class="n">4</span><span>네 번째가 <b>의사(한의사)의 역할</b>입니다.</span></h3>
    <p>저는 저의 역할을 <b>코치</b>에 비유합니다.<br>운동선수 옆에서 코치가 대신 뛰어줄 수는 없습니다.<br>하지만 자세를 잡아주고, 컨디션을 살피고, 힘을 더 낼 수 있게 도와줍니다.</p>
    <p>침, 전자뜸, 부항, 약침, 한약 등은 모두 <b>몸이 스스로 회복하는 힘을 끌어올리도록 돕는 도구</b>입니다.</p>

    <h2 id="s4">근육통을 빨리 낫게 하려면 이렇게 합시다.</h2>
    <figure><img src="images/column-2-tug.jpg" alt="병세(병의 기세)와 회복력(몸이 스스로 낫는 힘)의 줄다리기. 병세를 돕는 것: 다친 정도, 일상에서 무리. 회복력을 돕는 것: 충분한 수면, 무리하지 않기, 한의사 치료. 회복력을 돕는 힘이 많을수록 몸은 빨리 낫습니다." width="743" height="557" loading="lazy"><figcaption>병세와 회복력의 줄다리기</figcaption></figure>
    <p>저는 질병 상태를 극복하는 과정을 위의 그림과 같이 <b>병세</b>와 <b>회복력(치유력)</b> 사이의 줄다리기라고 생각합니다.</p>
    <p>그래서 근육통의 빠른 회복을 위해서는 환자와 의사의 협력이 필요합니다.</p>
    <p>앞서 살펴봤던 회복속도를 좌우하는 네 가지 요인들 중,<br>우리가 어찌할 수 없는 것은 첫번째 <b>다친 정도</b>입니다.<br>이건 이미 일어난 일이니 되돌릴 수는 없습니다.</p>
    <ul class="dl">
      <li><b>환자 입장</b>할 게 없습니다.</li>
      <li><b>의사 입장</b>원인이 무엇인지 진단하여 앞으로의 경과를 예측해 줄 수 있습니다.</li>
    </ul>
    <p>나머지 세가지 요인은 환자와 의사가 힘을 합쳐 긍정적인 방향으로 이끌 수 있습니다.</p>
    <ul class="roles">
      <li><b class="who">의사</b>치료를 통해, 회복하기 좋은 상태를 만들어 환자의 <b>치유력(회복력)</b>을 돕습니다.</li>
      <li><b class="who">환자분</b>'<b>일상에서 무리하지 않음</b>'을 지켜 병세가 진행되지 않도록 합니다.
        <p class="sub">허리 근육통의 경우, 예를 들면 이런 것들입니다.</p>
        <ul class="checks">
          <li>{ic("check")}<span>무거운 물건 드는 일, 갑자기 허리를 숙이거나 비트는 동작, 격한 운동 등은 당분간 쉬어 주세요.</span></li>
          <li>{ic("check")}<span>오래 앉아 계실 때는 중간중간 일어나 가볍게 몸을 풀어 주세요.(505법칙)</span></li>
        </ul>
      </li>
      <li><b class="who">환자분</b>또한 <b>충분한 수면</b>을 취함으로써 <b>치유력(회복력)</b>을 올릴 수 있습니다.
        <p class="sub">우리 몸은 잠을 자는 동안 손상된 조직을 활발히 복구합니다.<br>평소보다 1~2시간 일찍 주무시거나, 그 이상 더 주무시는 것도 치유에 아주 많은 도움이 됩니다.</p>
      </li>
    </ul>

    <h2 id="s5">정리하며</h2>
    <p>몸을 기계처럼 생각해서 "수리했으니(치료했으니) 이제 끝"이라고 여기시면 안 됩니다.<br>우리 몸은 살아 숨쉬는 생명체입니다.<br>부품을 갈아 끼우면 그 자리에서 복구가 끝나는 기계와는 다릅니다.</p>
    <ul class="checks">
      <li>{ic("check")}<span>의사(한의사)가 하는 <b>치료</b>와,</span></li>
      <li>{ic("check")}<span>환자분이 몸의 <b>치유</b>를 위해 <b>일상에서 주의</b>하면서 <b>회복력을 높이기 위해서 하는 노력들</b>.</span></li>
    </ul>
    <p>이 두 가지가 함께 할 때 회복도 한결 빨라집니다.</p>
    <p class="ps">ps. 저도 마음 같아서는 정말 침 한방에 낫게 해 드리고 싶습니다...TT;;<br>하지만 빠른 회복은 결국 의사와 환자분이 <b>함께 만들어 가는</b> 거랍니다.</p>
    <p class="sign">한의학박사 · 한방재활의학과 전문의 <b>박장우</b></p>
  </div>

  <aside class="ccta" aria-label="진료 안내">
    <div class="ccta-top"><img src="images/c9de5ada.png" alt="" width="220" height="220"><div><b>정관고려한의원 진료 안내</b><p>예약 없이 방문하세요. {ADDR}</p></div></div>
    <div class="acts"><a class="btn-gold" href="{TEL_HREF}">{ic("phone")}전화 문의 {TEL}</a><a class="btn-line" href="index.html#hours">진료시간</a></div>
  </aside>

  <p class="src-link"><a href="https://blog.naver.com/jgkorea8275/224461619969" target="_blank" rel="noopener">네이버 블로그에서 원문 보기{ic("ext")}</a></p>

  <div class="tools">
    <a class="back" href="index.html#column">{ic("back")}목록으로</a>
    <div class="r">
      <button type="button" data-share>{ic("share")}공유하기</button>
      <button type="button" data-font aria-label="글자 크기: 보통"><span class="ga" aria-hidden="true">가</span>글자 크기</button>
    </div>
  </div>

  <nav class="related" aria-label="함께 보기">
    <h2>함께 보기</h2>
    <ul>
      <li><a href="column-3.html">칼럼 · 어깨가 아프면 다 오십견일까요?{ic("chev")}</a></li>
      <li><a href="column-1.html">칼럼 · 삐끗했는데 왜 이렇게 오래 가죠?{ic("chev")}</a></li>
      <li><a href="essay-3.html">에세이 · 몸은 쉬라고 하는데, 삶은 멈출 수 없을 때{ic("chev")}</a></li>
      <li><a href="index.html#area">근육통·관절통 진료 안내{ic("chev")}</a></li>
      <li><a href="index.html#treatment">치료 방법 · 침·약침·부항{ic("chev")}</a></li>
    </ul>
  </nav>
</main>
{footer()}
{dock('index.html')}
<script src="assets/site.js?v={VER}"></script>
{ANALYTICS}
</body>
</html>
'''
    return head + '\n' + body

COL3_URL = 'https://jgkorea8275.co.kr/column-3.html'
COL3_TITLE = '어깨가 아프면 다 오십견일까요? (오십견의 특징과 운동법)'
COL3_LD = {"@context": "https://schema.org", "@type": "Article", "headline": "어깨가 아프면 다 오십견일까요? 오십견의 특징과 운동법", "datePublished": "2026-11-04", "image": ["https://jgkorea8275.co.kr/images/column-3-hero.jpg"], "mainEntityOfPage": "https://jgkorea8275.co.kr/column-3.html", "author": {"@type": "Person", "name": "박장우", "jobTitle": "한의학박사, 한방재활의학과 전문의"}, "publisher": {"@type": "Organization", "name": "정관고려한의원", "logo": {"@type": "ImageObject", "url": "https://jgkorea8275.co.kr/favicon.png"}}}
COL3_CRUMB = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "정관고려한의원", "item": "https://jgkorea8275.co.kr/"},
    {"@type": "ListItem", "position": 2, "name": "칼럼 및 에세이", "item": "https://jgkorea8275.co.kr/#column"},
    {"@type": "ListItem", "position": 3, "name": "어깨가 아프면 다 오십견일까요?", "item": "https://jgkorea8275.co.kr/column-3.html"}]}

def column3():
    title = COL3_TITLE.replace('"', '&quot;')
    title_plain = title
    title_attr = title
    desc = '어깨가 아프다고 다 오십견은 아닙니다. 오십견의 특징과 혼동하기 쉬운 질환, 경과와 치료, 집에서 하는 운동법까지 정리했습니다.'
    toc = [('s1', '오십견이란 어떤 병인가요?'), ('s2', '오십견은 왜 생길까요?'), ('s3', '오십견의 특징적인 증상'), ('s4', '오십견과 혼동하기 쉬운 어깨 질환'),
           ('s5', '오십견은 얼마나 오래 가나요?'), ('s6', '"오십견은 치료 안해도 기다리면 낫는다"는 말이 있던데요?'), ('s7', '오십견의 치료는 어떻게 하나요?'),
           ('s8', '집에서 하는 오십견 운동 6가지'), ('s9', '마치며')]
    chk = lambda t: f'<li>{ic("check")}<span>{t}</span></li>'
    toc_html = ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    head = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title_plain} | 칼럼 | 정관고려한의원</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<meta name="theme-color" content="#171511">
<link rel="canonical" href="{COL3_URL}">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="alternate" type="application/rss+xml" title="정관고려한의원 칼럼·에세이" href="https://jgkorea8275.co.kr/rss.xml">
<meta property="og:type" content="article">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="정관고려한의원">
<meta property="og:title" content="{title_attr} | 정관고려한의원 칼럼">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{COL3_URL}">
<meta property="og:image" content="https://jgkorea8275.co.kr/images/column-3-hero.jpg">
<meta property="og:image:width" content="743">
<meta property="og:image:height" content="743">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://jgkorea8275.co.kr/images/column-3-hero.jpg">
<meta property="article:published_time" content="2026-11-04">
<script type="application/ld+json">{json.dumps(COL3_LD, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(COL3_CRUMB, ensure_ascii=False)}</script>
{FONTS}
<link rel="stylesheet" href="assets/site.css?v={VER}">
</head>'''

    body = f'''<body class="has-dock">
{SPRITE}
{header('index.html')}
<div class="cbanner">
  <img src="images/column-banner.jpg" alt="" width="1600" height="900">
  <div class="wrap"><p class="ttl">건강 칼럼</p><p>진료실에서 자주 받는 질문을 쉽게 풀어 씁니다.</p></div>
</div>
<main class="art column">
  <a class="back" href="index.html#column">{ic("back")}목록으로</a>
  <header class="art-head">
    <span class="chip">칼럼 · 오십견·어깨 통증</span>
    <h1>{title}</h1>
    
    <p class="art-meta"><span><time datetime="2026-11-04">2026.11.04</time></span><span>정관고려한의원 건강 칼럼</span></p>
  </header>

  <section class="sum" aria-labelledby="sum-h">
    <h2 id="sum-h">이 글에서 알 수 있는 내용</h2>
    <ul>
      {chk('오십견은 어떤 병이고, 어떤 증상이 특징일까요')}
      {chk('오십견과 헷갈리기 쉬운 어깨 질환과 집에서 해 보는 자가감별법')}
      {chk('오십견의 경과와 치료, 집에서 하는 운동 6가지')}
    </ul>
    <details class="toc"><summary>목차 보기{ic("down")}</summary><ol>{toc_html}</ol></details>
  </section>

  <div class="prose" data-size="0">
    <figure><img src="images/column-3-hero.jpg" alt="오십견·어깨 통증 · 어깨가 아프면 다 오십견일까요? · 특징부터 감별·운동법까지" width="743" height="743"></figure>

    <p class="lead-quote">"원장님, 저 오십견이죠?"</p>
    <p>진료를 하다 보면 어깨가 아파서 오시는 분들 중에 "오십견인 것 같아요" 하시는 분들이 많습니다.<br>하지만 실제로 체크해 보면 오십견이 아닌 경우도 많습니다.</p>
    <p>어깨가 아프다고 다 오십견은 아닙니다.<br>힘줄에 문제가 생겨도, 석회가 쌓여도, 관절이 닳아도 비슷하게 아플 수 있습니다.</p>
    <p>오십견은 굳은 관절을 <b>풀어야</b> 낫지만, 회전근개 손상 같은 힘줄 손상의 경우엔 억지로 운동하면 오히려 손상이 커질 수 있습니다.</p>
    <p>그러므로, 이번에는 오십견의 특징과 감별해야 할 다른 질환에 대해 알아보고,<br>오십견의 예후와 치료법, 운동법 등에 대해 설명드리겠습니다.</p>

    <h2 id="s1">오십견이란 어떤 병인가요?</h2>
    <p>오십견의 정식 명칭은 <b>유착성 관절낭염</b>입니다.</p>
    <p>50대 전후의 나이에 별다른 이유 없이 또는 부상이나 수술 후 어깨를 오래 움직이지 못한 뒤 어깨 통증과 함께 <b>어깨가 서서히 굳어져 움직이는 각도가 제한</b>되는 병입니다.</p>
    <p>어깨 관절은 관절낭이라는 얇은 주머니에 싸여 있는데, 이 주머니에 염증이 생기고 두꺼워지면서 쪼그라들게 됩니다. 그래서 어깨의 가동 범위가 점차 줄어드는 현상이 나타납니다.</p>
    <figure><img src="images/column-3-capsule.jpg" alt="어깨 속에서는 무슨 일이? 건강한 어깨는 주머니가 말랑하고 여유 주름이 있지만, 오십견 어깨는 주머니가 두꺼워져 쪼그라들어 남이 들어 올려도 팔이 걸립니다." width="743" height="847" loading="lazy"></figure>
    <ul class="checks">
      <li>{ic("check")}<span>어깨가 얼어붙은 것처럼 굳는다고 해서 서구에서는 '<b>동결견(Frozen Shoulder)</b>'이라고도 부릅니다.</span></li>
      <li>{ic("check")}<span>우리나라에서는 50대 전후로 많이 발병한다고 '<b>오십견</b>'이라는 별명이 붙어있습니다.</span></li>
      <li>{ic("check")}<span>한의학에서는 오십견을 견비통(肩臂痛)의 범주로 보고, 나이가 들며 기혈이 약해진 틈에 풍한습(風寒濕)의 나쁜 기운이 어깨에 머물러 굳는다고 보았습니다.</span></li>
    </ul>

    <h2 id="s2">오십견은 왜 생길까요?</h2>
    <p><b>아직 오십견의 발병 원인은 정확히 밝혀진 바가 없습니다.</b></p>
    <p>하지만, 발병 배경은 크게 두 가지로 설명할 수 있습니다.</p>
    <ul class="dl">
      <li><b>뚜렷한 계기 없이 발생하는 경우</b>다친 적이 없는데도 서서히 통증이 생기고 어깨가 굳어집니다.</li>
      <li><b>부상·수술 후 발생하는 경우</b>골절이나 어깨 손상, 수술 등으로 어깨를 오랫동안 움직이지 못한 뒤 생길 수 있습니다.</li>
    </ul>
    <p><b>그리고 당뇨병과 갑상선 질환, 고지혈증은 발병 위험을 높이는 요인</b>입니다.</p>
    <p class="key"><b>어깨를 감싼 주머니가 염증으로 두꺼워지고 쪼그라들면서, 어깨의 가동 범위가 줄어드는 겁니다.<br>특별히 다치지 않아도 생길 수 있고, 당뇨가 있거나 다친 뒤 오래 움직이지 못했을 때 더 잘 생깁니다.</b></p>

    <h2 id="s3">오십견의 특징적인 증상</h2>
    <p>오십견의 가장 큰 특징은 <b>혼자 움직일 때뿐 아니라, 다른 사람이 도와줘도 어깨의 가동 범위가 줄어든다</b>는 점입니다.</p>
    <p>힘이 없어서가 아니라 관절 주머니 자체가 쪼그라들어 걸리기 때문입니다.<br>특히 팔꿈치를 몸에 붙이고 팔을 바깥으로 돌리는 동작이 제한되는 경우가 많습니다.</p>
    <p class="note">(다만 어깨 관절염이나 심한 통증 때문에도 움직임이 제한될 수 있으므로, 이 특징만으로 오십견을 확진하지는 않습니다.)</p>
    <figure><img src="images/column-3-signs.jpg" alt="오십견의 특징적인 증상: 1. 도움을 받아도 팔이 잘 안 올라갑니다 2. 옷을 입거나 뒷짐을 지기가 어렵다 3. 팔꿈치를 붙이고 바깥으로 돌리기 어렵습니다 4. 밤에 아프고 아픈 쪽으로 눕기 어렵습니다" width="743" height="1115" loading="lazy"><figcaption>오십견의 특징적인 증상</figcaption></figure>
    <p class="note">※ 이 중 4번 야간 통증은 회전근개 질환(어깨 힘줄 손상)에서도 나타나니 주의해야 합니다.</p>

    <h2 id="s4">오십견과 혼동하기 쉬운 어깨 질환</h2>
    <p><b>어깨 통증은 오십견 뿐 아니라 여러 질환에서 나타나고, 원인에 따라 치료와 운동 방법이 달라집니다.</b></p>
    <p>그러므로, 나이가 오십 전후이거나 밤에 아프다는 이유만으로 오십견이라고 판단해서는 안되고 정확한 감별 진단이 필요합니다.</p>
    <figure><img src="images/column-3-mimics.jpg" alt="어깨가 아프면 다 오십견일까요? 오십견과 혼동하기 쉬운 질환: 회전근개 질환, 석회성 건염, 어깨 관절염, 목에서 내려오는 통증. 증상은 서로 겹칠 수 있으며 정확한 감별은 진찰과 필요한 영상검사로 합니다." width="743" height="1115" loading="lazy"></figure>
    <h3 class="sub-h">[타 질환이 오십견과 비슷한 점]</h3>
    <ul class="checks">
      <li>{ic("check")}<span><b>회전근개 질환(어깨 힘줄 손상)</b>도 팔을 들 때 아프고 야간통이 생깁니다. 파열이 있으면 근력 저하가 동반될 수 있습니다.</span></li>
      <li>{ic("check")}<span><b>석회성 건염</b>은 갑자기 극심한 통증이 생겨 팔을 거의 못 움직이기도 합니다.</span></li>
      <li>{ic("check")}<span><b>어깨 골관절염</b>도 오십견처럼 남이 도와줘도 움직임이 제한될 수 있습니다.</span></li>
      <li>{ic("check")}<span><b>목에서 내려오는 통증(목디스크 등)</b>도 어깨가 아픈 것으로 느껴질 수 있습니다.</span></li>
    </ul>
    <h3 class="sub-h">[타 질환이 오십견과 다른 점]</h3>
    <ul class="checks">
      <li>{ic("check")}<span><b>회전근개 질환(어깨 힘줄 손상)</b>은 혼자서는 팔을 못 들지만 남이 도와주면 올라가는데, 이는 관절보다는 팔을 들어 올리는 힘줄의 문제이기 때문입니다.</span></li>
    </ul>
    <p class="note">(다만 통증이 심하거나 오십견이 함께 생기면, 도움을 받아도 움직임이 제한될 수 있습니다.)</p>
    <p>오십견과 회전근개 질환을 감별하는데 참고할 만한 방법은 아래 그림과 같습니다.<br>(단, 통증을 참으며 억지로 올리지는 마세요)</p>
    <figure><img src="images/column-3-selftest.jpg" alt="집에서 아픈 쪽 어깨 확인하기: 바로 누워 왼손으로 오른팔을 받쳐 천천히 머리 쪽으로 올려 보세요. 도움을 받아도 잘 올라가지 않는다면 오십견 의심, 도움을 받으면 머리 위까지 올라간다면 회전근개 등 힘줄 질환 감별 필요. 자가 확인만으로 확진할 수 없습니다." width="743" height="1115" loading="lazy"><figcaption>오십견과 회전근개 질환 자가감별법</figcaption></figure>
    <ul class="checks">
      <li>{ic("check")}<span><b>석회성 건염, 어깨 골관절염</b>은 엑스레이로도 오십견과 구별할 수 있습니다.</span></li>
    </ul>
    <p>오십견은 관절낭의 문제이기 때문에 엑스레이에서는 뚜렷한 이상이 보이지 않는 경우가 많습니다.</p>
    <ul class="checks">
      <li>{ic("check")}<span>하지만, 똑같이 어깨가 굳는 <b>어깨 골관절염</b>의 경우엔 아래의 오른쪽 사진처럼 퇴행성 변화(관절 간격 좁아짐, 모서리 지저분함)가 나타납니다.</span></li>
    </ul>
    <figure><img src="images/column-3-xray-oa.jpg" alt="정상 어깨(왼쪽)와 관절염이 있는 어깨(오른쪽)의 X선 사진" width="563" height="360" loading="lazy"><figcaption>정상 어깨(왼쪽)와 관절염이 있는 어깨(오른쪽)의 X선 사진</figcaption></figure>
    <ul class="checks">
      <li>{ic("check")}<span><b>석회성 건염</b>도 엑스레이 상 비교적 쉽게 관찰할 수 있습니다.</span></li>
    </ul>
    <figure><img src="images/column-3-xray-calcific.jpg" alt="석회성 건염 엑스레이 사진 (화살표: 힘줄 부위의 석회 침착)" width="743" height="359" loading="lazy"><figcaption>석회성 건염 엑스레이 사진</figcaption></figure>
    <p>정리하면 다음과 같습니다.</p>
    <div class="tbl-wrap"><table class="tbl tbl-sm">
      <thead><tr><th scope="col">질환</th><th scope="col">대표적인 X선 소견</th></tr></thead>
      <tbody>
        <tr><th scope="row">오십견</th><td>대체로 관절 간격과 뼈 모양이 보존됨</td></tr>
        <tr><th scope="row">어깨 골관절염</th><td>관절 간격 감소, 골극</td></tr>
        <tr><th scope="row">석회성 건염</th><td>힘줄 부위의 하얀 석회 침착</td></tr>
      </tbody>
    </table></div>
    <p class="key"><b>어깨가 아프다고 다 오십견은 아닙니다.<br>힘줄에 문제가 생겨도, 석회가 쌓여도, 관절이 닳아도 비슷하게 아플 수 있습니다.<br>오십견인 줄 알고 기다리거나 무리하게 운동하기 전에, 무엇 때문에 아픈지부터 확인해야 합니다.</b></p>

    <h2 id="s5">오십견은 얼마나 오래 가나요?</h2>
    <p>오십견은 수개월에서 <b>수년에 걸쳐</b> 호전되는 경우가 많습니다.</p>
    <p>흔히 <b>통증기·강직기·완해기</b>로 설명하지만, 단계가 서로 겹칠 수 있고 기간도 사람마다 다릅니다.<br>통증이 줄어든 뒤에도 움직임 제한이 남는 경우가 있습니다.</p>
    <figure><img src="images/column-3-stages.jpg" alt="오십견, 언제쯤 나을까요? 회복은 보통 3단계로 진행됩니다. 1 통증기(약 3~9개월): 어깨가 아프고 밤에 통증이 심해 일상생활이 힘듭니다. 2 강직기(약 4~12개월): 통증은 조금 줄지만 어깨가 굳어 움직임이 제한됩니다. 3 완해기(약 6~12개월): 움직임이 서서히 늘어나고 일상생활이 조금씩 수월해집니다." width="743" height="1115" loading="lazy"><figcaption>오십견의 3단계 경과</figcaption></figure>

    <h2 id="s6">"오십견은 치료 안해도 기다리면 낫는다"는 말이 있던데요?</h2>
    <p><b>치료하지 않아도 호전될 수는 있습니다.<br>하지만 “그냥 두면 누구나 완전히 낫는다”고 말할 수는 없습니다.</b></p>
    <p>오십견은 시간이 지나면서 통증이 줄고 움직임이 회복되는 경향이 있습니다.<br>다만 회복에 수년이 걸리거나, 통증은 줄었어도 팔 올리기·외회전·등 뒤로 손 보내기 등의 제한이 남을 수 있습니다.<br>2025년 국내 진료지침도 <b>모든 환자가 완전한 자연 회복에 이르는 것은 아니라</b>고 정리했습니다.</p>
    <p>여기서 <b>‘통증이 없어지는 것’과 ‘어깨 기능이 회복되는 것’은 구별</b>해야 합니다.<br>덜 아파졌다고 해도 어깨가 굳어 옷 입기나 머리 감기가 불편하다면 충분히 회복됐다고 보기는 어렵습니다.</p>
    <p>치료와 재활의 목적은 <b>기다리는 동안의 통증과 생활 불편을 줄이고</b>, <b>움직임 회복을 돕기 위해서</b> 입니다.</p>

    <h2 id="s7">오십견의 치료는 어떻게 하나요?</h2>
    <p>오십견 치료는 <b>통증을 줄이면서, 굳어진 어깨의 움직임을 조금씩 회복</b>하는 것이 핵심입니다.</p>
    <p>대부분 비수술적으로 치료하며, 통증과 강직 정도에 맞춰 강도를 조절합니다.</p>
    <div class="tbl-wrap"><table class="tbl tbl-sm">
      <thead><tr><th scope="col">단계</th><th scope="col">치료의 중심</th></tr></thead>
      <tbody>
        <tr><th scope="row">1. 통증기</th><td>통증 조절과 수면 확보, 편안한 범위의 가벼운 운동</td></tr>
        <tr><th scope="row">2. 강직기</th><td>관절 가동 운동과 스트레칭으로 움직임 회복</td></tr>
        <tr><th scope="row">3. 완해기</th><td>운동 범위를 점차 넓히고 근력·일상 기능 회복</td></tr>
      </tbody>
    </table></div>
    <p>한방에서는 <b>침과 뜸, 약침, 부항, 물리치료, 한약</b> 등을 통해 통증완화와 운동 회복을 돕습니다.</p>
    <figure><img src="images/column-3-treat.jpg" alt="한의원에서는 이렇게 도와요. 몸이 스스로 풀어 가는 힘을 돕는 치료: 침(통증 가라앉히기), 전자뜸(따뜻하게 풀기), 부항(뭉친 근막 풀기), 약침(염증 다스리기), 한약(몸 안부터 회복)" width="743" height="768" loading="lazy"></figure>
    <p class="note">※ 저는 초기 '통증기'에 <b>야간통</b>이 극심해서 잠을 자기 힘든 경우에는, <b>양방 치료도 병행</b>하도록 안내드립니다. 왜냐하면 수면의 질이 떨어지면 회복도 더디고, 삶의 질도 저하되기 때문입니다.</p>

    <h2 id="s8">집에서 하는 오십견 운동 6가지</h2>
    <p>운동은 오십견 치료의 기본입니다.<br><b>하지만, 세게 한다고 좋은 것이 아닙니다.</b><br>통증을 참아가며 억지로 꺾기보다, 상태에 맞는 운동을 꾸준히 시행하는 것이 중요합니다.</p>
    <p>그림에서 빨간 표시가 아픈 쪽 어깨입니다.</p>
    <figure class="tall"><img src="images/column-3-exercise.jpg" alt="오십견 운동법(오른쪽 어깨의 경우): 1 시계추 운동(코드만 운동) 2 누워서 팔 올리기 3 앉아서 팔 올리기 4 선 자세에서 바깥돌리기 5 벽 타고 올라가기(거미운동) 6 수건으로 등 뒤 스트레칭. 통증이 심하지 않은 범위에서 부드럽게 하세요." width="724" height="2172" loading="lazy"><figcaption>오십견 운동법</figcaption></figure>
    <h3 class="sub-h">★ 운동할 때 주의할 점</h3>
    <ol class="steps">
      <li>샤워 직후나 온찜질 10~15분 뒤처럼 <b>몸을 따뜻하게 한 다음에</b> 하는 것이 좋습니다.</li>
      <li><b>시원하게 당기는 느낌까지만</b> 하고, 찌르는 통증이 오면 멈춥니다.</li>
      <li>운동 후 통증이 오래 남거나 그날 밤·다음 날 더 아프면 강도와 횟수를 줄입니다.</li>
      <li>한 번에 세게 하는 것보다 <b>하루 2~3번 가볍게</b> 하는 것이 좋습니다.</li>
    </ol>

    <h2 id="s9">마치며</h2>
    <p>오십견은 시간이 지나면서 호전되는 경우가 많지만, 회복 속도와 회복 정도는 사람마다 다릅니다.</p>
    <p>오래 불편을 겪지 않으려면 먼저 <b>무엇 때문에 아픈지 정확히 확인</b>하는 것이 중요합니다.<br>어깨가 아프다고 혼자 오십견으로 단정하지 마시고, 진찰과 필요한 검사를 받아보시기 바랍니다.</p>
    <p class="sign">한의학박사 · 한방재활의학과 전문의 <b>박장우</b></p>

    <details class="refs">
      <summary>참고자료 · 영상 자료 출처{ic("down")}</summary>
      <ol>
        <li>이호준. 흔히 발생하는 어깨통증의 감별진단. 대한의사협회지. 2014;57(8):653–660. — 오십견, 회전근개 질환, 석회성 건염 등의 감별진단. <a href="https://doi.org/10.5124/jkma.2014.57.8.653" target="_blank" rel="noopener">doi.org/10.5124/jkma.2014.57.8.653</a></li>
        <li>Lee BC, et al. Clinical Practice Guidelines for Diagnosis and Non-Surgical Treatment of Primary Frozen Shoulder. Annals of Rehabilitation Medicine. 2025;49(3):113–138. — 국내 일차성 동결견 진료지침. 진단, 자연경과, 운동 및 비수술적 치료. <a href="https://doi.org/10.5535/arm.250057" target="_blank" rel="noopener">doi.org/10.5535/arm.250057</a></li>
        <li>Hand C, Clipsham K, Rees JL, Carr AJ. Long-term outcome of frozen shoulder. Journal of Shoulder and Elbow Surgery. 2008;17(2):231–236. — 오십견의 장기 경과와 잔존 증상. <a href="https://doi.org/10.1016/j.jse.2007.05.009" target="_blank" rel="noopener">doi.org/10.1016/j.jse.2007.05.009</a></li>
        <li>Dyer BP, et al. Diabetes as a risk factor for the onset of frozen shoulder: a systematic review and meta-analysis. BMJ Open. 2023;13:e062377. — 당뇨병과 오십견 발병 위험의 연관성. <a href="https://doi.org/10.1136/bmjopen-2022-062377" target="_blank" rel="noopener">doi.org/10.1136/bmjopen-2022-062377</a></li>
        <li>Dyer BP, et al. Diabetes as a Prognostic Factor in Frozen Shoulder: A Systematic Review. Archives of Rehabilitation Research and Clinical Translation. 2021;3(3):100141. — 당뇨병 유무에 따른 오십견의 통증·기능·가동범위 예후. <a href="https://doi.org/10.1016/j.arrct.2021.100141" target="_blank" rel="noopener">doi.org/10.1016/j.arrct.2021.100141</a></li>
        <li>Qin Y, et al. Traditional Chinese medicine for frozen shoulder: An evidence-based guideline. Journal of Evidence-Based Medicine. 2023;16(2):246–258. — 중국에서 개발된 동결견 치료지침. 침치료 등 관련 치료의 효과와 근거 수준. <a href="https://doi.org/10.1111/jebm.12530" target="_blank" rel="noopener">doi.org/10.1111/jebm.12530</a></li>
      </ol>
      <p class="refs-h">영상 자료 출처</p>
      <ul>
        <li>Asia Medical Specialists. Frozen Shoulder FAQs. Fig. 4: 정상 어깨와 어깨 관절염의 엑스레이 비교. <a href="https://asiamedicalspecialists.hk/en/health-info/60/Frozen-Shoulder-FAQs" target="_blank" rel="noopener">asiamedicalspecialists.hk</a></li>
        <li>American Academy of Orthopaedic Surgeons. OrthoInfo: Calcific Tendinitis of the Shoulder. 석회성 건염 엑스레이 원출처: Suzuki K, Potts A, Anakwenze O, Singh A. Calcific Tendinitis of the Rotator Cuff: Management Options. Journal of the American Academy of Orthopaedic Surgeons. 2014;22(11):707–717. <a href="https://www.orthoinfo.org/bodypart/shoulder/calcific-tendinitis-of-the-shoulder/" target="_blank" rel="noopener">orthoinfo.org</a></li>
      </ul>
    </details>
  </div>

  <aside class="ccta" aria-label="진료 안내">
    <div class="ccta-top"><img src="images/c9de5ada.png" alt="" width="220" height="220"><div><b>정관고려한의원 진료 안내</b><p>예약 없이 방문하세요. {ADDR}</p></div></div>
    <div class="acts"><a class="btn-gold" href="{TEL_HREF}">{ic("phone")}전화 문의 {TEL}</a><a class="btn-line" href="index.html#hours">진료시간</a></div>
  </aside>

  <p class="src-link"><a href="https://blog.naver.com/jgkorea8275/224465217044" target="_blank" rel="noopener">네이버 블로그에서 원문 보기{ic("ext")}</a></p>

  <div class="tools">
    <a class="back" href="index.html#column">{ic("back")}목록으로</a>
    <div class="r">
      <button type="button" data-share>{ic("share")}공유하기</button>
      <button type="button" data-font aria-label="글자 크기: 보통"><span class="ga" aria-hidden="true">가</span>글자 크기</button>
    </div>
  </div>

  <nav class="related" aria-label="함께 보기">
    <h2>함께 보기</h2>
    <ul>
      <li><a href="column-4.html">칼럼 · 자다가 종아리에 쥐가 나요{ic("chev")}</a></li>
      <li><a href="column-2.html">칼럼 · 근육통 회복 속도를 결정하는 네가지 요인{ic("chev")}</a></li>
      <li><a href="column-1.html">칼럼 · 삐끗했는데 왜 이렇게 오래 가죠?{ic("chev")}</a></li>
      <li><a href="index.html#area">근육통·관절통 진료 안내{ic("chev")}</a></li>
      <li><a href="index.html#treatment">치료 방법 · 침·약침·부항{ic("chev")}</a></li>
    </ul>
  </nav>
</main>
{footer()}
{dock('index.html')}
<script src="assets/site.js?v={VER}"></script>
{ANALYTICS}
</body>
</html>
'''
    return head + '\n' + body

COL5_URL = 'https://jgkorea8275.co.kr/column-5.html'
COL5_TITLE = '자고 일어났더니 목이 안 돌아가요 — 목 담결림(낙침) 원인, 경과, 침치료, 주의사항'
COL5_LD = {"@context": "https://schema.org", "@type": "Article", "headline": "자고 일어났더니 목이 안 돌아가요 — 목 담결림(낙침) 원인, 경과, 침치료, 주의사항", "datePublished": "2026-11-10", "image": ["https://jgkorea8275.co.kr/images/column-5-hero.jpg"], "mainEntityOfPage": "https://jgkorea8275.co.kr/column-5.html", "author": {"@type": "Person", "name": "박장우", "jobTitle": "한의학박사, 한방재활의학과 전문의"}, "publisher": {"@type": "Organization", "name": "정관고려한의원", "logo": {"@type": "ImageObject", "url": "https://jgkorea8275.co.kr/favicon.png"}}}
COL5_CRUMB = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "정관고려한의원", "item": "https://jgkorea8275.co.kr/"},
    {"@type": "ListItem", "position": 2, "name": "칼럼 및 에세이", "item": "https://jgkorea8275.co.kr/#column"},
    {"@type": "ListItem", "position": 3, "name": "자고 일어났더니 목이 안 돌아가요", "item": "https://jgkorea8275.co.kr/column-5.html"}]}

def column5():
    title = COL5_TITLE.replace('"', '&quot;')
    title_plain = title
    title_attr = title
    desc = '자고 일어났더니 목이 안 돌아가는 목 담결림(낙침). 원인 네 가지와 자연경과·침치료 경과, 빨리 회복하는 법, 바로 진료가 필요한 경우를 정리했습니다.'
    toc = [('s1', '목의 담결림, 낙침이란?'), ('s2', '왜 생기는 걸까요?'), ('s3', '경과는 어떻게 될까요? — 자연경과 vs 침치료'),
           ('s4', '빨리 회복하려면 이것 만은 지켜 주세요'), ('s5', '마지막으로 제일 중요! 이럴 땐 바로 진료를 받으세요')]
    chk = lambda t: f'<li>{ic("check")}<span>{t}</span></li>'
    toc_html = ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    head = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title_plain} | 칼럼 | 정관고려한의원</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<meta name="theme-color" content="#171511">
<link rel="canonical" href="{COL5_URL}">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="alternate" type="application/rss+xml" title="정관고려한의원 칼럼·에세이" href="https://jgkorea8275.co.kr/rss.xml">
<meta property="og:type" content="article">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="정관고려한의원">
<meta property="og:title" content="{title_attr} | 정관고려한의원 칼럼">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{COL5_URL}">
<meta property="og:image" content="https://jgkorea8275.co.kr/images/column-5-hero.jpg">
<meta property="og:image:width" content="743">
<meta property="og:image:height" content="743">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://jgkorea8275.co.kr/images/column-5-hero.jpg">
<meta property="article:published_time" content="2026-11-10">
<script type="application/ld+json">{json.dumps(COL5_LD, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(COL5_CRUMB, ensure_ascii=False)}</script>
{FONTS}
<link rel="stylesheet" href="assets/site.css?v={VER}">
</head>'''

    body = f'''<body class="has-dock">
{SPRITE}
{header('index.html')}
<div class="cbanner">
  <img src="images/column-banner.jpg" alt="" width="1600" height="900">
  <div class="wrap"><p class="ttl">건강 칼럼</p><p>진료실에서 자주 받는 질문을 쉽게 풀어 씁니다.</p></div>
</div>
<main class="art column">
  <a class="back" href="index.html#column">{ic("back")}목록으로</a>
  <header class="art-head">
    <span class="chip">칼럼 · 목 담결림</span>
    <h1>{title}</h1>
    
    <p class="art-meta"><span><time datetime="2026-11-10">2026.11.10</time></span><span>정관고려한의원 건강 칼럼</span></p>
  </header>

  <section class="sum" aria-labelledby="sum-h">
    <h2 id="sum-h">이 글에서 알 수 있는 내용</h2>
    <ul>
      {chk('목 담결림(낙침)은 왜 생기고, 목디스크와 어떻게 다를까요')}
      {chk('그냥 둘 때와 침치료를 받을 때의 경과')}
      {chk('빨리 회복하는 법과 바로 진료가 필요한 경우')}
    </ul>
    <details class="toc"><summary>목차 보기{ic("down")}</summary><ol>{toc_html}</ol></details>
  </section>

  <div class="prose" data-size="0">
    <figure><img src="images/column-5-hero.jpg" alt="담결림 · “원장님, 혹시 디스크는 아니죠?” 자고 일어나니 목이 안 돌아가요 · 목 담결림(낙침), 원인과 경과·침치료" width="743" height="743"></figure>

    <p class="lead-quote">"원장님, 자고 일어났더니 갑자기 목이 안 돌아가요."</p>
    <p>가끔 이렇게 목을 부여잡고 힘들어 하며 진료실에 들어오시는 환자분이 계십니다.</p>
    <figure><img src="images/column-5-stiff.jpg" alt="목 뒤를 손으로 감싸 쥐고 아파서 얼굴을 찡그리는 남성" width="743" height="498" loading="lazy"></figure>
    <p>자고 일어나 갑자기 목이 아프고 잘 안 돌아가는 걸 한방에서는 '<b>낙침(落枕)</b>'이라고 합니다.<br>낙침이 세게 오면 처음 며칠은 꽤 힘들 수 있습니다.</p>
    <p>오늘은 왜 이런 현상이 생기는지, 얼마나 지나야 풀리는지, 집에서는 뭘 조심하면 좋은지 말씀드리겠습니다.</p>

    <h2 id="s1">목의 담결림, 낙침이란?</h2>
    <p>"<b>담 결렸다</b>"는 말은 다들 한 번 쯤 들어보거나 써 보셨을 겁니다.<br>그중에서도 자고 일어나서 생긴 목 담결림을 <b>낙침</b>(落枕)이라고 부릅니다.<br>베개에서 목이 떨어진 채로 잤다는 뜻입니다~</p>
    <p>양방에서는 보통 목 근육이 갑자기 뭉친 <b>급성 경부통</b>(영어로는 흔히 stiff neck)으로 봅니다.</p>

    <h3 class="sub-h">목 안에서는 무슨 일이 일어난 걸까요?</h3>
    <p>목 근육이 한계를 넘으면, 더 다치지 않으려고 근육이 스스로 <b>꽉 붙잡고 버티는 상태</b>가 됩니다.<br>고개를 돌리려 하면 이 근육이 "움직이지 마!" 하고 더 세게 버티니, 아프고 돌아가지 않는 것입니다.</p>

    <h3 class="sub-h">이런 증상이 나타납니다</h3>
    <ul class="checks">
      <li>{ic("check")}<span>아침에 일어나자마자 목이 아프고 깁스한 것처럼 잘 안 돌아갑니다.</span></li>
      <li>{ic("check")}<span>한쪽으로 돌리거나 기울일 때 <b>"악!"</b> 소리가 날 만큼 아픕니다.</span></li>
      <li>{ic("check")}<span>날개뼈 안쪽, 어깨 위까지 당깁니다.</span></li>
      <li>{ic("check")}<span>아픈 쪽을 피하려고 고개가 한쪽으로 살짝 기운 채 지내기도 합니다.</span></li>
    </ul>

    <h3 class="sub-h">목디스크와는 어떻게 다를까요?</h3>
    <p>많은 분들이 "혹시 디스크 아닌가요?" 하고 걱정하십니다.</p>
    <p>목디스크는 팔이나 손까지 통증이 뻗치거나, 저리거나 힘이 빠지기도 합니다.<br>하지만, 담결림은 목과 어깨 주변만 뭉치고 아픕니다.</p>

    <h2 id="s2">왜 생기는 걸까요?</h2>
    <p>원인은 크게 네 가지입니다.<br>한 가지 만으로 생기기도 하고, 두 세 가지가 겹치는 경우도 많습니다.</p>

    <h3 class="factor"><span>① 우선, 평소 쌓인 목 근육의 피로입니다</span></h3>
    <p>목 근육은 하루 종일 무거운 머리를 받치고 있습니다.<br>이 피로가 조금씩 쌓이다가 <b>임계점을 넘는 순간</b> 탈이 납니다.</p>
    <p>같은 베개를 수 년 간 베셨는데 왜 하필 오늘 아침일까요?<br>그동안 쌓인 피로가 넘친 날이기 때문입니다.</p>
    <ul class="checks">
      <li>{ic("check")}<span>오랜 시간 스마트폰·컴퓨터 보기</span></li>
      <li>{ic("check")}<span>장거리 운전</span></li>
      <li>{ic("check")}<span>이사, 김장처럼 평소 안 하던 일로 무리</span></li>
      <li>{ic("check")}<span>잠이 부족했거나, 스트레스가 많았던 날</span></li>
    </ul>

    <h3 class="factor"><span>② 두 번째로, 자는 동안의 나쁜 자세입니다</span></h3>
    <ul class="checks">
      <li>{ic("check")}<span>엎드려서 고개를 한쪽으로 돌리고 자기</span></li>
      <li>{ic("check")}<span>소파나 의자에서 고개를 떨군 채 졸기</span></li>
      <li>{ic("check")}<span>너무 높은 베개, 또는 옆으로 누웠을 때 너무 낮은 베개</span></li>
    </ul>
    <figure><img src="images/column-5-sleep.jpg" alt="엎드려 고개를 한쪽으로 돌리고 자는 모습과 소파에 앉아 고개를 떨군 채 조는 모습" width="743" height="498" loading="lazy"></figure>
    <p>자는 동안에는 불편해도 자세를 고치지 못하니, 목 근육이 몇 시간 씩 한쪽으로 당겨진 채 버티게 됩니다.</p>

    <h3 class="factor"><span>③ 그 다음! 찬바람입니다</span></h3>
    <p>여름에는 <b>선풍기·에어컨 바람</b>, 날씨가 서늘해질 때는 <b>새벽의 찬 기운</b>이 목에 닿는 것 만으로도 근육이 움츠러듭니다.</p>
    <p>한의학에서는 이것을 <b>풍한(風寒)</b>, 즉 찬 바람이 근육에 들어왔다고 봅니다.<br>쉽게 말해 <b>목 근육이 감기에 걸린 것</b>이죠.</p>
    <p>그래서 에어컨을 많이 트는 한여름과, 일교차가 큰 환절기에 목 담결림이 유독 많습니다.</p>

    <h3 class="factor"><span>④ 마지막으로, 기저 질환이 있는 경우입니다</span></h3>
    <p><b>일자목, 목디스크, 반복되는 목 통증</b>처럼 목에 구조적인 문제가 있는 분들은 목 담결림이 자주 재발하거나 회복이 더딜 수 있습니다.</p>

    <h2 id="s3">경과는 어떻게 될까요? — 자연경과 vs 침치료</h2>
    <p>이게 제일 궁금해 하실 부분인데요.</p>

    <h3 class="sub-h">그냥 두면 (자연경과)</h3>
    <p>목 담결림은 기본적으로 <b>저절로 좋아지는 병</b>입니다.<sup>1</sup> 하지만 바로 좋아지지는 않습니다.</p>
    <p>저는 환자분들께 이렇게 말씀드립니다.</p>
    <p class="key"><b>"목 근육에 감기몸살 걸렸다고 생각하세요."</b></p>
    <p>감기몸살도 하루 만에 낫지 않고, 2~3일은 더 심해졌다가 좋아지는 경우가 많죠? 담결림도 똑같습니다. 처음 며칠은 더 심해지기도 합니다.</p>
    <p>회복되는 데 걸리는 기간도 감기처럼, 며칠이나 1주일 안에 낫는 분도 있고 2~3주 가는 분도 있습니다.</p>
    <p>그래서 처음 오신 분께 미리 말씀드립니다.</p>
    <p class="key"><b>"담 쎄게 오면 처음 2~3일은 뭘 해도 힘듭니다. 원래 그런 거니 너무 걱정하지 마세요."</b></p>
    <p>환자분들은 하루 아침에 갑자기 고개를 못 돌리니 '이거 큰 병 아닌가?', '혹시 이러다가 큰 일 나는 건 아닐까?' 불안해 하시거든요.</p>

    <h3 class="sub-h">침치료를 받으면</h3>
    <p><b>가볍게 담이 온 분</b>은 며칠 사이에 한결 편해지기도 합니다.</p>
    <p>하지만, <b>고개가 아예 안 돌아갈 만큼 심하게 온 분</b>은 침을 맞아도 처음 2~3일 정도는 힘들 수 있습니다.</p>
    <p>아래 그래프와 영상은 <b>담결림이 심하게 온 분</b>들의 경과를 제가 진료실에서 본 경험을 바탕으로 그린 예시입니다.</p>
    <figure><img src="images/column-5-course.jpg" alt="심한 목 담결림의 침치료 경과 예시: 고개가 아예 안 돌아갈 만큼 심한 경우, 침 하나는 침치료 받은 날. 그냥 둘 때는 통증이 오래 높게 이어지고, 침치료를 받을 때는 3일까지 진행한 뒤 꺾이기 시작해 정점을 찍고 내려오면서 좋아집니다." width="743" height="541" loading="lazy"></figure>
    <p>움직이는 영상으로 보시면 더 쉽습니다~</p>
    <figure class="video"><video controls playsinline preload="none" poster="images/column-5-video-poster.jpg" width="1920" height="1080" aria-label="심한 목 담결림의 경과 영상: 그냥 두었을 때는 3일까지 점점 심해지고 그 뒤로 아주 천천히 풀립니다. 침치료 1~3회는 침을 안 맞으면 더 나빠질 것을 침을 맞아서 좀 덜 나빠지게 합니다. 침치료 4~5회에 통증이 정점을 찍고 꺾이기 시작하면서 좋아지기 시작하고, 6~7회에 한 계단, 8~10회에 또 한 계단 내려옵니다."><source src="videos/column-5-course.mp4" type="video/mp4"></video></figure>
    <p>제 경험 상, 담이 세게 오면 침을 맞아도 처음 이틀, 사흘은 꽤 힘들 수 있습니다.<br>며칠 비슷하다가 어느 날 고개가 한결 잘 돌아가는 분도 계십니다.</p>
    <p class="note">영상 속 치료 횟수는 이런 경과를 설명하기 위한 예시입니다. 좋아지기 시작하는 시점과 필요한 치료 횟수는 사람마다 다릅니다.</p>
    <p>2024년에 낙침 환자를 대상으로 한 여러 임상 시험을 종합한 연구에서, 침치료를 받은 쪽의 통증이 더 줄고 목을 움직이는 범위도 더 넓어졌다고 보고했습니다.<sup>3</sup></p>
    <p>정관고려한의원에서는 목 담결림 치료를 위해 <b>침·전침, 부항(습식, 건식), 약침, 전자뜸, 온찜질, 물리치료</b> 등을 시행합니다.</p>

    <h2 id="s4">빨리 회복하려면 이것 만은 지켜 주세요</h2>

    <h3 class="factor"><span>① 따뜻하게 해 주세요</span></h3>
    <ul class="checks">
      <li>{ic("check")}<span><b>온찜질</b></span></li>
      <li>{ic("check")}<span><b>사우나, 온수 샤워</b></span></li>
    </ul>
    <p>따뜻한 샤워 물을 목에 맞으면서, 손으로 머리를 가볍게 밀어 주며 스트레칭 하는 것도 좋은 방법입니다.</p>
    <figure><img src="images/column-5-shower.jpg" alt="따뜻한 샤워 물을 목에 맞으며 손으로 머리를 가볍게 옆으로 밀어 목을 스트레칭하는 모습 세 장면" width="743" height="315" loading="lazy"></figure>

    <h3 class="factor"><span>② 찬바람과 냉찜질은 피해 주세요</span></h3>
    <p>아프다고 얼음찜질을 하시는 분들이 계시는데, 담결림에는 <b>냉찜질이 맞지 않습니다.</b></p>
    <p>선풍기·에어컨 바람도 목에 직접 닿지 않게 해 주세요. 얇은 목도리도 좋습니다~</p>

    <h3 class="factor"><span>③ 충분히 쉬고, 푹 주무세요</span></h3>
    <p>지친 근육이 회복하려면 충분한 휴식과 잠이 필요합니다.<br>아픈 동안에는 야근이나 무리한 일정을 조금 줄여 보시기 바랍니다.</p>

    <h3 class="factor"><span>④ 억지로 돌리거나 세게 주무르지 마세요</span></h3>
    <p>"풀어야지" 하고 아픈 쪽으로 자꾸 돌려 보거나, 세게 주물러 "뚝" 소리를 내면 굳은 근육이 더 놀라 단단히 버티게 됩니다.</p>
    <p><b>아프지 않은 범위 안에서만</b> 천천히 움직이시면 됩니다.</p>
    <p>그렇다고 꼼짝 않고 있는 것도 좋지 않습니다. 목 보호대도 요즘은 권하지 않습니다.<sup>2</sup> 오히려 더 굳을 수 있기 때문입니다.</p>

    <h3 class="factor"><span>⑤ 운전은 특히 조심하세요</span></h3>
    <p>고개가 잘 안 돌아가 옆이나 뒤를 살피기 어렵다면 운전은 미루세요.</p>

    <h2 id="s5">마지막으로 제일 중요! 이럴 땐 바로 진료를 받으세요</h2>
    <ul class="checks">
      <li>{ic("check")}<span><b>목이 뻣뻣하면서 열이 나거나 심한 두통이 있으면 바로 응급 진료를 받으세요.<br>아이가 열이 나면서 목을 잘 못 움직일 때도 마찬가지 입니다.</b></span></li>
      <li>{ic("check")}<span>사고 뒤 목이 아프거나 새로 팔·손이 저리거나 힘이 빠지면 신속히 진료 받으세요.</span></li>
      <li>{ic("check")}<span>통증이 계속 심해지거나 며칠이 지나도 풀리는 기미가 없으면 진료를 받으세요.</span></li>
    </ul>

    <p>목은 하루에도 수백 번 움직이며 무거운 머리를 받치고 있습니다.</p>
    <p>담 결림은 그동안 쌓인 피로에 목이 보내는 "<b>잠깐 쉬어 가자</b>"는 신호입니다.</p>
    <p>이번 기회에 그동안 쌓인 목의 피로도 한번 풀어 주시기 바랍니다.^^</p>
    <p class="sign">한의학박사 · 한방재활의학과 전문의 <b>박장우</b></p>

    <details class="refs">
      <summary>참고 자료 · 그림 출처{ic("down")}</summary>
      <ol>
        <li>Vasseljen O, et al. Natural course of acute neck and low back pain in the general population: the HUNT study. Pain. 2013. <a href="https://doi.org/10.1016/j.pain.2013.03.032" target="_blank" rel="noopener">doi.org/10.1016/j.pain.2013.03.032</a></li>
        <li>Patient.info — Torticollis (목 보호대 비권장). <a href="https://patient.info/health/torticollis-leaflet/symptoms-and-diagnosis" target="_blank" rel="noopener">patient.info</a></li>
        <li>Efficacy and safety of acupuncture treatment for stiff neck: A systematic review and meta-analysis. Medicine (Baltimore). 2024. <a href="https://doi.org/10.1097/MD.0000000000040415" target="_blank" rel="noopener">doi.org/10.1097/MD.0000000000040415</a></li>
      </ol>
      <p class="refs-h">그림 출처</p>
      <ul>
        <li>삽화: 이 칼럼을 위해 새로 제작한 그림입니다.</li>
      </ul>
    </details>
  </div>

  <aside class="ccta" aria-label="진료 안내">
    <div class="ccta-top"><img src="images/c9de5ada.png" alt="" width="220" height="220"><div><b>정관고려한의원 진료 안내</b><p>예약 없이 방문하세요. {ADDR}</p></div></div>
    <div class="acts"><a class="btn-gold" href="{TEL_HREF}">{ic("phone")}전화 문의 {TEL}</a><a class="btn-line" href="index.html#hours">진료시간</a></div>
  </aside>

  <p class="src-link"><a href="https://blog.naver.com/jgkorea8275/224472243346" target="_blank" rel="noopener">네이버 블로그에서 원문 보기{ic("ext")}</a></p>

  <div class="tools">
    <a class="back" href="index.html#column">{ic("back")}목록으로</a>
    <div class="r">
      <button type="button" data-share>{ic("share")}공유하기</button>
      <button type="button" data-font aria-label="글자 크기: 보통"><span class="ga" aria-hidden="true">가</span>글자 크기</button>
    </div>
  </div>

  <nav class="related" aria-label="함께 보기">
    <h2>함께 보기</h2>
    <ul>
      <li><a href="column-2.html">칼럼 · 근육통 회복 속도를 결정하는 네가지 요인{ic("chev")}</a></li>
      <li><a href="column-1.html">칼럼 · 삐끗했는데 왜 이렇게 오래 가죠?{ic("chev")}</a></li>
      <li><a href="column-3.html">칼럼 · 어깨가 아프면 다 오십견일까요?{ic("chev")}</a></li>
      <li><a href="index.html#area">담결림 진료 안내{ic("chev")}</a></li>
      <li><a href="index.html#treatment">치료 방법 · 침·약침·부항{ic("chev")}</a></li>
    </ul>
  </nav>
</main>
{footer()}
{dock('index.html')}
<script src="assets/site.js?v={VER}"></script>
{ANALYTICS}
</body>
</html>
'''
    return head + '\n' + body

COL6_URL = 'https://jgkorea8275.co.kr/column-6.html'
COL6_TITLE = '침 치료 원리, 과학적으로 쉽게 설명드립니다 (관문조절설, 엔도르핀, 전침)'
COL6_LD = {"@context": "https://schema.org", "@type": "Article", "headline": "침 치료 원리, 과학적으로 쉽게 설명드립니다 (관문조절설, 엔도르핀, 전침)", "datePublished": "2026-11-17", "image": ["https://jgkorea8275.co.kr/images/column-6-hero.jpg"], "mainEntityOfPage": "https://jgkorea8275.co.kr/column-6.html", "author": {"@type": "Person", "name": "박장우", "jobTitle": "한의학박사, 한방재활의학과 전문의"}, "publisher": {"@type": "Organization", "name": "정관고려한의원", "logo": {"@type": "ImageObject", "url": "https://jgkorea8275.co.kr/favicon.png"}}}
COL6_CRUMB = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "정관고려한의원", "item": "https://jgkorea8275.co.kr/"},
    {"@type": "ListItem", "position": 2, "name": "칼럼 및 에세이", "item": "https://jgkorea8275.co.kr/#column"},
    {"@type": "ListItem", "position": 3, "name": "침 치료 원리, 과학적으로 쉽게 설명드립니다", "item": "https://jgkorea8275.co.kr/column-6.html"}]}

def column6():
    title = COL6_TITLE.replace('"', '&quot;')
    title_plain = title
    title_attr = title
    desc = '"원장님, 침은 어떻게 해서 낫는 거예요?" 관문조절설, 몸속 진통물질(엔도르핀), 침 자리의 변화, 뇌·신경 조절까지 침 치료의 원리를 쉽게 풀었습니다.'
    toc = [('s1', "경락은 '옛 사람들이 그린 몸의 지도'입니다"), ('s2', "① 통증이 지나가는 '문'을 조절합니다"), ('s3', '② 몸이 스스로 진통제를 만들도록 합니다'),
           ('s4', '③ 침 맞은 자리에서도 변화가 일어납니다'), ('s5', '④ 뇌와 몸 전체가 반응합니다'), ('s6', '한눈에 정리하면'), ('s7', '다시 그 학생 이야기로 돌아와서')]
    chk = lambda t: f'<li>{ic("check")}<span>{t}</span></li>'
    toc_html = ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    head = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title_plain} | 칼럼 | 정관고려한의원</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<meta name="theme-color" content="#171511">
<link rel="canonical" href="{COL6_URL}">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="alternate" type="application/rss+xml" title="정관고려한의원 칼럼·에세이" href="https://jgkorea8275.co.kr/rss.xml">
<meta property="og:type" content="article">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="정관고려한의원">
<meta property="og:title" content="{title_attr} | 정관고려한의원 칼럼">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{COL6_URL}">
<meta property="og:image" content="https://jgkorea8275.co.kr/images/column-6-hero.jpg">
<meta property="og:image:width" content="743">
<meta property="og:image:height" content="743">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://jgkorea8275.co.kr/images/column-6-hero.jpg">
<meta property="article:published_time" content="2026-11-17">
<script type="application/ld+json">{json.dumps(COL6_LD, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(COL6_CRUMB, ensure_ascii=False)}</script>
{FONTS}
<link rel="stylesheet" href="assets/site.css?v={VER}">
</head>'''

    body = f'''<body class="has-dock">
{SPRITE}
{header('index.html')}
<div class="cbanner">
  <img src="images/column-banner.jpg" alt="" width="1600" height="900">
  <div class="wrap"><p class="ttl">건강 칼럼</p><p>진료실에서 자주 받는 질문을 쉽게 풀어 씁니다.</p></div>
</div>
<main class="art column">
  <a class="back" href="index.html#column">{ic("back")}목록으로</a>
  <header class="art-head">
    <span class="chip">칼럼 · 침 치료 원리</span>
    <h1>{title}</h1>
    
    <p class="art-meta"><span><time datetime="2026-11-17">2026.11.17</time></span><span>정관고려한의원 건강 칼럼</span></p>
  </header>

  <section class="sum" aria-labelledby="sum-h">
    <h2 id="sum-h">이 글에서 알 수 있는 내용</h2>
    <ul>
      {chk('경락과 경혈, 현대 과학은 어떻게 보고 있을까요')}
      {chk('침이 통증을 줄이는 네 가지 원리')}
      {chk('침은 몸이 스스로 진통제를 만들도록 깨우는 치료')}
    </ul>
    <details class="toc"><summary>목차 보기{ic("down")}</summary><ol>{toc_html}</ol></details>
  </section>

  <div class="prose" data-size="0">
    <figure><img src="images/column-6-hero.jpg" alt="침의 원리 · “원장님, 침은 어떻게 해서 낫는 거예요?” 침은 어떻게 통증을 줄일까요? 침 치료 원리, 과학으로 쉽게 풀어 봅니다" width="743" height="743"></figure>

    <p>오늘은 <b>침이 어떻게 우리 몸을 낫게 하는지</b>, 침치료의 원리에 대해 이야기해 보겠습니다.</p>
    <p>얼마 전, 허리가 아파 침을 맞으러 오는 고교 남학생 환자가 이렇게 물었습니다.</p>
    <p class="lead-quote">"원장님, 침은 어떻게 해서 낫는 거예요?"</p>
    <p>그래서 이렇게 설명해 주었습니다.</p>
    <p class="quote">"우리 몸에는 <b>경락</b>이라는, 기(氣)가 흐르는 길이 있어.<br>그 길 위의 중요한 지점을 <b>경혈</b>, 흔히 혈자리라고 하지.<br>침으로 혈자리를 자극하면 기가 잘 돌게 되고,<br>몸이 스스로 낫도록 돕는 거야."</p>
    <p>학생이 잠시 생각하더니 웃으며 말했습니다.</p>
    <p class="quote">"왠지…무협지 같아요.^^"</p>
    <p>듣고 보니 그럴 만합니다.<br>혈자리, 기의 흐름.<br>무협 소설에서 많이 본 말들이니까요.</p>
    <p>그래서 현대인의 관점에서 이해되기 쉽도록 과학적인 설명을 곁들여 주었습니다.<br>오늘은 그 내용을 조금 더 자세히 풀어 보겠습니다.</p>
    <figure><img src="images/column-6-talk.jpg" alt="침대에 엎드려 허리에 침을 맞고 있는 학생이 고개를 돌려 웃고, 흰 가운을 입은 한의사가 손짓하며 설명하는 모습" width="743" height="557" loading="lazy"></figure>

    <h2 id="s1">경락은 '옛 사람들이 그린 몸의 지도'입니다</h2>
    <p>경락은 수천 년 동안 환자를 보며 쌓은 경험을 정리한 <b>몸의 지도</b>입니다.<br>"여기를 자극하니 저기가 편해지더라"는 관찰을 선으로 이어 놓은 것이죠.<br>하지만 현대 해부학에서 경락이라는 관이 따로 발견된 것은 아닙니다.</p>
    <p>그렇다면 이런 질문이 생깁니다.</p>
    <p class="quote"><b>"침을 놓으면 몸 안에서 실제로 무슨 일이 일어날까요?"</b></p>
    <p>이 질문에 답하기 위해 미국과 유럽을 비롯한 여러 나라에서 연구가 이루어지고 있습니다.<br>1997년에는 미국 국립보건원(NIH)이 침 치료에 대한 합의 회의를 열기도 했습니다.<sup>1</sup></p>
    <p>아직 침의 모든 원리가 밝혀진 것은 아닙니다만, 지금까지 어떤 연구가 이루어졌는지 하나씩 살펴보겠습니다.</p>

    <h2 id="s2">① 통증이 지나가는 '문'을 조절합니다</h2>
    <h3 class="sub-h">관문조절설</h3>
    <p>어딘가에 부딪혔을 때 아픈 부위를 손으로 문지른 적 있으시죠?<br>문지르면 조금 덜 아프게 느껴질 때가 있습니다.</p>
    <p>1965년 멜잭과 월이라는 두 학자가 이 현상을 설명했습니다.<sup>2</sup><br>척수에는 통증 신호가 뇌로 올라가는 <b>문(관문)</b>이 있는데, 만지고 누르는 자극이 먼저 들어오면 이 문이 닫혀 통증 신호가 덜 올라간다는 것입니다.<br>이것을 <b>관문조절설</b>이라고 합니다.</p>
    <p>침 자극으로 통증이 줄어드는 과정에도 이러한 신경계의 조절이 관여할 수 있습니다.</p>
    <figure class="tall"><img src="images/column-6-gate.jpg" alt="같은 높이의 척수로 두 신호가 함께 들어갑니다: 허리의 아픈 곳에 놓은 침 자극과 통증 신호가 함께 척수의 ‘관문’으로 들어가고, 뇌는 통증을 덜 느낍니다" width="743" height="929" loading="lazy"><figcaption>아픈 곳에 놓은 침의 자극이 척수의 문을 닫아, 통증 신호가 덜 올라가게 합니다.</figcaption></figure>
    <p>다만 침의 효과를 관문조절설 하나로 모두 설명할 수는 없습니다.</p>

    <h2 id="s3">② 몸이 스스로 진통제를 만들도록 합니다</h2>
    <h3 class="sub-h">내인성 진통물질</h3>
    <p>우리 몸 안에는 <b>천연 진통제</b>가 있습니다.<br>엔도르핀, 엔케팔린 같은 물질입니다.<br>이런 물질을 <b>내인성 진통물질</b>이라고 합니다.<br>('내인성'은 몸 안에서 만들어진다는 뜻입니다.)</p>
    <p>1970년대 동물 실험에서, 침으로 통증이 줄어든 상태에서 이 물질들의 작용을 막는 약(날록손)을 주면 침의 진통 효과가 사라졌습니다.<sup>3</sup></p>
    <p>침의 효과가 기분 탓이 아니라, <b>몸속 진통물질 덕분</b>이라는 뜻입니다.</p>
    <p>중국의 한지성 교수는 전침의 자극 주파수에 따라 나오는 물질이 다르다는 것도 밝혔습니다.<sup>4</sup></p>
    <p>낮은 주파수에서는 엔도르핀·엔케팔린이, 높은 주파수에서는 다이노르핀이 주로 나옵니다.</p>
    <p>한마디로 요약해서 말씀드리면,</p>
    <p class="key"><b>침은 진통제를 넣는 것이 아니라,<br>몸이 진통제를 만들도록 깨우는 치료입니다.</b></p>
    <figure><img src="images/column-6-glow.jpg" alt="엎드려 허리에 침을 맞은 사람의 몸에서 침 자리부터 척추를 따라 뇌까지 빛나는 신경 신호가 퍼져 나가는 모습" width="743" height="557" loading="lazy"><figcaption>침 자극이 신경을 타고 뇌에 전해지면, 몸 안에서 천연 진통제가 퍼져 나갑니다.</figcaption></figure>

    <h2 id="s4">③ 침 맞은 자리에서도 변화가 일어납니다</h2>
    <p>2010년 학술지 『네이처 뉴로사이언스』에 흥미로운 쥐 실험 연구가 실렸습니다.</p>
    <p>침을 놓고 돌리면 그 주변 조직에서 <b>아데노신</b>이라는 물질이 늘어나고, 이 물질이 통증을 누그러뜨린다는 것입니다.<sup>5</sup></p>
    <p>또 침을 놓으면 근육을 싸고 있는 막(근막)과 결합조직이 침에 살짝 감기며 세포에 자극이 전달된다는 가설을 제시한 연구도 있습니다.<sup>6</sup></p>
    <p>침을 맞을 때 뻐근하고 묵직한 느낌, 한의학에서 말하는 <b>득기(得氣)</b>도 이 현상과 관련이 있다고 봅니다.</p>

    <h2 id="s5">④ 뇌와 몸 전체가 반응합니다</h2>
    <p>뇌 영상(fMRI) 연구에서는 침을 맞는 동안 통증과 감정을 처리하는 뇌 부위의 활동이 달라지는 모습이 관찰됐습니다.<sup>7</sup></p>
    <p>2021년에는 과학 학술지 『네이처』에 쥐의 다리 혈자리(족삼리)에 전침을 놓았더니 <b>미주신경–부신 경로</b>가 활성화되어 몸의 염증 반응이 조절되었다는 연구가 실렸습니다.<sup>8</sup></p>
    <p>침 한 자리의 자극이 신경을 타고 <b>몸 전체의 균형</b>에 영향을 준다는 것.</p>
    <p>옛 사람들이 "기의 흐름을 돕는다"고 표현한 것을, 지금의 과학은 신경과 물질의 언어로 하나씩 설명해 가고 있는 셈입니다.</p>

    <h2 id="s6">한눈에 정리하면</h2>
    <figure><img src="images/column-6-summary.jpg" alt="침치료의 원리: 침 자극을 가운데 두고 ① 통증 신호 조절(관문), ② 몸속 진통물질의 작용, ③ 침 놓은 자리의 변화, ④ 뇌·신경 조절의 네 갈래로 나뉜 그림" width="743" height="743" loading="lazy"><figcaption>침치료의 원리</figcaption></figure>
    <p>이렇게 침 자극에 대한 우리 몸의 반응은 한 가지로만 설명하기 어렵습니다.</p>
    <p><b>통증 신호의 조절, 몸속 진통물질의 작용, 침 놓은 자리의 변화, 뇌와 신경계의 반응</b> 등이 함께 연구되고 있습니다.</p>
    <p class="note">위의 번호는 설명을 위한 순서입니다. 이런 반응이 반드시 ①부터 ④까지 차례대로 일어난다는 뜻은 아닙니다.</p>

    <h2 id="s7">다시 그 학생 이야기로 돌아와서,</h2>
    <p>요즘 그 학생은 침을 맞고 나면 허리가 한결 가볍다고 합니다.</p>
    <p>이제는 "무협지 같다"는 말 대신<br>"제 몸이 진통제를 만드는 거죠?" 하고 묻습니다.^^</p>
    <p>침은 몸에 없는 것을 억지로 넣는 치료가 아닙니다.</p>
    <p class="key"><b>우리 몸이 원래 가진 회복하는 힘을 깨워 주는 치료입니다.</b></p>
    <p>경락은 옛 사람들의 지도였고,<br>과학은 지금 그 지도를 하나씩 확인해 가는 중입니다.</p>
    <p class="ps">ps. 질문하는 환자는 늘 반갑습니다. 덕분에 저도 다시 공부하게 되네요.</p>
    <p class="sign">한의학박사 · 한방재활의학과 전문의 <b>박장우</b></p>

    <details class="refs">
      <summary>참고문헌{ic("down")}</summary>
      <ol>
        <li>NIH Consensus Conference. Acupuncture. <i>JAMA</i>. 1998;280(17):1518-1524. <a href="https://doi.org/10.1001/jama.280.17.1518" target="_blank" rel="noopener">doi:10.1001/jama.280.17.1518</a></li>
        <li>Melzack R, Wall PD. Pain mechanisms: a new theory. <i>Science</i>. 1965;150(3699):971-979. <a href="https://doi.org/10.1126/science.150.3699.971" target="_blank" rel="noopener">doi:10.1126/science.150.3699.971</a></li>
        <li>Pomeranz B, Chiu D. Naloxone blockade of acupuncture analgesia: endorphin implicated. <i>Life Sciences</i>. 1976;19(11):1757-1762. <a href="https://doi.org/10.1016/0024-3205(76)90084-9" target="_blank" rel="noopener">doi:10.1016/0024-3205(76)90084-9</a></li>
        <li>Han JS. Acupuncture: neuropeptide release produced by electrical stimulation of different frequencies. <i>Trends in Neurosciences</i>. 2003;26(1):17-22. <a href="https://doi.org/10.1016/s0166-2236(02)00006-1" target="_blank" rel="noopener">doi:10.1016/s0166-2236(02)00006-1</a></li>
        <li>Goldman N, Chen M, Fujita T, et al. Adenosine A1 receptors mediate local anti-nociceptive effects of acupuncture. <i>Nature Neuroscience</i>. 2010;13(7):883-888. <a href="https://doi.org/10.1038/nn.2562" target="_blank" rel="noopener">doi:10.1038/nn.2562</a></li>
        <li>Langevin HM, Churchill DL, Cipolla MJ. Mechanical signaling through connective tissue: a mechanism for the therapeutic effect of acupuncture. <i>FASEB Journal</i>. 2001;15(12):2275-2282. <a href="https://doi.org/10.1096/fj.01-0015hyp" target="_blank" rel="noopener">doi:10.1096/fj.01-0015hyp</a></li>
        <li>Hui KK, Liu J, Makris N, et al. Acupuncture modulates the limbic system and subcortical gray structures of the human brain: evidence from fMRI studies in normal subjects. <i>Human Brain Mapping</i>. 2000;9(1):13-25. <a href="https://doi.org/10.1002/(SICI)1097-0193(2000)9:1%3C13::AID-HBM2%3E3.0.CO;2-F" target="_blank" rel="noopener">doi:10.1002/(SICI)1097-0193(2000)9:1&lt;13::AID-HBM2&gt;3.0.CO;2-F</a></li>
        <li>Liu S, Wang Z, Su Y, et al. A neuroanatomical basis for electroacupuncture to drive the vagal-adrenal axis. <i>Nature</i>. 2021;598(7882):641-645. <a href="https://doi.org/10.1038/s41586-021-04001-4" target="_blank" rel="noopener">doi:10.1038/s41586-021-04001-4</a></li>
      </ol>
    </details>
  </div>

  <aside class="ccta" aria-label="진료 안내">
    <div class="ccta-top"><img src="images/c9de5ada.png" alt="" width="220" height="220"><div><b>정관고려한의원 진료 안내</b><p>예약 없이 방문하세요. {ADDR}</p></div></div>
    <div class="acts"><a class="btn-gold" href="{TEL_HREF}">{ic("phone")}전화 문의 {TEL}</a><a class="btn-line" href="index.html#hours">진료시간</a></div>
  </aside>

  <p class="src-link"><a href="https://blog.naver.com/jgkorea8275/224480664949" target="_blank" rel="noopener">네이버 블로그에서 원문 보기{ic("ext")}</a></p>

  <div class="tools">
    <a class="back" href="index.html#column">{ic("back")}목록으로</a>
    <div class="r">
      <button type="button" data-share>{ic("share")}공유하기</button>
      <button type="button" data-font aria-label="글자 크기: 보통"><span class="ga" aria-hidden="true">가</span>글자 크기</button>
    </div>
  </div>

  <nav class="related" aria-label="함께 보기">
    <h2>함께 보기</h2>
    <ul>
      <li><a href="column-2.html">칼럼 · 근육통 회복 속도를 결정하는 네가지 요인{ic("chev")}</a></li>
      <li><a href="column-5.html">칼럼 · 자고 일어났더니 목이 안 돌아가요{ic("chev")}</a></li>
      <li><a href="essay-4.html">에세이 · 불은 그대로인데 사이렌만 끄고 있지는 않습니까?{ic("chev")}</a></li>
      <li><a href="index.html#treatment">치료 방법 · 침과 전침{ic("chev")}</a></li>
    </ul>
  </nav>
</main>
{footer()}
{dock('index.html')}
<script src="assets/site.js?v={VER}"></script>
{ANALYTICS}
</body>
</html>
'''
    return head + '\n' + body

COL7_URL = 'https://jgkorea8275.co.kr/column-7.html'
COL7_TITLE = '얼굴이 떨리고 저릴 때, 걱정해야 할까요? (눈꺼풀 떨림, 안면경련, 구안와사, 뇌졸중 신호)'
COL7_LD = {"@context": "https://schema.org", "@type": "Article", "headline": "얼굴이 떨리고 저릴 때, 걱정해야 할까요? (눈꺼풀 떨림, 안면경련, 구안와사, 뇌졸중 신호)", "datePublished": "2026-11-19", "image": ["https://jgkorea8275.co.kr/images/column-7-hero.jpg"], "mainEntityOfPage": "https://jgkorea8275.co.kr/column-7.html", "author": {"@type": "Person", "name": "박장우", "jobTitle": "한의학박사, 한방재활의학과 전문의"}, "publisher": {"@type": "Organization", "name": "정관고려한의원", "logo": {"@type": "ImageObject", "url": "https://jgkorea8275.co.kr/favicon.png"}}}
COL7_CRUMB = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "정관고려한의원", "item": "https://jgkorea8275.co.kr/"},
    {"@type": "ListItem", "position": 2, "name": "칼럼 및 에세이", "item": "https://jgkorea8275.co.kr/#column"},
    {"@type": "ListItem", "position": 3, "name": "얼굴이 떨리고 저릴 때, 걱정해야 할까요?", "item": "https://jgkorea8275.co.kr/column-7.html"}]}

def column7():
    title = COL7_TITLE.replace('"', '&quot;')
    title_plain = title
    title_attr = title
    desc = '눈꺼풀 떨림부터 반측성 안면경련, 구안와사, 삼차신경통, 대상포진, 뇌졸중 신호까지. 걱정하지 않아도 될 떨림과 바로 119를 불러야 할 신호를 구분해 정리했습니다.'
    toc = [('s1', '먼저 결론부터'), ('s2', "얼굴에는 두 종류의 '전깃줄'이 있습니다"), ('s3', '떨릴 때'), ('s4', '얼굴 한쪽이 굳을 때'),
           ('s5', '저리거나 아플 때'), ('s6', '실제로 떨리는 것과 떨리는 느낌만 있는 것은 다릅니다'), ('s7', '이럴 땐 망설이지 마세요'),
           ('s8', '한의학에서는 어떻게 볼까요'), ('s9', '집에서 해 볼 수 있는 것'), ('s10', '한눈에 정리'), ('s11', '마치며')]
    chk = lambda t: f'<li>{ic("check")}<span>{t}</span></li>'
    toc_html = ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    head = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title_plain} | 칼럼 | 정관고려한의원</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<meta name="theme-color" content="#171511">
<link rel="canonical" href="{COL7_URL}">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="alternate" type="application/rss+xml" title="정관고려한의원 칼럼·에세이" href="https://jgkorea8275.co.kr/rss.xml">
<meta property="og:type" content="article">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="정관고려한의원">
<meta property="og:title" content="{title_attr} | 정관고려한의원 칼럼">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{COL7_URL}">
<meta property="og:image" content="https://jgkorea8275.co.kr/images/column-7-hero.jpg">
<meta property="og:image:width" content="743">
<meta property="og:image:height" content="743">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://jgkorea8275.co.kr/images/column-7-hero.jpg">
<meta property="article:published_time" content="2026-11-19">
<script type="application/ld+json">{json.dumps(COL7_LD, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(COL7_CRUMB, ensure_ascii=False)}</script>
{FONTS}
<link rel="stylesheet" href="assets/site.css?v={VER}">
</head>'''

    body = f'''<body class="has-dock">
{SPRITE}
{header('index.html')}
<div class="cbanner">
  <img src="images/column-banner.jpg" alt="" width="1600" height="900">
  <div class="wrap"><p class="ttl">건강 칼럼</p><p>진료실에서 자주 받는 질문을 쉽게 풀어 씁니다.</p></div>
</div>
<main class="art column">
  <a class="back" href="index.html#column">{ic("back")}목록으로</a>
  <header class="art-head">
    <span class="chip">칼럼 · 얼굴 떨림·저림</span>
    <h1>{title}</h1>
    
    <p class="art-meta"><span><time datetime="2026-11-19">2026.11.19</time></span><span>정관고려한의원 건강 칼럼</span></p>
  </header>

  <section class="sum" aria-labelledby="sum-h">
    <h2 id="sum-h">이 글에서 알 수 있는 내용</h2>
    <ul>
      {chk('걱정하지 않아도 되는 떨림과 진료가 필요한 떨림')}
      {chk('저리고 아플 때 원인을 알려 주는 단서')}
      {chk('바로 119를 불러야 하는 뇌졸중 신호')}
    </ul>
    <details class="toc"><summary>목차 보기{ic("down")}</summary><ol>{toc_html}</ol></details>
  </section>

  <div class="prose" data-size="0">
    <figure><img src="images/column-7-hero.jpg" alt="얼굴 떨림·저림 · “원장님, 눈 밑이 며칠째 떨려요” 얼굴이 떨리고 저릴 때 · 얼굴 떨림·저림, 걱정할 떨림과 서두를 신호" width="743" height="743"></figure>

    <p>눈 밑이 저 혼자 파르르 떨린 적 있으신가요?<br>얼굴 한쪽이 내 살 같지 않고 멍한 느낌이 든 적은요?</p>
    <figure><img src="images/column-7-mirror.jpg" alt="거울 앞에서 눈 밑을 손가락으로 짚으며 걱정스러운 얼굴로 들여다보는 여성" width="743" height="499" loading="lazy"></figure>
    <p>이런 증상이 생기면 두 가지 마음이 듭니다.<br>"설마 큰 병인가?" 하는 걱정, 그리고 "피곤해서 그렇겠지" 하는 방심입니다.</p>
    <p>진료실에서는 두 경우를 모두 자주 봅니다.<br>걱정하지 않아도 될 분은 너무 걱정하시고, 서둘러야 할 분은 너무 늦게 오시는 경우가 많습니다.</p>
    <p>오늘은 그 둘을 구분하는 법을 쉽게 정리해 드리겠습니다.</p>

    <h2 id="s1">먼저 결론부터</h2>
    <p><b>얼굴 떨림은 대부분 피곤해서 생깁니다.</b><br>푹 자고 쉬면 대개 저절로 좋아지는 경우가 많습니다.</p>
    <p class="key alert">하지만,<br><b>얼굴이 갑자기 한쪽으로 처지거나<br>말이 어눌해지거나<br>팔다리에 힘이 빠지면</b><br>뇌졸중의 신호일 수 있으니 기다리지 마시고 <b>바로 119</b>를 부르시기 바랍니다.</p>

    <h2 id="s2">얼굴에는 두 종류의 '전깃줄'이 있습니다</h2>
    <p>우리 얼굴에는 뇌에서 나온 신경이 전깃줄처럼 퍼져 있습니다.<br>그 중 중요한 두 신경이 있습니다.</p>
    <figure class="tall"><img src="images/column-7-nerves.jpg" alt="얼굴에는 두 종류의 ‘전깃줄’이 있습니다: 안면신경은 얼굴을 ‘움직이게’ 하는 줄로 문제가 생기면 떨림·마비, 삼차신경은 얼굴을 ‘느끼게’ 하는 줄로 문제가 생기면 저림·찌릿한 통증" width="743" height="966" loading="lazy"></figure>
    <p><b>하나는 얼굴을 '움직이게' 하는 줄, 안면신경입니다.</b><br>눈을 감고, 웃고, 입을 오므리는 일을 합니다.<br>이 줄에 전기가 제멋대로 흐르면 얼굴이 떨리고, 전기가 잘 안 흐르면 얼굴이 마비됩니다.</p>
    <p><b>다른 하나는 얼굴을 '느끼게' 하는 줄, 삼차신경입니다.</b><br>손이 닿는 느낌, 뜨겁고 차가운 느낌, 아픈 느낌을 뇌로 전해 줍니다.<br>이 줄에 문제가 생기면 저리거나, 멍하거나, 찌릿하게 아픕니다.</p>
    <p>그러니까 간단히 말해,</p>
    <p class="key"><b>"떨린다"는 안면신경의 이야기,<br>"저리다·아프다"는 삼차신경의 이야기입니다.</b></p>
    <p class="note">(물론 모든 얼굴떨림과 저림이 이 두 신경 자체의 문제로 생기는 것만은 아닙니다.)</p>

    <h2 id="s3">떨릴 때</h2>
    <h3 class="factor"><span>① 눈 밑이나 눈꺼풀만 파르르 떨린다면</span></h3>
    <p>가장 흔한 경우이고, 걱정하지 않으셔도 됩니다.<br>의학적으로는 <b>안검근파동증(눈꺼풀 떨림)</b>이라고 부릅니다.</p>
    <p>잠을 못 잤거나, 신경 쓸 일이 많거나, 커피를 많이 마셨거나, 휴대폰을 오래 보셨을 때 잘 생깁니다.<br>몸이 "좀 쉬어 달라"고 보내는 신호입니다.</p>
    <figure><img src="images/column-7-rest.jpg" alt="밤늦게 침대에서 휴대폰을 보는 피곤한 여성과, 소파에 기대어 따뜻한 수건을 눈에 얹고 쉬는 여성의 두 장면" width="743" height="415" loading="lazy"></figure>
    <p>눈꺼풀 일부가 파르르 떨리다가 멈추기를 반복합니다.<br>본인은 심하게 떨리는 것 같지만, 다른 사람이 보기에는 잘 보이지 않을 정도로 미세한 경우도 많습니다.<br>보통 <b>며칠, 길면 몇 주 안에 저절로 멈춥니다.</b><sup>1</sup></p>
    <p>영양제를 찾기보다 잠을 충분히 자고 커피를 줄이고, 눈을 쉬게 해주는 것이 좋습니다.</p>
    <div class="qbox">
      <p class="qbox-h">눈꺼풀이 떨리면 마그네슘이 부족한 걸까요?</p>
      <p>눈꺼풀이 떨리면 마그네슘을 드시는 분들이 많습니다.<br>마그네슘은 신경과 근육이 정상적으로 움직이는 데 필요한 영양소입니다.</p>
      <p>실제로 심하게 부족하면 근육이 떨리거나 경련이 생길 수 있습니다.<br>하지만 건강한 사람에게 나타나는 일시적인 눈꺼풀 떨림이 대부분 마그네슘 부족 때문이라는 근거는 부족합니다.</p>
      <p>오히려 <b>피로, 수면 부족, 스트레스, 카페인 섭취</b> 등이 더 흔하게 관련됩니다.</p>
      <p>따라서 눈꺼풀이 떨린다고 무조건 마그네슘 영양제부터 드실 필요는 없습니다.</p>
    </div>

    <h3 class="factor"><span>② 눈에서 볼, 입꼬리까지 번진다면</span></h3>
    <p>이때는 이야기가 다릅니다.<br>처음에는 눈가만 떨리다가 점점 볼과 입꼬리까지, <b>얼굴 한쪽이 통째로 실룩거립니다.</b><br>몇 달이 지나도 나아지지 않고 점점 심해질 수 있습니다.<br>이것을 <b>반쪽얼굴연축(반측성 안면경련)</b>이라고 합니다.</p>
    <p>대부분은 머릿속에서 혈관이 안면신경을 꾹 누르고 있어서 생깁니다.<sup>2</sup><br>전깃줄을 계속 눌러 스파크가 튀는 것과 비슷합니다.<br>그래서 자고 쉬어서 풀리는 문제가 아닙니다.</p>
    <p><b>신경과에서 진찰을 받고, 필요하면 MRI 검사로 원인을 확인하는 것이 먼저입니다.</b><br>증상에 따라 보톡스 주사나 혈관을 신경에서 떼어 놓는 수술(미세혈관감압술)로 좋아질 수 있습니다.</p>
    <figure class="tall"><img src="images/column-7-spread.jpg" alt="떨림, 어디까지 번지는지 보세요: 눈 밑에서만 파르르 떨리면 대부분 피로 신호(안검근파동증)로 푹 쉬면 대개 멈추고, 눈에서 볼, 입꼬리까지 한쪽으로 번지면 반측성 안면경련 가능성이 있어 신경과 진료가 먼저입니다" width="743" height="966" loading="lazy"></figure>
    <p><b>기억하실 점은 한 가지입니다.</b></p>
    <p>눈꺼풀만 가끔 떨린다면 대부분 피로와 관련이 있지만, 떨림이 오래 지속되거나 심해지고 같은 쪽 입 주변까지 번진다면 신경과 진료를 받아보는 것이 좋습니다.</p>

    <h2 id="s4">얼굴 한쪽이 굳을 때</h2>
    <h3 class="factor"><span>귀 뒤가 아프고, 얼굴이 먹먹하고, 맛이 이상하다면</span></h3>
    <p>흔히 '입이 돌아간다'고 하는 <b>구안와사(안면신경마비)</b>를 생각해 볼 수 있습니다.<br>그 중 뚜렷한 원인이 확인되지 않는 경우를 '벨마비'라고 합니다.</p>
    <p>귀 뒤 통증, 얼굴이 먹먹한 느낌, 맛이 이상한 느낌이 하루 이틀 먼저 오고, 그 뒤에 한쪽 눈이 잘 안 감기고 물을 마시면 입가로 새는 일이 생깁니다.</p>
    <p class="key">안면신경마비는<br><b>증상이 시작되고 72시간(3일) 안에<br>병원에서 스테로이드 치료를 시작하는 것</b>이<br>회복에 가장 중요합니다.<sup>5,6</sup></p>
    <p>저는 평소 스테로이드를 되도록 피하자고 말씀드리는 편이지만, 이 경우만큼은 꼭 필요한 치료입니다.</p>
    <p>다만 갑자기 얼굴이 마비되었다면 벨마비인지 뇌졸중인지 먼저 구별해야 합니다.<br>스스로 판단하지 마시고 신속하게 진료를 받으시기 바랍니다.</p>
    <p>침치료 등은 환자의 상태에 따라 병원 치료와 함께 보조적으로 고려할 수 있습니다.</p>

    <h2 id="s5">저리거나 아플 때</h2>
    <p>감각이 이상할 때는 <b>'어떻게' 이상한지</b>가 원인을 알려 주는 단서입니다.</p>
    <h3 class="factor"><span>① 찌릿! 전기 오듯 몇 초간 아프다면</span></h3>
    <p>세수하거나, 양치하거나, 찬바람을 맞을 때 얼굴에 전기가 튀는 것처럼 확 아팠다가 멈춥니다.<br>삼차신경이 예민해져서 생기는 <b>삼차신경통</b>일 수 있습니다.<br>자꾸 반복되면 진료를 받으시기 바랍니다.<sup>3</sup></p>
    <h3 class="factor"><span>② 화끈·따끔하다가 물집이 생겼다면</span></h3>
    <p><b>대상포진</b>일 수 있습니다.<br>몸의 면역력이 떨어졌을 때 얼굴 한쪽에 잘 생깁니다.<br>얼굴 대상포진은 대부분 삼차신경을 따라 생기고, 특히 이마와 눈 주변에 많습니다.<br>물집이 보이기 전에 따갑고 아픈 느낌만 먼저 오기도 해서 처음엔 다른 병으로 오해하기 쉽습니다.</p>
    <p>대상포진은 가능한 한 빨리 진료를 받아 항바이러스제 치료가 필요한지 확인하는 것이 좋습니다.</p>
    <p>특히 눈 근처나 코끝에 물집이 생겼다면 눈에도 영향을 줄 수 있으므로 신속한 진료가 필요합니다.</p>
    <p>귀 주변에 물집이 생기면서 얼굴까지 마비되는 경우(람세이헌트 증후군, 안면신경 쪽에 생기는 경우)<sup>4</sup>도 있어 서둘러야 합니다.</p>
    <h3 class="factor"><span>③ 검사는 괜찮다는데 은근히 저리다면</span></h3>
    <p>검사를 받아도 특별한 원인이 발견되지 않는 경우가 있습니다.<br><b>스트레스가 심하거나, 숨을 지나치게 빠르게 쉬거나, 턱 주변 근육이 긴장</b>되어 있을 때도 얼굴이 얼얼하거나 불편한 느낌이 들 수 있습니다.</p>
    <p>다만 한쪽 얼굴의 감각이 실제로 떨어지거나 증상이 계속된다면 다시 진료를 받아보는 것이 좋습니다.</p>

    <h2 id="s6">실제로 떨리는 것과 떨리는 느낌만 있는 것은 다릅니다</h2>
    <p>환자분들은 두 경우를 모두 "얼굴이 떨린다"고 표현하기도 합니다.<br>하지만 자세히 살펴보면 차이가 있습니다.</p>
    <p><b>첫 번째는 실제로 근육이 움직이는 경우입니다.</b></p>
    <p>눈꺼풀이나 입꼬리가 파르르 움직이거나 씰룩거립니다.<br>이때는 근육을 움직이는 신경의 문제를 먼저 생각합니다.</p>
    <p><b>두 번째는 겉으로 움직임이 없는데 떨리는 느낌만 있는 경우입니다.</b></p>
    <p>피부 아래에서 무언가 꿈틀거리거나 전기가 흐르는 듯한 느낌이 들기도 합니다.<br>이런 경우에는 아주 미세한 근육 떨림일 수도 있고, 감각신경에서 생긴 이상한 느낌일 수도 있습니다.</p>
    <p>따라서 실제 근육이 움직이는지, 단지 그런 느낌만 있는지를 구별하는 것이 중요합니다.<br>증상이 나타날 때 휴대전화로 짧은 영상을 찍어두면 진료에 도움이 될 수 있습니다.</p>

    <h2 id="s7">이럴 땐 망설이지 마세요</h2>
    <p>이 글에서 가장 중요한 부분입니다.<br>아래 중 하나라도 <b>갑자기</b> 생겼다면, 내일 병원 갈 일이 아닙니다.<br><b>지금 바로 119입니다.</b></p>
    <figure class="tall"><img src="images/column-7-stroke.jpg" alt="이런 증상이 갑자기 생기면 바로 119: ① “이~” 하고 웃어 보기 — 얼굴 한쪽이 처지거나 입꼬리가 비뚤어진다, ② 두 팔 앞으로 들기 — 한쪽 팔이 스르르 내려간다, ③ 말해 보기 — 말이 꼬이거나 하고 싶은 말이 안 나온다. 증상이 시작된 시각을 꼭 기억해 두세요" width="743" height="1329" loading="lazy"></figure>
    <ul class="checks">
      <li>{ic("check")}<span>얼굴 한쪽이 갑자기 처지거나 입꼬리가 비뚤어진다.</span></li>
      <li>{ic("check")}<span>한쪽 팔이나 다리에 힘이 빠진다.</span></li>
      <li>{ic("check")}<span>말이 어눌해지거나 말을 이해하기 어렵다.</span></li>
      <li>{ic("check")}<span>한쪽 얼굴의 감각이 갑자기 둔해진다.</span></li>
      <li>{ic("check")}<span>갑자기 한쪽 눈이 잘 안 보이거나, 물체가 두 개로 보인다.</span></li>
      <li>{ic("check")}<span>갑자기 걷기 어려울 정도로 어지럽거나 극심한 두통이 생긴다.</span></li>
    </ul>
    <p>이런 증상은 <b>뇌졸중(중풍)</b>의 신호일 수 있습니다.<br>뇌졸중은 뇌혈관이 막히거나 터져서 뇌의 기능에 문제가 생기는 질환입니다.</p>
    <p>특히 뇌혈관이 막힌 경우에는 정해진 시간 안에 치료를 시작해야 효과를 기대할 수 있는 치료들이 있습니다.<sup>7</sup><br>따라서 빨리 병원에 도착하는 것이 중요합니다.</p>
    <p>119에 연락할 때는 증상이 언제 시작되었는지, 마지막으로 정상이었던 시각이 언제인지 알려주시기 바랍니다.</p>
    <figure><img src="images/column-7-call.jpg" alt="소파에 앉은 노인이 두 팔을 앞으로 들었는데 한쪽 팔이 내려가고, 옆에서 가족이 노인의 어깨를 짚으며 전화로 119에 연락하는 두 장면" width="743" height="415" loading="lazy"></figure>
    <p>또 한 가지 기억하실 점이 있습니다.</p>
    <p><b>갑자기 한쪽 얼굴의 감각만 둔해졌더라도 뇌졸중일 가능성을 배제할 수 없습니다.</b><br>몇 분 뒤 정상으로 돌아왔다고 안심해서도 안 됩니다.<br>뇌혈관이 일시적으로 막혔다가 다시 뚫리는 현상(TIA)일 수도 있기 때문입니다.<br>이런 경우는 앞으로 뇌졸중이 발생할 위험을 알리는 경고 신호가 될 수 있습니다.</p>

    <h2 id="s8">한의학에서는 어떻게 볼까요</h2>
    <p>한의학에서는 떨리고, 저리고, 갑자기 생기는 증상을 바람에 빗대어 <b>풍(風)</b>이라고 불렀습니다.<br>바람이 나뭇잎을 흔들 듯, 몸의 기운이 흔들리면 얼굴이 떨리고 저리다고 본 것이죠.<br>그 바탕에는 몸이 지쳐서 근육과 신경에 영양이 충분히 가지 못하는 상태, 즉 기혈(氣血, 몸의 기운과 혈액)이 부족한 상태로 보기도 합니다.</p>
    <p>솔직하게 말씀드리면, 위에서 "바로 119", "신경과 진료"라고 적은 경우는 그쪽이 먼저입니다.</p>
    <p>그렇다면 한의학적 치료는 언제 도움이 될까요?</p>
    <h3 class="sub-h">피곤해서 오는 떨림과 저림</h3>
    <p>수면 상태와 피로, 스트레스 등을 살펴보고 필요에 따라 침치료나 생활관리를 보조적으로 고려할 수 있습니다.</p>
    <h3 class="sub-h">구안와사가 회복되는 동안</h3>
    <p>필요한 병원 치료를 받으면서 침치료 등을 함께 합니다.</p>
    <h3 class="sub-h">검사는 괜찮은데 계속 불편할 때</h3>
    <p>몸 상태와 생활습관을 함께 살펴보고, 증상을 악화시키는 요인이 있는지 확인합니다.<br>다만 증상이 지속되거나 악화된다면 추가 검사가 필요한지 다시 판단해야 합니다.</p>
    <figure><img src="images/column-7-acu.jpg" alt="침대에 편안히 누운 여성의 얼굴에 흰 가운을 입은 한의사가 가는 침을 놓는 모습" width="743" height="499" loading="lazy"></figure>
    <p>얼굴에 침을 맞는다고 하면 겁이 나실 수 있는데요.<br>머리카락만큼 가는 침을 쓰기 때문에 생각보다 훨씬 덜 아픕니다.</p>

    <h2 id="s9">집에서 해 볼 수 있는 것</h2>
    <p>단순한 눈꺼풀 떨림이라면 다음과 같은 생활관리가 도움이 될 수 있습니다.</p>
    <ul class="checks">
      <li>{ic("check")}<span><b>잠 충분히 자기</b> — 수면 부족은 눈꺼풀 떨림의 흔한 유발 요인입니다.</span></li>
      <li>{ic("check")}<span><b>커피 줄이기</b> — 카페인을 많이 마신다면 섭취량을 줄여보세요.</span></li>
      <li>{ic("check")}<span><b>눈 쉬게 하기</b> — 휴대전화나 컴퓨터를 오래 사용했다면 중간중간 쉬어주세요.</span></li>
      <li>{ic("check")}<span><b>스트레스 관리하기</b> — 충분한 휴식과 규칙적인 생활이 도움이 됩니다.</span></li>
      <li>{ic("check")}<span><b>증상 기록하기</b> — 언제, 어느 부위가, 얼마나 오래 떨리거나 저렸는지 적어두세요.</span></li>
    </ul>
    <p>단, 갑작스러운 얼굴 감각저하나 마비가 나타났다면 이런 방법으로 기다리지 말고 즉시 진료를 받아야 합니다.</p>

    <h2 id="s10">한눈에 정리</h2>
    <div class="tbl-wrap"><table class="tbl tbl-sm sum">
      <thead><tr><th scope="col">이럴 때</th><th scope="col">생각할 것</th><th scope="col">이렇게</th></tr></thead>
      <tbody>
        <tr><th scope="row">눈꺼풀만 가끔 파르르</th><td>피로·잠 부족·커피<br>(안검근파동증)</td><td>푹 쉬기.<br>한 달 넘게 가면 진료</td></tr>
        <tr><th scope="row">떨림이 얼굴 한쪽으로 번짐</th><td>반측성 안면경련</td><td>신경과 진료</td></tr>
        <tr><th scope="row">전기 오듯 몇 초간 찌릿</th><td>삼차신경통</td><td>반복되면 진료</td></tr>
        <tr><th scope="row">화끈·따끔하다가 물집</th><td>대상포진</td><td>바로 진료</td></tr>
        <tr><th scope="row">귀 뒤 통증 후 눈·입이 한쪽만 안 움직임</th><td>구안와사<br>(안면신경마비)</td><td>3일 안에 병원<br>(스테로이드 치료)</td></tr>
        <tr class="hot"><th scope="row">갑자기 얼굴이 처지거나, 한쪽 얼굴의 감각이 둔해지거나, 말이 어눌해지거나 팔다리에 힘이 빠짐</th><td>뇌졸중(중풍) 가능성</td><td><b>바로 119</b></td></tr>
      </tbody>
    </table></div>

    <h2 id="s11">마치며</h2>
    <p>얼굴이 떨리거나 저린다고 해서 모두 큰 병은 아닙니다.</p>
    <p>하지만 떨림이 점점 심해지거나, 얼굴의 감각이 갑자기 둔해지거나, 얼굴마비와 말이 어눌해지는 증상이 나타난다면 그냥 넘기지 마세요.</p>
    <p>중요한 것은 무조건 걱정하는 것도, 무조건 참는 것도 아닙니다.</p>
    <p class="key"><b>어떤 증상인지 구별하고, 필요한 때에 진료를 받는 것입니다.</b></p>
    <p class="sign">한의학박사 · 한방재활의학과 전문의 <b>박장우</b></p>

    <details class="refs">
      <summary>참고문헌{ic("down")}</summary>
      <ol>
        <li>Barmettler A, et al. Eyelid myokymia: not always benign. <i>Orbit</i>. 2011;30(6):289-90.</li>
        <li>Lu AY, et al. Hemifacial spasm and neurovascular compression. <i>ScientificWorldJournal</i>. 2014;2014:349319.</li>
        <li>Cruccu G, et al. Trigeminal neuralgia: New classification and diagnostic grading. <i>Neurology</i>. 2016;87(2):220-8.</li>
        <li>Sweeney CJ, Gilden DH. Ramsay Hunt syndrome. <i>J Neurol Neurosurg Psychiatry</i>. 2001;71(2):149-54.</li>
        <li>Baugh RF, et al. Clinical practice guideline: Bell's palsy. <i>Otolaryngol Head Neck Surg</i>. 2013;149(3 Suppl):S1-27.</li>
        <li>Madhok VB, et al. Corticosteroids for Bell's palsy. <i>Cochrane Database Syst Rev</i>. 2016;7:CD001942.</li>
        <li>Powers WJ, et al. Guidelines for the Early Management of Acute Ischemic Stroke: 2019 Update. <i>Stroke</i>. 2019;50(12):e344-e418.</li>
      </ol>
    </details>
  </div>

  <aside class="ccta" aria-label="진료 안내">
    <div class="ccta-top"><img src="images/c9de5ada.png" alt="" width="220" height="220"><div><b>정관고려한의원 진료 안내</b><p>예약 없이 방문하세요. {ADDR}</p></div></div>
    <div class="acts"><a class="btn-gold" href="{TEL_HREF}">{ic("phone")}전화 문의 {TEL}</a><a class="btn-line" href="index.html#hours">진료시간</a></div>
  </aside>

  <p class="src-link"><a href="https://blog.naver.com/jgkorea8275/224483198255" target="_blank" rel="noopener">네이버 블로그에서 원문 보기{ic("ext")}</a></p>

  <div class="tools">
    <a class="back" href="index.html#column">{ic("back")}목록으로</a>
    <div class="r">
      <button type="button" data-share>{ic("share")}공유하기</button>
      <button type="button" data-font aria-label="글자 크기: 보통"><span class="ga" aria-hidden="true">가</span>글자 크기</button>
    </div>
  </div>

  <nav class="related" aria-label="함께 보기">
    <h2>함께 보기</h2>
    <ul>
      <li><a href="column-6.html">칼럼 · 침 치료 원리, 과학적으로 쉽게 설명드립니다{ic("chev")}</a></li>
      <li><a href="column-5.html">칼럼 · 자고 일어났더니 목이 안 돌아가요{ic("chev")}</a></li>
      <li><a href="column-4.html">칼럼 · 자다가 종아리에 쥐가 나요{ic("chev")}</a></li>
      <li><a href="index.html#treatment">치료 방법 · 침과 전침{ic("chev")}</a></li>
    </ul>
  </nav>
</main>
{footer()}
{dock('index.html')}
<script src="assets/site.js?v={VER}"></script>
{ANALYTICS}
</body>
</html>
'''
    return head + '\n' + body

COL8_URL = 'https://jgkorea8275.co.kr/column-8.html'
COL8_TITLE = '어깨 힘줄(회전근개) 부분 파열, 수술해야 하나요? 치료방법과 회복기간'
COL8_LD = {"@context": "https://schema.org", "@type": "Article", "headline": "어깨 힘줄(회전근개) 부분 파열, 수술해야 하나요? 치료방법과 회복기간", "datePublished": "2026-11-21", "image": ["https://jgkorea8275.co.kr/images/column-8-hero.jpg"], "mainEntityOfPage": "https://jgkorea8275.co.kr/column-8.html", "author": {"@type": "Person", "name": "박장우", "jobTitle": "한의학박사, 한방재활의학과 전문의"}, "publisher": {"@type": "Organization", "name": "정관고려한의원", "logo": {"@type": "ImageObject", "url": "https://jgkorea8275.co.kr/favicon.png"}}}
COL8_CRUMB = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "정관고려한의원", "item": "https://jgkorea8275.co.kr/"},
    {"@type": "ListItem", "position": 2, "name": "칼럼 및 에세이", "item": "https://jgkorea8275.co.kr/#column"},
    {"@type": "ListItem", "position": 3, "name": "어깨 힘줄(회전근개) 부분 파열, 수술해야 하나요?", "item": "https://jgkorea8275.co.kr/column-8.html"}]}

def column8():
    title = COL8_TITLE.replace('"', '&quot;')
    title_plain = title
    title_attr = title
    desc = '회전근개 부분 파열은 수술 없이 좋아지는 경우가 많습니다. 수술이 필요한 경우, 치료 기간, 재활운동·침치료·주사치료, 집에서 하는 단계별 어깨 운동까지 정리했습니다.'
    toc = [('s1', '회전근개 부분 파열이란'), ('s2', '수술해야 하나요?'), ('s3', '얼마나 치료 받아야 하나요?'), ('s4', '치료는 어떻게 하나요?'),
           ('s5', '회복 중에는 이런 동작을 피하세요'), ('s6', '집에서 하는 어깨 재활운동'), ('s7', '꼭 기억하세요')]
    chk = lambda t: f'<li>{ic("check")}<span>{t}</span></li>'
    toc_html = ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    head = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title_plain} | 칼럼 | 정관고려한의원</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<meta name="theme-color" content="#171511">
<link rel="canonical" href="{COL8_URL}">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="alternate" type="application/rss+xml" title="정관고려한의원 칼럼·에세이" href="https://jgkorea8275.co.kr/rss.xml">
<meta property="og:type" content="article">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="정관고려한의원">
<meta property="og:title" content="{title_attr} | 정관고려한의원 칼럼">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{COL8_URL}">
<meta property="og:image" content="https://jgkorea8275.co.kr/images/column-8-hero.jpg">
<meta property="og:image:width" content="743">
<meta property="og:image:height" content="743">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://jgkorea8275.co.kr/images/column-8-hero.jpg">
<meta property="article:published_time" content="2026-11-21">
<script type="application/ld+json">{json.dumps(COL8_LD, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(COL8_CRUMB, ensure_ascii=False)}</script>
{FONTS}
<link rel="stylesheet" href="assets/site.css?v={VER}">
</head>'''

    body = f'''<body class="has-dock">
{SPRITE}
{header('index.html')}
<div class="cbanner">
  <img src="images/column-banner.jpg" alt="" width="1600" height="900">
  <div class="wrap"><p class="ttl">건강 칼럼</p><p>진료실에서 자주 받는 질문을 쉽게 풀어 씁니다.</p></div>
</div>
<main class="art column">
  <a class="back" href="index.html#column">{ic("back")}목록으로</a>
  <header class="art-head">
    <span class="chip">칼럼 · 회전근개 파열</span>
    <h1>{title}</h1>
    
    <p class="art-meta"><span><time datetime="2026-11-21">2026.11.21</time></span><span>정관고려한의원 건강 칼럼</span></p>
  </header>

  <section class="sum" aria-labelledby="sum-h">
    <h2 id="sum-h">이 글에서 알 수 있는 내용</h2>
    <ul>
      {chk('회전근개 부분 파열, 수술이 필요한 경우와 아닌 경우')}
      {chk('치료 기간과 재활운동·침치료·주사치료')}
      {chk('회복 중 피할 동작과 집에서 하는 단계별 어깨 운동')}
    </ul>
    <details class="toc"><summary>목차 보기{ic("down")}</summary><ol>{toc_html}</ol></details>
  </section>

  <div class="prose" data-size="0">
    <figure><img src="images/column-8-hero.jpg" alt="회전근개손상 · “원장님, 꼭 수술해야 하나요?” 어깨 힘줄이 찢어졌대요 · 회전근개 부분 파열, 수술 여부와 회복기간" width="743" height="743"></figure>

    <p>어깨가 아파 검사를 받았는데 <b>"회전근개 힘줄이 일부 찢어졌습니다"</b>라는 말을 들으면 걱정부터 됩니다.</p>
    <p class="quote">"수술해야 하나요?"<br>"얼마나 치료 받아야 낫나요?"<br>"운동은 언제 다시 할 수 있나요?"</p>
    <p>진료실에서 자주 듣는 질문입니다.</p>
    <p>결론부터 말씀드리면,</p>
    <p class="key"><b>회전근개 부분 파열은 수술 없이 좋아지는 경우가 많습니다.</b></p>
    <p>(단, <b>다친 직후 팔을 갑자기 못 들거나 힘이 크게 떨어졌다면</b> 수술도 고려해 봐야 합니다.)</p>

    <h2 id="s1">회전근개 부분 파열이란</h2>
    <p>회전근개는 어깨를 움직이고 잡아주는 <b>네 개의 근육과 힘줄</b>입니다.<br>그중 <b>극상근 힘줄</b>이 가장 흔히 손상됩니다.</p>
    <ul class="dl">
      <li><b>부분 파열</b> : 힘줄이 일부만 찢어진 상태</li>
      <li><b>전층 파열</b> : 힘줄이 겉부터 속까지 찢어진 상태</li>
    </ul>
    <figure><img src="images/column-8-tear.jpg" alt="어깨 관절 해부 그림: 위팔뼈 머리 위를 덮는 회전근개 힘줄의 일부가 찢어져 붉게 보이고, 오른쪽 원 안에 찢어진 부분을 확대해 보여 줍니다" width="743" height="495" loading="lazy"><figcaption>그림 1. 회전근개 힘줄이 일부 찢어진 모습</figcaption></figure>
    <p>힘줄이 찢어지는 원인은 크게 두 가지입니다.</p>
    <h3 class="sub-h">나이가 들면서 조금씩 닳아서</h3>
    <p>오랜 세월 어깨를 쓰면서 힘줄이 약해져 찢어집니다. 가장 흔한 경우입니다.</p>
    <h3 class="sub-h">다쳐서</h3>
    <p>넘어지며 팔을 짚거나, 무거운 것을 갑자기 들다가 찢어지기도 합니다.</p>

    <h2 id="s2">수술해야 하나요?</h2>
    <p><b>회전근개 부분 파열은 대부분 수술 없이 치료할 수 있습니다.</b></p>
    <p class="quote">"그냥 두면 더 찢어지지 않을까요?"</p>
    <p>그럴 수 있습니다.<br>하지만 수술 없이 지켜본 여러 연구에서 <b>약 2년 동안 환자 4명 중 3명꼴로 파열이 더 커지지 않았습니다.</b><sup>1</sup></p>
    <p>그렇다고 <b>그냥 방치해도 된다는 뜻은 아닙니다.</b><br>어깨에 무리가 가는 동작을 피하고, 치료하면서 회복 상태를 살펴봐야 합니다.<br>통증이 다시 심해지거나 팔의 힘이 떨어지면 진료를 받고, 필요하면 초음파나 MRI로 확인합니다.</p>
    <div class="qbox qwarn">
      <p class="qbox-h">이럴 때는 정형외과에서 수술 상담을 받으세요</p>
      <ul class="checks">
        <li>{ic("check")}<span>넘어지거나 다친 뒤 <b>팔을 거의 들지 못할 때</b></span></li>
        <li>{ic("check")}<span>예전보다 팔을 들거나 바깥으로 돌리는 <b>힘이 뚜렷하게 약해졌을 때</b></span></li>
        <li>{ic("check")}<span>힘줄이 <b>절반 이상</b> 찢어지고 팔을 쓰기가 계속 힘들 때</span></li>
        <li>{ic("check")}<span>충분히 치료했는데도 <b>밤에 아프고 생활이 불편할 때</b></span></li>
      </ul>
      <p>특히 다친 뒤 갑자기 팔에 힘이 빠졌다면 <b>몇 달씩 기다리지 말고 바로 진료 받으세요.</b><sup>2</sup></p>
    </div>

    <h2 id="s3">얼마나 치료 받아야 하나요?</h2>
    <ol class="steps">
      <li><b>처음 몇 주</b><br>통증이 줄어드는지 살펴봅니다.</li>
      <li><b>3개월</b><br>치료하며 경과를 봅니다.<br>통증이 좋아져도 <b>힘이 돌아오는 데는 시간이 더 걸립니다.</b></li>
      <li><b>6개월</b><br>수술을 생각하기 전까지는 <b>6개월 정도 충분히 치료</b>하는 것이 좋습니다.<sup>3</sup></li>
    </ol>
    <p>검사 결과에 너무 겁먹지 않으셔도 됩니다.<br>실제로 부분 파열이 있어도 <b>아프지 않은 사람이 많습니다.</b><sup>4</sup></p>
    <p>찢어진 힘줄이 검사 사진에서 완전히 붙지 않았더라도, 통증 없이 일상 생활을 하는 분들이 있습니다.</p>
    <p class="key"><b>아프지 않고 팔의 힘과 움직임이<br>충분히 돌아왔다면, 회복된 것으로 봅니다.</b></p>
    <p>다만 힘줄이 완전히 아문 것은 아닐 수 있으므로, <b>무리한 운동은 조심해야 합니다.</b></p>

    <h2 id="s4">치료는 어떻게 하나요?</h2>
    <p>수술이 아니라면, 찢어진 힘줄을 바로 붙이는 주사나 약은 아직 양방에도 한방에도 없습니다.</p>
    <p>그래서 치료의 목표는 <b>통증을 줄이고, 힘줄이 스스로 회복할 수 있는 환경을 만드는 것</b>입니다.</p>

    <h3 class="factor"><span>치료의 중심, 재활운동</span></h3>
    <p>재활운동은 어깨의 움직임과 힘을 되찾는 데 도움이 됩니다.<br>그래서 진료지침에서도 <b>운동재활을 우선 치료</b>로 권고합니다.<sup>5</sup></p>

    <h3 class="factor"><span>침치료는 재활운동을 할 수 있게 돕습니다</span></h3>
    <p>통증이 심하면 재활운동을 제대로 하기 어렵습니다. 이때 침치료가 도움이 됩니다.</p>
    <p>침치료는 <b>통증을 줄이고 굳은 어깨를 풀어 주어</b>, 재활운동을 시작하기 쉽게 합니다.</p>
    <p>여러 임상시험을 모아 분석한 연구에서, 침치료는 치료 초기(3개월 이내)에 <b>통증을 줄이고 어깨의 움직임을 개선하는 데 도움이 됐습니다.</b><sup>6</sup></p>
    <p>동물실험에서는 전침(침에 약한 전기를 흘려 주는 치료)이 손상된 힘줄의 염증을 줄이고, 힘줄을 더 튼튼하게 했다는 결과도 있습니다.<sup>7</sup><br>다만 사람에게서 같은 효과가 있는지는 아직 연구가 더 필요합니다.</p>

    <h3 class="factor"><span>양방 주사치료는 필요할 때만</span></h3>
    <p>밤에 아파 잠을 못 자거나 통증이 너무 심하다면, 양방 주사치료를 함께 받으실 수 있습니다.</p>
    <p>스테로이드 주사는 통증과 염증을 줄이지만, <b>찢어진 힘줄을 붙이는 치료는 아닙니다.</b></p>
    <p>진료지침에서는 단기간의 통증 완화를 위해 <b>스테로이드 주사 한 차례 정도만</b> 고려할 수 있다고 합니다.<sup>8</sup><br>반복해서 맞으면 오히려 힘줄에 좋지 않을 수 있어 주의해야 합니다.<sup>9</sup></p>
    <p>혈소판 풍부 혈장(PRP) 주사도 쓰입니다. 통증을 줄이는 데 도움이 될 수 있지만, 연구마다 결과가 달라 아직 확실한 근거는 부족합니다.<sup>3,10</sup></p>

    <h3 class="factor"><span>힘줄을 약하게 만드는 요인 피하기</span></h3>
    <ul class="checks">
      <li>{ic("check")}<span>흡연은 회전근개 파열의 위험 요인입니다. <b>이번 기회에 끊으시기 바랍니다.</b><sup>11</sup></span></li>
      <li>{ic("check")}<span>아픈데 무리해서 운동하면 손상된 힘줄에 부담을 줄 수 있으니 피하셔야 합니다.</span></li>
    </ul>

    <h2 id="s5">회복 중에는 이런 동작을 피하세요</h2>
    <p>치료 받는 동안에는 다음과 같은 <b>어깨에 큰 힘이 들어가는 동작</b>을 피하세요.</p>
    <ul class="checks avoid">
      <li>{ic("x")}<span>높은 선반 위의 물건 내리기</span></li>
      <li>{ic("x")}<span>차 안에서 몸을 뒤로 돌려 뒷자리 물건 잡기</span></li>
      <li>{ic("x")}<span>아픈 쪽 어깨를 깔고 누워 자기</span></li>
      <li>{ic("x")}<span>무거운 덤벨 들기와 팔굽혀펴기</span></li>
      <li>{ic("x")}<span>아픈데도 억지로 하는 스트레칭</span></li>
    </ul>
    <p><b>골프와 배드민턴 등의 운동은 충분히 회복될 때까지 쉬세요.</b></p>
    <p>운동을 하다 보면 나도 모르게 무리하게 되기 쉽습니다.<br>통증이 없어지고 팔의 힘과 움직임이 충분히 돌아온 뒤 다시 시작하세요.</p>

    <h2 id="s6">집에서 하는 어깨 재활운동</h2>
    <p>가벼운 재활운동은 힘줄을 바로 붙이는 운동이 아니라, <b>어깨가 굳지 않도록 하고 나중에 힘을 되찾기 위한 것</b>입니다.</p>
    <p>통증이 심할 때는 쉬는 것이 먼저이고, 통증이 줄면 <b>아프지 않은 범위에서</b> 시작하세요.</p>

    <h3 class="sub-h">[1단계] 통증이 조금 가라앉으면</h3>
    <ul class="dl">
      <li><b>추 운동</b> : 탁자를 짚고 숙여, 힘 뺀 팔을 작게 흔듭니다.</li>
      <li><b>탁자 밀기</b> : 탁자 위 수건을 앞으로 천천히 밀어 줍니다.</li>
    </ul>
    <figure><img src="images/column-8-ex1.jpg" alt="탁자를 한 손으로 짚고 몸을 숙여 반대쪽 팔을 힘 빼고 늘어뜨린 추 운동 자세와, 의자에 앉아 탁자 위 수건을 손으로 앞으로 밀어 주는 탁자 밀기 자세" width="743" height="380" loading="lazy"><figcaption>그림 2. 추 운동(왼쪽) · 탁자 밀기(오른쪽)</figcaption></figure>

    <h3 class="sub-h">[2단계] 팔을 움직이기가 조금 편해지면</h3>
    <ul class="dl">
      <li><b>벽 타기</b> : 손가락으로 벽을 타고, 아프지 않은 높이까지만 올라갑니다.</li>
      <li><b>날개뼈 모으기</b> : 가슴을 펴고 날개뼈를 모아 5초 버팁니다.</li>
    </ul>
    <figure><img src="images/column-8-ex2.jpg" alt="벽 앞에 서서 손가락으로 벽을 타고 팔을 올리는 벽 타기 자세와, 의자에 앉아 가슴을 펴고 양쪽 날개뼈를 모으는 뒷모습" width="743" height="372" loading="lazy"><figcaption>그림 3. 벽 타기(왼쪽) · 날개뼈 모으기(오른쪽)</figcaption></figure>

    <h3 class="sub-h">[3단계] 통증이 충분히 가라앉으면</h3>
    <ul class="dl">
      <li><b>밴드 바깥 돌리기</b> : 팔꿈치를 옆구리에 붙이고, 약한 밴드를 천천히 바깥으로 당깁니다.</li>
    </ul>
    <figure><img src="images/column-8-ex3.jpg" alt="옆구리와 팔꿈치 사이에 수건을 끼우고 팔꿈치를 붙인 채, 벽 손잡이에 묶은 초록색 밴드를 바깥쪽으로 천천히 당기는 중년 남성" width="743" height="557" loading="lazy"><figcaption>그림 4. 밴드 바깥 돌리기: 약한 강도로 시작하세요</figcaption></figure>
    <p class="key alert"><b>운동하다 아프거나 다음 날 더 아프면, 운동량을 줄이거나 쉬세요.</b></p>

    <h2 id="s7">꼭 기억하세요</h2>
    <p>오늘 내용을 다섯 가지로 정리하면 이렇습니다.</p>
    <ol class="steps">
      <li><b>어깨 힘줄(회전근개)의 부분 파열은 대부분 수술 없이 좋아집니다.</b></li>
      <li><b>다친 뒤 팔을 못 들거나 힘이 확 빠지면 바로 진료를 받으세요.</b><br>이때는 수술이 필요할 수 있습니다.</li>
      <li><b>치료는 3~6개월 꾸준히 받으세요.</b><br>통증은 먼저 줄고, 힘은 천천히 돌아옵니다.</li>
      <li><b>회복의 중심은 재활운동입니다.</b><br>침치료는 통증을 줄여 재활운동을 할 수 있게 돕습니다. 스테로이드 주사는 통증이 심할 때 한 차례 고려할 수 있지만, 반복해서 맞는 것은 신중해야 합니다.</li>
      <li><b>회복될 때까지 스포츠 활동은 쉬고,</b><br>어깨에 무리가 가는 동작은 피하세요.</li>
    </ol>
    <p>MRI 사진 상 깨끗해지는 것보다,</p>
    <p class="key"><b>아프지 않고 팔을 편하게 쓰는 것이 진짜 회복</b>입니다.</p>
    <p>조급해하지 마시고, 한 단계씩 어깨를 회복해 나가시기 바랍니다.</p>
    <p class="sign">한의학박사 · 한방재활의학과 전문의 <b>박장우</b></p>

    <details class="refs">
      <summary>참고문헌 · 그림 안내{ic("down")}</summary>
      <ol>
        <li>Garcia MJ, et al. Disparities in Rotator Cuff Tear Progression Definitions and Rates: A Systematic Review. <i>JBJS Open Access</i>. 2024;9(4):e24.00097. <a href="https://doi.org/10.2106/JBJS.OA.24.00097" target="_blank" rel="noopener">doi.org/10.2106/JBJS.OA.24.00097</a></li>
        <li>AAOS OrthoInfo. Rotator Cuff Tears.</li>
        <li>Kany J, et al. (ESSKA-ESA). The 2026 formal consensus on partial-thickness posterosuperior rotator cuff tears, Part 2. <i>Knee Surg Sports Traumatol Arthrosc</i>. 2026. <a href="https://doi.org/10.1002/ksa.70622" target="_blank" rel="noopener">doi.org/10.1002/ksa.70622</a></li>
        <li>Johns Hopkins Medicine. Partial Rotator Cuff Tear.</li>
        <li>Desmeules F, et al. Rotator Cuff Tendinopathy: Diagnosis, Nonsurgical Medical Care, and Rehabilitation—A Clinical Practice Guideline. <i>J Orthop Sports Phys Ther</i>. 2025;55(4):235-274. <a href="https://doi.org/10.2519/jospt.2025.13182" target="_blank" rel="noopener">doi.org/10.2519/jospt.2025.13182</a></li>
        <li>Zhang HN, et al. Efficacy comparison between acupuncture and other modalities in the treatment of rotator cuff diseases: meta-analysis of randomized controlled trials. <i>Am J Transl Res</i>. 2024;16(2):599-616. <a href="https://doi.org/10.62347/NCRJ1270" target="_blank" rel="noopener">doi.org/10.62347/NCRJ1270</a></li>
        <li>Song W, et al. Electro-acupuncture promotes repair of rotator cuff injury in rats. <i>Nan Fang Yi Ke Da Xue Xue Bao</i>. 2020;40(10):1513-1517. <a href="https://doi.org/10.12122/j.issn.1673-4254.2020.10.19" target="_blank" rel="noopener">doi.org/10.12122/j.issn.1673-4254.2020.10.19</a></li>
        <li>American Academy of Orthopaedic Surgeons (AAOS). Management of Rotator Cuff Injuries: Evidence-Based Clinical Practice Guideline. 2025. <a href="https://www.aaos.org/rccpg2025" target="_blank" rel="noopener">aaos.org/rccpg2025</a></li>
        <li>Puzzitiello RN, et al. Adverse impact of corticosteroid injection on rotator cuff tendon health and repair: a systematic review. <i>Arthroscopy</i>. 2020;36(5):1468-1475. <a href="https://doi.org/10.1016/j.arthro.2019.12.006" target="_blank" rel="noopener">doi.org/10.1016/j.arthro.2019.12.006</a></li>
        <li>Desouza C, Shetty V. Effectiveness of platelet-rich plasma in partial-thickness rotator cuff tears: a systematic review. <i>J ISAKOS</i>. 2024;9(4):699-708. <a href="https://doi.org/10.1016/j.jisako.2024.04.010" target="_blank" rel="noopener">doi.org/10.1016/j.jisako.2024.04.010</a></li>
        <li>Tashjian RZ. Epidemiology, natural history, and indications for treatment of rotator cuff tears. <i>Clin Sports Med</i>. 2012;31(4):589-604. <a href="https://doi.org/10.1016/j.csm.2012.07.001" target="_blank" rel="noopener">doi.org/10.1016/j.csm.2012.07.001</a></li>
      </ol>
      <p class="refs-h">그림 안내</p>
      <ul><li>그림은 설명을 돕기 위해 만든 것입니다. 실제 운동은 어깨 상태에 따라 달라질 수 있습니다.</li></ul>
    </details>
  </div>

  <aside class="ccta" aria-label="진료 안내">
    <div class="ccta-top"><img src="images/c9de5ada.png" alt="" width="220" height="220"><div><b>정관고려한의원 진료 안내</b><p>예약 없이 방문하세요. {ADDR}</p></div></div>
    <div class="acts"><a class="btn-gold" href="{TEL_HREF}">{ic("phone")}전화 문의 {TEL}</a><a class="btn-line" href="index.html#hours">진료시간</a></div>
  </aside>

  <p class="src-link"><a href="https://blog.naver.com/jgkorea8275/224486440105" target="_blank" rel="noopener">네이버 블로그에서 원문 보기{ic("ext")}</a></p>

  <div class="tools">
    <a class="back" href="index.html#column">{ic("back")}목록으로</a>
    <div class="r">
      <button type="button" data-share>{ic("share")}공유하기</button>
      <button type="button" data-font aria-label="글자 크기: 보통"><span class="ga" aria-hidden="true">가</span>글자 크기</button>
    </div>
  </div>

  <nav class="related" aria-label="함께 보기">
    <h2>함께 보기</h2>
    <ul>
      <li><a href="column-3.html">칼럼 · 어깨가 아프면 다 오십견일까요?{ic("chev")}</a></li>
      <li><a href="column-1.html">칼럼 · 삐끗했는데 왜 이렇게 오래 가죠?{ic("chev")}</a></li>
      <li><a href="column-6.html">칼럼 · 침 치료 원리, 과학적으로 쉽게 설명드립니다{ic("chev")}</a></li>
      <li><a href="index.html#area">근육통·관절통 진료 안내{ic("chev")}</a></li>
    </ul>
  </nav>
</main>
{footer()}
{dock('index.html')}
<script src="assets/site.js?v={VER}"></script>
{ANALYTICS}
</body>
</html>
'''
    return head + '\n' + body

COL9_URL = 'https://jgkorea8275.co.kr/column-9.html'
COL9_TITLE = '허리디스크, 꼭 수술해야 하나요? 치료 기간과 좋아지는 신호'
COL9_LD = {"@context": "https://schema.org", "@type": "Article", "headline": "허리디스크, 꼭 수술해야 하나요? 치료 기간과 좋아지는 신호", "datePublished": "2026-11-23", "image": ["https://jgkorea8275.co.kr/images/column-9-hero.jpg"], "mainEntityOfPage": "https://jgkorea8275.co.kr/column-9.html", "author": {"@type": "Person", "name": "박장우", "jobTitle": "한의학박사, 한방재활의학과 전문의"}, "publisher": {"@type": "Organization", "name": "정관고려한의원", "logo": {"@type": "ImageObject", "url": "https://jgkorea8275.co.kr/favicon.png"}}}
COL9_CRUMB = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "정관고려한의원", "item": "https://jgkorea8275.co.kr/"},
    {"@type": "ListItem", "position": 2, "name": "칼럼 및 에세이", "item": "https://jgkorea8275.co.kr/#column"},
    {"@type": "ListItem", "position": 3, "name": "허리디스크, 꼭 수술해야 하나요?", "item": "https://jgkorea8275.co.kr/column-9.html"}]}

def column9():
    title = COL9_TITLE.replace('"', '&quot;')
    title_plain = title
    title_attr = title
    desc = '"디스크가 터졌대요." 허리디스크는 대부분 수술 없이 좋아집니다. 수술이 필요한 경우, 디스크의 자연 흡수, 양·한방 치료와 침치료 연구, 치료 기간과 좋아지는 신호까지 정리했습니다.'
    toc = [('s1', '허리디스크란?'), ('s2', '수술해야 하나요?'), ('s3', '양방 치료와 한방 치료'), ('s4', '얼마나 치료하면 낫나요?'),
           ('s5', '디스크 위치에 따라 다리 아픈 곳이 다릅니다'), ('s6', '꼭 기억하세요')]
    chk = lambda t: f'<li>{ic("check")}<span>{t}</span></li>'
    toc_html = ''.join(f'<li><a href="#{i}">{t}</a></li>' for i, t in toc)
    head = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title_plain} | 칼럼 | 정관고려한의원</title>
<meta name="claude:viewport-fit-sides" content="cover">
<meta name="description" content="{desc}">
<meta name="theme-color" content="#171511">
<link rel="canonical" href="{COL9_URL}">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="alternate" type="application/rss+xml" title="정관고려한의원 칼럼·에세이" href="https://jgkorea8275.co.kr/rss.xml">
<meta property="og:type" content="article">
<meta property="og:locale" content="ko_KR">
<meta property="og:site_name" content="정관고려한의원">
<meta property="og:title" content="{title_attr} | 정관고려한의원 칼럼">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{COL9_URL}">
<meta property="og:image" content="https://jgkorea8275.co.kr/images/column-9-hero.jpg">
<meta property="og:image:width" content="743">
<meta property="og:image:height" content="743">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://jgkorea8275.co.kr/images/column-9-hero.jpg">
<meta property="article:published_time" content="2026-11-23">
<script type="application/ld+json">{json.dumps(COL9_LD, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(COL9_CRUMB, ensure_ascii=False)}</script>
{FONTS}
<link rel="stylesheet" href="assets/site.css?v={VER}">
</head>'''

    body = f'''<body class="has-dock">
{SPRITE}
{header('index.html')}
<div class="cbanner">
  <img src="images/column-banner.jpg" alt="" width="1600" height="900">
  <div class="wrap"><p class="ttl">건강 칼럼</p><p>진료실에서 자주 받는 질문을 쉽게 풀어 씁니다.</p></div>
</div>
<main class="art column">
  <a class="back" href="index.html#column">{ic("back")}목록으로</a>
  <header class="art-head">
    <span class="chip">칼럼 · 허리디스크</span>
    <h1>{title}</h1>
    
    <p class="art-meta"><span><time datetime="2026-11-23">2026.11.23</time></span><span>정관고려한의원 건강 칼럼</span></p>
  </header>

  <section class="sum" aria-labelledby="sum-h">
    <h2 id="sum-h">이 글에서 알 수 있는 내용</h2>
    <ul>
      {chk('허리디스크, 수술이 필요한 경우와 아닌 경우')}
      {chk('양방 치료와 한방 치료, 침치료는 어떻게 도움이 될까요')}
      {chk('치료 기간과 좋아지는 신호, 디스크 위치별 저린 곳')}
    </ul>
    <details class="toc"><summary>목차 보기{ic("down")}</summary><ol>{toc_html}</ol></details>
  </section>

  <div class="prose" data-size="0">
    <figure><img src="images/column-9-hero.jpg" alt="허리디스크 · “원장님, 디스크가 터졌대요. 어떡하죠?” 허리디스크, 꼭 수술해야 하나요? · 요추 추간판 탈출증, 치료 기간과 좋아지는 신호" width="743" height="743"></figure>

    <p>MRI를 찍고 <b>"디스크가 터졌습니다"</b>라는 말을 들으면 덜컥 겁부터 납니다.</p>
    <p class="quote">"수술해야 하나요?"<br>"얼마나 치료받아야 낫나요?"</p>
    <p>진료실에서 가장 많이 듣는 질문입니다.</p>
    <p>한마디로 요약해서 말씀드리면,</p>
    <p class="key"><b>허리디스크는 대부분 수술 없이 좋아집니다.</b></p>
    <p>다만 <b>수술을 서둘러야 하는 경우</b>도 분명히 있습니다.</p>
    <p>차근차근 설명드리겠습니다.</p>

    <h2 id="s1">허리디스크란?</h2>
    <p>허리디스크의 정확한 의학 명칭은 <b>'요추 추간판 탈출증'</b>입니다.</p>
    <p>척추뼈와 척추뼈 사이에는 충격을 흡수하는 쿠션이 있습니다.<br>이것을 추간판, 흔히 '디스크'라고 부릅니다.</p>
    <ul class="dl">
      <li><b>수핵</b> : 디스크 가운데에 있는 젤리 같은 부분</li>
      <li><b>섬유륜</b> : 수핵 바깥을 감싸고 있는 질긴 막</li>
    </ul>
    <p>섬유륜이 찢어지면서 수핵이 밖으로 밀려 나오면, 바로 옆을 지나가는 <b>신경을 압박하고 염증</b>을 일으킵니다.<br>이것이 허리디스크입니다.</p>
    <figure><img src="images/column-9-disc.jpg" alt="정상 디스크와 탈출된 디스크를 위에서 본 단면 그림: 정상 디스크는 섬유륜 안에 수핵이 있고 뒤쪽에 신경 다발과 신경근이 지나가며, 탈출된 디스크는 섬유륜이 찢어져 밀려 나온 수핵이 신경근을 누르고 있습니다" width="743" height="495" loading="lazy"><figcaption>그림 1. 정상 디스크와 탈출된 디스크</figcaption></figure>
    <p>허리디스크의 대표적인 증상은 두 가지입니다.</p>
    <ul class="dl">
      <li><b>요통</b> : 허리가 아픈 증상</li>
      <li><b>하지방산통</b> : 다리 쪽으로 뻗치는 통증</li>
    </ul>
    <p>밀려 나온 수핵이 다리로 가는 신경을 자극하면, 엉덩이에서 허벅지, 종아리, 발까지 찌릿하거나 당길 수 있습니다.</p>
    <p>허리는 별로 안 아픈데 <b>한쪽 다리만 아프거나 저린 분</b>도 있습니다.</p>

    <h2 id="s2">수술해야 하나요?</h2>
    <p><b>대부분은 수술 없이 치료할 수 있습니다.</b></p>
    <p>허리디스크 환자 100명 중 수술이 필요한 분은 <b>5~10명 정도</b>입니다.<sup>1</sup></p>
    <p class="quote">"터져 나온 디스크가 그대로 남아 있으면 어떡하죠?"</p>
    <p>걱정하실 필요가 없습니다.</p>
    <p>튀어나온 디스크는 시간이 지나면서 우리 몸이 스스로 흡수해 줄어드는 경우가 많습니다.<br>이것을 <b>자연 흡수</b>라고 합니다.</p>
    <p>여러 연구를 모아 분석해 보니, <b>디스크가 많이 튀어나올수록 오히려 더 잘 흡수</b>되었습니다.<sup>3,4</sup></p>
    <figure class="tall"><img src="images/column-9-regress.jpg" alt="튀어나온 디스크는 얼마나 줄어들까요? 디스크 모양별로 추적 MRI에서 크기가 줄어든 비율: 넓게 부푼 팽윤 13.3%, 한쪽으로 볼록 나온 돌출 52.5%, 디스크 조직이 밀려 나온 탈출 70.4%, 조각이 떨어져 나온 격리 93.0%. 일부만 줄어든 경우도 포함합니다" width="743" height="1115" loading="lazy"><figcaption>그림 2. 디스크 모양에 따라 MRI에서 크기가 줄어든 비율<sup>4</sup><br>(MRI 재촬영 시점은 평균 약 11.5개월 뒤였습니다.)</figcaption></figure>
    <p>밖으로 많이 나온 디스크는 우리 몸의 면역세포가 '이물질'로 알아보고 청소하기 때문입니다.<br>우리 몸의 자생력이 일하는 것이죠.</p>

    <h3 class="factor"><span>이런 경우에는 수술을 고려해야 합니다</span></h3>
    <p>아래 경우는 망설이지 마시고 신경외과·정형외과 전문의 진료를 받으셔야 합니다.</p>
    <div class="qbox qalert">
      <p class="qbox-h">바로 응급실로 가셔야 하는 경우</p>
      <ul class="checks">
        <li>{ic("check")}<span><b>대소변이 안 나오거나 새는 증상이 있을 때</b></span></li>
        <li>{ic("check")}<span><b>항문 주위, 사타구니가 감각이 없고 멍할 때</b></span></li>
        <li>{ic("check")}<span><b>양쪽 다리 힘이 급격히 떨어질 때</b></span></li>
      </ul>
      <p>이 상태를 <b>'마미증후군'</b>이라고 합니다.<br>신경 다발 전체가 눌린 응급 상황입니다.</p>
      <p>※ 이 중 하나라도 생기면 바로 응급실로 가셔야 합니다.<br>수술이 늦어지면 <b>마비가 남을 수 있습니다.</b><sup>2</sup></p>
    </div>
    <div class="qbox qwarn">
      <p class="qbox-h">빨리 수술 상담이 필요한 경우</p>
      <ul class="checks">
        <li>{ic("check")}<span>발목이나 엄지발가락을 들어 올리는 힘이 점점 약해질 때 (발이 끌리거나 슬리퍼가 잘 벗겨짐)</span></li>
        <li>{ic("check")}<span>6~8주 이상 충분히 치료했는데도 다리 통증이 일상생활을 못 할 만큼 계속될 때<sup>1,2</sup></span></li>
      </ul>
    </div>
    <p>반대로, 이런 경우가 아니라면 <b>서둘러 수술할 필요는 없습니다.</b></p>
    <p>심한 좌골신경통 환자를 두 그룹으로 나눠 비교한 연구가 있습니다.<br>'바로 수술한 그룹'과 '비수술 치료를 계속한 그룹'입니다.</p>
    <p>수술을 일찍 받으면 다리 통증은 더 빨리 줄 수 있습니다.<br>다만 우선 비수술 치료를 받고 필요할 때 수술한 분들도 <b>1년 뒤 경과는 비슷했습니다.</b><sup>5</sup></p>
    <figure class="tall"><img src="images/column-9-check.jpg" alt="한눈에 보는 체크리스트: 바로 응급실로 가셔야 합니다(마미증후군 의심) — 소변·대변이 잘 안 나오거나 참지 못하고 새어 나올 때, 항문 주위·사타구니 감각이 없고 멍할 때, 양쪽 다리 마비가 동반될 때. 빨리 수술 상담이 필요합니다(신경외과·정형외과 진료) — 발목·엄지발가락을 들어 올리는 힘이 점점 약해질 때, 6~8주 이상 치료해도 다리 통증이 일상생활을 못 할 만큼 계속될 때. 비수술 치료로 좋아질 수 있습니다(허리디스크 환자의 90% 이상) — 위 증상 없이 허리·다리 통증만 있을 때, 다리 힘이 빠지지 않을 때, 치료하면서 통증이 조금씩 줄어들 때" width="743" height="1124" loading="lazy"><figcaption>그림 3. 한눈에 보는 체크리스트</figcaption></figure>

    <h2 id="s3">양방 치료와 한방 치료</h2>
    <p>양방 치료와 한방 치료는 서로 대립하는 치료가 아닙니다.<br>통증의 정도와 회복 단계에 맞춰 <b>함께 활용</b>할 수 있습니다.</p>

    <h3 class="factor"><span>양방 치료와 병행 권유</span></h3>
    <p>양방의 약물치료(<b>소염진통제, 근이완제</b>)와 <b>신경차단술</b>은 <b>급성기 통증을 잡는 데 효과적</b>입니다.<br>신경차단술은 신경 주변의 염증을 직접 가라앉히는 주사치료입니다.</p>
    <p>통증이 심해 밤잠을 설치거나, 한의원에 오시는 것조차 힘드신 분들도 계십니다.<br>이런 분들께는 저 역시 <b>양방 치료를 함께 받아 급한 통증의 불부터 끄시라고</b> 권합니다.</p>
    <p>통증이 가라앉으면 몸이 스스로 회복하도록 돕는 치료를 함께 하셔야 합니다.</p>

    <h3 class="factor"><span>한방 치료</span></h3>
    <p>한방 치료는 <b>염증을 가라앉히고, 굳은 근육을 풀고, 신경 주변의 혈액순환을 돕습니다.</b><br>몸이 디스크를 스스로 흡수하고 회복하도록 돕는 것이 목표입니다.</p>
    <ul class="dl">
      <li><b>침 · 전침</b> : 경직된 척추 기립근과 신경 주변 근육을 이완합니다. 전기 자극을 더해 통증 신호를 차단합니다.</li>
      <li><b>전자뜸</b> : 화상 위험을 줄이면서 일정한 온열 자극을 전달합니다. 혈류 순환을 돕고 굳은 조직을 부드럽게 풀어줍니다.</li>
      <li><b>약침 · 봉침</b> : 한약 추출물이나 정제한 벌독을 아픈 부위에 주입해 염증을 가라앉힙니다.</li>
      <li><b>부항 (건식 · 습식)</b> : 건식 부항으로 뭉친 근막을 이완합니다. 염증과 어혈이 심하게 정체된 부위에는 습식 부항으로 국소 순환을 개선합니다.</li>
      <li><b>물리치료</b> : 온찜질, 전기자극 등 보조 요법으로 통증과 근육 긴장을 완화합니다.</li>
      <li><b>한약</b> : 신경 주변의 부종과 염증을 줄입니다. 약해진 척추 주변 인대와 근육을 보강해 회복을 돕습니다.</li>
    </ul>

    <h3 class="factor"><span>침 치료는 허리디스크에 어떻게 효과가 있을까요?</span></h3>
    <p>침은 신경과 근육, 혈액순환에 작용하는 치료입니다.<br>진료지침과 연구에서도 효과가 확인되어 있습니다.</p>
    <p>침이 통증을 줄이는 원리는 크게 세 가지입니다.</p>
    <ol class="steps">
      <li><b>몸속 진통 물질이 나옵니다</b><br>침 자극이 뇌와 척수에 전달되면 엔도르핀 같은 진통 물질이 분비됩니다. 그래서 통증을 덜 느끼게 됩니다.</li>
      <li><b>혈액순환이 좋아집니다</b><br>침을 놓은 부위 주변 혈관이 넓어집니다. 눌린 신경 주변으로 혈액이 잘 돌고, 염증이 가라앉는 데 도움이 됩니다.</li>
      <li><b>굳은 근육이 풀립니다</b><br>통증 때문에 딱딱하게 뭉친 허리 주변 근육을 풀어 줍니다. 그만큼 디스크에 가해지는 부담이 줄어듭니다.</li>
    </ol>
    <p>국내 한의표준임상진료지침은 허리디스크 환자의 증상 개선을 위해 <b>침치료를 권고</b>합니다.<sup>10</sup></p>
    <p>2024년 발표된 연구도 있습니다.<br>좌골신경통이 오래된 허리디스크 환자들이 4주간 침치료를 받았더니, 가짜침 치료를 받은 분들보다 <b>다리 통증이 더 줄고 일상 기능도 더 좋아졌습니다.</b><sup>11</sup></p>
    <p>좌골신경통 연구들을 모아 분석한 결과에서도, 침 치료는 진통제와 비교해 다리 통증을 줄이는 효과가 확인되었습니다.<sup>6</sup></p>
    <p>한방 치료를 받은 허리디스크 환자를 5년 동안 지켜본 국내 연구도 있습니다.<br>침, 약침, 봉침, 추나, 한약 치료를 받은 환자들입니다.</p>
    <p class="key"><b>다리 통증(10점 만점) 7.5점 → 0.9점</b></p>
    <p>치료 6개월 뒤 다리 통증이 <b>0.9점</b>으로 줄었고, 5년 뒤까지 그대로 유지되었습니다.<sup>7</sup></p>

    <h2 id="s4">얼마나 치료하면 낫나요?</h2>
    <p>대부분의 허리디스크는 <b>6~12주(1~3개월)</b> 사이에 많이 좋아집니다.<sup>2,8</sup></p>
    <p>진통제만 드신 환자도 3개월 뒤에는 <b>10명 중 8~9명</b>이 통증이 줄었다는 보고가 있습니다.<sup>2</sup></p>
    <p>다만 디스크가 흡수되기까지는 시간이 더 걸립니다.<br>통증이 줄어든 뒤에도 <b>3~6개월은 무리하지 말고 조심</b>하셔야 합니다.<sup>1,7</sup></p>

    <h3 class="factor"><span>좋아지는 신호 — "다리 통증이 허리로 올라온다"</span></h3>
    <p>치료가 잘 되고 있는지는 <b>다리 통증의 위치</b>를 보면 알 수 있습니다.</p>
    <h3 class="sub-h sig-good">○ 좋아지는 경우 (중심화 현상)</h3>
    <p>발끝까지 저리던 통증이 → 종아리 → 허벅지 → 엉덩이로 점점 <b>위로 올라옵니다.</b><br>마지막에는 허리만 아프다가, 그 통증마저 사라집니다.</p>
    <p class="quote">"다리는 덜 저린데 허리가 더 아파요."</p>
    <p>하시는 분들이 계십니다.<br>걱정하지 않으셔도 됩니다.<br>오히려 <b>좋아지고 있다는 신호</b>입니다.</p>
    <p>이렇게 통증이 몸 가운데로 모이는 것을 <b>'중심화 현상(Centralization)'</b>이라고 합니다.<br>중심화 현상이 나타나는 환자는 경과가 좋다는 것이 여러 연구에서 확인되었습니다.<sup>9</sup></p>
    <h3 class="sub-h sig-bad">✕ 나빠지는 경우 (말초화 현상)</h3>
    <p>반대로, 통증이 다리 쪽으로 <b>점점 더 내려가면</b> 신경 압박이 심해지고 있다는 신호입니다.<br>이것을 <b>'말초화 현상(Peripheralization)'</b>이라고 합니다.</p>
    <p>허벅지까지 아프던 통증이 종아리, 발끝까지 내려가거나 저린 범위가 넓어지는 경우입니다.<br>이럴 때는 <b>바로 진료를 받아 상태를 다시 확인</b>하셔야 합니다.</p>
    <figure><img src="images/column-9-central.jpg" alt="중심화와 말초화: 중심화는 좋아지는 신호로 통증이 허리 쪽으로 올라와 모이고, 말초화는 나빠지는 신호로 통증이 발끝 쪽으로 점점 내려갑니다" width="743" height="757" loading="lazy"><figcaption>그림 4. 중심화와 말초화</figcaption></figure>

    <h2 id="s5">디스크 위치에 따라 다리 아픈 곳이 다릅니다</h2>
    <p>어느 디스크가 어느 신경을 누르느냐에 따라 다리의 아픈 곳과 힘이 빠지는 곳이 다릅니다.</p>
    <p>그래서 진료실에서는 MRI를 보기 전에도 <b>"어디가 저리세요?"</b>를 꼭 여쭤봅니다.</p>
    <div class="tbl-wrap"><table class="tbl tbl-sm sum">
      <thead><tr><th scope="col">디스크</th><th scope="col">눌리는 신경</th><th scope="col">저린 곳</th><th scope="col">약해지는 힘</th></tr></thead>
      <tbody>
        <tr><th scope="row">① 요추 3-4번 사이</th><td>4번 요추 신경근</td><td>허벅지 앞 → 무릎 → 정강이 안쪽</td><td>무릎 펴는 힘 약화, 계단 내려갈 때 무릎 꺾임</td></tr>
        <tr><th scope="row">② 요추 4-5번 사이</th><td>5번 요추 신경근</td><td>엉덩이 → 허벅지·종아리 바깥 → 발등 → 엄지발가락</td><td>엄지발가락·발목을 위로 젖히기 어려움 (뒤꿈치로 걷기 어려움)</td></tr>
        <tr><th scope="row">③ 요추 5번-천추 1번 사이</th><td>1번 천추 신경근</td><td>엉덩이 → 허벅지·종아리 뒤 → 발바닥·새끼발가락 쪽</td><td>발꿈치를 들고 까치발로 걷기 어려움</td></tr>
      </tbody>
    </table></div>
    <figure><img src="images/column-9-derm.jpg" alt="디스크 위치에 따라 저린 곳이 다릅니다: ① 요추 3-4번 사이(L4 신경근)는 허벅지 앞에서 정강이 안쪽, ② 요추 4-5번 사이(L5 신경근)는 허벅지·종아리 바깥에서 발등과 엄지발가락, ③ 요추 5번-천추 1번 사이(S1 신경근)는 허벅지·종아리 뒤에서 발바닥과 새끼발가락 쪽. 대표적인 감각 분포이며 실제 저린 범위는 사람마다 다를 수 있습니다" width="743" height="583" loading="lazy"><figcaption>그림 5. 디스크 위치에 따라 저린 곳</figcaption></figure>
    <p>가장 흔한 것은 <b>요추 4-5번 사이, 요추 5번-천추 1번 사이</b> 디스크입니다.</p>
    <p><b>엄지발가락 쪽</b>이 저리면 요추 4-5번 사이 디스크를 먼저 의심합니다.<br><b>새끼발가락 쪽과 발바닥</b>이 저리면 요추 5번-천추 1번 사이 디스크를 먼저 의심합니다.</p>
    <p>다만 디스크가 옆쪽으로 튀어나오면 한 마디 위 신경을 누르기도 합니다.<br>그래서 항상 위 구분과 똑같지는 않습니다.<br>정확한 진단은 진찰과 영상 검사로 함께 확인합니다.</p>

    <h2 id="s6">꼭 기억하세요</h2>
    <p>오늘 내용을 다섯 가지로 정리하면 이렇습니다.</p>
    <ol class="steps">
      <li><b>허리디스크는 90% 이상 수술 없이 좋아집니다.</b></li>
      <li><b>튀어나온 디스크는 몸이 스스로 흡수하는 경우가 많습니다.</b></li>
      <li><b>대소변 장애는 바로 응급실로,</b><br>다리 힘이 점점 빠지면 바로 수술 상담이 필요합니다.</li>
      <li><b>통증이 심할 때는 양방 치료를 함께 받으셔도 됩니다.</b></li>
      <li><b>다리 통증이 위로 올라오면 좋아지는 신호,</b><br>아래로 내려가면 나빠지는 신호입니다.</li>
    </ol>
    <p class="sign">한의학박사 · 한방재활의학과 전문의 <b>박장우</b></p>

    <details class="refs">
      <summary>참고문헌{ic("down")}</summary>
      <ol>
        <li>Jordan J, Konstantinou K, O'Dowd J. Herniated lumbar disc. <i>BMJ Clin Evid</i>. 2009;2009:1118. (PMC2907819)</li>
        <li>Deyo RA, Mirza SK. Herniated Lumbar Intervertebral Disk. <i>N Engl J Med</i>. 2016;374(18):1763-1772. <a href="https://doi.org/10.1056/NEJMcp1512658" target="_blank" rel="noopener">doi.org/10.1056/NEJMcp1512658</a></li>
        <li>Chiu CC, et al. The probability of spontaneous regression of lumbar herniated disc: a systematic review. <i>Clin Rehabil</i>. 2015;29(2):184-195. <a href="https://doi.org/10.1177/0269215514540919" target="_blank" rel="noopener">doi.org/10.1177/0269215514540919</a></li>
        <li>Rashed S, et al. Systematic review and meta-analysis of predictive factors for spontaneous regression in lumbar disc herniation. <i>J Neurosurg Spine</i>. 2023;39(4):471-478. <a href="https://doi.org/10.3171/2023.6.SPINE23367" target="_blank" rel="noopener">doi.org/10.3171/2023.6.SPINE23367</a></li>
        <li>Peul WC, et al. Surgery versus prolonged conservative treatment for sciatica. <i>N Engl J Med</i>. 2007;356(22):2245-2256. <a href="https://doi.org/10.1056/NEJMoa064039" target="_blank" rel="noopener">doi.org/10.1056/NEJMoa064039</a></li>
        <li>Han KH, et al. The effectiveness and safety of acupuncture treatment on sciatica: A systematic review and meta-analysis. <i>Complement Ther Med</i>. 2022;71:102872. <a href="https://doi.org/10.1016/j.ctim.2022.102872" target="_blank" rel="noopener">doi.org/10.1016/j.ctim.2022.102872</a></li>
        <li>Shin JS, et al. Long-Term Course of Alternative and Integrative Therapy for Lumbar Disc Herniation and Risk Factors for Surgery: A Prospective Observational 5-Year Follow-Up Study. <i>Spine</i>. 2016;41(16):E955-E963. <a href="https://doi.org/10.1097/BRS.0000000000001494" target="_blank" rel="noopener">doi.org/10.1097/BRS.0000000000001494</a></li>
        <li>Koes BW, van Tulder MW, Peul WC. Diagnosis and treatment of sciatica. <i>BMJ</i>. 2007;334(7607):1313-1317. <a href="https://doi.org/10.1136/bmj.39223.428495.BE" target="_blank" rel="noopener">doi.org/10.1136/bmj.39223.428495.BE</a></li>
        <li>Aina A, May S, Clare H. The centralization phenomenon of spinal symptoms — a systematic review. <i>Man Ther</i>. 2004;9(3):134-143. <a href="https://doi.org/10.1016/j.math.2004.03.004" target="_blank" rel="noopener">doi.org/10.1016/j.math.2004.03.004</a></li>
        <li>한국한의약진흥원 한의표준임상진료지침개발사업단. 요추추간판탈출증 한의표준임상진료지침. <a href="https://nikom.or.kr/board/boardFile/download/32/142/1854.do" target="_blank" rel="noopener">nikom.or.kr</a></li>
        <li>Tu JF, et al. Acupuncture vs Sham Acupuncture for Chronic Sciatica From Herniated Disk: A Randomized Clinical Trial. <i>JAMA Intern Med</i>. 2024;184(12):1417-1424. <a href="https://doi.org/10.1001/jamainternmed.2024.5463" target="_blank" rel="noopener">doi.org/10.1001/jamainternmed.2024.5463</a></li>
      </ol>
    </details>
  </div>

  <aside class="ccta" aria-label="진료 안내">
    <div class="ccta-top"><img src="images/c9de5ada.png" alt="" width="220" height="220"><div><b>정관고려한의원 진료 안내</b><p>예약 없이 방문하세요. {ADDR}</p></div></div>
    <div class="acts"><a class="btn-gold" href="{TEL_HREF}">{ic("phone")}전화 문의 {TEL}</a><a class="btn-line" href="index.html#hours">진료시간</a></div>
  </aside>

  <p class="src-link"><a href="https://blog.naver.com/jgkorea8275/224488736563" target="_blank" rel="noopener">네이버 블로그에서 원문 보기{ic("ext")}</a></p>

  <div class="tools">
    <a class="back" href="index.html#column">{ic("back")}목록으로</a>
    <div class="r">
      <button type="button" data-share>{ic("share")}공유하기</button>
      <button type="button" data-font aria-label="글자 크기: 보통"><span class="ga" aria-hidden="true">가</span>글자 크기</button>
    </div>
  </div>

  <nav class="related" aria-label="함께 보기">
    <h2>함께 보기</h2>
    <ul>
      <li><a href="column-6.html">칼럼 · 침 치료 원리, 과학적으로 쉽게 설명드립니다{ic("chev")}</a></li>
      <li><a href="column-5.html">칼럼 · 자고 일어났더니 목이 안 돌아가요{ic("chev")}</a></li>
      <li><a href="essay-4.html">에세이 · 불은 그대로인데 사이렌만 끄고 있지는 않습니까?{ic("chev")}</a></li>
      <li><a href="index.html#area">허리·목디스크 진료 안내{ic("chev")}</a></li>
    </ul>
  </nav>
</main>
{footer()}
{dock('index.html')}
<script src="assets/site.js?v={VER}"></script>
{ANALYTICS}
</body>
</html>
'''
    return head + '\n' + body

def v2(html):
    html = html.replace('<body class="has-dock" id="top">', '<body class="v2" id="top">')
    a = '<body class="has-dock">'
    html = html.replace(a, '<body class="v2">')
    for p in ('', 'index.html'):
        html = html.replace(dock(p) + '\n', '').replace(dock(p), '')
    assert 'class="dock"' not in html and 'id="fab"' not in html
    a = f'<a class="btn-gold" href="{TEL_HREF}">{ic("phone")}전화 문의하기{ic("chev","ic chev")}</a>'
    if a in html:
        html = html.replace(a, f'<a class="hero-call" href="{TEL_HREF}"><i>{ic("phone")}</i><span><small>전화 바로 연결</small><b>{TEL}</b></span></a>')
    a = f'{ic("menu","ic bars")}{ic("x","ic x")}</button>'
    assert a in html
    html = html.replace(a, f'{ic("menu","ic bars")}{ic("x","ic x")}<span class="lbl lbl-o">메뉴</span><span class="lbl lbl-c">닫기</span></button>')
    html = html.replace(f'<a class="hd-call" href="{TEL_HREF}">', f'<a class="hd-call" href="{TEL_HREF}" aria-label="전화 {TEL}" title="전화 {TEL}">')
    return html

# ---------------------------------------------------------------- RSS (네이버·검색엔진용 새 글 목록)
SITE = 'https://jgkorea8275.co.kr/'
POSTS = [  # 최신 글이 위로. 새 칼럼·에세이를 올리면 여기에 한 줄 추가
    {'url': 'column-9.html', 'title': '허리디스크, 꼭 수술해야 하나요? 치료 기간과 좋아지는 신호', 'date': 'Mon, 23 Nov 2026 18:14:00 +0900', 'cat': '칼럼',
     'desc': '"디스크가 터졌대요." 허리디스크는 대부분 수술 없이 좋아집니다. 수술이 필요한 경우, 디스크의 자연 흡수, 양·한방 치료와 침치료 연구, 치료 기간과 좋아지는 신호까지 정리했습니다.',
     'img': 'images/column-9-hero.jpg'},
    {'url': 'column-8.html', 'title': '어깨 힘줄(회전근개) 부분 파열, 수술해야 하나요? 치료방법과 회복기간', 'date': 'Sat, 21 Nov 2026 23:22:00 +0900', 'cat': '칼럼',
     'desc': '회전근개 부분 파열은 수술 없이 좋아지는 경우가 많습니다. 수술이 필요한 경우, 치료 기간, 재활운동·침치료·주사치료, 집에서 하는 단계별 어깨 운동까지 정리했습니다.',
     'img': 'images/column-8-hero.jpg'},
    {'url': 'column-7.html', 'title': '얼굴이 떨리고 저릴 때, 걱정해야 할까요? (눈꺼풀 떨림, 안면경련, 구안와사, 뇌졸중 신호)', 'date': 'Thu, 19 Nov 2026 11:38:00 +0900', 'cat': '칼럼',
     'desc': '눈꺼풀 떨림부터 반측성 안면경련, 구안와사, 삼차신경통, 대상포진, 뇌졸중 신호까지. 걱정하지 않아도 될 떨림과 바로 119를 불러야 할 신호를 구분해 정리했습니다.',
     'img': 'images/column-7-hero.jpg'},
    {'url': 'column-6.html', 'title': '침 치료 원리, 과학적으로 쉽게 설명드립니다 (관문조절설, 엔도르핀, 전침)', 'date': 'Tue, 17 Nov 2026 15:50:00 +0900', 'cat': '칼럼',
     'desc': '"원장님, 침은 어떻게 해서 낫는 거예요?" 관문조절설, 몸속 진통물질(엔도르핀), 침 자리의 변화, 뇌·신경 조절까지 침 치료의 원리를 쉽게 풀었습니다.',
     'img': 'images/column-6-hero.jpg'},
    {'url': 'column-5.html', 'title': '자고 일어났더니 목이 안 돌아가요 — 목 담결림(낙침) 원인, 경과, 침치료, 주의사항', 'date': 'Tue, 10 Nov 2026 23:05:00 +0900', 'cat': '칼럼',
     'desc': '자고 일어났더니 목이 안 돌아가는 목 담결림(낙침). 원인 네 가지와 자연경과·침치료 경과, 빨리 회복하는 법, 바로 진료가 필요한 경우를 정리했습니다.',
     'img': 'images/column-5-hero.jpg'},
    {'url': 'column-4.html', 'title': '자다가 종아리에 쥐가 나요 (야간 하지 경련의 원인과 대처법)', 'date': 'Sun, 08 Nov 2026 16:33:00 +0900', 'cat': '칼럼',
     'desc': '밤에 자다가 종아리에 쥐가 나는 야간 하지 경련. 원인과 증상, 쥐가 났을 때 대처법 4가지, 예방 스트레칭과 한방 치료를 정리했습니다.',
     'img': 'images/column-4-hero.jpg'},
    {'url': 'column-3.html', 'title': '어깨가 아프면 다 오십견일까요? (오십견의 특징과 운동법)', 'date': 'Wed, 04 Nov 2026 22:24:00 +0900', 'cat': '칼럼',
     'desc': '어깨가 아프다고 다 오십견은 아닙니다. 오십견의 특징과 혼동하기 쉬운 질환, 경과와 치료, 집에서 하는 운동법까지 정리했습니다.',
     'img': 'images/column-3-hero.jpg'},
    {'url': 'column-2.html', 'title': '"침 한방에 낫게 해주소~" 근육통 회복 속도를 결정하는 네가지 요인', 'date': 'Sun, 01 Nov 2026 23:55:00 +0900', 'cat': '칼럼',
     'desc': '같은 근육통도 회복 속도는 다릅니다. 다친 정도, 일상 관리, 몸의 회복력, 한의사의 역할까지 네 가지 요인을 정리했습니다.',
     'img': 'images/column-2-hero.jpg'},
    {'url': 'essay-4.html', 'title': '[에세이04] 불은 그대로인데 사이렌만 끄고 있지는 않습니까?', 'date': 'Sat, 31 Oct 2026 01:22:00 +0900', 'cat': '에세이',
     'desc': '통증주사에 익숙해진 시대, 통증이 사라져도 몸의 회복은 계속됩니다. 한방재활의학과 전문의 박장우 원장의 에세이.',
     'img': 'images/essay-4-hero.jpg'},
    {'url': 'essay-3.html', 'title': '[에세이03] 몸은 쉬라고 하는데, 삶은 멈출 수 없을 때', 'date': 'Fri, 30 Oct 2026 01:07:00 +0900', 'cat': '에세이',
     'desc': '일을 쉴 수 없는 분들의 근육·힘줄 통증, 과사용 증후군 이야기. 한방재활의학과 전문의 박장우 원장의 에세이.',
     'img': 'images/essay-3-hero.jpg'},
    {'url': 'essay-2.html', 'title': '[에세이02] 내 몸 안의 의사를 믿는다는 것', 'date': 'Wed, 28 Oct 2026 16:39:00 +0900', 'cat': '에세이',
     'desc': '우리는 왜 통증을 없애는 데만 익숙해졌을까요? 통증은 몸이 보내는 편지입니다. 한방재활의학과 전문의 박장우 원장의 에세이.',
     'img': 'images/essay-2-hero.jpg'},
    {'url': 'column-1.html', 'title': '삐끗했는데 왜 이렇게 오래 가죠? 근육·인대·힘줄 손상의 회복 이야기', 'date': 'Sat, 24 Oct 2026 09:00:00 +0900', 'cat': '칼럼',
     'desc': '삐끗한 뒤 회복 기간은 근육 1~4주, 인대 2~8주, 힘줄 6주~3개월. 다친 조직에 따라 다른 이유를 정관고려한의원이 정리했습니다.',
     'img': 'images/column-1-hero.jpg'},
]

def rss():
    from xml.sax.saxutils import escape
    def size(path):
        try: return os.path.getsize(os.path.join(OUT, path))
        except OSError: return 0
    items = ''
    for p in POSTS:
        u = SITE + p['url']; img = SITE + p['img']
        items += f"""
    <item>
      <title>{escape(p['title'])}</title>
      <link>{u}</link>
      <guid isPermaLink="true">{u}</guid>
      <category>{escape(p['cat'])}</category>
      <pubDate>{p['date']}</pubDate>
      <description>{escape('<p><img src="' + img + '" alt=""></p><p>' + p['desc'] + '</p>')}</description>
      <enclosure url="{img}" length="{size(p['img'])}" type="image/jpeg"/>
      <media:content url="{img}" medium="image" type="image/jpeg"/>
    </item>"""
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom" xmlns:media="http://search.yahoo.com/mrss/">
  <channel>
    <title>정관고려한의원</title>
    <link>{SITE}</link>
    <atom:link href="{SITE}rss.xml" rel="self" type="application/rss+xml"/>
    <description>정관고려한의원. 한의학박사·한방재활의학과 전문의 진료. 교통사고 후유증, 허리·목디스크, 근육통·관절통, 담결림, 보약. 예약 없이 방문 가능.</description>
    <language>ko</language>
    <lastBuildDate>{POSTS[0]['date']}</lastBuildDate>
    <image>
      <url>{SITE}og-image-2.jpg</url>
      <title>정관고려한의원</title>
      <link>{SITE}</link>
    </image>{items}
  </channel>
</rss>
"""

if __name__ == '__main__':
    # 확정안(v2): 대문 전화 바로 연결, 하단 검은 바·떠 있는 메뉴 단추 없음, 로고 키움, 메뉴 글자 표시
    open(os.path.join(OUT, 'index.html'), 'w').write(v2(index()))
    open(os.path.join(OUT, 'column-1.html'), 'w').write(v2(column1()))
    open(os.path.join(OUT, 'essay-2.html'), 'w').write(v2(essay2()))
    open(os.path.join(OUT, 'essay-3.html'), 'w').write(v2(essay3()))
    open(os.path.join(OUT, 'essay-4.html'), 'w').write(v2(essay4()))
    open(os.path.join(OUT, 'column-2.html'), 'w').write(v2(column2()))
    open(os.path.join(OUT, 'column-3.html'), 'w').write(v2(column3()))
    open(os.path.join(OUT, 'column-5.html'), 'w').write(v2(column5()))
    open(os.path.join(OUT, 'column-6.html'), 'w').write(v2(column6()))
    open(os.path.join(OUT, 'column-7.html'), 'w').write(v2(column7()))
    open(os.path.join(OUT, 'column-8.html'), 'w').write(v2(column8()))
    open(os.path.join(OUT, 'column-9.html'), 'w').write(v2(column9()))
    open(os.path.join(OUT, 'rss.xml'), 'w').write(rss())
    print('built')
