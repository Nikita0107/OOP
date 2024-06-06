class Singleton:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)
        return cls.__instance


class Dog(Singleton):
    def __init__(self, age, name):
        self.age = age
        self.name = name
    
    def __setattr__(self, key, value):
        return object.__setattr__(self, key, value)
    
    def __getattribute__(self, item):
        return object.__getattribute__(self, item)
    
    def __getattr__(self, item):
        return False
    
    def get_age(self):
        return self.age
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name_new):
        self.__name = name_new
    
    @name.deleter
    def name(self):
        del self.__name
    
    @staticmethod
    def voice():
        print("Гав-гав!")


'''Пример'''
dog1 = Dog(2, 'Барсик')
dog2 = Dog(3, 'Соня')

'''Проверяем совпадение'''
print(dog1 is dog2)
# print((lambda a, b: a if a > b else b)(8, 9))
# print((lambda x, y: x + y)(8, 7))
dg = Dog(5, 'Барсик')
# del dg.name
dg.name = 'juja'
dg.age = 7
dg.old = 5
print(dg.__dict__)
del dg.old
print(dg.__dict__)
print(Dog.name.__dir__())
print(Dog.__mro__)