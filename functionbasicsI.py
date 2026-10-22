#1
def a():
    return 5
print(a())

#it will return and print 5


#2
def a():
    return 5
print(a()+a())

# it will return 5 two times and prints 10

#3
def a():
    return 5
    return 10
print(a())
#it will print 5 because return braks the function so the secound return will not be reached

#4
def a():
    return 5
    print(10)
print(a())
#it will print 5 because return braks the function so anything after the return will not be reached

#5
def a():
    print(5)
x = a()
print(x)
#will print  5 and then the value of x which captured the nothing because there is no return value for the function


#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
# i thout it will print nothing but it raized an error cant concate nothing type


#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
#will print 25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# will print 100 then will print 10 and 7 in unreachable



#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# will print 7 then 14 then 21




#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

# will print 8


#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)


#will print 500 then 500 then 300 then 500


#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
#will print 500 then 500 then 300 then 500


#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
#will print 500 then 500 then 300 then 300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

# i thoght it will give error b() not initialized but no we invoke a() after a() and b() initialized so it will print 1 3 2


#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

# it will print 1 3 5 10