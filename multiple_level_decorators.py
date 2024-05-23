from functools import wraps


class Raid:
    level = None
    
    @staticmethod
    def plain():
        print('I am plain')
    
    def login_logout( *aargs ):
        def inner( func ):
            @wraps(func)
            def wrapper(*args, **kwargs):            
                __class__.level = aargs[0]
                print(f'+loggin with {aargs[0]}')
                func(*args, **kwargs)    
                print(f'+logout with {aargs[0]}')
            return wrapper
        return inner
        
    def set_level( *aargs ):
        def inner( func ):
            @wraps(func)
            def wrapper(*args, **kwargs):            
                __class__.level = aargs[0]
                print(f'+Set to level {aargs[0]}')
                func(*args, **kwargs)    
                print(f'-Set to level {aargs[0]}')
            return wrapper
        return inner
        
    def set_disk( *aargs ):
        def inner( func ):
            @wraps(func)
            def wrapper(*args, **kwargs):            
                __class__.disk = aargs[0]
                print(f'+Set to disk {aargs[0]}')
                func(*args, **kwargs)    
                print(f'-Set to disk {aargs[0]}')
            return wrapper
        return inner
    
    @login_logout(())    
    @set_level(0)
    @set_disk(5)
    def my_function(self, name, address):   #my_function = decorator(my_function)()
        print(f'{name} {address}')
        print(f'using level {type(self).level}')
        print(f'using level {type(self).disk}')
    
    def decorator_handler(*top_args):
        def inner( func ):
            def wrapper(*args, **kwargs):   
                for fn in top_args:
                    fn()
                
                func(*args, **kwargs)               
            return wrapper
        return inner

@Raid.decorator_handler(Raid.plain, Raid.plain, Raid.plain)
def test():
    print('I am test')
    
if 1:
    r = Raid()
    r.my_function('dar','can')    
    
    test()


