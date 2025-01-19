origlist = [45,32,88]

origlist.append("cat")

######

origlist = [45,32,88]
print("origlist:", origlist)
print("the identifier:", id(origlist))             #id of the list before changes
newlist = origlist + ['cat']
print("newlist:", newlist)
print("the identifier:", id(newlist))              #id of the list after concatentation
origlist.append('cat')
print("origlist:", origlist)
print("the identifier:", id(origlist))             #id of the list after append is used

######

st = "Warmth"
a = []
a.append(st[0])
a.append(st[1])
a.append(st[2])
a.append(st[3])
a.append(st[4])
a.append(st[5])
print(a)

######

st = "Warmth"
a = []
b = a + [st[0]]
c = b + [st[1]]
d = c + [st[2]]
e = d + [st[3]]
f = e + [st[4]]
g = f + [st[5]]
print(g)

##### lower to upper chars

ss = "Hello, World"
print(ss.upper())

tt = ss.lower()
print(tt)
print(ss)

######

ss = "    Hello, World    "

els = ss.count("l")
print(els)

print("***"+ss.strip()+"***")

news = ss.replace("o", "***")
print(news)

######

food = "banana bread"
print(food.upper())

######

s = "python rocks"
print(s.count("o") + s.count("p"))


s = "python rocks"
print(s[1]*s.index("n"))

r_count = s.count("r")
all_case_r_count = s.lower().count("r")
r_precentage = all_case_r_count/len(s) * 100

# use mostly variables inside f-strings or format()
first_str = f"The number of r characters: {r_count}."
second_str = "The percentage of r characters (upper or lower case): {:.2f}%.".format(r_precentage)

# display
print( first_str + " " + second_str)