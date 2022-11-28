import requests                  # 웹 페이지의 HTML을 가져오는 모듈
from bs4 import BeautifulSoup    # HTML을 파싱하는 모듈
 
# 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
response = requests.get('https://pythondojang.bitbucket.io/weather/observation/currentweather.html')
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table',{'class':'table_develop3'})

lines = table.find_all('tr')

print(lines)

for line in lines[2:] : 
    weather = line.find_all('td')
    temp = line[2]
    humid = line[5]
    