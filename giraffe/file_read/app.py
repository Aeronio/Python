#This is how you open a file, "r" makes it read-only
#"w" is write, "a" is append (You append info to the file, you can't change the file)
#r+ is read AND write
employee_file = open("employees.txt", "r")

#Good idea to check if a file you opened is readable
print(employee_file.readable())

#reads the entire file
#print(employee_file.read())

#read a line of the file, moves cursor in the file to the next line
#print(employee_file.readline())
#print(employee_file.readline())

#Reads the entire file and puts it into a list
#print(employee_file.readlines())

#Access individual elements like an array/list
#print(employee_file.readlines()[0])

#Loop over the read file
for employee in employee_file.readlines():
    print(employee)
employee_file.close()