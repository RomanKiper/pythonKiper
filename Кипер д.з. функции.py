import random
import turtle
# написать функцию которая принимает число, возвращает его значение умноженное на 2

# def number_multiplied(n):
#     n = n * 2
#     return n
#
# print(number_multiplied(8))


#  написать функцию которая определяет параметр на четность. Если четное чило, то принтим Yes
#если нет то принтим NO

# def even_odd(n):
#     if n %2 == 0:
#         return("Yes")
#     else:
#         return("NO")
#
# print(even_odd(8))
# print(even_odd(9))

# пишем функцию принимающую 2 аргумента.После чего проверим если первое число больше 10 принтим ДА, если меньше НЕТ

# def two_arguments(a, b):
#     if a > 10:
#         return ("ДА")
#     else:
#         return ("НЕТ")
# print(two_arguments(5,8))
# print(two_arguments(12,8))

# создадим пустую функцию которая ничего не возвращает

# def empty_function():
#     pass

#Сдалать так, чтобы случайным образом рисовало многоуголькики от 3 до 10 углов например.

def draw_square(side):
    n = random.randint(3,10)
    for i in range(n):
        t.forward(side)
        a = 180 -((n - 2) * 180 / n)
        t.left(a)

def replace(x, y):
    t.up()
    t.goto(x, y)
    t.down()

t = turtle.Pen()
t.width(5)
colors = ['pink','red','blue', 'green', 'yellow','gray', 'black']
for i in range(10):
    t.color(random.choice(colors))
    x_cor = random.randint(-200, 200)
    y_cor = random.randint(-200, 200)
    replace(x_cor, y_cor)
    draw_square(random.randint(10, 100))

turtle.mainloop()

