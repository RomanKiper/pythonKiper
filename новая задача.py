# написать функцию которая генерирует пароли
import random
import string
def password_generator():
    numbers = string.ascii_letters
    digits = string.digits
    all = list(numbers+digits)
    numbers = random.randint(1,20)
    random.shuffle(all)
    return ''.j(str(all[:numbers]))
    print(numbers, digits)
