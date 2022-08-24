employee_file = open("employees.txt", "a")

#Use "w" to overwrite the filem or create a new file
#employee_file = open("employees.txt", "w")

employee_file.write("\nToby - Human Resources")
employee_file.close()

#creating new file
employee_file_new = open("employees1.txt", "w")
employee_file_new.write("\nKelly - Customer Service")
employee_file_new.close()