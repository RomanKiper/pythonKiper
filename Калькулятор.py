# задание № 2
# калькулятор
# Созайте класс, где реализованы функции (методы) математических операций. А также функция для ввода данных.


class Calculator():
    def __init__(self):
        self.func4()

    def add(self):
        return self.a + self.b

    def substract(self):
        return self.a - self.b

    def myltiply(self):
        return self.a * self.b

    def devide(self):
        if self.b == 0:
            return 'error'
        else:
            return self.a / self.b
    def func4(self):
        self.a = int(input())
        self.b = int(input())

while True:
    print('пробел -  прерывание программы. Введите - +,-,*,/')
    x = input()
    if x == ' ':
        break
    print('Введите значения:')
    calculator = Calculator()
    if x == '+':
        print(calculator.add())
    if x == '-':
        print(calculator.substract())
    if x == '*':
        print(calculator.myltiply())
    if x == '/':
        print(calculator.devide())




