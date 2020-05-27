province = input("What province do you live in? ")
tax = 0

## You may need to ckeck multiple conditions to determine the correct action
if province == 'Alberta':
    tax = 0.05
elif province == 'Nunavut':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print(tax)

## if multiple conditions cause the same action they can be combined into a single condition
if province == 'Alberta' or province == 'Nunavut':
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print(tax)


## if you have a list of possible values to check, you can use the IN operator
if province in ('Alberta' ,'Nunavut', 'Yukon'):
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print(tax)

## if an action dependes on a combination of conditions you can nest if statements
country = input("What country do you live in? ")
if country.lower() == "canada":
    province = input("What province do you live in? ")
    tax = 0

    if province in ('Alberta' ,'Nunavut', 'Yukon'):
        tax = 0.05
    elif province == 'Ontario':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0
print(tax)
