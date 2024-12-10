import requests

from bs4 import BeautifulSoup as Bs
from requests.exceptions import ConnectionError


def get_html(url: str) -> str|None:
    try:
        response = requests.get(url)
        status = response.status_code
        if status != 200 and str(status)[0] !=3:
            print(f'ошибка запроса. Код ответа - {status}')
            return None
        print(f"Код ответа - {status}")
        html = response.text
        return html
    except ConnectionError as error:
        print('Нет ответа от сервера')
        print(type(error))
        return None

def parse_html(html: str):
    soup: Bs = Bs(html, 'html.parser')
    current_data = soup.find('h2', class_="h2 blue").text.split('\n')[-1].strip()[:10]
    # table =
    pass

URL = "https://www.alta.ru/currency"
html = get_html(URL)
if html:
    parse_html(html)