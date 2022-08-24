#[] denotes that it's a list/array
#They can be a list of any types of values
friends = ["Kevin", "Karen", "Jim", "David", "Oscar", "Ray", "Toby"]

print(friends)
print(friends[1])

#NEAT THING WITH PYTHON you can access backwards with NEGATIVE numbers
#It loops back around to the last element in the list
print(friends[-1])

#Access ranges in a list similiar to Go
print(friends[1:])
print(friends[1:3])
#last position not grabbed, but first position is

friends[1] = "DudeGuy"
print(friends[1])