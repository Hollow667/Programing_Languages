# Strings can be stored in variables
first_name = 'Christopher'
print(first_name)

# You can combine strings with +
first_name = 'Christopher'
last_name = 'Harrison'
print(first_name + last_name)
print('Hello ' + first_name + ' ' + last_name)

# Custom string formating
output = 'Hello ' + first_name + ' ' + last_name
output = 'Hello, {} {}'.format(first_name, last_name)
output = 'Hello, {0} {1}'.format(first_name, last_name)
# Only available in Python 3
output = f'Hello, {first_name} {last_name}'

# You can use functions to modify strings
sentence = 'The dog is named sammy'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))

# The functions help us format strings we save to files and databases, or display to users
first_name = input('what is your first name? ')
last_name = input('What is your last name? ')
print('Hello ' +  first_name.capitalize() + ' ' \
       + last_name.capitalize())
