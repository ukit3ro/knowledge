# Алгоритм работы метода зависит от типа объекта(исходных условий), к которому он применяется

class Payment:
    _balance = 100

    def pay(self):
        ...


class CardPayment(Payment):
    def pay(self, price):
        self._balance -= price
        return 'Check' + str(price)


class CashPayment(Payment):
    def pay(self, price):
        change = self._balance - price
        return 'Check' + str(price), change


p1 = CardPayment()
print(p1.pay(30))
p2 = CashPayment()
print(p2.pay(40))
