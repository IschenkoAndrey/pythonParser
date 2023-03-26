# pip freeze > requirements.txt
from bs4 import BeautifulSoup
import requests
import fake_useragent
import json
# import certifi


def get_company():
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

def get_listtendercompany():
    ua = fake_useragent.UserAgent()
    #edr = '38855066'
    #url_listtender = 'https://clarity-project.info/tenders/?tenderer=38855066&tenderer_status=supplier'
    #url_tender = 'https: //clarity-project.info/tender/48ad84f232614f42b6bfb010282558c1'
    #i = '38855066'

    req = requests.get('https://clarity-project.info/tenders/?tenderer=38855066&tenderer_status=supplier', headers={"User-Agent": ua.random})
    # #json_data = json.loads(req.text)
    # #html_response = json_data["html"]
    #

    #with open(f"data/index_{i}.html", "w") as file:
    #
    #     #     file.write(req.text)

    #with open(f"data/index_{i}.html") as file:
    #html_file = open(f"data/index_{i}.html", encoding='UTF-8').read()
    #soup = BeautifulSoup(html_file,'lxml')
    soup = BeautifulSoup(req.text, 'lxml')
    soup.find('table', class_='table-wrapper tenders-list one-line').find_all('tr', class_='table-row')
    return tag.has_attr('class') and not tag.has_attr('id')

    for row in soup.find('table', class_='table-wrapper tenders-list one-line').find_all('tr', class_='table-row'):
        if row.has_attr('data-id'):
            id_tender = soup.find('table', class_='table-wrapper tenders-list one-line').find_all('tr', class_='table-row')[1].get("data-id")

            #заголовок данных soup.find('table', class_='table-wrapper tenders-list one-line').find_all('tr', class_='table-row')[1].find('td', class_='tender-info').find('div', class_='tender-edrs clearfix').find_all({'h4','div'})
            # данные по тендеру
            url_tender = f'https: //clarity-project.info/tender/{id_tender}'
            req_tender = requests.get(url_tender, headers={"User-Agent": ua.random})
            soup = BeautifulSoup(req_tender.text,'lxml')











def get_listtendercompanyFile():
    ua = fake_useragent.UserAgent()
    edr = '38855066'
    url_listtender = 'https://clarity-project.info/tenders/?tenderer=38855066&tenderer_status=supplier'
    # url_tender = 'https: //clarity-project.info/tender/48ad84f232614f42b6bfb010282558c1'
    # i = '38855066'

    req = requests.get('https://clarity-project.info/tenders/?tenderer=38855066&tenderer_status=supplier',
                       headers={"User-Agent": ua.random})
    with open(f"data/index_{edr}.html", "w",encoding="utf-8") as file:
        file.write(req.text)
    file.close()
    soup = BeautifulSoup(req.text, 'html.parser')



    for row in soup.find('table', class_='table-wrapper tenders-list one-line').find_all('tr', class_='table-row'):
        if row.has_attr('data-id'):
            id_tender = row.get("data-id")
            url_tender = f'https://clarity-project.info/tender/{id_tender}'
            req = requests.get(url_tender,
                               headers={"User-Agent": ua.random})
            with open(f"data/tender_{id_tender}.html", "w",encoding="utf-8") as file:
                file.write(req.text)
            file.close()


def main():
    # Get_Company()
    #get_listtendercompany()
    get_listtendercompanyFile()


if __name__ == '__main__':
    main()