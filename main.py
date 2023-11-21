from bs4 import BeautifulSoup
import requests
import json

def info_web_json(catgory):
    res = requests.get(f'https://upl.uz/{catgory}/').text
    soup = BeautifulSoup(res, 'html.parser')

    box = soup.find('div', id='dle-content')
    articles = box.find_all('div', class_='short-story')
    data = []
    for article in articles:
        title = article.find('h2', class_='sh-tit').get_text()
        link = article.find('h2', class_='sh-tit').find('a')['href']
        description = article.find('div',class_='sh-pan').get_text(strip=True).split('...')[0]+'...'
        image = 'https://upl.uz' + article.find('img', class_='lazy-loaded')['data-src']
        data.append(
            {
                'title': title,
                'link': link,
                'description': description,
                'image': image
            }
        )
    with open(f'{catgory}.json', mode='w', encoding='utf-8') as file:
        json.dump(data, file,indent=4, ensure_ascii=False)
    print('...................')
    print('Json file tayyor!!!')

while True:
    catgory = input('Yonalish:')
    info_web_json(catgory)