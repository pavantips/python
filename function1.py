def hello2(s):
   print("Hello " + s)
   print("Glad to meet you")

hello2("Nick")

####

def hello2(s):
    print("Hello " + s)
    print("Glad to meet you")

hello2("Iman" + " and Jackie")
hello2("Class " * 3)

###

def family (family_name):
    print ("Hello " + family_name + " family" )
    print ("hope you guys are doing fine")

family ("RamLakhan")

####

def cyu(s1, s2):
   if len(s1) > len(s2):
      print(s1)
   else:
      print(s2)

cyu("Hello", "Goodbye")


##### addition

def add(x,y):
   print (x+y)

add (1,2)

##### substraction

def product(x,y):
   print (x*y)

product (10,20)

###  division

def divide (x,y):
   print (int(x/y))


divide (200,20)

#### square 

def square(x):
   y = x * x
   return y

toSquare  = 10
result = square(toSquare)
print ("The result of {} squared is {}.".format(toSquare, result))

####

def show_me_numbers(list_of_ints):
    print(10)
    print("Next we'll accumulate the sum")
    accum = 0
    for num in list_of_ints:
        accum = accum + num
    return accum
    print("All done with accumulation!")

show_me_numbers([4,2,3])

####
def same(input_string):
    return input_string

word = same("hello")
print (word)

#####

def substract_three (n1):
   return (n1-3)

n2 = substract_three (9)
print (n2)

####

def change (n1):
   return (n1+7)

n2 = change (9)
print (n2)

####

def intro(name):
    return f"Hello, my name is {name} and I love SI 106."

####

def s_change(action):
    return action + " for fun." 

###

def decision(word):
   if len(word) > 17:
      return "This is a long string"
   else:
      return "This is a short string"

print(decision("whatever"))

#####

def total(lst):
   tot = 0
   for num in lst:
      tot = tot + num
   return tot

y = total([10,20,30])
print (y)

####

def count(numbers):
   return len(numbers)

y = count([19,9,9,99,1938,1937,847])
print (y)

####

def adding(x):
    y = 3
    z = y + x + x
    return z

def producing(x):
    z = x * y
    return z

print(producing(adding(4)))