import re


s1 = """[Web발신]
10월 신규 프로젝트 
45,000,000원 마감
손실 회복 원금 복구
문의!
https://dokdo.in/EcI
"""

s2 = """[Web발신]
(광고)

최고 전문가와
2시부터
하락 장 대응
mjw.li/ko4m06
코드 2222

무료거부
0801364481
"""
s3 = """[Web발신]
(광고)ce
김다정님이
오픈채팅방 초대합니다
50분시작
ko.gl/sYDnA

무료거부 0805509500
"""

s4 = """[Web발신]
(광고)
무료방선착순50명
매일두시매수사인
bit.ly/3F4vj7V
코드 2222
무료거부
0801364481
"""

s5= """[Web발신]
(광고)
카카오 데이터 센터 화재 숨겨진 수혜주 공개

주도가 되는 테마를 정확히 알고 선점할 수 있어야 이익을 낼 수 있습니다.

최근 카카오 데이터 센터 화재로 인하여 관련 항목들 모두 영향을 받고 있습니다. B2B 대상 인터넷 인프라 서비스 제공, 시스템통합 유지보수 사업, 클라우드 센터 구축 등 기업들의 신규투자 소식이 속속 발표될겁니다. 카카오의 펀더멘탈에 끼치는 영향은 제한적으로 예상되기에 카카오 그룹주를 저가 매수하는 것 보다 이번 사태로 인하여 수혜를 보는 항목, 앞으로 주도가 될 테마를 금일 공개하겠습니다.

▼결제 없는 오픈방 입장▼
https://han.gl/qzoSr

※비영리 목적으로 운영이 되므로 일체 금전 관련 요구는 없습니다.
※오전/오후 상황 및 향후 흐름 짚어드립니다.
※자유롭게 소통 가능합니다.

▼결제 없는 오픈방 입장▼
https://han.gl/qzoSr

방문 조건은 호응과 참여입니다.

들어오셔서 같이 올바른 매매 배우시고 소통하시면서
시장을 바라보는 견해를 넓히시기를 바라겠습니다.

금일 저녁은 방을 닫을 예정이며

입장하셔서 보유 항목 말씀 주시면 대응 도와드리겠습니다.

매너는 꼭 지켜주셔야합니다.

언제까지 개미로 손실만보실순 없으실겁니다,

금일이지나면 방문이 어려워지니 기회 꼭 잡아보시기 바라겠습니다.

▼결제 없는 오픈방 입장▼
https://han.gl/qzoSr

이런 분들은 필히 입장 후 지켜보세요

- 유료 리딩 방 / 지인 추천으로 큰돈을 잃었는데 주식 관련 투.자는 계속하려는 분
- 간절한 마음으로 원금 회복과 주식 투.자에서 성공하고 싶으신 분
- 월급과 함께 새로운 소득원을 원하시는 분
- 투자의 기준을 잡지 못하고 이리저리 휘둘리는 분
무료거부0808552998
"""

s6 = """[Web발신]
5만원 준비
전 주 18,470,000 달성
밴드 확인
https://kr.pe/OfTOe
"""

s_junk = '''[Web발신]
(광고)무료 주식 세.력 공유방에 
초대되셨습니다.

이번해 남은 2개월 동안
현재 예수금 잔고 금액 10배 만들어드리겠습니다.
단 돈1원도 발생 없습니다.지켜만 보셔도 됩니다
만약 미 달성시
5000 만.원
바로 즉.시 지급하겠습니다
그만큼 자신있습니다.

https://open.kakao.com/o/gsFifBLe

[클릭후 들어오셔서 대기하시면 됩니다]

내일부터 100 만.원 가지고 시작하시면
년말까지 계좌에 1000 만.원 이상
무조건 보장 합니다

구경만 해보셔도 상관없습니다. 
3일안에 수.익 없을시 나가셔도 좋습니다.

매도타이밍 드리고 절대로 버리고
가지 않습니다. 무조건 다같이 함께갑니다

★단돈1원도 받지 않습니다,유.료.변.경 하지않습니다★

★5배 이상 무조건 보장
세력들과 함께 움직입니다.

https://open.kakao.com/o/gsFifBLe

[클릭 하신후 입장하시고 대기하시면 됩니다]
무료거부 0805905747
'''

s_junk1 = '''[Web발신]
강남에 사는 보승씨는
매일 큰 돈을 법니다
비법을 공유 해드리겠습니다.

https://ko.gl/OJBjL
'''

s_junk2 = '''[Web발신]
11월 8일 종목 받아보기
상승종목 [한국정보통신]
https://fastkakao.com/E4db
입장코드[4949]
'''

