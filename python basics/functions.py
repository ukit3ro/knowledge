#Функция - обособленный участок кода, который можно вызвать несколько раз, обративщись к нему по имени
def name_func(args):
    pass

#рекурсивная функция - функция, вызывающая сама себя и обрабатывающая полученный результат
#до тех пор, пока не достигнет терминального условия
def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n-1) #условие заверщения

#поиск самого большого элемента в массиве
a = [3, 2, 5, 6, 1]

def custom_max(a):
    if len(a) == 1:
        return a[0]

    first_elem = a[0]
    tail = a[1:]
    tail_max = custom_max(tail)

    if first_elem > tail_max:
        return first_elem
    else:
        return tail_max

print(custom_max(a))

#подсчёт суммы цифр в числе
n = 14132

def sum_digit(n):
    if n == 0:
        return 0

    last_digit = n % 10
    tail = n // 10
    tail_sum = sum_digit(tail)

    return last_digit + tail_sum

print(sum_digit(n))
