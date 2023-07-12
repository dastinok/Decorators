'''Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.'''
import json
import os.path
import random
from typing import Callable
from random import randint



def outer(file_name) -> Callable:

    def inner_func(func):
        def wrapper(*args, **kwargs):
            my_dict = {func(*args, **kwargs): [arg for arg in args] + [(key, value) for key,value in kwargs.items()]}

            if os.path.exists(file_name):
                with open(file_name, 'a', encoding='utf-8') as f:
                    json.dump(my_dict, f, ensure_ascii = False, indent=4)
            else:
                with open(file_name, 'a', encoding='utf-8') as f:
                    json.dump(my_dict, f, ensure_ascii = False, indent=4)
            return func(*args, **kwargs)
        return wrapper
    return inner_func

@outer('file.json')
def get_json(a,b,c) -> str:

    return a + b + c





if __name__ == '__main__':
    print(get_json(1,2,3))
    print(get_json(1, 2, c = 3))
    print(get_json(a = 1, b = 2, c = 3))
