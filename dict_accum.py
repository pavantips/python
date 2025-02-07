txt = "MISSISSIPPI" # create a string

char = {} # create an empty dictionary

for c in txt:
    if c not in char:
        char [c] = 0
    char [c] = char[c] + 1

#chars  =(char.keys())

print (char)
