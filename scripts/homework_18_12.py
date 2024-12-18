import requests
from bs4 import BeautifulSoup
import json


def parse_page(url, num_items=6):
    """Парсит страницу и извлекает названия товаров и цены, ограничиваясь num_items.
    Записывает результат в JSON.

    Args:
        url: URL-адрес страницы.
        num_items: Количество товаров для извлечения (по умолчанию 6).

    Returns:
        JSON строка.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        items = soup.find_all('div', class_='item')  # Находим все блоки с товарами

        results = []
        for item in items[:num_items]:  # Берем только первые num_items товаров
            name_element = item.find('a', class_='name')
            price_element = item.find('p', class_='price')

            if name_element and price_element:
                name = name_element.text.strip()
                price = price_element.text.strip()
                results.append(f"{name} - {price}")
        return json.dumps(results, ensure_ascii=False, indent=4)  # преобразовываем список в JSON строку
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе: {e}")
        return None
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")
        return None


if __name__ == '__main__':
    url = "https://parsinger.ru/html/index1_page_1.html"
    json_output = parse_page(url)

    if json_output:
        print(json_output)