
class People:
    """
    Напишите класс, который принимает список людей с интерфейсом добавления новых и при итерации возвращал имена людей.
    """
    def __init__(self, name):
        self.name = name
        self.people_list = []
    def add_person(self, name):
        self.people_list.append(name)
        return self.people_list

    def __iter__(self):
        return iter(self.people_list)

    def __next__(self):
        return next(self.people_list)


people = People("People List")

people.add_person("Lena")
people.add_person("Masha")
people.add_person("Dasha")

#  Метод extend() в Python позволяет добавить новые элементы в конец списка.
people.people_list.extend(["Katya", "Sergey", "Olya"])

for person in people:
    print(person)
#  Метод join() в Python используется для объединения списка строк в одну
#  строку с использованием указанного разделителя.
people_string = ', '.join(people)
print(people_string)
print(People.__doc__)
print(people.people_list)
