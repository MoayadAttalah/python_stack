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


def first_plus_length(li):
    
    return li[0]+len(li)
    

print(first_plus_length([1,5,6]))    


#####################

# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
def values_greater_than_second(li):
    new_list=[]
    if len(li)<2:
        return False
    second=li[1]
    for i in li:
        if i>second:
            new_list.append(i)
    
    else:
        print(len(new_list))
    return new_list
    

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([]))




