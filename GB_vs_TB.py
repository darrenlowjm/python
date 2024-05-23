import operator
from shcore.utilities.text_utils import getBytesValue
import re

operator_dict = {'=': operator.eq,
                     '>=': operator.ge,
                     '<=': operator.le,
                     '<': operator.lt,
                     '>': operator.gt,
                     '!=': operator.ne
                     }

def convert_size_string_to_GB_float(string):
    if 1:
        def mapper(string):
            #if (not isinstance(string, str)) or not (string[-2:].upper() in ['TB', 'GB']):
            if (not isinstance(string, str)) or not re.search( r'[KMGT]i?B$',string):
                return string
            #return float(string[:-2]) * (1000 if 'TB' in string.upper() else 1)
            return getBytesValue(string)
        
        return map(mapper, string) if isinstance(string, list) else mapper(string)    
    else:
        if not isinstance(string, str):
            # do nothing if not a str
            # do nothing if is str that doesnt have 'TB/GB' at last 2 chars
            return string
        return map(getBytesValue, string) if isinstance(string, list) else getBytesValue(string)

    
    
    
def compare(sz1,sz2,comparator):
    #return  operator_dict[comparator](convert_size_string_to_GB_float(sz1),convert_size_string_to_GB_float(sz2))
    return eval( f'convert_size_string_to_GB_float(sz1) {comparator} convert_size_string_to_GB_float(sz2) ')


assert(compare(123,123, '==') ==  True)
assert(compare('100GB','0.1TB', '==') ==  True)
assert(compare('100GB','0.1TB', '>') ==  False)
assert(compare('100GB','0.1TB', '<') ==  False)
assert(compare('100GB','0.1TB', '<=') ==  True)
assert(compare('100GB','0.1TB', '!=') ==  False)
assert(compare('100GB','0.1TB', '>=') ==  True)
#
assert(compare('100.0GB','0.1TB', '==') ==  True)
assert(compare('100.1GB','0.1TB', '>') ==  True)
assert(compare('99.9GB','0.1TB', '<') ==  True)
assert(compare('10TB','10.1TB', '<=') ==  True)
assert(compare('10TB','10000GB', '==') ==  True)
assert(compare('10TB','10001GB', '<') ==  True)
assert(compare('10.001TB','10001GB', '==') ==  True)
assert(compare('10.002TB','10001GB', '>') ==  True)
assert(compare('10.0TB','10.0TB', '==') ==  True)
assert(compare('10.0TB','10.0TiB', '<') ==  True)
assert(compare('10KB','10KiB', '<') ==  True)
assert(compare(10*1024,'10KiB', '==') ==  True)
assert(compare(10*1024*1024,'10MiB', '==') ==  True)
assert(compare(10*1024*1024*1024,'10GiB', '==') ==  True)
assert(compare(10*1024*1024*1024*1024,'10TiB', '==') ==  True)
#
assert(compare(10,10.1, '<') ==  True)
assert(compare('10.0TB', ['10.0TB', '12TB'],'in') ==  True)




