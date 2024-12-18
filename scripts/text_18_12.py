import requests
from bs4 import BeautifulSoup
import json


def parse_page(url, num_items=6, output_filename="output.json"):
    """
    Парсит страницу, извлекает названия товаров и цены, ограничиваясь num_items.
    Сохраняет результат в JSON-файл.

    Args:
        url: URL-адрес страницы.
        num_items: Количество товаров для извлечения (по умолчанию 6).
        output_filename: Имя файла для сохранения JSON (по умолчанию "output.json").
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        items = soup.find_all('div', class_='item')

        results = []
        for item in items[:num_items]:
            name_element = item.find('a', class_='name')
            price_element = item.find('p', class_='price')

            if name_element and price_element:
                name = name_element.text.strip()
                price = price_element.text.strip()
                results.append(f"{name} - {price}")

        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
        print(f"Данные сохранены в файл '{output_filename}'")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")


if __name__ == '__main__':
    url = "https://parsinger.ru/html/index1_page_1.html"
    parse_page(url)  # По умолчанию сохранит в файл output.json
    # parse_page(url, num_items=10, output_filename='my_output.json') # пример сохранения 10 товаров в другой файл