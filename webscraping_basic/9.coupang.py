# Get 방식과 Post 방식

import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=&rocketAll=false&searchIndexingToken=1=4&backgroundColor="

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"} 
res = requests.get(url, headers=headers)  
# 가져온 주소가 문제가 있으면 프로그램을 끝내라!
res.raise_for_status() 

soup = BeautifulSoup(res.text, "lxml")

# print(res.text)
# class명이 search-product로 시작하는 모든 element를 리스트 태그에서 가져. 무슨 형태로? 리스트 형태로!!!!!!!!!!!!
notebooks = soup.find_all("li", attrs={"class":re.compile("^search-product")})

for i in notebooks:
    print(i.find("div",attrs={"class":"name"}).get_text())
