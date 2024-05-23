import re
string = '$variable and $user'
#string = '$nothing$'
pattern = r'\$\w+\$'

def my_fn(matchobj):
    print( matchobj.group(0) )
    return matchobj.group(0).replace('$', '@@')  
    




a = re.sub(pattern,   my_fn, string)
print(a)