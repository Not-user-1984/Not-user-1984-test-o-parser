import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
from logger.logger import logger


def get_main_page(url, page_number):
    chrome_options = Options()
    # chrome_options.add_argument('--headless')

    browser = webdriver.Chrome(
        service=ChromeService(),
        options=chrome_options
    )

    try:

        logger.info(f"Загрузка страницы {url}")
        browser.get(url)
        time.sleep(5)
        page_content = browser.page_source

        soup = BeautifulSoup(page_content, 'html.parser')
        blok = soup.find(
            'div',
            text='www.ozon.ru needs to review the security of your connection before proceeding.'
        )
        if blok is None:
            file_path = f"parser/src/html/page_{page_number}.html"
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(page_content)
            logger.info(f"Страница {page_number} сохранена в файл: {file_path}")
        else:
            logger.critical("Страница заблокированна")
            raise Exception("Страница заблокированна")

    finally:
        logger.info("Закрытие браузера")
        browser.quit()
