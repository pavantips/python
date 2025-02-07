### - Read the first 10 chars from the local file

infile = open("splitfile.txt", "r")
print(infile.read()[35])
infile.close()

### assign the number of line to a variable

num_lines = None

# Open the file in read mode
with open("/Users/ptipparaju/Desktop/html/Python/splitfile.txt", "r") as file:
    # Read all lines and count them
    num_lines = len(file.readlines())

# Print the total number of lines
print(num_lines)

###

ls = ['run', 'world', 'travel', 'lights', 'moon', 'baseball', 'sea']
new = ls[2:4]
print(new)