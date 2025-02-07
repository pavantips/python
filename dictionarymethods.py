####

inventory = {'apples': 430, 'bananas': 312, 'pears': 217, 'oranges': 525}

for akey in inventory.keys():     # the order in which we get the keys is not defined
    print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())       # Make a list of all of the keys
print(ks)
print(ks[0])                      # Display the first key

####

mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
answer = mydict.get("cat")//mydict.get("dog")
print(answer)

####

medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}

events = list(medal_events.keys())
print (events)

####

fruits = {'apple': 10, 'banana': 20}
items = fruits
fruits['orange'] = 30
print (fruits)
print(items['orange'])
