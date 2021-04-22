from functools import wraps


def val_checker(validation):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            if validation(*args) == True:
                return func(*args)
            else:
                raise ValueError
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


print(calc_cube(5))
print(calc_cube(-5))
