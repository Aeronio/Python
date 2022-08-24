from Student import Student

student1 = Student("Rad", "Nursing", 3.5)
student2 = Student("Thurston", "Business", 2.5)

#You call a class function same as any, it's object.function()
print(student1.on_honor_roll())
print(student2.on_honor_roll())