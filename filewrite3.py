olympians = [("John Aalberg", 31, "Cross Country Skiing, 15KM"), #### DATA
             ("Minna Maarit Aalto", 30, "Sailing"),
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

outfile = open("reduced_olympics2.csv", "w") #### Create and open file

outfile.write('"Name","Age","Sport"') # output the header row
outfile.write('\n') # newline after header row

for olympian in olympians: # loop to add DATA to the file after header row
    row_string = '"{}", "{}", "{}"'.format(olympian[0], olympian[1], olympian[2])
    outfile.write(row_string) # create new row after writing data to each line
    outfile.write('\n') # newline after each rowstring
outfile.close() # close the file after completing the data insertion