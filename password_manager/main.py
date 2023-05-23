import json
import string
import random

symbols = string.ascii_letters + string.digits + "!_"
g = 'aiuoe'
s = "znkjdvgbwlsftqhpmryxc"

def load_db(filename):
    with open(filename) as file:
        db = json.load(file)
    return db
        

def save_db(filename, db):
    with open(filename, 'w') as file:
        json.dump(db, file, indent=2)
        
        

def add_pass(db):
    site = input(" Введите название сайта: ")
    login = input(" Введите свой логин: ")
    password = input(" Введите пароль: ")
    
    db.append({
        "login": login,
        "password": password,
        "site": site
    })
    
def change(subject, prev):
    t = input(f" Введите {subject} ({prev}): ")
    if t == "":
        return prev
    else:
        return t

def change_pass(info):
    info["site"] = change("Название сайта", info["site"])
    info["login"] = change("Логин", info["login"])
    info["password"] = change("Пароль", info["password"])


def compare(s1, s2):
    s1_set = set(s1)
    s2_set = set(s2)
    
    inter = s1_set.intersection(s2_set)
    return len(inter) > 0


def gen_pass(L):
    while True:
        res = ""
        for i in range(L):
            res += random.choice(symbols)
            
        bools = [
            compare(res, string.ascii_lowercase),
            compare(res, string.ascii_uppercase),
            compare(res, string.digits),
            compare(res, "!_"),
            res[0] not in string.ascii_uppercase           
            
        ]
            
        if all(bools):
            return res

def gen_easy_pass(L):
    res = ""
    for i in range(L-3):
        if i % 2 == 0:
            res += random.choice(s)
        else:
            res += random.choice(g)
            
    for i in range(3):
        res += random.choice(string.digits)
        
    return res


def add_and_gen(db):
    site = input(" Введите название сайта: ")
    login = input(" Введите свой логин: ")
    L = int(input(" Введите длину пароля: "))
    t = input("Генерировать сложный пароль (y/n)? ")
    if "y" in t.lower():
        password = gen_pass(L)
    else:
        password = gen_easy_pass(L)
    
    db.append({
        "login": login,
        "password": password,
        "site": site
    })


def show(info, num):
    print(f"{num:3} | {info['site']} | {info['login']} | {info['password']}")
    
def search(db):
    site = input(" Введите название сайта: ")
    results = []
    for info in db:
        if site in info["site"]:
            results.append(info)
            
    for num, info in enumerate(results):
        show(info, num)
    
    m = pass_mode()
    if m == 2:
        num = int(input("Введите номер:"))
        db.remove(results[num])
    elif m == 3:
        num = int(input("Введите номер:"))
        info = results[num]
        change_pass(info)
            

def pass_mode():
    print('Список ваших действий:')
    print('1. Выйти из поиска ')
    print('2. Удалить пароль ')
    print('3. Изменить пароль')
    return int(input('Выберите номер нужного действия: '))

def check(db):
    cnt = {}
    for info in db:
        if info['password'] in cnt:
            cnt[info['password']] += 1
        else:
            cnt[info['password']] = 1
            
    for password, num in cnt.items():
        if num > 1:
            print(f' Пароль "{password}" не безопасен! Он используется на сайтах:')
            for info in db:
                if info['password'] == password:
                    print(f"Сайт: {info['site']:15}, Логин: {info['login']:15}")


def mode():
    print()
    print('-'*30)
    print('Список доступных действий: ')
    print('1. Добавить пароль')
    print('2. Сгенерировать пароль')
    print('3. Найти пароль')
    print('4. Найти уязвимости')
    print('5. Выйти из программы')
    print("-"*30)
    print()
    return int(input('Выберите номер нужного действия: '))
        
    
def loop(filename):
    db = load_db(filename)
    
    while True:
        m = mode()
        
        if m == 1:
            add_pass(db)
        elif m == 2:
            add_and_gen(db)
        elif m == 3:
            search(db)
        elif m == 4:
            check(db)
        elif m == 5:
            break
        else:
            print('Нет такого режима')
    save_db(filename, db)
    
loop('user.json')
    
    