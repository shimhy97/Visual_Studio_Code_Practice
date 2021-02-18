#모듈이란 필요한것끼리 잘 만들어진 파일?

#범퍼가 파손 시 범퍼만 교체
#부품이 파손되면 그 부품만 고치게끔, 코드의 유지보수가 쉽게끔 해놓은 장치이다.
#함수 정의, 클래스 등등 이런것을 담고 있는것을 모듈이라고 함

#잔돈을 돌려주지 않는 영화관

def price(people):
    print("{0}명 가격은 {1}원 입니다.".format(people,people*10000))

#조조할인 가격
def price_morning(people):
    print("{0}명 가격은 {1}원 입니다.".format(people,people*6000))

#군인 할인 가격
def price_soldier(people):
    print("{0}명 가격은 {1}원 입니다.".format(people,people*4000))


#모듈을 쓰려는 경로와 같은 폴더 혹은 workspace 내에 있어야 함.