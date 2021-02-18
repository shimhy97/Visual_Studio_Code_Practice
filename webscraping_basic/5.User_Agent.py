#403에러가 떴던 이유?
#PC에서 접속했을때 스마트폰에서 접속했을때 뜨는 화면이 다름
#브라우저가 웹사이트에 접속할때 헤더 정보에 따라서 다른 정보를 줌
#만약 사람이 아니고 크롤링을 하는 PC가 접속할 시 접속을 차단할 수 있음.
#따라서, request를 이용했을 시 차단당해서 403에러가 뜰 수 있음. 이를 useragent로 해결이 가능.

# import requests
# res = requests.get("http://nadocoding.tistory.com")  #만약에 응답코드가 403이 뜨는 오류가 난다면 html이 깨져서 보인다. 이럴땐 어떻게 해야할까..?
# res.raise_for_status()
# with open("./webscraping_basic/nadocoding.html","w", encoding="utf8") as f:
#     f.write(res.text)


import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75"} 
res = requests.get(url, headers=headers)  

res.raise_for_status()
with open("nadocoding.html","w", encoding="utf8") as f:
    f.write(res.text)



#구글에 user agent string 검색 ㄱㄱ
#https://www.whatismybrowser.com/detect/what-is-my-user-agent
#접속하는 브라우저에 따라서 user agent는 다르게 나온다.
#크롬 기준
#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75