#Question 1

letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters, reverse = True)

print (sorted_letters)

#Question 2

animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)

print (animals_sorted) 

#Question 3

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(medals)
print (alphabetical)

#Question 4

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(medals.items())
print (alphabetical)

#Question 5
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
most_needed = sorted(groceries.items(), reverse=True)
print (most_needed)


#Question 6

def last_four(single_id):
    return int(str(single_id)[-4:])

test = last_four(1234567890)
print (test)

