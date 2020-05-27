## Creating a class
class Presenter():
    def __init__(self, name):
        # Constructor
        self.name = name
    def say_hello(self):
        # method
        print('Hello, ' + self.name)

## Using a class
presenter = Presenter('Chris')
presenter.say_hello()

## Adding Properties
class Presenter():
    def __init__(self, name):
        # Constructor
        self.name = name
        # the code above will call @name.setter function

    @property        
    def name(self):
        # var = object.name
        return self.__name
    @name.setter
    def name(self, value):
        # cool validation here
        # object.name = value
        self.__name = value

presenter = Presenter('Chris')
presenter.name = 'Christopher'
print(presenter.name)
