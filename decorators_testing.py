from abc import ABC, abstractmethod

class Microwave_cls(ABC):
    def __init__(self, value):
        self.something = value


    @abstractmethod
    def heat_up_mtd(self):
        pass

class item_cls(Microwave_cls):
    def __init__(self, brand):
        super().__init__(12)
        self.brand = brand

    def heat_up_mtd(self):
        print('I am heating up..')



if __name__ == '__main__':
    item = item_cls('toshiba')
    print(item.brand)
    item.heat_up_mtd()
    print(item.something)

