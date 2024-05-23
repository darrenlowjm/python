class OB:
    def __init__(self):
        self.aa=1
    def __del__(self):
        print('Destroying OB objects')
    def ppp(self):
        print('ppp')



class HelloContextManager:
    def __init__(self, ob):
        self.something = 1
        self.connection = ob
        print('*Entering __init__')


    def __enter__(self):
        print("-> Entering the context...")
        #return self # self is then stored as helloObj in the statement 'with HelloContextManager() as helloObj"
        try:
            connection = self.connection.__enter__()
            # Yup it's a connection.  Change our internal items.
            print("&&&&&&&&&&  ENTERING THIS PART $$$$$$$$$$$$$$$$")
        except AttributeError:
            # Not a factory, the connection is the connection.
            print("&&&&&&&&&&  AttributeError $$$$$$$$$$$$$$$$")        
        
        return self.connection


    def __exit__(self, exc_type, exc_value, exc_tb):
        print("<- Leaving the context...")
        if 0:
            print(exc_type, exc_value, exc_tb, sep="\n")

            return True     #by returning True, it means NO exception will be raised
            #return None     #by returning none, it means any exception will be raised
        if 1:
            if isinstance(exc_value, IndexError):
                print(exc_value)
                return True


ob_object = OB()

with HelloContextManager(ob_object) as helloObj:
    #print(helloObj.something)
    helloObj.ppp()
with HelloContextManager(ob_object) as helloObj:
    #print(helloObj.something)
    helloObj.ppp()
with HelloContextManager(ob_object) as helloObj:
    #print(helloObj.something)
    helloObj.ppp()

print('Ending')