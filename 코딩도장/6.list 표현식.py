
a = [i for i in range(10)]        # 0부터 9까지 숫자를 생성하여 리스트 생성

b = list(i for i in range(10))    # 0부터 9까지 숫자를 생성하여 리스트 생성




# //////




# 이번에는 리스트 표현식에서 if 조건문을 사용해보겠습니다. 다음과 같이 if 조건문은 for 반복문 뒤에 지정합니다.

# [식 for 변수 in 리스트 if 조건식]
# list(식 for 변수 in 리스트 if 조건식)
a = [i for i in range(10) if i % 2 == 0]    # 0~9 숫자 중 2의 배수인 숫자(짝수)로 리스트 생성



a = [i * j for j in range(2, 10) for i in range(1, 10)] # 구구단


a = [1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))   #list와 map
