# 홈페이지 원본 (사이트에는 나타나지 않음)

이 폴더는 홈페이지를 만드는 원본입니다. 이름이 `_`로 시작해서 깃허브 페이지에는 공개되지 않습니다.

- `build.py` : 메인(index.html), 칼럼(column-1.html), 에세이(essay-2~4.html), rss.xml을 만드는 원본
  - 실행: 저장소 폴더 구조를 `site/`(= 저장소 루트의 페이지·assets·images) 옆에 두고 `python3 build.py`
  - 새 글: 에세이 함수(essayN)와 05 목록 카드, RSS의 POSTS에 한 줄 추가
- `tools/sync_jgkr1.py` : jgkr1 저장소용 변환 (주소를 깃허브 주소로, 메인 썸네일은 흰 가운 원장 사진 유지)
- `tools/precheck.sh` : 반영 전 점검 (다른 대화에서 올린 변경, 바뀌는 부분, 원본 밖 페이지 확인)
- `tools/essay*_body.html` : 에세이 본문 원고
- `map/` : 오시는 길 약도 원본(SVG)과 그림 만드는 스크립트
- `preview/` : 모바일 미리보기 창, 컴퓨터 화면 대문 사진 조절 화면

원본이 만들지 않는 페이지: `traffic-accident.html`(교통사고 후유증 안내), `404.html` — 반영할 때 그대로 둡니다.
