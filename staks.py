# def third_digit(n):
#     n_int = list(str(n))
#     if len(n_int) < 3:
#         return "число должно содержать не меньше 3 чисел"
#     return n_int[2]
#
#
# n = int(input())
# print(third_digit(n))

# def weight(n):
#     if n < 60:
#         return 'Лёгкий вес'
#     elif n <= 64:
#         return 'Первый полусредний вес'
#     elif n <= 69:
#         return 'Полусредний вес'
#     else:
#         return 'Вес выше полусреднего'
#
# n = int(input())
# print(weight(n))

class Phonenumber:
    def __init__(self, number, fio):
        self.number = number
        self.fio = fio


class PhoneBook:
    def __init__(self):
        self.book = {}
    
    def add_phone(self, Phonenumber):
        self.book[Phonenumber.number] = Phonenumber.fio
    
    def get_phone_list(self):
        return self.book
    
    def remove_phone(self, indx):
        del self.book[indx]
    
    
p = PhoneBook()
p.add_phone(Phonenumber(12345678901, "Сергей Балакирев"))
p.add_phone(Phonenumber(21345678901, "Панда"))
phones = p.get_phone_list()
print(phones)
