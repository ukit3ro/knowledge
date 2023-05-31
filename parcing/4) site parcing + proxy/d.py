import requests
from bs4 import BeautifulSoup
import lxml

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.3.766 (beta) Yowser/2.5 Safari/537.36"
}

for i in range(0, 192, 24):
    url = f'https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=31%20May%202023&to_date=&maxprice=500&o={i}&bannertitle=June'
    print(url)
    
    
    