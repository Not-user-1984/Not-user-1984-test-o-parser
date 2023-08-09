from parser.get_main import get_main_page
from parser.get_items_product import process_page
from parser.get_product import get_products_in_json

def main():
    url_template = "https://www.ozon.ru/seller/proffi-1/products/?miniapp=seller_1&page={}"
    total_pages = 10
    for page_number in range(1, total_pages + 1):
        get_main_page(url_template.format(page_number), page_number)
        process_page(page_number)
        get_products_in_json(page_number)

if __name__ == "__main__":
    main()