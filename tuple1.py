

####
def add(x, y):
    return x + y

print(add(3, 4))
z = (5, 4)
print(add(*z)) # use * symbol to unpack tuple, OR use values in variable z to do x+y calculation

#####

tuples_lst = [
    ("Beijing", "China", 2008),
    ("London", "England", 2012),
    ("Rio", "Brazil", 2016, "Current"),
    ("Tokyo", "Japan", 2020, "Future"),
]
country = None

# YOUR CODE HERE

country = []

for cntry in tuples_lst:
    country.append(cntry[0])
print (country)

####

