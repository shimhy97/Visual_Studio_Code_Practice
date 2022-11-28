#pip install lxml -> 구문을 분석하는 도구
#pip install beatifulsoup4

import requests

from bs4 import BeautifulSoup

res = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
res.raise_for_status()
# print(res.status_code)

with open ("naver.html", "w",  encoding="utf8") as f:
    f.write(res.text)

soup = BeautifulSoup(res.text, "lxml") # 우리가 가져온 res.text를 lxml라는 파써를 통해서 뷰티풀숲 객체로 만든것.

# print(soup.a)               # soup 객체에서 처음 발견되는 a element를 출력
# print(soup.a.attrs)         # a라는 element의 속성정보를 반환해줌
# print(soup.a["href"])       # a라는 elment의 href 속성 '값' 정보를 출력할 수 있다.

#하지만!!!!!! 웹스크래핑 대상 페이지에 대한 정보를 잘 모르니까 이렇게 쓰기 힘들다
# 이때 사용하는 것이 find

# soup.find("a", attrs={"class":"Nbtn_upload"})       #class 값이 "Nbtn_upload" 인 a element를 찾아줘. (처음 나오는것)
# soup.find(attrs={"class":"Nbtn_upload"})       #class 값이 "Nbtn_upload" 인 어떤 element를 찾아줘 

rank1 = soup.find("li", attrs={"class":"rank01"}) #li 태그에 해당하는 html 중 class:rank01 속성을 갖는 것을 찾아서 저장한다.
print(rank1)
print(rank1.next_sibling.next_sibling)          # 다음 친척 찾는것은 이것도 되지만
rank2 = rank1.find_next_sibling()
print(rank2)            #이것도 된다.

print(rank2.get_text())     # get_text() : 문자열만 추출함.

rank1 = rank2.find_previous_sibling()       # 이전 친척 찾음.
print(rank1)

###
rank_list = soup.find("li", attrs={"class":"rank01"})
print(rank_list.find_next_siblings("li"))  # 해당 태그에 포함된 모든 친척들을 다 끌고옴. 