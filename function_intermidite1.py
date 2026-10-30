import random
def randInt(min=0,max=100):
    if (min<0):
        min=0
    if max<0:    
        max=0
    elif (min>max):
        min,max=max,min
    else:
        return int(random.random()*(max-min)+min)
        
    
        
        
    
print(randInt())     
print(randInt(min=10)) 
print(randInt(max=50)) 
print(randInt(min=10,max=200))    



    
