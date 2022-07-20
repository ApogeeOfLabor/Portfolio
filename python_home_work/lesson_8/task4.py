from functools import wraps


def val_checker(_callback):
    def decor(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if _callback(*args):
                res = func(*args, **kwargs)
                return res
            else:
                raise ValueError(f'ValueError {args[0]}')
        return wrapper
    return decor


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


print(calc_cube(10), calc_cube.__name__)
