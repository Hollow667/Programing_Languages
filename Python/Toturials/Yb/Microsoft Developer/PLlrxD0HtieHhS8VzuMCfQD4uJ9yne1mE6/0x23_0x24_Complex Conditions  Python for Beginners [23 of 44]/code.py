gpa = float(input("What was your Grade Point Average? "))
lowset_grade = float(input("What was your lowest grade? "))
## Sometimes you can combine conditions with AND instead of nesting if statements
if gpa >= .85:
    if lowset_grade >= .70:
        print('Well done')
# the same as
if gpa >= 0.85 and lowset_grade >= .70:
    print('Well done')
    

#W if you need to remember the results of a condition check later in your code, use Boolean variables as flags
honour_roll = False
if gpa >= .85 and lowset_grade >= .70:
    honour_roll = True
else:
    honour_roll = False
# Somewhere later in your code
if honour_roll:
    print('Well done')