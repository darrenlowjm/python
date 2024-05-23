

a = Exception('I am an exception!')
print(a.args)
print(a)

print('====================================')
a = Exception('I am an exception!', 'and I hate it')
print(a.args)
print(a.args[0])
print(a.args[1])

print('====================================')

a = Exception('I am a bad error!')
try:
    raise a
except Exception as e:
    print(e)
    #raise


print('====================================')

try:
    # raise AttributeError
    raise ValueError('shit')
except (ValueError, KeyError, TypeError) as e:
    print(e)
    #raise

print('====================================')


# inheriting the BaseException class
class FirstLevel_Error(Exception):
    def __str__(self):
        return 'I am adding some special information here!'
    pass

class SecondLevel_Error(FirstLevel_Error):
    pass


try:
    raise FirstLevel_Error()
except Exception as e:
    print(e)
    #raise

print('====================================')


#raise SecondLevel_Error


try:
    # raise ValueError('I am a value errror')
    raise ValueError
except ValueError:
    print("caught")
    
    
    

