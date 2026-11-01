# jgkorea8275 → jgkr1 변환: 주소만 바꾸고, 메인 썸네일은 기존 원장 사진 유지
import sys
B='https://jangwoo328-create.github.io/jgkr1/'
def conv(name, s):
    for og in ('og-image-2.jpg','og-image-3.jpg'):
        s=s.replace('https://jgkorea8275.co.kr/'+og, B+'images/db6368d7.jpg')
    if name=='index.html':
        s=s.replace('<meta property="og:image:width" content="1200">','<meta property="og:image:width" content="1296">')
        s=s.replace('<meta property="og:image:height" content="630">','<meta property="og:image:height" content="961">').replace('<meta property="og:image:height" content="1200">','<meta property="og:image:height" content="961">')
        for alt in ('정관고려한의원 입구 금색 간판','정관고려한의원 박장우 원장 · 한의학박사·한방재활의학과 전문의'):
            s=s.replace('<meta property="og:image:alt" content="'+alt+'">','<meta property="og:image:alt" content="정관고려한의원 박장우 원장">')
    return s.replace('https://jgkorea8275.co.kr/', B).replace('https://jgkorea8275.co.kr', B.rstrip('/'))
if __name__=='__main__':
    src, name, out = sys.argv[1], sys.argv[2], sys.argv[3]
    open(out,'w').write(conv(name, open(src).read()))
