fileref = open("/Users/ptipparaju/Desktop/html/Python/olympics.txt", "r")  # Open the file

# Read ALL contents of the file
contents = fileref.read()

# Reset the file pointer to the beginning
#fileref.seek(0)

# Read the lines of the file
lines = fileref.readlines()

# Print the first 4 lines with proper formatting
for lin in lines[:4]:
    print(lin.strip())  # Use strip() to remove trailing newline characters

# Close the file to free resources
fileref.close()