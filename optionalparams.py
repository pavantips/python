#1

def mult(x, y=4):
    return x*y

print (mult(5))


#2

def greeting (name, greeting ="hello", excl="!"):
   return "{} {}{}".format(greeting, name, excl)

#3

def sum(intx, intz=5):
    return intx+intz

print (sum(5))

#4

def test(x, bool=True, dict1={2:3, 4:5, 6:8}):
    if bool == True:  # or just: if bool:
        if x in dict1:
            return dict1[x]
        else:
            return None  # or some default when key not found
    else:  # when bool == False
        return False

#5

def test(integer, bool=True, dict1={2:3, 4:5, 6:8}):
    if bool == True:  # or just: if bool:
        if integer in dict1:
            return dict1[integer]
        else:
            return None  # or some default when key not found
    else:  # when bool == False
        return False

#6
def checkingIfIn_2(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]
        
# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn_2("cherry")

# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn_2("cherry", False)
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans = checkingIfIn_2 ("fruit")
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn_2

