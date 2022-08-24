is_male = False
is_tall = True

#This is how you write if statements in python, || is "or", 
#if and else are the same but with the indented line structure
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")
    
 
 #elif is else if, not() is !   
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You arenot a male and not tall")