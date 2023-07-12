'''Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами
из диапазонов.'''
import random
from typing import Callable
from random import randint

def outer(func) -> Callable:
    #def wrapper(number: int, attemps: int):
    #    if 0 < number < 101 and attemps
    #        result = func(number, attemps)
#
    #    return result
    def wrapper(guess: int, attemps: int):
        guess = guess if 1 < guess < 100 else random.randint(1,100)
        attemps = attemps if 1 < attemps < 10 else random.randint(1,10)
        return func(guess, attemps)
    return wrapper

@outer

def get_game(num_sc, attemps) -> None:
    while attemps:
        print(f'осталось попыток {attemps}', end=' ')
        attemps -= 1
        num = int(input('Введите число: '))
        if num == num_sc:
            print(f'Число угадано - {num}')
            break
        else:
            advice = ['меньше', 'больше']
            print(f'Ваше число {advice[num>num_sc]} больше')
    else:
        print(f'Вы проиграли. Число было {num_sc}')




#@outer()
#def main():
#    game = outer()
#    game()
if __name__ == '__main__':
    get_game(200,300)
