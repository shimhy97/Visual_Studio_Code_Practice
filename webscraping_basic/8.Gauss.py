# bequtifulsoup 구글에 검색
# 들어가면 자세한 설명이 잘되어있음

import requests

from bs4 import BeautifulSoup


url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554"
res = requests.get(url)

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("td", attrs={"class":"title"})
for i in cartoons :
    title = i.a.get_text()
    link = "https://comic.naver.com" + i.a["href"]
    print(title , link)

#평점 구하기

stars = soup.find_all("div", attrs={"class":"rating_type"})
for i in stars:
    ratings = i.strong.get_text()
    print(ratings)