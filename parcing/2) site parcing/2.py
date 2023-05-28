import requests
from bs4 import BeautifulSoup


""" url = 'http://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'

headers = {
    "Accept": "*/*",
    "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.3.766 (beta) Yowser/2.5 Safari/537.36"
}


req = requests.get(url, headers=headers)
src = req.text

with open('index.html', 'w') as file:
    file.write(src) """
    
with open('index.html') as file:
    src = file.read()
    
soup = BeautifulSoup(src, 'lxml')