
class Test:
    a = 'a'
    _b = '_b' #protected
    __c = '__c' #private
    
    def get_c(self):
        return self.__c
    
    def set_c(self, v):
        if isinstance(v, str):
            self.__c = v
        else:
            raise ValueError
    

t = Test()
t.a = 3
t.set_c('3')
print(t.a, t._b, t.get_c())


