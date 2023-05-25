
class Test:
    a = 'a'
    
    def __init__(self, b):
        self.b = b
    def f1(self):
        return self.a, self.b
    
    @classmethod #имеет доступ к ограниченному к-ву элементов класса
    def f2(cls):
        return cls.a
    @staticmethod #не имеет доступа к объектам класса
    def f3():
        return '...'
    
t = Test('b')
print(t.a, t.b, t.f1(), t.f2(), t.f3(), sep=';') #Для экземпляра
print(Test.a, Test.f2(), Test.f3(), sep=';') #Для класса
print(Test.f3()) #Статическому методу
