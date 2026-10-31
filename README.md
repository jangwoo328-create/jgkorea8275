# 정관고려한의원 홈페이지 (jgkorea8275.co.kr)

- `index.html` : 홈페이지 본문 (이 파일을 고치면 내용이 바뀝니다)
- `column-1.html` : 건강 칼럼 1편
- `traffic-accident.html` : 교통사고 후유증 안내 페이지 (홈페이지 "교통사고 후유증" 카드를 누르면 열립니다)
- `assets/site.css`, `assets/site.js` : 두 페이지가 함께 쓰는 디자인과 동작(메뉴, 회전 사진 등)
- `images/`, `videos/` : 사진과 방송 영상
- `CNAME` : 연결할 도메인(jgkorea8275.co.kr). 지우거나 고치지 마세요.
- `robots.txt`, `sitemap.xml` : 검색 노출용 파일
- `.nojekyll`, `404.html`, `favicon.png` : 배포 보조 파일

## 배포 방법 (GitHub Pages)
1. GitHub에서 새 저장소를 만들고(Public) 이 폴더 안의 파일을 전부 올립니다. (폴더째가 아니라 index.html이 저장소 맨 위에 오도록)
2. 저장소 Settings → Pages → Branch를 main / (root)로 지정하고 Save.
3. 같은 화면 Custom domain에 `jgkorea8275.co.kr`이 보이면 정상입니다.

## 호스팅케이알 DNS 설정
도메인 관리 → DNS(네임서버) 설정에서 아래 레코드를 추가합니다.

| 종류 | 호스트 | 값 |
|---|---|---|
| A | @ (비워둠) | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | (GitHub아이디).github.io |

반영에는 보통 수 분~몇 시간이 걸립니다. 연결이 확인되면 GitHub Settings → Pages에서 **Enforce HTTPS**를 켜 주세요.

## 이후 수정
저장소의 `index.html`을 고치고 저장(Commit)하면 1~2분 안에 사이트에 반영됩니다.
