import functools

@functools.cache   
def myfn(firstname, lastname):
    print('I am running myfn..')
    
    return f'{firstname} + {lastname}'


''' 
print(myfn('a', 'b'))   # this is executed
print(myfn('a', 'b'))   # this is a cache-hit
print(myfn('1', 'b'))   # this is executed
'''

@functools.lru_cache(maxsize=8)   
def my_new_fn(firstname, lastname):
    print('I am running my_new_fn..')
    
    return f'{firstname} + {lastname}'

print(my_new_fn(1, 'b'))   # this is executed
print(my_new_fn('a', 'b'))   # this is a cache-hit
print(my_new_fn('1', 'b'))   # this is executed
print(my_new_fn('a', 'b'))   # this is a cache-hit if maxsize>1, else this is executed

@functools.lru_cache(maxsize=8)   
def __fn_2(namw):
    print('I am running my_fn_2..')        



@functools.lru_cache(maxsize=8)   
def fn_1(name):       
    __fn_2(1)


class myclass:
    @functools.cached_property
    def my_value(self):
        print('Running my_value')
        return 1221
        
aa = myclass()