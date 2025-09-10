
#/ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

#or s in ex_lst:
 
 #   print(s[1])

def second_let(string):
        return string[1]

test = second_let(['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance'])

print (test)



def last_char(string):
    return string[-1]

nums_sorted = last_char(['beta', 'alpha', 'gamma', 'delta'])

print (nums_sorted)

fruits = ['peach', 'kiwi', 'apple', 'blueberry', 'papaya', 'mango', 'pear']
print(sorted(fruits, key=lambda fruit_name: (-len(fruit_name), fruit_name), reverse=True))

letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters) reverse = True