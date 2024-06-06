class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dogs(Dog):
    def __init__(self, name, age, color, weight):
        self.color = color
        self.weight = weight
        super().__init__(name, age)
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        self._age = new_age
    
    def get_weight(self):
        return self.weight


d = Dogs('valera', 11, 'green', 25)
