# class Clock:
#     __DAY = 86400  # число секунд в 1 дне!
#     def __init__(self, seconds: int):
#         if not isinstance(seconds, int):
#             raise TypeError('Секунды должны быть целым числом!')
#         self.seconds = seconds % self.__DAY
#     @classmethod
#     def __veri_date(cls, other):
#         if not isinstance(other, (int, Clock)):
#             raise TypeError('Объект должен быть класса Clock! или int!')
#         return other if isinstance(other, int) else other.seconds
#
#     def __eq__(self, other):
#         sc = self.__veri_date(other)
#         return self.seconds == sc
#
#     def __lt__(self, other):
#         sc = self.__veri_date(other)
#         return self.seconds < sc
#
#     def __le__(self, other):
#         sc = self.__veri_date(other)
#         return self.seconds <= sc
#
# c1 = Clock(1000)
# c2 = Clock(2000)
# print(c1 >= c2)
class FRange:
    def __init__(self, start=0.0, stop=0.0, step=1.0):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        self.value = self.start - self.step
        return self
       
    def __next__(self):
        if self.value + self.step < self.stop:
            self.value += self.step
            return self.value
        else:
            raise StopIteration('bla bla')
  
class FRange2d:
    def __init__(self, start=0.0, stop=0.0, step=1.0, rows=5):
        self.rows = rows
        self.fr = FRange(start, stop, step)
        
    def __iter__(self):
        self.valur = 0
        return self
    
    def __next__(self):
        if self.valur < self.rows:
            self.valur += 1
            return iter(self.fr)
        else:
           raise StopIteration('Stoop')
            
    
fr = FRange2d(0,2,0.5, 4)
for row in fr:
    for x in row:
        print(x, end=' ')
    print()
    
    
    
    