# 기존 print문의 비밀..!
# 콤마로 연결하면 띄어쓰기 적용, +로 연결하면 띄어쓰기 미적용.. 왜그럴까?
print("PYthon","seal")

print("Python", "Java", sep = "?", end = " ")    # 콤마 연결 시, sep 은 단어사이 구분 하는 단어를 지정,  end는 문장 끝에 붙일 단어를 지정하면서 다음줄 연달아 출력
print("C++", "C#")

import sys
print( "python", "Java", file=sys.stdout)
print( "Python", "Java", file=sys.stderr) #에러 발생 시 콘솔에 에러 메시지를 띄울 때 사용하는 방법이다. 빨간줄 대신 내가 지정한 문구가 나옴.




scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items() :                   #items() 를 쓰게되면 사전 형태에서 키와 밸류가 페어로 나온다. 
    print ( subject.ljust(8), str(score).rjust(4), sep = ":")       # ★주의 : 숫자는 str 꼭 붙여야 한다!


## 은행 대기순번표
# 001, 002, 003, ...

for i in range(1,21):
    print("대기번호 : {0}".format(str(i).zfill(3)))         #num.zfill(3) : 세자리 공간 할당하고 빈 공간은 0으로 채움

answer = input("숫자를 입력하세요") 
print(type(answer))                                 # 중요!!!! ★★★input 명령어는 항상 str 타입으로 반환함. 따라서 굳이 str()을 해줄 필요가 없음
print ( "입력하신 값은 '{}'입니다".format(answer))