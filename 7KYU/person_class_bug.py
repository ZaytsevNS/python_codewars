class Person():

    def __init__(self, first_name: str, last_name: str, age: int, full_name = None):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = "{} {}".format(first_name, last_name)
        self.age = age
        