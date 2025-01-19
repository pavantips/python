numbers_str = "13.1, 17.4, 22, 0"
numbers_l = numbers_str.split(",")
print (type(numbers_l))


## assertion example

x = 4
y = x
print("x is {} and y is {}".format(x, y))
assert x==y
x +=1
print("x is {} and y is {}".format(x, y))
assert x==y
print("That was easy!")