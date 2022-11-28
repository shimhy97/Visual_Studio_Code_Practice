try:
    print("한자리 나눗셈 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요. :"))
    num2 = int(input("두 번쨰 숫자를 입력하세요. :"))
    if num1 >= 10 or num2 >=10 :
        raise ValueError                                #에러가 발생하면 이를 처리하는 구문으로 넘어감
    print(f"{num1} / {num2} = {(num1/num2)}")
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except ZeroDivisionError:
    print("0으로 나누면 안됩니다.")
    

