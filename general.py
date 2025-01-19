fruit = "banana"
f = (fruit[-1])
print (f)
midchar = fruit[len(fruit)//2]
print (midchar)

fruit = "Banana"
print(len(fruit))

fruit = "Banana"
sz = len(fruit)
last = fruit[sz-1]       # ERROR!
print(last)

fruit = "Banana"
sz = len(fruit)
lastch = fruit[sz-1]
print(lastch)

alist =  ["hello", 2.0, 5]
print(len(alist))
print(len(alist[0]))


s = "python rocks"
print(len(s))
print(s[3:8])

alist = [3, 67, "cat", 3.14, False]
print(len(alist))

lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
output = len(lst)
print (output)

# slicing
singers = "peter, paul and mary"
print (singers[6:12])

a_list = ["a","b","c","d","e","f"]
print  (a_list[1:3])
print  (a_list[:4])
print  (a_list[3:])
print  (a_list[:])

alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
print(alist[4:])

L = [0.34, '6', 'SI106', 'Python', -2]
print(len(L[1:-1]))

new_lst = ["computer", "luxurious", "basket", "crime", 0, 2.49, "institution", "slice", "sun", ["water", "air", "fire", "earth"], "games", 2.7, "code", "java", ["birthday", "celebration", 1817, "party", "cake", 5], "rain", "thunderstorm", "top down"]
sub_lst = new_lst[5:8]
print (sub_lst)

new_lst = ["computer", "luxurious", "basket", "crime", 0, 2.49, "institution", "slice", "sun", ["water", "air", "fire", "earth"], "games", 2.7, "code", "java", ["birthday", "celebration", 1817, "party", "cake", 5], "rain", "thunderstorm", "top down"]
sub_lst = new_lst[8:12]
print (sub_lst)

lst = ["swimming", 2, "water bottle", 44, "lollipop", "shine", "marsh", "winter", "donkey", "rain", ["Rio", "Beijing", "London"], [1,2,3], "gold", "bronze", "silver", "mathematician", "scientist", "actor", "actress", "win", "cell phone", "leg", "running", "horse", "socket", "plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"]
output = lst[5:13]
print (output)


# Concatenation and Repetition 

fruit = ["apple","banana", "orange", "cherry"]
print (fruit+[1,2] + [3,4])
print ([1,2] + [3,4])
print ([0]*4)

fruit = ['apple', 'orange', 'banana', 'cherry'] + [1] * 4
print (fruit)

# count and index

a = "the team is doing really good this season"
print (a.count("e")) #count
print (a.index("s")) #index

qu = "wow, welcome week!"
ty = qu.index("we")
print (ty)

# splits and joining strings

song = ' the rain in spain'
print (song.split())
print (song.split("a"))

str1 = "OH THE PLACES YOU'LL GO"
output = str1.split()
print (output)


qu = "wow, welcome week! Were you wanting to go?"
ty = qu.count("we")
