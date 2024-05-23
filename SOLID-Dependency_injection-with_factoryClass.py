from abc import ABC, abstractmethod

class Appliance_abstractClass(ABC):
    """ this is the abstract class that all appliance must inherit
    """
    
    @abstractmethod
    def switch_on(self):
        raise NotImplementedError('abstract method not defined yet!')
    
    @abstractmethod
    def switch_off(self):
        raise NotImplementedError('abstract method not defined yet!')


class Light_bulb_class(Appliance_abstractClass):
    """ This is the actual concrete class for a light bulb
    """
    def switch_on(self):
        print(f'Turning on the {type(self)}')
    def switch_off(self):
        print(f'Turning OFF the {type(self)}')


class kitchen:
    """ This is the high level class that takes in an object of type Appliance_abstractClass
    and using that known interface, it calls the switch_on() and switch_off() methods
    """
    def __init__(self, appliance:Appliance_abstractClass ):
        self.appliance = appliance

    def on(self):
        self.appliance.switch_on()
    
    def off(self):
        self.appliance.switch_off()
    
    def __repr__(self):
        return self.__doc__
        


        
my_kitchen = kitchen(Light_bulb_class())        
my_kitchen.on()
my_kitchen.off()
