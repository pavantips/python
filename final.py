scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"

scores_list = scores.split()

a_scores =0

for nums in scores_list:
    if int(nums) >= 90:
        a_scores = a_scores + 1
        
print (a_scores)

########
stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

words = org.split()

# Initialize an empty string for the acronym
acro = ""

# Iterate over the words
for word in words:
    if word not in stopwords:  # Exclude stopwords
        acro += word[0].upper()  # Take the first letter and capitalize it

print(acro)

#########

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

words= sent.split()

acro = ""

for word in words:
    if word not in stopwords:
        acro += word[0:2].upper() + "."

print (acro)

#######

p_phrase = "was it a car or a cat I saw"

r_phrase = p_phrase[::-1]

is_palindrome = p_phrase == r_phrase

print("Reversed Phrase:", r_phrase)
print("Is Palindrome:", is_palindrome)


#######

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for item in inventory:
    # Split each string into its components
    name, stock, price = item.split(", ")
    
    # Print the formatted string
    print("The store has {} {}, each for {} USD.".format(stock, name, price))