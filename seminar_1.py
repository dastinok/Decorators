'''Создайте функцию-замыкание, которая запрашивает два целых
числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит
угадать загаданное число за указанное число попыток. '''

import random




def count(num: int = 1):
    def deco(func):
        def wrapper(*args, **kwargs):
            result = random.randint(0, 100)
            #print(result)
            for _ in range(num):
                if result > func(*args, **kwargs):
                    print('Введите число больше')
                elif result < func(*args, **kwargs):
                    print('Введите число меньше')

                else:
                    print('Yes')
                    break

            return result

        return wrapper

    return deco

@count(10)
def guess():
    my_guess = int(input('Введите число до 100: '))
    return my_guess

print(guess())