# ================================================================
# ================================================================
class decorator_cls:
    def _pre(): return None
    def _post(): return None

    def __init__(self, func):
        self.func = func
        pass

    def set_decorator_pre(self, whatfn):
        # setattr( __class__, '_pre', getattr(__class__,whatfn) )
        __class__._pre = getattr(__class__, whatfn)

    def set_decorator_post(self, whatfn):
        # setattr( __class__, '_post', getattr(__class__,whatfn) )
        __class__._post = getattr(__class__, whatfn)

    def method1():
        print('called method1')

    def method2():
        print('called method2')

    def __call__(self, *args, **kwargs):
        print('entering __call__')
        __class__._pre()
        ret = self.func(*args, **kwargs)
        __class__._post()
        print('leaving __call__')
        return ret


@decorator_cls
def my_function(name, address):
    print(f'{name} {address}')


my_function.set_decorator_pre('method2')
my_function.set_decorator_post('method1')
r = my_function('peter', 'amk')
