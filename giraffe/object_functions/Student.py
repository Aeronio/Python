class Student:
    
    #This is the map of the attributes this Student class should have
    #You are defining what this class/datatype is
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa
    
    #Make sure self is always the first parameter when refering to the object's attribute
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False