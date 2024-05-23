class fn_decorating_class:

    def __init__(self, func):
        self.func = func
        self.counter = 0
        print('Initializing fn_decorating_class...')

    def __call__(self, *args, **kwargs):
        print('Inside the __call__')
        # passing in the 'self' which is the instance of fn_decorating_class
        # so that this fn can access attributes of fn_decorating_class
        self.func(self, *args, **kwargs)

class Outer:
    @fn_decorating_class
    def do_fn(self, age):
        # passing in the 'self' which is the instance of fn_decorating_class
        # so that this fn can access attributes of fn_decorating_class
        print(f'This is my age : {age}')
        self.counter += 1
    
    def another_one(self, age):
        return self.do_fn(age)
    
outer = Outer()    
    
outer.do_fn(22)    
outer.do_fn(45)    
print(f'do_fn is a type of {type(outer.do_fn)}')
print(f'The counter variable is now:  {outer.do_fn.counter}')