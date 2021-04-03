from bs4 import BeautifulSoup
import requests as req
# 아래는 저자:윤동주 부분인데 이는 웹사이트에서 복사하면 된다.

headers = {r'user-agent':r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'referer':r'https://nid.naver.com/login/sso/finalize.nhn?url=https%3A%2F%2Fwww.naver.com&sid=KBwWbyEJdJL521l3&svctype=1'}

url = r"https://ko.wikisource.org/wiki/%EC%A0%80%EC%9E%90:%EC%9C%A4%EB%8F%99%EC%A3%BC"

html = req.get(url,headers=headers).text

soup = BeautifulSoup(html,'lxml')

print(soup)