practice = "y", "h", "z", "x"

print (practice)

tup1 = "a", "b", "c"

###
lst_tups = [('Articuno', 'Moltres', 'Zaptos'), ('Beedrill', 'Metapod', 'Charizard', 'Venasaur', 'Squirtle'), ('Oddish', 'Poliwag', 'Diglett', 'Bellsprout'), ('Ponyta', "Farfetch'd", "Tauros", 'Dragonite'), ('Hoothoot', 'Chikorita', 'Lanturn', 'Flaaffy', 'Unown', 'Teddiursa', 'Phanpy'), ('Loudred', 'Volbeat', 'Wailord', 'Seviper', 'Sealeo')]

t_check = []
for tup in lst_tups:
    t_check.append(tup[2])
print(t_check)

#####

tups = [('a', 'b', 'c'), (8, 7, 6, 5), ('blue', 'green', 'yellow', 'orange', 'red'), (5.6, 9.99, 2.5, 8.2), ('squirrel', 'chipmunk')]

seconds = []
for tup in tups:
    seconds.append(tup[1])

#####

def information(name, birth_year, fav_color, hometown):
    return (name, birth_year, fav_color, hometown)

####
def info(name, age, birth_year, year_in_college, hometown):
    return (name, age, birth_year, year_in_college, hometown)

person = ("pavan", 44, 1979, 2024, "chicago")
print (person)