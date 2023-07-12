from math import sqrt

def get_quadratic(func):
    def wrapper(a, b, c):

        if a == 0:
            return 'Не квадратное уравнение'


        D = b ** 2 - 4 * a * c


        if D < 0:
            return 'Корней нет'
        elif D == 0:
            x = -b / (2 * a)
            return f'Один корень: x = {x}'
        else:
            x1 = (-b + sqrt(D)) / (2 * a)
            x2 = (-b - sqrt(D)) / (2 * a)
            return f'Два корня: x1 = {x1}, x2 = {x2}'

    return wrapper

@get_quadratic
def result(a, b, c):
    pass


print(result(1,2,3))