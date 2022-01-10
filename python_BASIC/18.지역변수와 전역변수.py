#지역변수 : 함수 내부에서 일회용으로 쓰이는 변수

gun = 10            # 얘는 전역변수

# def check (soldiers) : 
#     gun = 20            # 얘는 지역변수
#     gun = gun - soldiers
#     print("함수 내부에서, 남은 총의 갯수는 {0} 입니다.".format(gun))

# check(5)

##이러면 결과가 15가 나온다! 그렇다면, 어떻게 함수 밖에 있는 변수를 그대로 끌어와서 전역변수로써 쓸 수 있을까?


# def check (soldiers) : 
#     global gun              # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("함수 내부에서, 남은 총의 갯수는 {0} 입니다.".format(gun))

# check(5)

#하지만, 전역변수를 너무 많이 사용할 경우 코드관리가 어려워지므로 권장되지 않음. 그렇다면 좀 더 깔끔한 방법은 없을까?

gun = 100

def check(gun,soldiers) :
    gun = gun - soldiers
    return gun

Remain_Gun_Num = check(50,20)
print(f"남은 총의 갯수는 {Remain_Gun_Num} 입니다.")