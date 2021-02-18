# QUIZ) 당신은 카카오 서비스를 이용하는 택시 기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1 : 승객 별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [0] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [0] 3번째 손님 (소요시간 : 5분)
# . . .
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 분

from random import *

count = 0
list_time = [randrange(5,51) for i in range(0,51)]
print(list_time)

for i in range(1,51) :
    if list_time[i] >=5 and  list_time[i]<=15 :
        mark = "O"
        count +=1
    else: 
        mark = " "
    print( f"[{mark}] {i}번째 손님 (소요시간 : {list_time[i]}분)")

print(f"총 탑승 승객 : {count}")