f = open('olympics.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
letter_counts = {} # start with an empty dictionary
for c in txt:
   letter_counts[c] = letter_counts.get(c, 0) + 1

print (letter_counts)
#print("t: " + str(letter_counts['t']) + " occurrences")
#print("s: " + str(letter_counts['s']) + " occurrences")

#####

stri = "what can I do"

char_d = {} # start with an empty dictionary
for c in stri:
   char_d[c] = char_d.get(c, 0) + 1

print (char_d)