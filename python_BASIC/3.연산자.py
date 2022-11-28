number = 2+3*4
print (number)  #14
number = number + 2  
print(number)  #16
number +=2
print (number) #18
number /=2   
print (number) #9
number -=2
print (number) #7

number %=2    ## 2로 나눈 나머지는?
print (number) # 1

print (abs(-5)) ## 5
print (max(5,12)) # 12
print (round(3.14)) # 3

from math import * #math 수입
print (floor(4.99)) #내림
print (ceil(3.14)) #올림
print (sqrt(16)) # 제곱근

##랜덤함수

from random import *  #random 수입

# print(random())   #난수 추출 (0.0 이상 ~ 1.0 미만의 수 임의 생성)
# print(random()*10) #0.0~10.0 미만의 임의의 수 생성
# print( int(random()*10))  # 0~10 사이의 임의의 정수 생성 0부터 9까지
# print( int(random()*10)+1)  # 1~10 사이의 임의의 정수 생성 1부터 10까지

print(randrange(0,45))   # randrange(a,b)는 a 이상 b 미만의 정수를 출력한다. 

print(randint(0,45))  # randint(a,b)는 a 이상 b 이하의 정수를 출력한다.