
import requests

from bs4 import BeautifulSoup


# 네이버웹툰 요일별 목록----

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)

soup = BeautifulSoup(res.text, "lxml")
# cartoons = soup.find("a", attrs ={"class":"title"})
cartoons = soup.find_all("a", attrs ={"class":"title"})
print(cartoons)
for i in cartoons :
    print(i.get_text())

