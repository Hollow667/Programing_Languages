## Your code needs the ability to take different actinon based on different conditions
price = 0.9
if price >= 1.00:
    tax = .07
    print(tax)
else:
    tax = 0
    print(tax)

## Be carful when comparing strings
country = "CANADA"
if country.lower() == "canada":
    print('Oh look a canadian')
else:
    print('Oh you are not from canada')    
