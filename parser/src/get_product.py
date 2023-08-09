import os
import json
from bs4 import BeautifulSoup
from logger.logger import logger


def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


def extract_product_info(product_element):
    product = {}
    name_element = product_element.find("div", class_="dx3")
    if name_element and name_element.find("span", class_="tsBody500Medium"):
        product["name"] = name_element.find(
            "span", class_="tsBody500Medium").text.strip()

    price_element = product_element.find(
        "span", class_="c3-a1 tsHeadline500Medium c3-b9")
    discount_element = product_element.find(
        "span", class_="tsBodyControl400Small c3-a2 c3-a7 c3-b1")
    if price_element and discount_element:
        product["price"] = price_element.text.strip()
        product["discount"] = discount_element.text.strip()

    image_element = product_element.find("img", class_="c9-a")
    if image_element and image_element.get("src"):
        product["image_url"] = image_element.get("src")
    link_element = product_element.find("a", href=True)

    if link_element and link_element.get("href"):
        link = "https://www.ozon.ru/" + link_element.get("href")
        product["product_url"] = link
    return product


def parse_page(page_number):
    file_path = f"parser/src/html_items/page_{page_number}.html"
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    product_elements = soup.find_all("div", class_="item")
    products = [extract_product_info(element) for element in product_elements]
    return products


def get_products_in_json(pages):
    all_products = []

    for page_number in range(1, pages + 1):
        products_on_page = parse_page(page_number)
        all_products.extend(products_on_page)

    output_data = {"product": all_products}
    if not os.path.exists("parser/src/json_items"):
        os.makedirs("parser/src/json_items")

    json_filename = "parser/src/json_items/all_products.json"
    save_to_json(output_data, json_filename)
    logger.info(f"Все данные сохранены в Json co страницы: {pages}")
