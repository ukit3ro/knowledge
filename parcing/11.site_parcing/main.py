import random

import requests
from requests import Session
from bs4 import BeautifulSoup
import json
import os
import time


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}


def get_data_file(url):
    response = requests.get(url, headers=headers)
    # with open('index.html', 'w') as file:
    #     file.write(response.text)
    # with open('index.html') as file:
    #     src = file.read()
    # soup = BeautifulSoup(src, 'lxml')
    #
    # cards = soup.find('div', class_='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 2xl:grid-cols-5 md:gap-6 gap-12 w-full').find_all('div', class_='relative group text-center')
    # project_urls = []
    # for card in cards:
    #     project_url = 'https://www.landingfolio.com/' + card.find('a').get('href')
    #     project_urls.append(project_url)

    # with open('project_urls_list.txt', 'a') as file:
    #     for line in project_urls:
    #         file.write(f'{line}\n')
    with open('project_urls_list.txt') as file:
        lines = [line.strip() for line in file.readlines()]

        data_dict = []
        count = 0

        for line in lines:
            q = requests.get(line)
            result = q.content

            soup = BeautifulSoup(result, 'lxml')
            company = soup.find('h2').text.strip()
            description = soup.find('p').text.strip()
            categories_list = soup.find('ul', class_='flex content-center items-center justify-start space-x-2 flex-wrap').find_all('a')
            categories = []
            for item in categories_list:
                category = item.find_all('span')
                for i in category:
                    catg = i.text
                    categories.append(catg)

            data = {
                'startup_name': company,
                'description': description,
                'categories': categories
            }
            count += 1
            time.sleep(random.randrange(1, 3))
            print(f'{count}: {line} выполнена')

            data_dict.append(data)
            with open('data.json', 'w') as json_file:
                json.dump(data_dict, json_file, indent=4, ensure_ascii=False)


# def download_imgs(file_path):
#     """Download images"""
#
#     try:
#         with open(file_path) as file:
#             src = json.load(file)
#     except Exception as _ex:
#         print(_ex)
#         return "[INFO] Check the file path!"
#
#     items_len = len(src)
#     count = 1
#
#     for item in src[:100]:
#         item_name = item.get("title")
#         item_imgs = item.get("images")
#
#         if not os.path.exists(f"data/{item_name}"):
#             os.mkdir(f"data/{item_name}")
#
#         for img in item_imgs:
#             r = requests.get(url=img["url"])
#
#             with open(f"data/{item_name}/{img['type']}.png", "wb") as file:
#                 file.write(r.content)
#
#         print(f"[+] Download {count}/{items_len}")
#         count += 1
#
#     return "[INFO] Work finished!"


def main():
    get_data_file('https://www.landingfolio.com/')


if __name__ == "__main__":
    main()
