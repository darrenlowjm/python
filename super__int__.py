class type:
    def __init__(self):
        self.something = 1
        print('I am in super class init()')


class SubType(type):
    def __init__(self, a):
        self.nothing = a
        super().__init__()

item = SubType('ha')