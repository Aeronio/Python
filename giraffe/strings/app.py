print("Something\nor\nOther")

print("This string says \"Something\"") #Putting a backslash before is how you get something to render literally, useful for inserting "

phrase_1 = "What's the password? "
phrase_2 = "Peanut Butter"

print(phrase_1 + phrase_2)
print(phrase_1.lower())
print(phrase_1.upper())
print(phrase_1.isupper())
print(phrase_1.upper().isupper()) #Stacking functions like this in a pipeline actually reminds me of Go!
print(len(phrase_1))
print(phrase_1[0])

 #index function tells where a phrase is in a string
print(phrase_1.index("W"))
print(phrase_1.index("pass"))

#Replace function
print(phrase_1.replace("password","codephrase"))