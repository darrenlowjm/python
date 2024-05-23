import traceback

class singleton:
    __instance = None
    __list_of_objects = list()

    def __init__(self, name_str):
        if type(self).__instance is None:
            type(self).__instance = self
            self.name = name_str
            print('Instance created successfully')
        else:
            print(f'Instance cannot be created! {name_str}')
            pass
            #type(self).__list_of_objects.append(self)
            raise Exception('Instance cannot be created more than once!')

    def some_method(self):
        print(f'I am {self.name}')

    @staticmethod
    def show_instance():
        print(__class__.__instance)

    def __del__(self):
        type(self).__instance = None
        print(f' deleting..')

    def __repr__(self):
        return f'Object {__class__.__name__} with name:{self.name}'

if __name__ == '__main__':
    obj1 = singleton('Peter')
    print(obj1)

    try:
        obj_2 = singleton('Jon1')
    except Exception as e:
        #traceback.print_exc()
        print('**%s'%e)
        pass

    del obj1

    obj_2 = singleton('Jon2')
    #print(obj_2)


    #singleton.show_instance()
