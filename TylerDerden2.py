import requests
import re
from bs4 import BeautifulSoup
import json
import time
headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }

url = 'https://agroserver.ru/zapchasti/Y2l0eT18cmVnaW9uPXxjb3VudHJ5PXxtZXRrYT18c29ydD0xfGFjY2VwdF9nZT0x/1/'
req = requests.get(url, headers = headers).text
with open('agro_main.html', 'w', encoding='utf-8') as file:
    file.write(req)
with open('agro_main.html',encoding='utf-8') as file:
    src = file.read()
soup = BeautifulSoup(src, 'lxml')
catalog = soup.find_all('div', class_ = 'line')
data = []
for item in catalog:
    product_page_link = 'https://agroserver.ru' + item.find('div', class_ = 'th').find('a').get('href')
    pg_src = requests.get(product_page_link, headers=headers).content
    pg_soup = BeautifulSoup(pg_src,'lxml')
    info_list = pg_soup.find('div', class_ = 'text').find_all('p')
    info = []
    for i in info_list:
        info.append(i.text)
    print(pg_src)
    name = item.find('div', class_ = 'th').find('a').text.strip()
    seller = item.find('a',class_ = 'personal_org_menu').text.strip()
    number = item.find('div', class_ = 'phone')
    if number is None:
        number = item.find('div', class_ = 'phone2')
    number_fixed = number.find('a').text.strip()
    local_data = {
        'Product name': name,
        'Product info': info,
        'Seller name': seller,
        'Number': number_fixed
    }   
    data.append(local_data)
    time.sleep(random.randrange(20,30))
with open('page_data','w',encoding='utf-8') as json_file:
    json.dump(data,json_file, indent=4,ensure_ascii=False)
    
# with open('agro_main.html', 'w', encoding='utf-8') as file:
#     file.write(req)
