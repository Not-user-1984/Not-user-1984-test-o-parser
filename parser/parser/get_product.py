import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()



def product_parser():
    file_path = "parser/html_items/page_1.html"
    html_content = read_html_file(file_path)
    print(html_content)
    # Создаем объект BeautifulSoup для предварительной обработки HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Получаем предобработанный HTML-код
    processed_html = soup.prettify()

    # Создаем объект ElementTree из предобработанного HTML
    tree = ET.ElementTree(ET.fromstring(processed_html))

    # Находим все span-элементы в дереве
    span_elements = tree.findall('.//span')

    # Извлекаем текст из span-элементов по позициям
    if len(span_elements) >= 3:
        скидочная_цена = span_elements[0].text.strip()
        исходная_цена = span_elements[1].text.strip()
        оставшееся_количество = span_elements[2].text.strip()

        # Выводим извлеченную информацию
        print("Скидочная цена:", скидочная_цена)
        print("Исходная цена:", исходная_цена)
        print("Оставшееся количество:", оставшееся_количество)
    else:
        print("Не удалось найти достаточно span-элементов")

product_parser()
