import requests
import json
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver

def get_data(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    }

    #получаем ссылки на отели

    r = requests.get('https://api.rsrv.me/hc.php?a=hc&most_id=1317&l=ru&sort=most', headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    hotel_cards = soup.find_all('div', class_='hotel_card_dv')

    for hotel_url in hotel_cards:
        hotel_url = hotel_url.find('a').get('href')
        print(hotel_url)

def get_data_with_selenium(url):
    options = webdriver.ChromeOptions()
    options.set_preference('general.useragent.override', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36')