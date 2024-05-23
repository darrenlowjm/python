class testing:
    def __init__(self):
        pass
        
    def __del__(self):
        print('Destroying instance!')
        
print('Instance is not destroyed here...')        
a = testing()        
b = testing()        

print('Instance is destroyed here...')        
a = 1
