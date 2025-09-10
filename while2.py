x = 0
while x < 5:
    x += 1
    ##print("LOOP")

###

    x = 0
while x < 5:
    if x == 3:
        continue
    x += 1
   ### print("LOOP")

####

def check_nums(numbers):

    if 5 not in numbers:
        return numbers
    
    newlist = []
    i = 0
    
    while i < len(numbers):
        if numbers[i] == 7:
            break
        newlist.append(numbers[i])
        i = i+1

    return newlist

####

def sublist(numbers):
    
    if 5 not in numbers:
        return numbers
    
    newlist = []
    i = 0
    
    while i < len(numbers) and numbers[i] !=5:
        newlist.append(numbers[i])
        i = i+1
    
    return newlist

####

