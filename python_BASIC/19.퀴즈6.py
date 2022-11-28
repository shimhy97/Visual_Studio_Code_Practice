# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

#  * 표준 체중 : 각 개인의 키에 적당한 체중

#  (성별에 따른 공식)
#  남자 : 키 * 키 * 22
#  여자 : 키 * 키 * 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#     *함수명 : std_weight
#     *전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

from math import *

def std_weight (height,gender) :
    
    if gender == "남자":
        weight = (height)*(height)*22
    elif gender =="여자":
        weight = (height)*(height)*21
    else :
        print("성별을 다시 입력하세요")

    return weight
height = input("키를 m 단위로 입력해주세요 ")
gender = input("성별을 \"남자\" 혹은 \"여자\" 로 입력해주세요 ")
weight = std_weight(1.7,gender)
print("해당 성별 : {0}, 그리고 키 : {1}m에 맞는 적정 체중은 {2}kg입니다.".format(gender, height, round(weight,2)))