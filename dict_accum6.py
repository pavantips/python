##

Junior = {
    "SI 206": 4,
    "SI 310": 4,
    "BL 300": 3,
    "TO 313": 3,
    "BCOM 350": 1,
    "MO 300": 3,
}
credits = None

credits = 0
for value in Junior.values():
    credits = credits+value

print(credits) 

####

str1 = "peter piper picked a peck of pickled peppers"
freq = None

freq = {}

for c in str1:
    if c not in freq:  # Check if the character is not already in the dictionary
        freq[c] = 0
    
    freq[c] += 1  # Increment the frequency of the character

print(freq)

#####

s1 = "hello"
counts = None

counts = {}

for c in s1:
    if c not in counts:  # Check if the character is not already in the dictionary
        counts[c] = 0
    
    counts[c] += 1  # Increment the frequency of the character

print(counts)

#####

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"

words = str1.split()

freq_words = {}

for word in words:
    if word not in freq_words:  # Check if the word is not already in the dictionary
        freq_words[word] = 0
    
    freq_words[word] += 1  # Increment the frequency of the word

print(freq_words)

####

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"
wrd_d = None

words = str1.split()

wrd_d = {}

for word in words:
    if word not in wrd_d:  # Check if the word is not already in the dictionary
        wrd_d[word] = 0
    
    wrd_d[word] += 1  # Increment the frequency of the word

print(wrd_d)

#####

sally = "sally sells sea shells by the sea shore"
characters = None
best_char = None

characters = {}
best_char = {}

for c in sally:
    if c not in characters:
        characters[c] = 0
    characters[c] = characters[c]+1
keys = list(characters.keys())
    
best_char = keys[0]
for key in keys:
    if characters[key] > characters[best_char]:
        best_char = key

print (characters)
print (best_char)

####

sally = "sally sells sea shells by the sea shore and by the road"
characters = None
worst_char = None

characters = {}
worst_char = {}

for c in sally:
    if c not in characters:
        characters[c] = 0
    characters[c] = characters[c]+1
keys = list(characters.keys())
    
worst_char = keys[0]
for key in keys:
    if characters[key] < characters[worst_char]:
        worst_char = key

print (characters)
print (worst_char)

######

p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d = None

low_d = {}

for c in p:
    # Convert the character to lowercase
    c_lower = c.lower()
    
    # If the character is already in the dictionary, increment its count
    if c_lower in low_d:
        low_d[c_lower] += 1
    # Otherwise, add it to the dictionary with a count of 1
    else:
        low_d[c_lower] = 1

print(low_d)