s_junk3 = '''[Web발신]
?국내시장 특급정보
직장인ㆍ주린이 참여가능

↓클릭입장↓
open.kakao.com/o/gfipLVZd
'''

s_junk_url = '''[Web발신]
항 셍 나 스 닥
안 전 한 H T S
먹 튀 없 는 해 선
me2.kr/6wd4q
'''

s_promo = '''[Web발신]
(광고)아이나비
[로보락 11월 연말결산 할인 알림문자] 

안녕하세요 아이나비입니다.
로보락의 관심고객 이벤트에 참여해주신 고객님들의 성원에 감사드립니다. 11월 연말결산 할인에 걸맞는 역.대.급 할인 혜택이 시작되었습니다. 지마켓, 옥션, 십일번가에서 행사가로 구매가 가능하오며 자세한 사항은 아래 내용을 참고해주시기 바랍니다. 
**금일 11/7 19시 십일번가에서 라이브방송을 통해 특별한 가격과 사은품 혜택이 제공 될 예정입니다. 많은 관심 부탁드립니다.

1) 로보락S7 Max V Ultra(열풍건조키트 포함 구성으로 변경)
- 출시 가격 : 1,590,000원
- 할인 가격 : 1,390,000원
- 기간 : 10/31(지마켓, 옥션), 11/1일(11번가) ~ 11/11
- 상품평 사은품 : 전용 물걸레 1set
- 판매처 URL 
11st : https://m.11st.co.kr/MW/Gate/liveBroadcastGate.tmall?broadcastNo=2196
G마켓 : http://rpp.gmarket.co.kr/?exhib=59036
옥션 : http://rpp.auction.co.kr/?exhib=59037

2) 로보락S7 Plus
- 출시 가격 : 947,000원
- 할인 가격 : 799,000원
- 기간 : 10/31(지마켓, 옥션), 11월 1일(11번가) ~ 11월 11일
- 상품평 사은품 : 전용 물걸레 1set
- 판매쳐 URL
11st : https://m.11st.co.kr/MW/Gate/liveBroadcastGate.tmall?broadcastNo=2196
G마켓 : http://rpp.gmarket.co.kr/?exhib=59036
옥션 : http://rpp.auction.co.kr/?exhib=59037

관심고객 이벤트에 대한 내용은 고객센터를 통해 확인하시기 바랍니다.
*아이나비 고객센터 : 1577-8911
무료거부 0808811251
'''

s_promo2 = '''[Web발신]
(광고) 겨울 민감피부 수분 진정케어 upto 33% off!  [라로슈포제 공식몰]

똘러리앙 고객님 주목!
1/ 최대 33% 할인
2/ 전제품 20% 할인
3/ 더블세트 구매시, 에빠끌라 미니 세트 증정 + 마일리지 더블적립
  
[수분 진정케어 보러가기]
https://bit.ly/3WE8Tks

고객케어센터 080-844-0088
무료수신거부 080-850-5639
'''

s_international_junk = '''[국제발신]
코인/주식/해선
누구든 할수있는 쉬운 거래법
A.I봇 2분거래
일일 수익률 55%
bit.ly/3JB5Xkt
비밀번호:2001
'''


# print(sample)
x = re.compile(r"^\[Web발신\][\s\S]*?(원금|하락)", re.MULTILINE)
y = x.search(s1)
print(y)

y = x.search(s2)
print(y)

x1 = re.compile(r"^\[Web발신\][\s\S]*?(무료|오픈|밴드)[\s\S]*?(방)", re.MULTILINE)
y1 = x1.search(s3)
print(y1)

x2 = re.compile(r"^\[Web발신\][\s\S]*?(무료|오픈|밴드|공유)[\s\S]*?(http|bit.ly)", re.MULTILINE)
y2 = x2.search(s4)
print(y2)

y2 = x2.search(s5)
print(y2)

y2 = x2.search(s6)
print(y2)

x_url_junk = re.compile(r"^\[Web발신\][\s\S]*?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)")

x_international_url_junk = re.compile(r"^\[국제발신\][\s\S]*?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)")

print(x_url_junk.search(s_junk))
print(x2.search(s_junk1))
print(x_url_junk.search(s_junk3))
print(x_url_junk.search(s_junk2))
print(x_url_junk.search(s_junk3))
print(x_url_junk.search(s_junk_url))


y_promo = x_url_junk.search(s_promo)
print(y_promo)

y_promo2 = x_url_junk.search(s_promo2)
print(y_promo2)


y_inter1 = x_international_url_junk.search(s_international_junk)
print(y_inter1)

