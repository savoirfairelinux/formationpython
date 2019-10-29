class Person:
    def __repr__(self):
        return 'Je suis une personne'

class Employe(Person):
    def __repr__(self):
        person = super().__repr__()
        
        return person + ', je suis un employee'
    
    def fly(self):
        return 'Je peux voler '


class Professor(Employe):
    def fly(self):
        return 'I can fly'

    def __repr__(self):
        person = super(Professor, self).__repr__()
        return person + ' et un professeur'

class Student(Person):
    def __repr__(self):
        return 'I m a student'

class Member(Professor, Student):

    def __init__(self):
        self._st_method = 'Property'

    def __repr__(self):
        self.static_method()
        return super().__repr__() +' et membre'

    @property
    def st_method(self):
        return self._st_method

    @st_method.setter
    def st_method(self, value):
        self._st_method = value








