import requests
from bs4 import BeautifulSoup as bs
from django.views.decorators.csrf import csrf_exempt

URL = 'https://oc.kg'

HEADERS = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15",
}

#start
@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req

#get data
@csrf_exempt
def get_data(html):
    soup = bs(html, "html.parser")
    items = soup.find_all('div', class_='item')
    cinema_kg = []

    for item in items:
        cinema_kg.append(
            {
                'title_name': item.find('div', class_='title').get_text(),
                'title_url': URL + item.find('a').get('href'),
                'image': URL + item.find('div', class_='cover').find('img').get('src'),
            }
        )
    return cinema_kg

#endparse
@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        cinema_kg2 = []
        for page in range(0, 1):
            html = get_html(f'https://oc.kg/#/catalog/page/1', params=page)
            cinema_kg2.extend(get_data(html.text))
        return cinema_kg2
    else:
        raise Exception('Error in parser!')