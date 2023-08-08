from parser.get_main import get_main_page
from parser.parser import process_page

def main():
    url_template = "https://www.ozon.ru/seller/proffi-1/products/?miniapp=seller_1&page={}"
    total_pages = 1
    for page_number in range(1, total_pages + 1):
        get_main_page(url_template.format(page_number), page_number)
        process_page(page_number)

if __name__ == "__main__":
    main()