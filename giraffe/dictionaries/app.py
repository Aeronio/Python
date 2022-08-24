#dictionaries are MAPs, key value pairs
#You denote them with {}

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

#How to access the values (use the keys)
print(monthConversions)
print(monthConversions["Nov"])

#Get func does the same thing, but you can specify a default value in case the one you want doesn't exist
print(monthConversions.get("Luv", "Not a Valid Key"))