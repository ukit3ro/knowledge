import re
from bs4 import BeautifulSoup

with open("parcing/index.html") as file:
    src = file.read()
    
soup = BeautifulSoup(src, "lxml")

#title = soup.title
#print(title)
#print(title.text)

# .find() - находит и забирает данные из 1 попавшегося искомого элемента .find_all() - найдёт все подходящие и сохранит в список
#page_h1 = soup.find('h1')
#print(page_h1)

#page_all_h1 = soup.find_all('h1')
#print(page_all_h1)

#for item in page_all_h1:
#    print(item.text)

#возможно конкретизировать свой запрос, указав атрибут тега
#user_name = soup.find('div', class_='user__name')
#print(user_name.text.strip())

#можно и так:
#user_name = soup.find(class_='user__name').find('span').text

#если в коде будет два элемента с одинаковым классом, метод выведет первый попавшийся


#если нужны жесткие параметры отбора, можно указать доп атрибут поиска
#user_name = soup.find('div', {"class": "user__name", "id":"aaa"}).find('span').text

#find_all_spans_in_user_info = soup.find_all(class_="span")
#print(find_all_spans_in_user_info)

#for item in find_all_spans_in_user_info:
    #print(item.text)

#print(find_all_spans_in_user_info)


#парсинг ссылок
#social_links = soup.find(class_="social__networks").find("ul").find_all("a")
#print(social_links)

#другой способ забрать все ссылки со страницы

#all_a = soup.find_all("a")
#print(all_a)

#for item in all_a:
    #item_text = item.text
    #item_url = item.get('href')
    #print(f'{item_text}: {item_url}')
    
# .find_parent(), .find_parents()

#post_div = soup.find(class_="post__text").find_parent('div', 'user__post ')
#print(post_div) - поднимается до родителя элемента

""" post_divs = soup.find(class_='post__text'). find_parents('div', 'user__post')
print(post_divs) """

# .next_element, previous_element работают за счёт прохода снизу вверх и наоборт
#next_el = soup.find(class_ = 'post__title').next_element.next_element.text
#print(next_el)

#next_el = soup.find(class_='post__title').find_next().text
#print(next_el)


# .find_next_sibling() .find_previous_sibling() - ищут и возвращают следующие и предыдущие элементы внутри искомого тега
#next_sib = soup.find(class_='post__title').find_next_sibling()
#print(next_sib)

#post_title = soup.find(class_='post__date').find_previous_sibling().find_next().text
#print(post_title)

#Отбор атрибутов из тегов
""" links = soup.find(class_='some__links').find_all('a')
print(links)

for link in links:
    link_href_attr = link.get("href")
    link_href_attr1 = link["href"] #можно забирать атрибуты и вот так
    link_data_attr = link.get("data-attr")
    print(link_href_attr)
    print(link_data_attr) """



#поиск по тексту, используя метод регулярных выражений re

""" find_a_by_text = soup.find("a", text=re.compile("Одежда"))
print(find_a_by_text) """

find_all_clothes = soup.find_all(text=re.compile('[Оо]дежда'))
print(find_all_clothes)

