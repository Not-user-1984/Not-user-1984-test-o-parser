import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager


def get_main_page(url, page_number):
    chrome_options = Options()
    chrome_options.headless = True

    browser = webdriver.Chrome(
        service=ChromeService(),
        # options=chrome_options
    )
    # browser = webdriver.Chrome(executable_path="parser/driver/chromedriver",
    #                           options=chrome_options)
    try:
        browser.get(url)

        # Ждем некоторое время для загрузки страницы (если необходимо)
        time.sleep(5)

        # Получаем HTML-код страницы
        page_content = browser.page_source

        # Задаем путь к файлу, в который хотим сохранить страницу
        file_path = f"parser/html/page_{page_number}.html"

        # Сохраняем HTML-код страницы в файл
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(page_content)

        print(f"Страница {page_number} сохранена в файл: {file_path}")

    finally:
        # Закрываем браузер после всех манипуляций
        browser.quit()
