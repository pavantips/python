
####

s = "python rocks"
for ch in s[3:8]:
   print(ch)

########

several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]


for things in several_things:
    print (things)
    
for things in several_things:
    print (type(things))

#####

t = [9, "setter", 3, "wing spiker", 10, "middle blocker"]
for z in t:
    print(z)

######
courses = ["ENGR 101", "SI 110", "ENG 125", "SI 106", "CHEM 130"]

if "SI 106" in courses:
    output = "You can apply to SI!"
else:
    output ="Take SI 106!"
    print (output)

######

x = -10
if x < 0:
    print("The negative number ",  x, " is not valid here.")
print("This is always printed")

######
x=3
y=5
z=2

if x < y and x < z:
    print("a")
elif y < x and y < z:
    print("b")
else:
    print("c")

###

s = "We are learning!"
x = 0
for i in s:
    if i in ['a', 'b', 'c', 'd', 'e']:
        x += 1
print(x)

###

a = ["holiday", "celebrate!"]
quiet = a
quiet.append("company")

print (a)

####

alist = [4,2,8,6,5]
blist = alist * 2
blist[3] = 999
print(alist)

####

sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']

sports.insert(2, "horseback riding" )

print(sports)

####

s = "python rocks"
print(s[1]*s.index("n"))

####

x = 2
y = 6
print('sum of {} and {} is {}; product: {}.'.format( x, y, x+y, x*y))

####

s = "I saw the movie, Mary Poppins Returns, and I thought it was great."

# all the expressions
r_count = s.count("r")
all_case_r_count = s.lower().count("r")
r_precentage = all_case_r_count/len(s) * 100

# use mostly variables inside f-strings or format()
first_str = f"The number of r characters: {r_count}."
second_str = "The percentage of r characters (upper or lower case): {:.2f}%.".format(r_precentage)

# display
print( first_str + " " + second_str)

####

numbs = [5, 10, 15, 20, 25]

newlist = []

for num in numbs:
    num= num+5
    newlist.append(num)
    print (newlist)


