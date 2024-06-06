# class Calculator:
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def sum(a, b):
#         return a + b
#
#
# class Calculator2(Calculator):
#
#     @staticmethod
#     def summa_str(a, b):
#         return str(a) + str(b)
#
#
# cl = Calculator()
# print(cl.sum(1, 2))
# cl2 = Calculator2()
# print(cl2.summa_str('qwe', '2'))

from abc import abstractmethod


class Animals:

    @abstractmethod
    def __init__(self):
        pass


class Cat(Animals):
    def __init__(self):
        pass

    @staticmethod
    def voice():
        print('муррр')


ct = Cat()
print(ct.voice())

cl = Animals
