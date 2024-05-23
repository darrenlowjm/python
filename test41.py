class Me:
    __glo = 1
    
    @property
    def get_glo(cls):
        return cls.__glo
    
    
    def __init__(self):
        self.loc = 10
    
    def get_loc(self):
        return self.loc + __class__.get_glo
        
    @property
    def pro(self):
        return __class__.__glo
        
        
a = Me()
print(a.get_loc())        