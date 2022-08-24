from gettext import translation


def translate(phrase):
    translation = ""
    for letter in phrase:
        #Special thing in python, this checks if "letter" is found in the specified string
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))