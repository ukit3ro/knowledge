#Напишите функцию, которая ищет
#cамый длинный общий префикс для строк из данного списка.

def find_pref(strs):
    L = min(map(len, strs))
    ans = ""
    for i in range(L+1):
        pref = strs[0][:i]
        flag = True
        for s in strs:
            if s[:i] != pref:
                flag = False
        if flag:
            ans = pref
        else:
            break
    return ans


print(find_pref(['flower', 'flow', 'flight']))
