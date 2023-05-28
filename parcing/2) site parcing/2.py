import requests
from bs4 import BeautifulSoup
import json

#
# url = 'http://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
#
# headers = {
#     "Accept": "*/*",
#     "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.3.766 (beta) Yowser/2.5 Safari/537.36"
# }
#
#
# req = requests.get(url, headers=headers)
# src = req.text
#
# with open('index.html', 'w') as file:
#     file.write(src)
    
with open('index.html') as file:
    src = file.read()
    
soup = BeautifulSoup(src, 'lxml')
all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")

all_categories_dict = {}
for item in all_products_hrefs:
    item_text = item.text
    item_href = 'http://health-diet.ru' + item.get('href')
    print(f'{item_text}: {item_href}')
    all_categories_dict[item_text] = item_href

with open('all_categories_dict.json', 'w') as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)
