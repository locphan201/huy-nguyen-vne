import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import sys
import os

links = [
    'https://vnexpress.net/thoi-su',
    'https://vnexpress.net/goc-nhin',
    'https://vnexpress.net/the-gioi',
    'https://vnexpress.net/the-thao',
    'https://vnexpress.net/kinh-doanh',
    'https://vnexpress.net/bat-dong-san',
    'https://vnexpress.net/khoa-hoc',
    'https://vnexpress.net/giai-tri',
    'https://vnexpress.net/phap-luat',
    'https://vnexpress.net/giao-duc',
    'https://vnexpress.net/suc-khoe',
    'https://vnexpress.net/doi-song',
    'https://vnexpress.net/du-lich',
    'https://vnexpress.net/so-hoa',
    'https://vnexpress.net/oto-xe-may',
    'https://vnexpress.net/y-kien'
]

FILEPATH = 'category_articles.txt'

urls = []

for link in tqdm(links, desc='Process pages'):

    for i in range(21):    
        templink = link if i == 0 else link + f'-p{i}'
        response = requests.get(templink)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            articles = soup.find_all('article', class_='item-news')

            for article in articles:
                h3_tag = article.find('h3')
                if h3_tag:
                    a_tag = h3_tag.find('a')
                    if a_tag and 'href' in a_tag.attrs:
                        urls.append(a_tag['href'])
        else:
            print(f'Failed to retrieve the web page. Status code: {response.status_code}')

with open(FILEPATH, 'w', encoding='utf-8') as file:
    file.write('\n'.join(urls))
    
print(f'Total urls: {len(urls)}')