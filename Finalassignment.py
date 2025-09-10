def strip_punctuation(string):
    for char in string:
        if char in string:
            string = string.replace(char, "")
    return string


test = strip_punctuation("Hello, I'm learning Python!")
print (test)    