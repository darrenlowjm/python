from contextlib import contextmanager

class SOME:
    def __init__(self):
        self.name = 'darren'
        
    def __enter__(self):
        print('Entering..')
        return self
    
    def __exit__(self, tb_type, tb_value, traceback):
        print('Cleaning up')
    
    
    @contextmanager
    def my_cm(self, string):
        #do soemthing with string
        print(string)
        try:
            yield 100
            
        finally:
            print('Cleaning up')

some = SOME()

'''
with some.my_cm('darren') as name:
    print('Do something')
    print(name)
    raise ValueError'''
    
@some.my_cm('darren')    
def test_1():
    print('running test1')
    raise ValueError
    
    
    