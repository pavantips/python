fileref = open("/Users/ptipparaju/Desktop/html/Python/olympics.txt", "r") ## open the file


#contents = fileref.read() ## read ALL contents of the file
#print(len(contents))
lines = fileref.readlines() ## read few lines of the file with \n 

for lin in lines[:4]:
    print(lin) ## read the the 4 lines with proper formatting

#for lin in fileref:
 #   print(lin) ## read ALL the contents of the file with proper formatting

#print(len(lines))
#print(contents) ## print ALL contents of the file
#print(contents[:100]) ## print first 100 chars of the file
#print(contents[:4]) ## print the first 4 lines of the file


fileref.close() ## close the file

##### lines in the file:


fileref = open("school_prompt2.txt", "r") ## open the file

lines = fileref.readlines()
print (len(lines))
fileref.close()

##### count of chars in the file:

fileref = open("school_prompt2.txt", "r") ## open the file

num_char = fileref.read()
print (len(num_char))
fileref.close()