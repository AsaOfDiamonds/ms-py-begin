# strings stored in variables 
first_name = 'Asa'
print(first_name)

# no keyword required to set a variable just give it a name

# combine strings with + operator
last_name = 'Shalom'
print('Greetings ' + first_name + ' ' + last_name)

# variable naming convention in python is always lower
# case if more than one word use underscore

# you can use functions to modify strings
sentence = 'The dog is named Hyper'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('e'))

# The functions help us format strings we save to files and databases,
# or display to users

first_name = input('What is your first name? ')
last_name= input('What is your last name? ')
print('Hello ' + first_name.capitalize() + ' '   + last_name.capitalize())
