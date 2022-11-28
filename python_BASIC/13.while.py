# while
# while은 while에 들어간 조건을 만족 할 때 까지 반복하라는 뜻임  
# = while의 조건을 만족시키지 않는 순간부터 반복문이 끝남!!!!!

customer = "토르"
index = 5
while index >=1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요." .format (customer, index))
    index -= 1
    if index ==0:
        print( "커피는 폐기처분 되었습니다.")


customer = "아이언맨"
index = 1
while index<=100:
    print("{0}, 커피가 준비되었습니다. 호출 {1}회." .format(customer, index))
    index += 1
print("커피 맛있게 드십시오.")
    
#무한루프 끝내기 위해 컨트롤 C 누르면 강제종료


## 손님을 계속 부르다가 맞는 손님이 오면 while문 종료
coffee = "토르"
customer = "unknown"

while coffee != customer :
    print ( f"{coffee}, 커피가 준비 되었습니다.")
    customer = input( "이름이 어떻게 되세요? ")            # input은 괄호 안의 내용을 출력 + 직접 타이핑하여 입력된 값을 받는다.
    
    print (f"{coffee}, 맛있게 드십시오.")