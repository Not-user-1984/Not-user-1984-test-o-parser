from bs4 import BeautifulSoup
from logger.logger import logger


def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def process_page(page_number):
    html_content = read_html_file(f"parser/src/html/page_{page_number}.html")
    soup = BeautifulSoup(html_content, 'html.parser')
    main_container = soup.find(
        'div', attrs={'class': 'widget-search-result-container q4i'})
    if not main_container:
        err = "Продукты не найдены или такого номера страница не существует"
        logger.error(err)
        raise Exception(err)
    product = main_container.find_all('div')
    first_product = product[0]
    all_products_html = ""
    div_ = '<div class="item">'
    _div = '</div>'
    for product in first_product:
        page_content = str(product)
        # Сохраняем HTML-код каждого продукта страницы в файл
        if page_content != " ":
            all_products_html += div_ + page_content + _div
    file_path = f"parser/src/html/page_{page_number}.html"
    soup = BeautifulSoup(all_products_html, 'html.parser')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())
        logger.info(f"Страница {page_number} сохранена в файл: {file_path}")
