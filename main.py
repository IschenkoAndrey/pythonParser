# pip freeze > requirements.txt
from bs4 import BeautifulSoup
import requests
import fake_useragent
import certifi

def Get_Company():
    ua = fake_useragent.UserAgent()

    #print(certifi.where())
    #LinkFind1='https://clarity-project.info/tenders/?tenderer=38855066&tenderer_status=supplier'
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

def Get_ListtenderCompany():

    url = f"https://clarity-project.info/tenders/?tenderer=38855066&tenderer_status=supplier"


    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    html_response = json_data["html"]

    with open(f"data/index_{i}.html", "w") as file:
        file.write(html_response)

    with open(f"data/index_{i}.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
def main():
    # get_data()
    Get_Company()


if __name__ == '__main__':
    main()