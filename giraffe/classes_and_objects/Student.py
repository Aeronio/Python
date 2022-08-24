#Making a class is simple, it's just "class SomeClass:"
class Student:
    
    #This is the map of the attributes this Student class should have
    #You are defining what this class/datatype is
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation