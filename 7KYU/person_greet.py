# TODO: This method needs to be called multiple times for the same person (my_name).
# It would be nice if we didnt have to always pass in my_name every time we needed to great someone.

class Person(object):
    
    def __init__(self, name):
        self.name = name
    
    def greet(self, your_name):
        return f'Hello {your_name}, my name is {self.name}'
