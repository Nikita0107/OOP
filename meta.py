# class Point:
#     MAX_cord = 100
#     MIN_cord = 0

# def meta_class_tore(name, bases, attr):
#     attr.update({'MAX_cord': 100, 'MIN_cord': 0})
#     return type(name, bases, attr)

class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs.update({'max_cords': 100, 'min_cords': 0})
        return type.__new__(cls, name, bases, attrs)
        
    # def __init__(cls, name, bases, attrs):
    #     super().__init__(name, bases, attrs)
    #     cls.max_cords = 100
    #     cls.min_cords = 0
        

class Point(metaclass=Meta):
    def  get_coords(self):
        return (0, 0)

pt = Point()
print(pt.min_cords)
print(pt.get_coords())
