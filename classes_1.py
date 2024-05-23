from enum import Enum, auto

class something:
    class constant(Enum):
        API = 1
        HTTP = 2


    def __init__(self):
        self.var : int
        pass

    def somefn(self):
        self.var = something.constant.API


a = something()
a.somefn()

print(a.var)


class CONST(Enum):
    A=1
    B=2
    
    @property
    def v(self):
        return 11
        
