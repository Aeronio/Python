#Similar to C# error handling
#Good practice = catch specific errors
#You could do a brought "except", but we want narrow catching
try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    #You can accept the error as a variable using "as"
    print(err)
except ValueError:
    print("Invalid Input")