import random
def randInt(min="unknown",max="unknown"):
    if min=="unknown" and max=="unknown":
        return int(random.random()*100)
    elif min=="unknown" and max!="unknown": 
        return int(random.random()*max)
    elif min!="unknown" and max=="unknown": 
            return int(random.random()*100+min)
    else:
            return int(random.random()*max+min)
        
        
    
print(randInt())     
print(randInt(min=10)) 
print(randInt(max=50)) 
print(randInt(min=10,max=200))    
    
###################################################

    