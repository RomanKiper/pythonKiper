# написать функцию которая генерирует пароли
import random
import string


def password_generator():
    numbers = string.ascii_letters
    digits = string.digits
    all = list(numbers + digits)
    numbers = random.randint(1, 20)
    print(all)
    random.shuffle(all) # Перемешивает весь список
    print(all)
    lst = all[:numbers] # Берем первые n элементов для пароля
    print(lst)
    password = ''.join(lst) # Объединяем список в строку
    return password


paroli = password_generator()
print(paroli)