import requests
from bs4 import BeautifulSoup

url = "http://www.daum.net/"

# 특정 주소(url)로 요청을 보내고, 응답받은 내용을 저장하자.
response = requests.get(url)
# print(response.text)



# 의미없는 데이터를 의미있는 데이터 타입으로 바꿔주는 라인. 출력해보면 response랑 똑같지만 type이 다르다.
# response의 타입은 str이다. 그냥 문자열일 뿐이다. 이것은 가공하기가 상당히 어려움.. 이때 뷰숲을 쓰는거다.
# BeautifulSoup(데이터, 파싱방법) / 파싱은 데이터를 의미있게 만드는 방법
soup = BeautifulSoup(response.text, 'html.parser')  



# file = open("daum.html","w")
# file.write(response.text)
# file.close

# print(soup.title)
# print(soup.title.string)
# print(soup.span)
# print(soup.findAll('span'))

# 크롤링 전, 가져오려는 자료의 공통점을 찾아내야 한다.
# 태그 가져올 시 극 태그의 자식값들까지 다 가져와진다.
results = soup.findAll('a','link_favorsch')    # soup에 저장된 의미있는 데이터 에서 a 태그, 속성이 link_favorsch인거 다 가져온다.


#  조금 더 정확히 표현하면 get_text() 메서드는 현재 태그를 포함하여 모든 하위 태그를 제거하고 유니코드 텍스트만 들어있는 문자열을 반환합니다.
for result in results:
    print(result.get_text(),"\n")