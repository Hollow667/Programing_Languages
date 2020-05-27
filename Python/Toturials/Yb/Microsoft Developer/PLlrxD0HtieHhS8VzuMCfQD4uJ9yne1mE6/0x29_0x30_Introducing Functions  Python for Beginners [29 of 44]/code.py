## Somtimes we copy and paste our code
import datetime
# print timestamps to see how long sections of code
# take to run

first_name = 'Susan'
print('task completed')
print(datetime.datetime.now())
print()

for x in range(0, 10):
    print(x)
print('task completed')
print(datetime.datetime.now())
print()

## Use functions instead of repeating code
import datetime
# Print the current time
def print_time():
    print('task completed')
    print(datetime.datetime.now())
    print()

first_name = 'Susan'
print_time()

for x in range(0, 10):
    print(x)
print_time()

## By moving the code to a function, you reduce rework and the chance of introducing bugs when you change the code you had copied
# Import the datetime class from datetime library
from datetime import datetime
# Print the current time
def print_time():
    print('task completed')
    # Now I don't need the extra datetime prefix
    print(datetime.now())
    print()
print_time()

## What if I want a diiferent message displayed
from datetime import datetime
# print timestamps to see how long sections of code
# take to run

first_name = 'Susan'
print('first name assigned')
print(datetime.now())
print()

for x in range(0, 10):
    print(x)
print('loop completed')
print(datetime.now())
print()

## Pass the task name as a parameter
from datetime import datetime

# print the current time and task name
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

first_name = 'Susan'
print_time('first name assigned')
for x in range(0, 10):
    print(x)
print_time('loop completed')

## Here's another example where the code looks different but we are doing the same logic over and over

first_name = input('Enter you first name: ')
first_name_initial = first_name[0:1]
last_name = input('Enter your last name: ')
last_name_initial = last_name[0:1]

print('Your initials are: ' + first_name_initial \
    + last_name_initial)

## I can use a function, but this time my function returns a value
def get_initial(name):
    initial = name[0:1]
    return initial
first_name = input('Enter you first name: ')
first_name_initial = get_initial(first_name)
last_name = input('Enter your last name: ')
last_name_initial = get_initial(last_name)

print('Your initials are: ' + first_name_initial \
    + last_name_initial)

## if you need to change something you only have to change it in one place!
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter you first name: ')
first_name_initial = get_initial(first_name)
last_name = input('Enter your last name: ')
last_name_initial = get_initial(last_name)

print('Your initials are: ' + first_name_initial \
    + last_name_initial)
## Functions that return values allow clever code, but you might trage readability for less code
def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input('Enter you first name: ')
last_name = input('Enter your last name: ')

print('Your initials are: ' + get_initial(first_name) \
    + get_initial(last_name))
