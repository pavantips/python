def sumTo(aBound):
    """ Return the sum of 1+2+3 ... n """

    theSum  = 0 ## sum of all numbers until the final number
    aNumber = 1 ## initialize with 1 and keep iterating until this is less than or equal to aBound or final number
    while aNumber <= aBound:
        theSum = theSum + aNumber
        aNumber = aNumber + 1
    return theSum

print(sumTo(4))

#print(sumTo(1000))

####

eve_nums = []    # Initialize empty list
counter = 0      # Initialize counter

while counter <= 15:
    if counter % 2 == 0:    # Check if number is even
        eve_nums.append(counter)
    counter += 1    # Increment counter

print(eve_nums)  

####

a = 0
b = 0
while a <= 15:
    b = a + 1
    a += 1

print(b)  # Will print 16

###

total_sum = 0
i = 0

while i <=10:
    total_sum+=i
print(total_sum)

    
