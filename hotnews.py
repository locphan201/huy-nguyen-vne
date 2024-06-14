import requests
from tqdm import tqdm

FILEPATH = 'hotnews_articles.txt'

links = [f'https://vnexpress.net/microservice/listhotnews/type/{i}' for i in range(1, 9)]

urls = []

for link in tqdm(links, desc='Process pages'):
    response = requests.get(link)

    if response.status_code == 200:
        data = response.json()

        if 'message' in data:
            tokens = data['message'].split(' ')
            for token in tokens:
                if not 'https://vnexpress.net' in token:
                    continue
                url = token.replace('href="', '').replace('"', '')
                if not url in urls and not '#box_comment_vne' in token:
                    urls.append(url)
        else:
            print('Empty message')
    else:
        print(f'Failed to retrieve the web page. Status code: {response.status_code}')

with open(FILEPATH, 'w', encoding='utf-8') as file:
    file.write('\n'.join(urls))
    
print(f'Total urls: {len(urls)}')