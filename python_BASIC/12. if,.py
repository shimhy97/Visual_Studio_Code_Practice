# weather = "비"
# if weather =="비":
#     print("우산을 챙기세요")
# elif weather =="미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")      # 해당 조건에 맞는 결과 출력하고 바로 조건문을 탈출함!!


# input("오늘 날씨는 어때요?") 사용자가 값을 입력함. scan처럼! 문자형태로(str) 저장됨.

# weather = input("오늘 날씨는 어떤가요? 입력해주세요")
# if weather == "눈" or weather == "비":
#     print("우산 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

temp = int(input("오늘의 기온은?"))

if temp >=30 :
    print("오늘 ㅈㄴ 더움")
elif temp <30 and temp >=20 : 
    print("그냥 약간 더운 정도.")
elif temp <20 and temp >=10 :
    print("선선합니디")
elif 0 <= temp <10 :
    print("추워요")
elif temp <0 :
    print("나가면 얼어요")