class GreatGrandParents_cls:
    def __init__(self):
        print("**Initializing Great Grand parents class...")
    def call_greatGrandParents_mtd(self):
        print('Calling call_greatGrandParents_mtd')


class Grandparent_cls(GreatGrandParents_cls):
    def __init__(self):
        print('*Initializing... class Grandparent_cls')
        self.grand_parent_age = 100
        super().__init__()

    def predict_grandparaent_age_mtd(self):
        print('Calling predict_grandparaent_age_mtd')
        #print(f'Current grandparent age is {self.grand_parent_age}')

class Parent_cls(Grandparent_cls):
    pass
    def __init__(self):
        self.parent_age = 50
        #super(Grandparent_cls, self).__init__()
        super().__init__()

if __name__ == '__main__':
   parent_obj =  Parent_cls()
   #print(parent_obj.parent_age)
   #print(parent_obj.grand_parent_age)
   parent_obj.predict_grandparaent_age_mtd()
   #parent_obj.call_greatGrandParents_mtd()