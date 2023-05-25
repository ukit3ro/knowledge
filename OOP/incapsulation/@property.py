#Использует методы как свойства объектов. Свойства позволяют обращаться с методами также, как и с атрибутами
#По сути, позволяет систематизировать код и задать ему определённые свойства

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    
    @property
    def full_name(self):
        return self.name  + ' ' + self.surname
    

tom = Person('Tomas', 'Smith')
print(tom.full_name)

#Пример с классом Test из data_protection.py
class Test:
    a = 'a'
    _b = '_b' #protected
    __c = '__c' #private
    
    @property
    def c(self):
        return self.__c
    @c.setter
    def c(self, v):
        if isinstance(v, str):
            self.__c = v
        else:
            raise ValueError
    
    
t = Test()
t.a = 3
t.c = '3'
print(t.c)