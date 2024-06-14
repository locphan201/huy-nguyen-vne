import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import sys
import os

READFILE = 'category_articles.txt'
FILEPATH = 'category_content.txt'

try:
    with open(READFILE, 'r') as file:
        urls = file.readlines()
except Exception as e:
    print('Error:', str(e))
    sys.exit()

if len(urls) == 0:
    print('Please run hotnews.py and category.py first!')
    sys.exit()

if not os.path.exists(FILEPATH):
    with open(FILEPATH, 'w', encoding='utf-8') as file:
        file.write('')

urls = [url.replace('\n', '') for url in urls]

for url in tqdm(urls, desc='Retrieving content'):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        article_detail = soup.find('article', class_='fck_detail')

        if article_detail:
            content = '\n'.join([p.get_text(strip=True) for p in article_detail.find_all('p')])

            with open(FILEPATH, 'a', encoding='utf-8') as file:
                file.write(content + '\n\n')
    else:
        print(f'Failed to retrieve the web page. Status code: {response.status_code}')
