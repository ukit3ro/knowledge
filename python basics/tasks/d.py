#Дан список целых чисел nums и
# число target, вернуть индексы двух чисел списка,
# которые в сумме дают число target.


def find_sum(nums, target):
    index = {}
    for i, num in enumerate(nums):
        index[num] = i

    for i, num in enumerate(nums):
        find = target - num
        if find in index and index[find] != 1:
            return [i, index[find]]


print(find_sum(nums=[2,7,11,15], target=9))
