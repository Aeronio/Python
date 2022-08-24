#def is how you create a function in python
#Everything considered inside the function must be indented
#tip: typical Python syntax is all lowercase, with underscores for spaces
def say_hi():
     print("Hello to you!")
     
#You don't even need to declare what type of variable it is, just put a variable for the func to use
def say_name(name):
     print("Hello to you, " + name + "!")
     

#call the function
say_hi()
say_name("Gorb")
your_name = input("What's your name?")
say_name(your_name)