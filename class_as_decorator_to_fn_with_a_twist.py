class fn_decorating_class:

    def __init__(self, func):
        self.func = func
        self.fn_decorating_class_counter = 0
        print('Initializing fn_decorating_class...')

    def __call__(self, *args, **kwargs):
        print('Inside the __call__')
        # passing in the 'self' which is the instance of fn_decorating_class
        # so that this fn can access attributes of fn_decorating_class
        print(f'original args : {args}')
        instance_outer_class = args[0]
        args = args[1:]     #remove the outer class element
        self.func(self, instance_outer_class, *args, **kwargs)


class outer_class:
    def __init__(self):
        self.outer_counter = 0

    @fn_decorating_class
    def do_fn(self, self_outer, age):
        # passing in the 'self' which is the instance of fn_decorating_class
        # so that this fn can access attributes of fn_decorating_class
        # also passing in the self_outer which is instance of the outer class
        # so that this fn can access attributes of outer class
        print(f'This is my age : {age}')
        self.fn_decorating_class_counter += 1
        
        self_outer.outer_counter += 99
    

outer_instance = outer_class()
    
    
outer_instance.do_fn(outer_instance, 22)    
outer_instance.do_fn(outer_instance, 45)    
print(f'do_fn is a type of {type(outer_instance.do_fn)}')
print(f'The fn_decorating_class_counter variable is now:  {outer_instance.do_fn.fn_decorating_class_counter}')
print(f'The outer_counter variable is now:  {outer_instance.outer_counter}')