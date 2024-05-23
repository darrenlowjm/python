class Some_class:
    def __init__(self):
        self.di = dict(
            test_connection_reset=1,
            test_connection_reset_error=2,
            test_connection_reset_ok=3 )
            
        for attr in vars(Test_set_class):
            # loop thru the Test_set_class and search for
            # all fn beginning with "test_", and store the function obj as
            # attributes of Some_class making these fns accessible
            if attr.startswith('test_'): setattr(self, attr, getattr(Test_set_class, attr))
            
        self.test_dict = {  attr : getattr(Test_set_class, attr)  for attr in vars(Test_set_class) if attr.startswith('test_') }  
            
    
    def __getattr__(self, name):
        #print(f"Unable to find such attribute:{name}")
        try:
            return self.test_dict[ name ]
        except KeyError:
            print(f"Unable to find such attribute:{name}")

    def __repr__(self):
        return str(self.test_dict)
        
    
    def __getitem__(self, key):
        try:
            return self.test_dict[ key ]()
        except KeyError:
            print(f"Unable to find such key:{key}")
    
    def __len__(self):
        return len(self.test_dict)
        
    

class Test_set_class:
    @staticmethod
    def test_connection_reset():
        print('Running test_connection_reset..')
    @staticmethod    
    def test_connection_reset_ok():
        print('Running test_connection_reset OK..')
    @staticmethod    
    def test_connection_reset_error():
        print('Running test_connection_reset ERROR..')
        

