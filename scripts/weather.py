import requests

from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as Bs
from fake_useragent import UserAgent


def get_html(url: str) -> str | None:
    headers = {'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:129.0) Gecko/20100101 Firefox/129.0"}
    try:
        response = requests.get(url, headers=headers)
        # если Успешный запрос ИЛИ переадресация - то хорошо
        if response.status_code == 200 or str(response.status_code)[0] == '3':
            html = response.text
            # with open("index_mob")
            return  html
        else:
            print(f"Оша запроса, Код отва: {response.status_code}")
            return None
    except ConnectionError as err:
        print(f"Оибка запроса..\n{err}")
        return None

def get_weather_from_day(html: str) -> dict:
    soup = Bs(html, "html.parser")

    pass

URL = "https://world-weather.ru/pogoda/russia/saint_petersburg/7days/"
html = get_html(url=URL)
if html:
    get_weather_from_day(html)
