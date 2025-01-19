with open("/Users/ptipparaju/Desktop/html/Python/olympics.txt", "r", encoding="utf-8") as fileref:
    #content = fileref.read()
    lines = fileref.readlines() ## read few lines of the file with \n 

for lin in lines[:4]:
    print(lin) 
