def doSomething_fn(*args, **kwargs):
    print(args)
    print(type(args))


class SomeClass_cls(object):
    def __init__(self):
        pass







if __name__ == '__main__'  :
    doSomething_fn(1,2,3)
    ob = SomeClass_cls()
    ob.name = 'darren'

    print(ob.name)