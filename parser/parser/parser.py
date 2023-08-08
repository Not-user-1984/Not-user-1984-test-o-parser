from bs4 import BeautifulSoup
import re
from unidecode import unidecode


def generate_filename(text):
    text_lower = text.lower()
    movie_name_translit = re.sub(r'\s+', '_', unidecode(text_lower))
    return movie_name_translit


def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_html_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


# Функция для поиска всех продуктов на странице и вывода их в принт
def process_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    products = soup.select('div.io3.o3i')
    for product in products:
        product_name = product.select_one('span.tsBody500Medium').text.strip()
        product_price = product.select_one('span.c3-a1.tsHeadline500Medium.c3-b9').text.strip()
        product_discount = product.select_one('span.tsBodyControl400Small.c3-a2.c3-a7.c3-b1').text.strip()

        product_image = product.select_one('a')['href'] if product.select_one('a') else "Ссылка на изображение не найдена"
        product_description = product.select_one('a.c3-a1.tsHeadline600Regular.c3-b6')['href'] if product.select_one('a.c3-a1.tsHeadline600Regular.c3-b6') else "Ссылка на подробное описание не найдена"

        product_link = product.select_one('div.tile-hover-target.li2.i3l')['href'] if product.select_one('div.tile-hover-target.li2.i3l') else "Ссылка на продукт не найдена"

        print(f"Название продукта: {product_name}")
        print(f"Цена продукта: {product_price}")
        print(f"Скидка: {product_discount}")
        print(f"Ссылка на продукт: {product_link}")
        print(f"Ссылка на изображение: https://www.ozon.ru/product{product_image}")
        print(f"Ссылка на подробное описание: {product_description}")
        print("==============================================")
# pompa-dlya-vody-pompa-pompa-dlya-vody-mehanicheskaya-proffi-759379209/?_bctx=CAQQAQ&asb=HH%252Fr559GwKuPcPxXgKLHSBQ%252FNurozeL2yHf0n%252B3HjQ0%253D&asb2=-Zl86GNjzm0n7ByXM4ayxVFtbl0NiRG6JG9WNVIlkyEcB6CZuQTJba4yWriY_wJP&avtc=1&avte=2&avts=1691505043&hs=1&miniapp=seller_1&sh=I7gZTn-CJA
html_content = read_html_file("parser/html/page_1.html")
process_page(html_content)

