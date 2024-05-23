
class Special_cls:
    num_int = 0
    registerLastCallers_cache = dict()
    registerCallers_list = list()

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('Inside the __call__')
        type(self).num_int += 1
        type(self).registerLastCallers_cache[self.func.__name__] = [*args]
        type(self).registerCallers_list.append( f'{self.func.__name__} : {args}' )
        self.func(*args, **kwargs)

@Special_cls
def doSomething_fn(name_sz, age_int):
    print(f'This is my {name_sz}')


class Decorator:
    @staticmethod
    def dec(func):
        def wrapper(*args, **kwargs):
            print('inside Decorator')
            func(*args, **kwargs)
        return wrapper
        
@Decorator.dec
def simple():
    print('I am simple')

if __name__ == '__main__':
    doSomething_fn('peter', 12)
    doSomething_fn('john', 23)
    doSomething_fn('andy', 45)
    print(Special_cls.num_int)
    print(Special_cls.registerLastCallers_cache)
    print(Special_cls.registerCallers_list)



simple()