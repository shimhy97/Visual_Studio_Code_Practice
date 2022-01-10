#동네에 있는 치킨집. 대기손님의 치킨요리 시간을 줄이고자 자동주문시스템 제작.
# 시스템 코드를 확인하고 적절한 예외처리 구문을 넣자.

#조건 1: 1보다 작거나 숫자가 아닌 입력값이 들어오면 ValueError로 처리
            # 출력 메시지 : "잘못된 값을 입력하였습니다."
#조건 2: 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
        # 치킨 소진 시 사용자 정의 에러[soldouterror]를 발생시키고 프로그램 종료
        # 출력 메시지 : "재고가 소진되어 더이상 주문을 받지 않습니다."

chicken = 10
waiting = 0

class soldouterror(Exception):
    pass

try:
    while (True) :
        order_chick = int(input("치킨 몇마리 주문하시겠습니까?"))
        if order_chick >= 1 :
            if chicken > order_chick :
                waiting +=1           
                chicken = chicken - order_chick
                print("주문번호 : {1}, 현재 남은 치킨은 {0}마리 입니다.".format(chicken,waiting))

            elif chicken == order_chick : 
                waiting +=1           
                chicken = chicken - order_chick
                print("주문번호 : {1}, 현재 남은 치킨은 {0}마리 입니다.".format(chicken,waiting))
                raise soldouterror("재고가 소진되어 더이상 주문을 받지 않습니다.")

            elif chicken < order_chick :
                print("남은 치킨이 {0}마리 이므로, 재고가 부족하여 주문을 받지 못합니다.".format(chicken))
        else :
            raise ValueError
except ValueError as err:
    print("1 이상의 수를 입력하세요")
    print (err)

except soldouterror as err:
    print(err)