import os
import requests
from bs4 import BeautifulSoup as bs

os.system("clear")
url = "https://www.iban.com/currency-codes"

res = requests.get(url)
html = res.text
soup = bs(html,'html.parser')


# print(soup)

results = soup.findAll('tbody')


countryname=[]
code = []

for i in results:
  data=[]
  data.append(i)

print(data)
