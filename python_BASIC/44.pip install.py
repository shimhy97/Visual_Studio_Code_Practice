# 파이썬은 이미 잘 만들어진 패키지를 가져와서 쓰는것도 중요한 역량이다.
# 다른사람이 만든 패키지는 어떤것이 있을까?

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

# pip list = 설치되어있는 패키지 목록 참조 가능.
# pip install --upgrade 패키지명
# pip uninstall 패키지명
