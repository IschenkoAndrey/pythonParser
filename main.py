# pip freeze > requirements.txt
# python -m pip install -r requirements.txt
# python -m venv venv
# venv\Scripts\activate
from bs4 import BeautifulSoup
import csv
import urllib
import time
import requests
import fake_useragent
import certifi

ua = fake_useragent.UserAgent()

#print(certifi.where())

r = requests.get('https://clarity-project.info/edr/37177306', headers={"User-Agent": ua.random})
soup = BeautifulSoup(r.content, 'html.parser')

entitycontent = soup.find(class_="entity-content")
#  table align-top mb-15 border-bottom w-100

rows = entitycontent.table.find_all('tr')
#print(rows)

for row in rows:
    print('************************************************')
    print(f'{row.get_text(strip=True)} - {row.get("href")}')
    print('************************************************')
    for tag in row.find_all('td'):
        print('------------------------------')
        print(f'{tag.get_text(strip=True)}')
#for datatag in entitycontent.table.find_all('tr')

#print(entitycontent.text)

# links = soup.find('nav').find_all('a')
# print(links)
# for link in links:
#     print(f'{link.get_text(strip=True)} - {link.get("href")}')