'''
1. Написать декоратор для логирования типов позиционных аргументов функции
2. если аргументов несколько - выводить данные о каждом через запятую
3. можете ли вы вывести тип значения функции?
4. Сможете ли решить задачу для именованных аргументов?
5. Сможете ли вы замаскировать работу декоратора?
6. Сможете ли вывести имя функции
'''
from functools import wraps


def type_loger1_2(func):
    def wrapper(*args, **kwargs):
        x = ', '.join(f'{num}: {type(num)}' for num in args)
        print(x)
        res = func(*args, **kwargs)
        return res
    return wrapper

def type_loger3(func):
    def wrapper(*args, **kwargs):
        res = func(*args)
        return res, type(res)
    return wrapper

def type_loger4(func):
    def wrapper(**kwargs):
        print(*kwargs.values(), type(*kwargs.values()))
        res = func(*kwargs.values())
        return res
    return wrapper


def type_loger5(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        x = ', '.join(f'{num}: {type(num)}' for num in args)
        print(x)
        res = func(*args, **kwargs)
        return res
    return wrapper


def type_loger6(func):
    def wrapper(*args, **kwargs):
        if args:
            x = ', '.join(f'{num}: {type(num)}' for num in args)
        else:
            x = ', '.join(f'{num}: {type(num)}' for num in kwargs.values())
        print(f'{func.__name__}({x})')
        res = func(*args, **kwargs)
        return res
    return wrapper

@type_loger6
def calc_cube(*args, **kwargs):
    if args:
        return [num ** 3 for num in args]
    else:
        return [num ** 3 for num in kwargs.values()]


print(*calc_cube(qwe=5, two=2))
