from bs4 import BeautifulSoup
from unidecode import unidecode


def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_html_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def process_page(page_number):
    html_content = read_html_file(f"parser/html/page_{page_number}.html")
    soup = BeautifulSoup(html_content, 'html.parser')
    main_container = soup.find('div', attrs={'class': 'widget-search-result-container q4i'})
    if not main_container:
        print("Элемент с классом 'widget-search-result-container q4i' не найден.")
        return
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
    file_path = f"parser/html_items/page_{page_number}.html"
    soup = BeautifulSoup(all_products_html, 'html.parser')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())


