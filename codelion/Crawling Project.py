from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
from collections import deque
import os

import requests

from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument("window-size=1500,1200")
options.add_argument("no-sandbox")
options.add_argument("disable-dev-shm-usage")
options.add_argument("disable-gpu")
options.add_argument("log-level=3")
webdriver = webdriver.Chrome(r'C:\chromedriver',chrome_options=options)

# urls = ['https://www.wadiz.kr/web/wreward/category/288?keyword=&endYn=ALL&order=recommend',
#        'https://www.wadiz.kr/web/wreward/category/290?keyword=&endYn=ALL&order=recommend',
#       'https://www.wadiz.kr/web/wreward/category/313?keyword=&endYn=ALL&order=recommend',
#       'https://www.wadiz.kr/web/wreward/category/293?keyword=&endYn=ALL&order=recommend']


url = 'https://www.wadiz.kr/web/wreward/category/288?keyword=&endYn=ALL&order=recommend'
address = []

webdriver.get(url)
last_height = webdriver.execute_script("return document.body.scrollHeight")
body = webdriver.find_element_by_tag_name("body")
while True:
    btn = webdriver.find_element_by_css_selector('#main-app > div.MainWrapper_content__GZkTa > div > div.RewardProjectListApp_container__1ZYeD.RewardMainProjectList_listApp__2noRS > div.ProjectCardList_container__3Y14k > div:nth-child(2) > div > button')
    if btn:
        try:
            webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")
            time.sleep(2)
        
        except:
            print('버튼 안됨/타임오류')
            break

    else:
        print('버튼 없음')
        break
        
    
try:
    atag = webdriver.find_elements_by_css_selector("#main-app > div.MainWrapper_content__GZkTa > div > div.RewardProjectListApp_container__1ZYeD.RewardMainProjectList_listApp__2noRS > div.ProjectCardList_container__3Y14k > div.ProjectCardList_list__1YBa2 > div a")
    for n in range(0,len(atag)):
        address.append(n)
except:
    print('태그 없어요')
    
# print(len(address))

df = pd.DataFrame(address)
df.to_csv(r'C:\패션잡화 디자인소품 모임 출판.csv')

r'C:\chromedriver'