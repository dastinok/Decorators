'''Создайте декоратор с параметром.
Параметр - целое число, количество запусков декорируемой
функции.'''
'''Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.'''
import json
import os
import random
from typing import Callable

def counter(number):
    def dec(func):
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(number):
                result.append(func(*args, **kwargs))
            return tuple(result)

        return wrapper
    return dec

def cheker(func) -> Callable:

    def wrapper(guess: int, attemps: int):
        guess = guess if 1 < guess < 100 else random.randint(1,100)
        attemps = attemps if 1 < attemps < 10 else random.randint(1,10)
        return func(guess, attemps)
    return wrapper

def writer(file_name):
    def inner_func(func):
        def wrapper(number, tries):
            my_dict = {str(func(number, tries)): (number, tries)}

            if os.path.exists(file_name):
                with open(file_name, 'a', encoding='utf-8') as f:
                    json.dump(my_dict, f, ensure_ascii=False, indent=4)
            else:
                with open(file_name, 'w', encoding='utf-8') as f:
                    json.dump(my_dict, f, ensure_ascii=False, indent=4)
            return func(number, tries)

        return wrapper


    return inner_func






@writer('guess.json')
@cheker
@counter(3)

def get_game(num_sc, attemps):
    result_attemps = 1
    while attemps:
        print(f'осталось попыток {attemps}', end=' ')
        attemps -= 1
        num = int(input('Введите число: '))
        if num == num_sc:
            print(f'Число угадано - {num}')
            return result_attemps
        else:
            advice = ['меньше', 'больше']
            print(f'Ваше число {advice[num>num_sc]} больше')
            result_attemps += 1
    else:
        print(f'Вы проиграли. Число было {num_sc}')

    return result_attemps

get_game(10,590)