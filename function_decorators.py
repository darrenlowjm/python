
#
# Simple
#
def decorator_fn(func):     #the function obj is passed in here
    def wrapper(*args, **kwargs):       # the function params is passed in here
        print('*Pre-decoration')
        #
        #args_repr = [repr(i) for i in args]
        #kwargs_repr =[f'{k}={v!r}' for k,v in kwargs.items()]
        #
        #print(f'Calling {func.__name__} with arguments ({", ".join(args_repr+kwargs_repr)})')
        #
        func(*args, **kwargs)   # call the func 
        #
        print('*Post-decoration')

    return wrapper

@decorator_fn
def my_fn(*args, **kwargs):
    print('my fn is executed here!')

#
# calling
#
#my_fn(1, 2, 3, na='darren', dept='eds')

# can be done this way too
# decorator_fn(my_fn)(1, 2, 3, na='darren', dept='eds')


#
# decorators that take in arguments
#
def topDecorator(*topargs):
    print(*topargs)
    def inner( func ):
        def wrapper(*args, **kwargs):            
            # do something
            print(*topargs)
            print("pre-decoration")
            func( *args, **kwargs )
            return 1
            print("post-decoration")
            # do something
        return wrapper
    return inner
    
@topDecorator('Top level is added')
def myFunction(name):
    print(f"I am executing {name}")
    

print(myFunction('peter'))