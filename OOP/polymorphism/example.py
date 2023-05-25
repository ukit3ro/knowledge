#Алгоритм работы метода зависит от типа объекта(исходных условий), к которому он применяется

class Payment:
    _balance = 100
    
    def pay(self):
        ...
        
class Card_payment(Payment):
    def pay(self, price):
        self._balance -= price
        return 'Check' + str(price)
    
class Cash_payment(Payment):
    def pay(self, price):
        change = self._balance - price
        return 'Check' + str(price), change
    
p1 = Card_payment()
print(p1.pay(30))
p2 = Cash_payment()
print(p2.pay(40))