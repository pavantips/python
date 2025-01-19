fruit = ["banana", "apple", "cherry"]

print (fruit)
print (fruit[2])

fruit[0] = "pear"

print (fruit)

fruit[-1] = "orange"

print (fruit)

########

alist = ["a","b","c","d","e","f","g"]
print (alist)

alist [1:2] = "p","q"
print (alist)

#########

greeting = "Hello, world!"
newGreeting = "J" + greeting[1:]

print (greeting)
print (newGreeting)


#########

phrase = "many moons"
phrase_expanded = phrase + " and many stars"
phrase_larger = phrase_expanded + " litter"
phrase_complete = "M" + phrase_larger[1:] + " the night sky."
excited_phrase_complete = phrase_complete[:-1] + "!"

print (phrase)
print (phrase_expanded)
print (phrase_larger)
print (phrase_complete)
print (excited_phrase_complete)

######### delete operator

a = ["one", "two", "three"]
print (a)
del a[1]

print (a)

##########

alist= ["a", "b", "c", "d", "e", "f"]

del alist [1:5]
print (alist)

##### aliasing

a = [81,82,83]
b = [81,82,83]
print(a is b)

b = a
print(a == b)
print(a is b)

b[0] = 5
print(a)

######

w = ['Jamboree', 'get-together', 'party']
y = ['celebration']
y = w

print (w)
print (y)

#######
alist = [4,2,8,6,5]
blist = alist
blist[3] = 999
print(alist)

#### Cloning

a= [81,82,83]

b = a [:]

print (a==b)
print (a is b)

b[0] = 5

print (a)
print (b)

alist = [4,2,8,6,5]
blist = alist * 2
blist[3] = 999
print(alist)


b = ['q', 'u', 'i']
z = b
b[1] = 'i'
z.remove('i')
print (b)
print (z)

sent = "Holidays can be a fun time when you have good company!"
phrase = sent
phrase = phrase + " Holidays can also be fun on your own!"

print (phrase)
