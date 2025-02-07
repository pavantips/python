## Question 1:
num = None

# YOUR CODE HERE

fileref = open("assets/travel_plans.txt", "r") ## open the file

num = fileref.read()
print (len(num))
fileref.close()

## Question 2:
num_words = None

with open("assets/emotion_words.txt", "r") as file:
    content = file.read()  # Read the entire file content

# Split the content into words by whitespace
num_words = content.split()

# Print the list of words
print (len(num_words))

## Question 3:
num_lines = None

fileref = open("assets/school_prompt.txt", "r") ## open the file

num_lines = fileref.readlines()
print (len(num_lines))

fileref.close()

##Question 4:


