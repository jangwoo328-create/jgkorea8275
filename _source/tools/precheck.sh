#!/bin/bash
# 반영 전 점검
#  1) 다른 대화에서 올린 커밋 표시
#  2) 새로 만든 페이지가 지금 홈페이지와 어디가 다른지 (버전 번호 제외) — 의도하지 않은 변경 찾기
#  3) 저장소에만 있고 원본이 만들지 않는 파일 (다른 대화에서 추가한 페이지 등) 알림
R=/home/claude/jgkorea8275; S=/home/claude/draft/site; ME=01LdwDgK9LZPerYcMWbk21i5
cd $R && git pull -q --rebase
echo "== 최근 커밋"
git log -8 --date=format:'%m-%d %H:%M' --format='%h %ad %s|%(trailers:key=Claude-Session,valueonly,separator=)' |
  awk -F'|' -v me="$ME" '{tag=($2 ~ me)?"":"   <-- 다른 대화에서 올림: 내용 확인 필요"; print $1 tag}'
norm() { sed 's/?v=[0-9a-z]*"/?v="/g' "$1"; }
for f in $(cd $S && ls *.html rss.xml); do
  if [ -f $R/$f ]; then
    d=$(diff <(norm $R/$f) <(norm $S/$f))
    [ -n "$d" ] && { echo "== $f 바뀌는 부분 ($(echo "$d" | grep -c '^[<>]')줄):"; echo "$d" | cut -c1-220 | head -40; }
  else echo "== $f : 새 파일"; fi
done
echo "== 원본이 만들지 않는 저장소 페이지 (그대로 둠):"
for f in $(cd $R && ls *.html); do [ -f $S/$f ] || echo "   $f"; done
echo "== 점검 끝"
