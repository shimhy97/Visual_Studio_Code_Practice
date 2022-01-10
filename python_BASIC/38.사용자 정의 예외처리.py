#우리가 직접 에러를 정의할 수도 있음!! 
#한자리 계산기의 예시를 직접 만들어 보자

class Bignumerror(Exception):  # 일단 만들고자 하는 에러를 클래스로써 정의해줘야 함. 안해주면 인식을 못하더라.
    pass

try:
    print("한자리 나눗셈 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요. :"))
    num2 = int(input("두 번쨰 숫자를 입력하세요. :"))
    if num1 >= 10 or num2 >=10 :
        raise Bignumerror("입력값 : {0},{1}".format(num1,num2))                              # 에러를 새로 만들었다!!
    print(f"{num1} / {num2} = {(num1/num2)}")


except Bignumerror as err:                  # 에러를 새로 정의할땐 as err?
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
