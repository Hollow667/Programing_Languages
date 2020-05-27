## We oftrn need current date and time when logging errors and saving data
# to get current date and time
# You need to use the datetime library
from datetime import datetime

current_date = datetime.now()
#the now function returns a datetime object
print('Today is: ' + str(current_date))

## There are functions you can use with datetime objects to manipulate dates
from datetime import datetime, timedelta
today= datetime.now()
print('Today is: ' + str(today))

# timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))


## Use date functions to control date formating
from datetime import datetime
current_date = datetime.now()

print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year: ' + str(current_date.year))


## somtimes you receive the date as string and need to convert it to a datetime object
from datetime import datetime
birthday = input('When is your birthday (dd/mm/yyy)? ')

birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print('Birthday: ' + str(birthday_date))
