def countdown(num):
    li=[]
    for i in range(num,-1,-1):
       li.append(i) 
    return li

print(countdown(5)) 

#####################################

def print_and_return(li):
    print(li[0])
    return li[1]
    

print(print_and_return([1,5]))    

############################
