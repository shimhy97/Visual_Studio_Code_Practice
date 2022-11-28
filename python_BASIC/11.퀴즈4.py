# from random import *

# li = [1,2,3,4,5]
# print(li)
# shuffle(li)        ## li 라는 자료구조의 자료 순서를 랜덤하게 섞음
# print(li)          
# print(sample(li,1))  ## li 라는 자료구조에서 자료 하나를 랜덤으로 추출함

# Quiz) 파이썬 코딩 대회 주체, 댓글 이벤트 진행, 1명은 치킨 3명은 커피 쿠폰 받게 됨. 추첨 프로그램 작성
# 조건1: 학생수20명, 아이디1-20
# 조건2: 무작위, 중복 불가
# 조건3: random 모듈의 shuffle과 sample을 활용
# # 출력 예제
# -- 당첨자 발표 --
# 치킨 당점자 : 1 
# 커피 당첨자 : [2,3,4]
# -- 축하합니다 --

from random import *

group = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

shuffle(group)

print("커피 당첨자는 ", group[0], "입니다")
print("치킨 당첨자는 ", group[1:4], "입니다")

