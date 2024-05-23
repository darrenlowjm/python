import copy

class value:
    def __init__(self, val):
        self.v = copy.deepcopy(val)
        
    def update(self, kv):
        self.v.update(kv)
        return self
        
a = dict(darr=1, low=2)

x=value(a)

x.update({'darr':22}).update({'low':55})

