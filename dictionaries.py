## CREATE Dictionary

medals = {"gold": 33, "silver":17, "bronze":12}
print (medals)

olympics = {"gold": 7, "silver":8, "bronze":6}
print (olympics)

places = {"Australia":2000, "Greece":2004, "China":2008, "England":2012}
places["Brazil"] = 2016 


## Delete 

inventory =  {'apples': 430, 'bananas': 569, 'oranges': 784, 'pears': 217}

del inventory["oranges"]

print (inventory)

####

my_dict = {
    "fruits": ["apple", "banana", "cherry"],
    "colors": ["red", "green", "blue"]
}

print(my_dict["fruits"])  # Output: ['apple', 'banana', 'cherry']
print(my_dict["colors"])  # Output: ['red', 'green', 'blue']

######

mydict = {"cat":12, "dog":6, "elephant":23}
mydict["mouse"] = mydict["cat"] + mydict["dog"]
print(mydict)
print(mydict["mouse"])

######

swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}
swimmers["Phelps"] = swimmers["Phelps"] + 5
print(swimmers["Phelps"])

######

total = 0
mydict = {'cat': 12, 'dog': 6, 'elephant': 23, 'bear': 20}


for key in mydict:
	if len(key) == 3:
    	    total += mydict[key]
			
print (total)