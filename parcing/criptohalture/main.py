import json
from bs4 import BeautifulSoup
import lxml
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import os


def choice():
    base_path = os.path.dirname(os.path.abspath(__file__))
    data_file_path = os.path.join(base_path, 'data.txt')
    
    with open(data_file_path, 'r') as file:
        content = file.read()
        
    perems = content.split('.')
    url = f'https://dexscreener.com/solana?rankBy=trendingScore{perems[0]}&order={perems[1]}&minLiq={perems[2]}&maxLiq={perems[3]}&maxMarketCap={perems[4]}&minAge={perems[5]}&maxAge={perems[6]}&min24HVol={perems[7]}'
    
    return url

def dexscreener_data(url):
    options = webdriver.ChromeOptions()
    # options.experimental_options("useAutomationExtension", False);
    options.add_argument("--disable-blink-features=AutomationControlled");
    driver = uc.Chrome(headless=False,use_subprocess=False)
    #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(url)
    
    i = 0
    time.sleep(8)
    pyautogui.moveTo(537, 416)
    pyautogui.click()
    time.sleep(8)
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(base_path, 'dexscreener_files')
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    html_file_path = os.path.join(output_folder, f'dexinfo_{i}.html')
    with open(html_file_path, 'w') as file:
        file.write(driver.page_source)
    
    if driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div[2]/div[5]/div/a'):
        driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div[2]/div[5]/div/a').click()
        time.sleep(5)
        next_html_file_path = os.path.join(output_folder, f'dexinfo_{i + 1}.html')
        with open(next_html_file_path, 'w') as file:
            file.write(driver.page_source)
        i += 1
    
    while True:
        try:
            if driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div[2]/div[5]/div/a[2]'):
                driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div[2]/div[5]/div/a[2]').click()
                time.sleep(5)
                next_html_file_path = os.path.join(output_folder, f'dexinfo_{i + 1}.html')
                with open(next_html_file_path, 'w') as file:
                    file.write(driver.page_source)
                i += 1
            else:
                break
        except Exception as e:
            print(e)
            break
    
    driver.close()
    driver.quit()

def dexdata_process():
    data  = []
    adresses = []
    cals = []
    base_path = os.path.dirname(os.path.abspath(__file__))
    files_dir = os.path.join(base_path, 'dexscreener_files')
    
    try:
        for i in range(20):
            file_path = os.path.join(files_dir, f'dexinfo_{i}.html')
        
            with open(file_path) as file:
                src = file.read()
            soup = BeautifulSoup(src, 'lxml')



            table = soup.find_all('a', class_='ds-dex-table-row ds-dex-table-row-top')
            for item in table:
                short_name = item.find('span', class_='ds-dex-table-row-base-token-symbol').text
                name = item.find('span', class_='ds-dex-table-row-base-token-name-text').text
                link = 'https://dexscreener.com' + item.get('href')
                cal = (item.find('div', class_='ds-table-data-cell ds-dex-table-row-col-price-change-h24').find('span').text)
                cal = float(cal.replace('%', '').replace(',', '.').replace(' ', ''))
                if -50 <= cal <= 50:
                    cals.append(cal)
                else:
                    cals.append(None)

                if (item.find('img', class_='ds-dex-table-row-token-icon')):
                    adressie = item.find('img', class_='ds-dex-table-row-token-icon').get('src')
                    parts = adressie.split('/')
                    if 'solana' in parts:
                        index = parts.index('solana') + 1
                    else:
                        index = parts.index('cms') + 2
                    adress = '/'.join(parts[index:])
                    adress = adress[:adress.rfind('.')]
                else:
                    adress = 'none'
                adresses.append(adress)
                if ((-50 <= cal <= 50) and (adress != 'none')):
                    data.append(
                    {
                        'token_name': name,
                        'short_name': short_name,
                        'link': link,
                        'token_adress': adress,
                        'solsniffer_link': 'https://solsniffer.com/scanner/' + adress,
                        'bubblemaps_link': 'https://app.bubblemaps.io/sol/token/' + adress,
                        'rugcheck_link': 'https://rugcheck.xyz/tokens/' + adress,
                        'mxmove': cal
                    }
                )
                
    except:
        pass
    print(f'Найдено {len(data)} токенов с учётом скрытого фильтра')
    return adresses, data


def solscan_data(adresses):
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled");
    driver = uc.Chrome(headless=False,use_subprocess=False)
    driver.maximize_window()
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    output_folder = os.path.join(base_path, 'solscans')
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i in adresses:
        driver.get(url=f'https://solscan.io/token/{i}#holders')
        if adresses.index(i) == 0:
            time.sleep(8)
            pyautogui.moveTo(537, 416)
        pyautogui.click()

        time.sleep(8)

        file_path = os.path.join(output_folder, f'{i}.html')
        with open(file_path, 'w') as file:
            file.write(driver.page_source)
        print(f'{i} записан')
        

    driver.close()
    driver.quit()


def solscan_process(adresses, data):
    new_data = []
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Формируем универсальный путь к директории с HTML-файлами
    files_dir = os.path.join(base_path, 'solscans')

        
    for i in adresses:
        file_path = os.path.join(files_dir, f'{i}.html')
        try:
            with open(file_path) as file:
                src = file.read()
            soup = BeautifulSoup(src, 'lxml')
            taglist = []
            if soup.find('div', class_='justify-center rounded-full border px-2.5 py-0.5 transition-colors flex-nowrap w-max bg-neutral0 border-neutral2 font-bold h-[20px] text-[10px] leading-[20px] flex gap-1 items-center'):
                tags = soup.find_all('div', class_='justify-center rounded-full border px-2.5 py-0.5 transition-colors flex-nowrap w-max bg-neutral0 border-neutral2 font-bold h-[20px] text-[10px] leading-[20px] flex gap-1 items-center')
                for tag in tags:
                    taglist.append(tag.text)
                if 'pump' in i:
                    taglist.append('Pump.Fun')
            
            procentholders = 0
            trs = soup.find_all('tr', class_='transition-colors hover:bg-neutral1 data-[state=selected]:bg-muted bg-neutral0')
            for numb in trs:
                curse = numb.find_all('td', class_='h-12 px-2 py-[10px] align-middle text-[14px] leading-[24px] font-normal text-neutral7 [&:has([role=checkbox])]:pr-0 border-b first:pl-4 last:pr-4')[4].text
                curse = float(curse.replace('%', '').replace(' ', '').replace(',', '.'))
                procentholders += curse
            procentholders = str(int(round(procentholders, 0))) + '%'


            i = adresses.index(i)
            new_data.append({
                'token_name': data[i]['token_name'],
                'short_name': data[i]['short_name'],
                'link': data[i]['link'],
                'token_adress': data[i]['token_adress'],
                'solsniffer_link': data[i]['solsniffer_link'],
                'bubblemaps_link': data[i]['bubblemaps_link'],
                'rugcheck_link': data[i]['rugcheck_link'],
                'mxmove': data[i]['mxmove'],
                'top10holders%': procentholders,
                'tags': taglist
            })
        except:
            break
    return new_data





url = choice()
dexscreener_data(url)
adresses, data = dexdata_process()
solscan_data(adresses)
new_data = solscan_process(adresses, data)
base_path = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(base_path, 'data.json')
with open(json_file_path, "a") as file:
    json.dump(new_data, file, indent=4, ensure_ascii=False)

