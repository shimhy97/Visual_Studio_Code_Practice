#예외처리란, 에러가 발생했을 때 처리 방식을 말함.
# 계산기에서 숫자 말고 다른게 들어갔을때 예제

#try 부분 내의 문장은 잘 동작 하다가, 에러가 발생하면 except  부분 실행
try:
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 :"))
    num2 = int(input("두 번째 숫자를 입력하세요 :"))

    print( num1 / num2)
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")

except ZeroDivisionError :
    print("0으로 나누면 안댑니다.")

except Exception as err:
    print(err)