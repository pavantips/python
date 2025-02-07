sentence  = 'As you sow, sow you reap'

words = sentence.split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] = word_counts[word]+ 1

print (word_counts)

## find out the count of chars or an alphabet
f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
t_count = 0 #initialize the accumulator variable
for c in txt:
    if c == 't':
        t_count = t_count + 1   #increment the counter
print("t: " + str(t_count) + " occurrences")

##### find the count of more than 1 char or alphabet

f = open('scarlet.txt', 'r')
txt = f.read()
# now txt is one long string containing all the characters
t_count = 0 #initialize the accumulator variable
s_count = 0 # initialize the s counter accumulator as well
for c in txt:
    if c == 't':
        t_count = t_count + 1   #increment the t counter
    elif c == 's':
        s_count = s_count + 1
print("t: " + str(t_count) + " occurrences")
print("s: " + str(s_count) + " occurrences")