# Кейс-задача № 2
# Написать тестовую программу, которая демонстрирует работу методов базового и производного классов.
# Ответом на задачу будет ссылка на репозиторий GitHub, где хранится Ваша программа. Или иным удобным для Вас способом.

# Создадим базовый класс
class Base:

    def __init__(self):
        self.base_attribute = 'Базовый аттрибут'

    def base_method(self):
        print(f'Этот метод демонстрирует работу базового класса: {self.base_attribute}')

# Создадим производный класс
class Derivative(Base):

    def __init__(self):
        super().__init__()
        self.derivative_attribute = 'Производный аттрибут'

    def derivative_method(self):
        print(f'Этот метод демонстрирует работу производного класса: {self.derivative_attribute}')

# Создадим инстанс производного
d = Derivative()

# Демонстрация работы методов
d.base_method()
d.derivative_method()
