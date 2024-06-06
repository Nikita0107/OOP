import logging

# Настройка журнала записи в log
logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")


class Class:
    """
    Напишите класс, содержит 3 любые атрибута и при изменении логгировать всё в консоль (при изменении старое->новое)
    """
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    # Получает текущее значение getattr(self, name, None). Если атрибута нет, то возвращается None.
    # родительский метод __setattr__ с помощью super()
    # __setattr__(name, value),  который отвечает за сохранение.
   
    def __setattr__(self, name, value):
        old_value = getattr(self, name, None)
        super().__setattr__(name, value)
        if old_value != value:
            logging.info(f"{name} изменилось с {old_value} на {value}")


cl = Class(5, 8, 7)
cl.b = 99
print(f"a = {cl.a}, b = {cl.b}, c = {cl.c}")
