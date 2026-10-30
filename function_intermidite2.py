x = [ [5,2,3], [10,8,9] ]
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
print(x)

students[0]['last_name']="Brayen"
print(students)
sports_directory['soccer'][0]="Andres"
print(sports_directory['soccer'][0])
z[0]["y"]=30
print(z[0]["y"])




#############################################################

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


# def iterateDictionary(students):
#     for i in range(0,len(students)):
#         for key,value in students[i].items():
#             print(key,value)
            
    
    
# iterateDictionary(students)    


def iterateDictionary(students):
    fname,lname=[],[]
    
    for i in range(0,len(students)):
        for key,value in students[i].items():
            fname.append(key)
            lname.append(value)
            
    for i in range(0,len(fname)):
        print(f"{fname[i].upper()}-{lname[i].upper()}")


    
x=iterateDictionary(students)   
print(x)


#3######################################################################

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterateDictionary2(key_name,some_list):
    for i in range(0,len(some_list)):
        print(some_list[i][key_name])
        
            

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

#4###############################

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printinfo(dict):
    valuesli=[]
    for keys,values in dict.items():
        print(f"{len(keys)} {keys}")
        # print(values)
        for item in values:
            print(item)
        
        
     
        

x=printinfo(dojo)
 
