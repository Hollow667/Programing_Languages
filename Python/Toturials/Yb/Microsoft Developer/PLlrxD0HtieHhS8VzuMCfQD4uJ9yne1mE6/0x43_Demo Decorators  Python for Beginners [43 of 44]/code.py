def logger(func):
    func()
    print("hi")

@logger
def sample():
    print("there")
