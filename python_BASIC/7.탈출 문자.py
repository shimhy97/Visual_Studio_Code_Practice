# 문장을  두줄에 나눠서 쓰고싶은데 print는 한번만 쓰고싶다?
# /n을 사용한다 : 줄바꿈의 기능 보유
print ("나는 바보 \n입니다.") #이러면 \n을 기점으로 문장이 나눠짐


#탈출문자란? \  코딩의 역할을 하지 않고 문자 그대로 출력하고 싶을떄

print ("나는 \"나도코딩\" 입니다.") # 문자 그대로 "를 출력할때의 오류를 방지함


#문자 그대로의 \를 출력하고 싶을 경우
# print ( "C:\Users\download\심훈용\고려대학교\수치해석" )  ##이러면 오류 발생
# \\ 는 실출력\와 같은 역할

print ( "C:\\Users\\download\\심훈용\\고려대학교\\수치해석" )

# \r : 커서를 맨앞으로
print ("Apple pen \rPine ")

# \b :백스페이스
print ("Redd\b Apple")

# \t :여러칸 띄우기
print ("Redd\tapple")