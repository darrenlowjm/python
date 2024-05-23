from abc import ABC, abstractmethod

class iAppliance_class(ABC):
    """ this is the abstract class that all appliance must inherit
    """
    
    @abstractmethod
    def switch_on(self):
        raise NotImplementedError('abstract method not defined yet!')
    
    @abstractmethod
    def switch_off(self):
        raise NotImplementedError('abstract method not defined yet!')

class _Appliance_Light_bulb(iAppliance_class):
    """ This is the actual concrete class for a light bulb
    """
    def switch_on(self):
        print(f'Turning on the {type(self)}')
    def switch_off(self):
        print(f'Turning OFF the {type(self)}')


class Appliance_Factory_class:

    @staticmethod
    def create_light_bulb_obj():
        return _Appliance_Light_bulb()
    
    @classmethod
    def show_appliances(cls):
        pass


class unknown:
    pass

class kitchen:
    """ This is the high level class that takes in an object of type iAppliance_class
    and using that known interface, it calls the switch_on() and switch_off() methods
    """
    def __init__(self, appliance:iAppliance_class ):
        
        if not isinstance(appliance,iAppliance_class ):
            raise TypeError('Unknown parameter type')            
        
        self.appliance = appliance

    def on(self):
        self.appliance.switch_on()
    
    def off(self):
        self.appliance.switch_off()
    
    def __repr__(self):
        return self.__doc__
        

#my_kitchen = kitchen( Appliance_Factory_class.create_light_bulb_obj() )
my_kitchen = kitchen( unknown() )
my_kitchen.on()
my_kitchen.off()

