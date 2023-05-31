import requests
from bs4 import BeautifulSoup
import lxml
from proxy_auth import proxies
import json


headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.3.766 (beta) Yowser/2.5 Safari/537.36"
}

fests_urls_list = []

for i in range(0, 24, 24):
    url = f'https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=31%20May%202023&to_date=&maxprice=500&o={i}&bannertitle=June'
    
    req = requests.get(url=url, headers=headers, proxies=proxies)
    json_data = json.loads(req.text)
    html_response = json_data['html']
    
    with open(f'data/index{i}.html', 'w') as file:
        file.write(html_response)
        
    with open(f'data/index{i}.html') as file:
        src = file.read()
        
    soup = BeautifulSoup(src, 'lxml')
    cards = soup.find_all('a', class_='card-details-link')
    
    for item in cards:
        fest_url = 'https://www.skiddle.com' + item.get('href')
        fests_urls_list.append(fest_url)


for url in fests_urls_list:
    req = requests.get(url=url, headers=headers, proxies=proxies)
    
    try:
        soup = BeautifulSoup(req.text, 'lxml')
        fest_name = soup.find('div', class_='MuiContainer-root MuiContainer-maxWidthFalse css-1krljt2').find('h1').text
        big_block = soup.find('div', class_='MuiBox-root css-42ibn8').find_all('div')
        

        print(big_block)
 #       fest_info_block = soup.find('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol').find_all('span')
 #       fest_date = fest_info_block[0].text + fest_info_block[1].text
 #       fest_location = soup.find('div', class_='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol').next_element

 #       print(fest_name)
 #       print(fest_date)
 #       print(fest_location)
 #       print('_'*20)
 #      print()

    except Exception as ex:
        print(ex)
        print('Error!')
    
    
    