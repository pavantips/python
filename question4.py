def test(integer, bool=True, dict1={2:3, 4:5, 6:8}):
    if bool == True:  
        if integer in dict1:
            return dict1[integer]
        else:
            return None  # or some default when key not found
    else:  # when bool == False
        return False
    

test1 = test(2)
print (test1);