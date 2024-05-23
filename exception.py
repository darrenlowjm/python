import traceback

try:
    raise NameError, "hihi"

except Exception as e:
    print('caught')
    print (e.args)
    
try:
	fi = open('c:\\opop.txt')
#except FileNotFoundError as e:
#    print (e)
#except OSError as e:
#    print(e.errno )


except :
    print('dar------------')
    print( traceback.format_exc() )
