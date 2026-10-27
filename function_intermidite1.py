import random
def randInt(min=0,max=100):
    if (min>=0 and max>0):
        return int(random.random()*(max-min)+min)
    else:
        return int(random.random()*((-1*max)-(-1*min)+(-min)))
        
    
        
        
    
print(randInt())     
print(randInt(min=10)) 
print(randInt(max=50)) 
print(randInt(min=10,max=200))    


