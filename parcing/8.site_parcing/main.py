import datetime
import json
import requests
from bs4 import BeautifulSoup

def get_data(url):
    headers = {
        "User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.3.766 (beta) Yowser/2.5 Safari/537.36"
                
    }
 #   r = requests.get(url, headers)
 #   
 #   with open('projects.html', 'w') as file:
#        file.write(r.text)
    with open('projects.html') as file:
        src = file.read()
        
    soup = BeautifulSoup(src, 'lxml')
    articles = soup.find('div', class_='catalog__group').find_all('product-item')
    prices = soup.find('div', class_='product__desc').find('product__info').find('product__add')
    
    tire_urls = []
    tire_prices = []
    for article in articles:
        tire_url = 'https://roscarservis.ru' + article.find('a').get('href')
        tire_urls.append(tire_url)
    
    for price in prices:
        tire_price = price.find('span', class_='product__price-value').text
        tire_prices.append(tire_price)
    print(tire_prices)
        
    for tire_url in tire_urls[0:1]:
        req = requests.get(tire_url, headers)
        tire_name = '-'.join(tire_url.strip('/').split('-')[5:])
        
        with open(f'data/{tire_name}.html', 'w') as file:
            file.write(req.text)
            
        with open(f'data/{tire_name}.html') as file:
            src = file.read()
            
        soup = BeautifulSoup(src, 'lxml')
        tire_data1 = soup.find('section', class_='product-screen')
        tire_title = tire_data1.find('div', class_='product-screen__name').find('p').text
 #       tire_price = tire_data1.find('p', class_='product-screen__price-value').text
#        print(tire_price)
            
get_data('https://roscarservis.ru/catalog/legkovye/?arCatalogFilter_458_1500340406=Y&set_filter=Y')

a = ''