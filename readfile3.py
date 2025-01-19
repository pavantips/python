
### - Read the first 10 chars from the local file

infile = open("squares.txt", "r")
print(infile.read()[:10])
infile.close()


