# Дан список целых чисел nums, каждый элемент
# списка встречается дважды,
# за исключением одного элемента. Найдите этот элемент.

def find_exception(nums):
    temp = 0
    for num in nums:
        temp = temp ^ num

    return temp


print(find_exception([1, 2, 2, 3, 7, 1]))
