#Дан список целых чисел prices, где prices[i] -
#цена акции в i-й день. Рассчитайте максимальную выгоду, которую можно получить.

def max_marge(prices):
    ans = 0
    for i in range(len(prices)-1):
        diff = prices[i+1] - prices[i]
        if diff > 0:
            ans += diff
    return ans


print(max_marge([7,6,3,1,5]))