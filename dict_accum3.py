f = open ('scarlet2.txt', 'r')
txt = f.read()

x ={}
for c in txt:
    if c not in x:
        x[c] = 0
    
    x[c] = x[c] + 1

print (x)


#####

travel = {"North America": 2, "Europe": 8, "South America": 3, "Asia": 4, "Africa":1, "Antarctica": 0, "Australia": 1}

total = 0
for continent in travel:
    total += travel[continent]
    
print(total)

####

schedule = {"UARTS 150": 3, "SPANISH 103": 4, "ENGLISH 125": 4, "SI 110": 4, "ENS 356": 2, "WOMENSTD 240": 4, "SI 106": 4, "BIO 118": 3, "SPANISH 231": 4, "PSYCH 111": 4, "LING 111": 3, "SPANISH 232": 4, "STATS 250": 4, "SI 206": 4, "COGSCI 200": 4, "AMCULT 202": 4, "ANTHRO 101": 4}

total_credits = 0

for credits in schedule:
    total_credits += schedule[credits]

print (total_credits)