from parser.get_main_html import process_page
import aiohttp
import asyncio

async def main():
    url_template = "https://www.ozon.ru/seller/proffi-1/products/?miniapp=seller_1&page={}"
    total_pages = 5
    async with aiohttp.ClientSession() as session:
        tasks = [process_page(url_template.format(page_number), page_number) for page_number in range(1, total_pages + 1)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
