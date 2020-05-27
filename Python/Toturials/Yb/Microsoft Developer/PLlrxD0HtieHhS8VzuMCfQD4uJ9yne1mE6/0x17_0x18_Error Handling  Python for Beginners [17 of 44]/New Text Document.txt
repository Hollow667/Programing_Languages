## Syntax error
'''
# This code won't run at all
x = 42
y = 206
if x == y
    print('Success!!')
'''

## Runtime errors
'''
# This code will fail when run
x = 42
y = 0
print(x / y)
'''
    
## Catching runtime errors
x = 42
y = 0
try:
    print(x / y)
except ZeroDivisionError as e:
    # Optionally, log e something
    print('Sorry, something went wromg')
except:
    print('Somethong really went wrong')
finally:
    print('This is always runs on success or failure')

## Logic errors:
# This code won't run at all
x = 206
y = 42
if x < y:
    print(str(x) + ' is greater than ' + str(y))
