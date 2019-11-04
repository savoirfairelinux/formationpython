class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self, other_name):
        return "Hi {0}. I'm {1}".format(other_name, self.name)

if __name__ == '__main__':
    some_person = Person('Bilal')
    print(some_person.greet('Larbi'))