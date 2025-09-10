def checkingIfIn(string, direction=True, d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        return string in d
    else:
        return string not in d


check = checkingIfIn("pear");
print (check)