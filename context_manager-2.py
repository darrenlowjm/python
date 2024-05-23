from enum import Enum, auto

class Some_cls:



    def __init__(self, something_int):
        self.something_int = something_int
        #self.type = Conn.API
        print('* Initializing..')

    def some_mtd(self, smth):
        self.something_int = smth


    def __enter__(self):
        print('-> entering')
        self.some_mtd('000')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'<- exiting..with self.something_int = {self.something_int}')
        pass

def okok():
    with Some_cls(22) as return_obj:
        print(return_obj.something_int)
        return_obj.some_mtd(999)
        print(return_obj.something_int)
        return 1
        
print(okok()        )