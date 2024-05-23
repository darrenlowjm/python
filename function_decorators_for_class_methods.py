
#
# this decorator is defines outside of class
#
def decorator_outside(func):
    def wrapper(*args, **kwargs):
        print('Using the outside decorator')
        func(*args, **kwargs)
    return wrapper


class something_cls:
    def __init__(self):
        pass
    #
    # this decorator is defined within a class to be used within the class
    #
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('Within the class function decorator of class!')
            func(*args, **kwargs)
        return wrapper


    @decorator_outside
    def do_smethg_mtd(self):
        print(f'I am the do_smething_mtd in class:{__class__.__name__}')

obj = something_cls()
obj.do_smethg_mtd()



