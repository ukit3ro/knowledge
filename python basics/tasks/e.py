#напишите функцию, которая переворачивает строку

def reverse(s):
    L = len(s)
    for i in range(L // 2):
        s[i], s[L-1-i] = s[L-1-i], s[i]

    return s

a = ['H', 'e', 'l', 'l', 'o']

print(reverse(a))
