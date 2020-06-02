num_of_trais = 0
while num_of_trais != 3:
    username = input("enter your username: ")
    password = input("enter your password: ")
    if username == "fadi" and password == "1234":
        print("welcome")
        num_of_trais = 3
    else:
        num_of_trais += 1
        print("Not Valid\n You have {} trie/s left".format(3 - num_of_trais))
