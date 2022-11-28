sentence = '나는 소년입니다.'
print (sentence)

sentence2 = "파이썬은 쉬워요"
print (sentence2)

sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""                           #변수를 줄바꿈을 해서 저장하고 싶을떄
print(sentence3)

#슬라이싱

jumin = "990120-1234567"
#여기서 필요한 부분만 잘라서 가져오고 싶어? 그렇다면 슬라이싱 사용
print ("성별: " + jumin[7])
print ("출생연도: " + jumin[0:2])   #0부터 2 직전까지!!!!!!!!!!!!!!!!!!
print ("출생월: " + jumin[2:4])
print ("주민번호 앞 여섯자리 : " + jumin[0:6])
print ("주민번호 앞 여섯자리 : " + jumin[:6])  # 처음부터 하는 세는 경우 0 안넣어줘도 됨
print ("뒤 7자리 : " + jumin[7:14]) 
print ("뒤 7자리 : " + jumin[7:])  # 끝까지 세는 경우 끝 숫자 안넣어줘도 됨 

print ("뒤 7자리 : " + jumin[-7:]) #이러면 맨 끝에서 7번째의 문자부터 끝까지 세줌



#문자열 처리 함수
python = "Python is Interesting."

print(python.lower())  # 변수를 모두 소문자로 출력
print(python.upper())  # 변수를 모두 대문자로 출력
print(python[0].lower())   #변수의 n번째 문자를 소문자로 출력
print(len(python)) #변수의 길이를 출력
print(python.replace("Python","Java"))  #변수의 특정 문자를 다른 문자로 치환 (앞-뒤)

index = python.index("n")
print(index)
index = python.index("e", 3)  # index(문자열, n ) n번째 숫자 뒤 부터 문자열의 위치를 반환함.
print(index)
print(python.find("n"))

print(python.find("JAVA"))   # find의 경우에는 없는 문자의 경우 -1을 반환
# print(python.index("JAVA"))  # index의 경우에는 없는 문자의 경우엔 에러가 뜨면서 멈춤

print(python.count("n"))  #변수에서 특정 문자의 갯수

python = "Python is Interesting"

print (python.upper())