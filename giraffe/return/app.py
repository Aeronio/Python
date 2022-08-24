#Python returns whatever you want to return, no need to specify

def cube(num):
    return num*num*num
    #Code after the return statement will never be used
    #print(num)
    
print(cube(10))

user_number = input("What do you want cubed? ")
print(cube(float(user_number)))