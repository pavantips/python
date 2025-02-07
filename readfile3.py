### - Read the first 10 chars from the local file

infile = open("squares.txt", "r")
print(infile.read()[:10])
infile.close()


# Open the file in read mode
with open("assets/travel_plans.txt", "r") as file:
    # Read the first 33 characters
    first_chars = file.read(33)

# Print the result to verify
print(first_chars)