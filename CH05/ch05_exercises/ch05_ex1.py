

class Person:
    name = "Default"

    def __init__(self, name):
        self.name = name
    
    def greet(self, other_name):
        return "Hi {0}, my name is {1}.".format(other_name, self.name)

    def print_greeting(self, other_name):
        print(self.greet(other_name))


person1 = Person("Marc")
person1.print_greeting("Richard")


person2 = Person("Marc2")