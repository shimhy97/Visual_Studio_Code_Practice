import requests
res1 = requests.get("http://google.com")
# res2 = requests.get("http://nadocoding.tistory.com")
# 서버 문제? 응답 코드?

print("응답코드 : ", res1.status_code) #200 이면 정상

# print("응답코드 : ", res2.status_code) #400 이면 비정상

# if res2.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 생김. [에러코드 {0}]".format(res2.status_code))

res1.raise_for_status()
print(res1)
# print(len(res1.text))
# print(res1.text)

with open("./webscraping_basic/mygoogle.html", "w", encoding="utf8") as f : #상대경로 
    f.write(res1.text)