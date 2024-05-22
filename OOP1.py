

class MeansOFTransport:
    def __init__(self, calor, brand):
        self.calor = calor
        self.brand = brand
        
    def show_color(self):
        print(f'color: {self.calor}')
        
    def show_brand(self):
        print(f'brand: {self.brand}')
        

    def __setattr__(self, key, value):
        if key == 'qwerty' or value == 123:
            raise AttributeError('qwerty не допускается')
        else:
            return object.__setattr__(self, key, value)
        
    def __getattr__(self, item):
        return False
class Car(MeansOFTransport):
    _car1 = ('Blue', 'lada', 4)
    __car2 = ('Black', 'porsche', 4)
    car_drive = 4
    
    def __str__(self):
        print('66666')
        return f'{self.calor} {self.brand} {self.wheels}'
    
    def __repr__(self):
        return f'Car({self.calor}, {self.brand}, {self.wheels})'
    
    def __len__(self):
        return str(self.wheels)
    
    def __getitem__(self, index):
        if index == 0:
            return self.calor
        elif index == 1:
            return self.brand
        elif index == 2:
            return self.wheels
        else:
            raise IndexError('Индекс вне диапазона')
        

    
    @staticmethod
    def Conclusion(car_drive):
        return car_drive
    
    def __init__(self, calor, brand, wheels):
        self.wheels = wheels
        super().__init__(calor, brand)
        
    def __delattr__(self, item):
        print(f'Удаление {item}')
        return super().__delattr__(item)


class Moped(MeansOFTransport):
    def __init__(self, calor, brand, wheels):
        self.wheels = wheels
        super().__init__(calor, brand)
    @staticmethod
    def calculate_time(distance, speed_Max):
        return distance / speed_Max


print(Moped.calculate_time(100, 20))
ts = MeansOFTransport('red', 'BMW')
ts.qwert = 12
ts.z = 5
car = Car('red', 'BMW', 4)
print(ts.calor, ts.brand, ts.qwe)
print(Car._car1)
print(Car.car_drive)
print(Car.Conclusion(6))
print(Car.car_drive)
print(str(car))
print(repr(car))
print(len(car.calor))
print(car[0])
print(car[2])
# del car.calor