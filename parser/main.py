from logger.logger import logger

from src.get_main import get_main_page
from src.get_items_product import process_page
from src.get_product import get_products_in_json


def main():
    url_template = "https://www.ozon.ru/seller/proffi-1/products/?miniapp=seller_1&page={}"
    total_pages = 15
    logger.info(f"Запуск парсера на {total_pages} страниц")

    for page_number in range(1, total_pages + 1):
        get_main_page(url_template.format(page_number), page_number)
        process_page(page_number)
        get_products_in_json(page_number)
        logger.info(f"Все задачи выполнены обработанo {page_number}")

    logger.info("Все задачи выполнены")

if __name__ == "__main__":
    main()
