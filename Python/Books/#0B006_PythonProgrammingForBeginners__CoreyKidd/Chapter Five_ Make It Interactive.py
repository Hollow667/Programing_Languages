#Ask the user for their name and age

user_name = input("Can I take your name: ")

user_age = input("And Your age: ")

#Display the information on the screen

print("Hello! My name is", user_name, "and I am", user_age, "yreas old.")

#to take age as integer

user_age = int(input("And your age: "))

#to take user_age as float
user_age = float(input("And your age: "))


##       Advance Printing

print("""Welcom to this Program

I will need to know you name

on the next page.""")
#you can use """ or '''

#escape charaters
print("TAB \t...")
print("New line \n...")
print("Backslash \\...")
print("double qoute \"...")
print("single qoute \'...")

##      Receive Input From Files

#open a file for appending
text_file = open('example.txt','a') # (file name, Mode)

#write to the file
text_file.write("first line\n")
text_file.write("second line\n")

#close the file
text_file.close()

#open the file for reading
text_file = open('example.txt','r')
first_line = text_file.readline()
second_line = text_file.readline()
print(first_line, second_line)

#close the file
text_file.close()


