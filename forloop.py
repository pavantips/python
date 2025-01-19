#for name in ["Amy","Rocky","John"]:
#    print ("Hi", name, "Please come to my party!")

#lst = [100]

#for i in lst:
   # print('X')

 #   for i in [1-10]:
  #      print (i)


x = [1, 2, 3, 4]
y = 0
for z in x:
        y = y + z
print(y)

nums = [1,2,3,4,5,6,7,8,9,10]
accum = 0
for w in nums:
        accum = accum+w
        print (accum)


accum = 0
for w in range(11):
        accum = accum+w
print (accum)

for i in range(5):
        print (i, "hello")


accum = 0
for w in range (3,11):
        accum = accum+w
        print (accum)

        print("range(5): ")
for i in range(5):
    print(i)

print("range(0,5): ")
for i in range(0, 5):
    print(i)

# Notice the casting of `range` to the `list`
print(list(range(5)))
print(list(range(0,5)))
numbers =(list(range(53)))
print (numbers)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for w in nums:
   accum = 0
   accum = accum + w
print(accum)

"""
Question - Count the number of characters in string str1. Do not use len(). Save the number in variable numbs.

str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
numbs = 0  # Initialize the counter

# Iterate through each character in the string
for char in str1:
    numbs += 1  # Increment the counter for each character

print(numbs)
"""

numbers =(list(range(41)))
print (numbers)
numbs = 0
for w in numbers:
    numbs = numbs+w


numbers = list(range(41))

# Initialize the accumulator
sum1 = 0

# Accumulate the total of the list's values
for num in numbers:
    sum1 += num

print("List of numbers:", numbers)
print("Sum of the numbers:", sum1)