# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

# 예) http://naver.com

# 규칙 1: http:// 부분은 제외 =>naver.com
# 규칙 2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

# 예) 생성된 비밀번호 : nav51!

name = "http://daum.comthrough"

name2 = name.replace("http://","") #naver.com

name3= name2[0:name2.index(".")]

password = name3[0:3]+str((len(name3)))+str(name.count("e"))+"!"

print(f"현재 {name} 사이트의 비밀번호는 {password} 입니다.")