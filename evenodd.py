
#1
x = 56

if x % 2 == 0:
    print (x, "is even")
else:
    print (x, "is odd")


courses = ["ENGR 101", "SI 101", "SI 100", "ENGR 125", "SI 106", "CHEM 130"]

# 2
if "SI 106" in courses:
    output = "You can apply to SI!"
else:
    output = "Take SI 106!"


#3
a = 20
b = 15
c = a+b

if b > a:
    print (a*2)

print (c)


#4

x = 9
y = 6

if x < y:
    print ("x is less than y")
else:
    if x > y:
        print ("x is greater than y")
    else:
        print ("x and y must be equal")

#5

str1 = "Today you are you! That is truer than true! There is no one alive who is you-er than you!"

if "false" in str1:
    output = "False, You aren't you?"
elif "true" in str1:
    output  = "True, You are you!"
else:
    output = "Neither true nor false"

print (output)

#6

a = 7
b = 5
c = 3
d = 2
if a > b and c > d:
    print("X")
elif a < b and c < d:
    print("Y")
else:
    print("Z")

#7

percent_rain = [94.3, 45, 100, 78, 16, 5.3, 79, 86]

resps = []

for percent in percent_rain:
    if percent > 90:
        resps.append('Bring an umbrella.')
    elif percent > 80:
        resps.append('Good for the flowers?')
    elif percent > 50:
        resps.append('Watch out for clouds!')
    else:
        resps.append('Nice day!')

print(resps)


#8 Testing Conditionals

x = 6
y = 4
if x < y:
    z = x
else:
    if x > y:
        z = y
    else:
        ## x must be equal to y
        assert x==y
        z = 0
print (z)

#9 accumulator with sequence

phrase  = "What a wonderful day to program"

tot = 0
for char in phrase:
    if char != " ":
        tot = tot+1

print (tot)

#10 count the vowels

s = "what if we went to the zoo"

x =0 
for i in s:
    if i in ['a','e','i','o','u']:
        x +=1
print (x)

#11 find the largest number

nums  = [1,2,3,4,5,6,700,8,9]
best_num =nums[0]

for n in nums:
    if n > best_num:
        best_num= n
print (best_num)

#12
lst = [1, 6, 5, 20, 1]
x = 0
for i in lst:
    if i % 2 == 0:
        x += 1
print(x)

#13 find the words more than 3 chars

words = ["water", "chair", "pen", "basket", "hi", "car"]

num_words = 0

for word in words:
    if len(word) > 3:
        num_words += 1
print (num_words)

#14 add chars to each words towards the end

words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"] # create a list

past_tense = [] # create and initialize a empty list to store results

for word in words: # variable to call each string in the list
    if word.endswith("e"): # if loop to iterate thru strings in the list which end with "e"
        past_tense.append(word+"d") # add "d" if the word is ending with e
    else: # else 
        past_tense.append(word+"ed") # add "ed" if the word does not end with e

print (past_tense) # print the result list

#15

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"

# Split the string into a list of rainfall values
rainfall_list = rainfall_mi.split(", ")

# Initialize a counter
num_rainy_months = 0

# Iterate through each value, convert to float, and check if it's greater than 3.0
for rainfall in rainfall_list:
    if float(rainfall) > 3.0:
        num_rainy_months += 1

print(num_rainy_months)

#16

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Split the sentence into words
words = sentence.split()

# Initialize the counter
same_letter_count = 0

# Iterate through each word in the list
for word in words:
    # Check if the first and last letters of the word are the same
    if word[0] == word[-1]:
        same_letter_count += 1

print(same_letter_count)

#17

items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]

acc_num =0 
for i in items:
    if 'w' in i:
        acc_num +=1
print (acc_num)

#18
num_lst = [3, 20, -1, 9, 10]

is_odd = []

for i in num_lst:
    if i % 2 != 0:  # Check if the number is odd
        is_odd.append(True)
    else:
        is_odd.append(False)

print(is_odd)
