class testing:
    def __init__(self):
        self.summary_table = {
            'HI':1,
            'HO':1,
            'HE':1,        
        }
    
    def getLevel(self, level):
        self.level = level        
        
        
    @property
    def value(self):
        return list(self.summary_table.keys())[self.level]
    
    def __iter__(self):
        for n in range(len(self.summary_table)):
            self.getLevel(n)
            yield self
            
a = testing()

for each in a:
    print(a.value)
    
    
class dict_helper:
    def __init__(self, dic_input):
        self.__dic_input = dic_input

    @property
    def dic(self):
        return self.__dic_input
        
    def __getattr__(self, attr):
        return getattr(self.dic, attr)
        
    def __len__(self):
        return len(self.dic)
        
        
temp = {
    'HI':0,
    'HO':1,
    'HE':2,        
}        

a = dict_helper(temp)


class ok:
    def __init__(self):
        pass
    def p(self):
        print('Yo!')
    def __call__(self):
        return self
        
from functools import lru_cache
class testing123:
    @staticmethod
    @lru_cache(maxsize=2)
    def show_p(wat):
        print(wat)

    def __getattr__(self, attr):
        get_disks = eval(attr)()
        setattr(self, attr, get_disks)
        return getattr(self, attr)

a=testing123()
a.show_p