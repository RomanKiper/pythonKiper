# задание № 2, калькулятор
# Созайте класс, где реализованы функции (методы) математических операций.
# А также функция для ввода данных.


class Calculator():
    def __init__(vnutri): # __init__ всегда отрабатывает при создании объекта
        vnutri.func4()

    # Все остальны функции отрабатывают только по вызову
    def add(self):
        return self.a + self.b

    def substract(self):
        return self.a - self.b

    def myltiply(self):
        return self.a * self.b

    def devide(vnut):
        if vnut.b == 0:
            return 'error'
        else:
            return vnut.a / vnut.b

    def func4(self):
        self.a = int(input('Введите первое значение:'))
        self.b = int(input('Введите второе значение:'))


while True:
    x = input('пробел - прерывание программы. Введите: +,-,*,/  \n')
    if x == ' ':
        break
    # print('Введите значения:')

    calculator = Calculator()  # Тут идет создание объекта calculator на основании класса Calculator()

    if x == '+':
        otvet = calculator.add() # Вызов функций (метода) класса
    if x == '-':
        otvet = calculator.substract()
    if x == '*':
        otvet = calculator.myltiply()
    if x == '/':
        otvet = calculator.devide()

    print('Результат: ', otvet)