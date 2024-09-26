list1 = [2, 4, 3]
list2 = [5, 6, 4]

""" test = '708'
print(list(test)) """
s1 = ''
for i in range(len(list1)):
    s1 = int(str(list1[i]) + str(s1))
s2 = ''
for i in range(len(list2)):
    s2 = int(str(list2[i]) + str(s2))
ans1 = list(str(s1 + s2))
ans2  = []
for i in ans1:
    ans2.append(int(i))
ans2 = ans2[::-1]
print(ans2)
    
    

