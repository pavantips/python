'''
def adding(x):
    y = 3
    z = y + x + x
    return z

def producing(x):
    z = x * y
    return z

print(producing(adding(4))) 
'''

####

def addit(n):
    return n + 5

def mult(m):
    return m * addit(m)


p = mult (3)
print (p)


####

def pow(b, p):
    y = b ** p
    return y

def square(x):
    a = pow(x, 2)
    return a

n = 5
result = square(n)
print(result)

######

def square(x):
    return x*x ## square of 2 is 4

def g(y):
    return y + 3 #### 4 + 3 = 7

def h(y):
    return square(y) + 3  ## y is 4 and add 3 = 7

print(h(2))

####

def square(x):
    return x*x ## square of 2 is 4

def g(y):
    return y + 3 ### 4 + = 7

def h(y):
    return square(y) + 3 ### 7 + 3 = 10

print(g(h(2)))
      
####

def double(y):
    y = 2 * y # when passed 5, this will become 2*5 = 10
    return y

num = 5
nm = double(num)
print(nm)


####

def changeit(lst):
    lst[0] = "Chicago"
    lst[1] = "Bulls"
    lst[2] = "are"
    lst[3] = "cool"

mylst = ['our', 'students', 'are', 'awesome']
changeit(mylst)
print(mylst)

###

def myfun(lst):
    lst = [1, 2, 3]

mylist = ['a', 'b']
myfun(mylist)
print(mylist)
