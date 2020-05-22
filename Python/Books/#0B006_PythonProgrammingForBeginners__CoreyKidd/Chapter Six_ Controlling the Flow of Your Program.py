x, y, z = 0,0,0

#Conditional Statements
x == y
x != y
x > y
x >= y
x < y
x <= y
x == y and x == z
x == y or x == z
not x == y

#The If Statement
check_input = input("Choose 1 or 2\n")
if check_input == "1":
    print("Sorry, you lose!")
elif check_input == "2":
    print("Congratilations! You win!")
else:
    print("Your choice is invalid")

##Loops
#For Loop
user_message = input("Type in a message: \n")
for a in user_message:
    print(a)

set_list = ["Zero", "One", "Two", "Three", "Four", "Five"]
for set_list_print in set_list:
    print(set_list_print)
#The While Loop
set_number = int(input("Type in a number between 5 and 20\n"))
while set_number > 0:
    print("Number: ", set_number)
    set_number -= 1
#break
num = 0
for set_list_print in set_list:
    print(num, set_list_print)
    num += 1
    if num == 3 : break
#continue
num = 0
for set_list_print in set_list:
    print(num, set_list_print)
    num += 1
    if num == 3 : continue
