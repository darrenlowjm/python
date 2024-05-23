



def __compare(current_val, compareOp, exp_val):
    """
    __compare(), compare current value and expect value with compare Operator
     param: current_val, current value
     param: compareOp, compare operate such as, ==, !=, in, not in, >, < etc
     param: exp_val, expect value
     return True if matched, False if not matched
    """


    result = False
    
    current_val = [current_val] if not isinstance(current_val, list) else current_val
    exp_val = [exp_val] if not isinstance(exp_val, list) else exp_val

    if len(current_val) == 1 and len(exp_val) > 1:
        exp_val = [exp_val]
    __match = [False] * len(exp_val)

    #breakpoint()
    
    for index in range(len(exp_val)):
        if __match[index]:   # skip check if it is matching previously, multiple condition may not happen at the same time
            continue
        new_str = f'"{current_val[index]}"' + compareOp
        new_str += f'"{exp_val[index]}"' if not isinstance(exp_val[index], list) else str(exp_val[index])
        result = eval(new_str)
        if result:
            __match[index] = True  # detected match for one expectation
        else:
            break
    return result
    

'''
print(__compare('RCON', 'in', ['INIT','RCON']))
print(__compare('RCON', '==', ['RCON']))
print( __compare(['RCON'], '==', ['RCON']))
print(__compare(['RCON', 'INIT'], '==', ['RCON','INIT']) )
'''

def compare(current_val, exp_val):            
    '''
    if isinstance(current_val, list) and isinstance(exp_val, list):
        # Both are list of different size        
        if len(current_val) != len(exp_val):
            raise ValueError('Size Mismatch: list size of current_val is different from exp_val')
    '''
    if type(current_val) is not type(exp_val):
        if not isinstance(exp_val, list):
            raise ValueError(f'Type Mismatch: current_val is {type(current_val)}, exp_val is {type(exp_val)}')

        

print( compare(1, 'RCON')) # is NOK
print( compare('RCON', 1)) # is NOK
print( compare(['RCON'], 'RCON')) # is NOK
print( compare('RCON', ['RCON', 'INIT'])) # is OK; defintely a 'in' operation


print( compare(['RCON'], ['INIT','RCON']))  # is OK; depends on the compareOp 
print( compare(['RCON'], [['INIT'],['RCON']]))  # is OK; depends on the compareOp 

