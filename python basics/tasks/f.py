# Дана строка s, найти индекс первого уникального символа

def find_unique(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    for i, char in enumerate(s):
        if count[char] == 1:
            return i

    return -1


a = 'gasdfc'
b = 'loveleetcode'

print(find_unique(a))
print(find_unique(b))
