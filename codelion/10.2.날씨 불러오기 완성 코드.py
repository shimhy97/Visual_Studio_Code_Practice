import requests
# json = javascript object notation // 자바스크립트의 object 문법을 따르는 문자 기반의 데이터 포맷.
# 데이터를 주고 받을 때  주로 사용하는 포맷이 바로 json이다. 이를 이용하면, 이쁘게 출력할 수 있는것이다.
import json

city = "Tokyo"
apikey = "cf538e545bc5545205c474942c87911e"
lang = "kr"

# ? 뒷부분이 parameter임 q= ~ 로 시작하는 이부분. 각 parameter들은 &로 이어붙여진다.
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"


# 크롤링 부분과 똑같다. url 대신 api 주소가 들어갔을 뿐. 
# 이때 result엔 응답이 성공했다는 response[200]이 저장된다. 텍스트 내용을 직접 보고싶다면, result.text를 출력하자.
result = requests.get(api) 

# 근데 문제가, result.text는 표면적으로 Dictionary 형식을 띠고 있긴 하지만, type은 str문자열이다. 즉 가공이 어렵다.
# 이를 해결하기 위해, str을 json 타입으로 바꿔주는 명령어 이다.
# print(type(result.text))
# print(type(data))
data = json.loads(result.text)

print(data["name"],"의 날씨입니다.")
print("날씨는 ",data["weather"][0]["description"],"입니다.")
print("현재 온도는 ",data["main"]["temp"],"입니다.")
print("하지만 체감 온도는 ",data["main"]["feels_like"],"입니다.")
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
print("습도는 ",data["main"]["humidity"],"입니다.")
print("기압은 ",data["main"]["pressure"],"입니다.")
print("풍향은 ",data["wind"]["deg"],"입니다.")
print("풍속은 ",data["wind"]["speed"],"입니다.")