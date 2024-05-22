
# class Vector:
#     Min_coord = 0
#     Max_coord = 100
#
#     @classmethod
#     def validate(cls, arg):
#         return cls.Min_coord <= arg <= cls.Max_coord
#
#     def __init__(self, x = 0, y = 0):
#         self.x = self.y = 0
#         if self.validate(x) and self.validate(y):
#             self.x = x
#             self.y = y
#         print(self.norm2(self.x, self.y))
#
#     def get_coords(self):
#         return self.x, self.y
#
#     @staticmethod
#     def norm2(x, y):
#         return x*x + y*y
# v = Vector(10, 20)
# print(Vector.norm2(5, 6))






# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#     def __len__(self):
#         return len(self.__coords)
#     def __abs__(self):
#         return list(map(abs, self.__coords))
#
#
# p = Point(1, 2, -8)
# print(len(p))
# print(abs(p))

class Clock:
    __DAY = 86400  # число секунд в 1 дне!
    def __init__(self, seconds = int):
        if not isinstance(seconds, int):
            raise TypeError('Секунды должны быть целым числом!')
        self.seconds = seconds % self.__DAY
        
    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"
    
    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, '0')
    
    def __mul__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('int')
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        
        return Clock(self.seconds * sc)
    
    
        
    
    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError('int')
        sc = other
        if isinstance(other, Clock):
            sc = other.seconds
        
        return Clock(self.seconds + sc)
    
    def __radd__(self, other):
        return self + other
    
c1 = Clock(1000)
c2 = Clock(2005)
c3 = c2 * 36

print(c3.get_time())
