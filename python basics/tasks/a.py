#Дан список целых чисел nums, вернуть
#True, если хоть одно число в списке встречается
# как минимум два раза, иначе вернуть False.

def check_double(nums):
    return len(set(nums)) < len(nums)

n = [1,2,3,4,5, 1]
print(check_double(n))
