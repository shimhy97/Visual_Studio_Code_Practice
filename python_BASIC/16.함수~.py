def open_account():  #def 함수이름(): 함수 정의
  print( "새로운 계좌가 생성되었습니다.")       # << '수행'부분

open_account()

# //////////////////////////#함수는 호출되기 전까진 출력되지 않음!!!

def deposit(balance,money): #입금
    print(f"입금이 완료되었습니다. 잔액은 {balance + money}원입니다.")
    return balance + money

def withdraw(balance,money): #출금
    if balance >= money:
        print(f"출금이 완료되었습니다. 잔액은 {balance - money}원 입니다.")
        return balance + money
    elif balance < money:
        print(f"잔액이 부족합니다. 잔액은 {balance}원 입니다.")
        return balance
    
# return에는 하나의 값만 반환할 수 있는게 아니고, 콤마를 써서 튜플 형식으로 여러개의 자료를 반환 가능하다!
o = 1000000

o = deposit(o,10000)
o = withdraw(o,100000)
o = deposit(o,10000)