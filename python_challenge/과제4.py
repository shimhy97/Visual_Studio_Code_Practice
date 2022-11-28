import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.iban.com/currency-codes")

indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")

currency_table = indeed_soup.find("tbody")

rows = currency_table.select('td')

print(rows)


table=[]
for row in rows:
    list=[]
    for j in range(3):
        list.append(rows[])
    rows.append(list)