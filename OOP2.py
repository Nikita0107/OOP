# class Calculator:
#     def __init__(self):
#         pass
#     def sum(self, a, b):
#         return a + b
#
# class Calculator2(Calculator):
#     def summa_str(self, a, b):
#         return str(a) + str(b)
#
#
# cl = Calculator()
# print(cl.sum(1, 2))
# cl2 = Calculator2()
# print(cl2.summa_str('qwe', '2'))

from abc import ABC, abstractmethod
class Animals:
    @abstractmethod
    def __init__(self):
        pass
class Cat(Animals):
    def __init__(self):
        pass
    
    def voice(self):
        print('муррр')

ct = Cat()
print(ct.voice())


    
    
