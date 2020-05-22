#Define the user name
user_firstname = "David"
user_surname = "Christopher"
user_sex = "Mr"

print(user_firstname, user_surname)
print([user_firstname+ user_surname])
print(user_firstname+ user_surname)


#     Formatting Strings

set_message = "Welcome to the game {0} {1} {2}".format(user_sex, user_firstname, user_surname)
print(set_message)

