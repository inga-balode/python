# для одного аргумента

def type_logger(func):
    def logger(*args, **kwargs):
        log = type(*args, **kwargs)
        print(f'{str(*args, **kwargs)}: {log}')
    return logger




@type_logger
def calc_cube(x):
   return x ** 3


calc_cube(5)

# если несколько аргументов


def type_loggers(func):
    def loggers(*args, **kwargs):
        result = []
        for i in args:
            log = type(i)
            result.append(f'{str(i)}: {log}')
        return result
    return loggers



@type_loggers
def calc_cubes(*args):
    result = []
    for i in args:
        result.append(i ** 3)

print(calc_cubes(5, 6, 7))