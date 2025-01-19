### formatting string methods

name = "Rodney Dangerfield"
score = -1  # No respect!
print("Hello " + name + ". Your score is " + str(score))

scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello " + name + ". Your score is " + str(score))

scores = [("Rodney Dangerfield", -1), ("Marlon Brando", 1), ("You", 100)]
for person in scores:
    name = person[0]
    score = person[1]
    print("Hello {}. Your score is {}.".format(name, score))


person = input('Your name: ')
greeting = 'Hello {}!'.format(person)
print(greeting)

person = input('Enter your name: ')
print('Hello {}!'.format(person))

## calculate percentages

origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${} discounted by {}% is ${}.'.format(origPrice, discount, newPrice)
print(calculation)


origPrice = float(input('Enter the original price: $'))
discount = float(input('Enter discount percentage: '))
newPrice = (1 - discount/100)*origPrice
calculation = '${:.2f} discounted by {}% is ${:.2f}.'.format(origPrice, discount, newPrice)
print(calculation)

name = "Sally"
greeting = "Nice to meet you"
s = "Hello, {}. {}."

print(s.format(name,greeting)) # will print Hello, Sally. Nice to meet you.

print(s.format(greeting,name)) # will print Hello, Nice to meet you. Sally.

print(s.format(name)) # 2 {}s, only one interpolation item! Not ideal.


x = 2
y = 6
print('sum of {} and {} is {}; product: {}.'.format( x, y, x+y, x*y))

#### f strings

name = "Rodney Dangerfield"
score = -1
print("Hello {}. Your score is {}.".format(name, score))
print(f"Hello {name}. Your score is {score}.")

first_name = "Peter"
last_name = "Huang"
score = 96.75
print(f"Hello {first_name} {last_name}. Your score is {max(score, 60)}.")

first_name = "Peter"
last_name = "Huang"
score = 96.75
print(f"Hello {first_name} {last_name}. Your score is {score:.1f}.")
print(f"Hello {first_name} {last_name}. Your score is {max(score, 60):.1f}.")

##########

s = "I saw the movie, Mary Poppins Returns, and I thought it was great."

# all the expressions
r_count = s.count("r")
all_case_r_count = s.lower().count("r")
r_precentage = all_case_r_count/len(s) * 100

# use mostly variables inside f-strings or format()
first_str = f"The number of r characters: {r_count}."
second_str = "The percentage of r characters (upper or lower case): {:.2f}%.".format(r_precentage)

# display
print( first_str + " " + second_str)