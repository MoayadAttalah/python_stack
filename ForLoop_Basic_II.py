#- Given a list, write a function that changes all positive numbers in the list to "big".
    
mynumbers=[0,1,-5,-6,5,6]
myChangedNumbers=[]
for i in mynumbers:
    if i>=0:
        myChangedNumbers.append("big")
    else:
        myChangedNumbers.append(i)    
               
print(myChangedNumbers)        



# - Given a list of numbers, create a function to replace the last value with the number of positive values.
#  (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it

def count_positive(li):
    count=0
    for i in li:
        if i>0:
            count+=1
    li.pop()
    li.append(count)
    return li


x=count_positive([-1,1,1,1])   
print(x) 

# - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10

def sum_total(li):
    sum=0
    for i in li:
        sum=sum+i
    return sum

print(sum_total([1,2,3]))


# - Create a function that takes a list and returns the average of all the values.x

def avarage(li):
    sum=0
    count=0
    for i in li:
        sum+=i
        count+=1
    return sum/count

print(avarage([1,2,3]))        



# - Create a function that takes a list and returns the length of the list.
    
def length(li):
    count=0
    for i in li:
        count+=1
    return count
print(length([0,1,2,3]))    
print(length([]))

# - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
def minimum(li):
    if length(li)==0:
        return False
    minvalue=li[0]
    for i in li:
        if i<minvalue:
            minvalue=i
    return minvalue


print(minimum([100,5,1,10,2]))


# - Create a function that takes a list of numbers and returns the maximum value in the list. If the list is empty, have the function return False.
def maximum(li):
    if length(li)==0:
        return False
    maxvalue=li[0]
    for i in li:
        if i>maxvalue:
            maxvalue=i
    return maxvalue


print(maximum([37,2,1,-9]))

    # - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
    # ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(li):
    a={
        "sumTotal":sum_total(li),
        'average':avarage(li),
        'minimum': minimum(li),
        'maximum':maximum(li),
        'length': length(li)
    }
    return a

print(ultimate_analysis([37,2,1,-9]))


# - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]    
def reverse_list(li):
    temp1=len(li)
    for i in range(len(li),0,-1):
        temp2=li[i-1]
        li.append(temp2)
        
       
       
    
    return li[temp1:]    # print(li[i])
a=reverse_list([37,2,1,-9])
print(a)
