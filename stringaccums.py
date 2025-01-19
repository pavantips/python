nums = [3,5,8]

accum = []
for w in nums:
    x = w**2
    accum.append (x)
    print (accum)
######

alist = [4,2,8,6,5]
blist = [ ]
for item in alist:
   blist.append(item+5)
print(blist)

#######

lst= [3,0,9,4,1,7]
new_list=[]
for i in range(len(lst)):
   new_list.append(lst[i]+5)
print(new_list)

######
verbs = ["kayak", "cry", "walk", "eat", "drink", "fly"]
ing = []
for v in verbs:
   ing.append(v + "ing")
print (ing)

wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]

past_wrds = []
for v in wrds:
   past_wrds.append(v + "ed")
print (past_wrds)

#####

numbs = [5, 10, 15, 20, 25]
new_list=[]
for i in numbs:
   new_list.append(i+5)
print(new_list)

########

numbs = [5, 10, 15, 20, 25]
for i in range(len(numbs)):  
    numbs[i] += 5  

print(numbs)

######

lst_nums = [4, 29, 5.3, 10, 2, 1817, 1967, 9, 31.32]

larger_nums=[]
for i in lst_nums:
   larger_nums.append(i*2)
print(larger_nums)

######

s = input("Enter some text")
ac = ""
for c in s:
    ac = ac + c + "-"

print(ac)

####

s = input("Enter some text")
ac = ""
for c in s:
    ac = c + ac

print(ac)

#####

s = "ball"
r = ""
for item in s:
   r = item.upper() + r
print(r)

#######

str1 = "I love python"
# HINT: what's the accumulator? That should go here.

chars = []  # Initialize an empty list
for char in str1:  # Iterate over each character in the string
    chars.append(char)  # Add the character to the list

print(chars)

######


