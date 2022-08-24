lucky_numbers = [4, 7, 10, 12, 24, 42, 88]
friends = ["Kevin", "Karen", "Jim", "David", "Oscar", "Ray", "Toby"]

# .extend is the equivalent to Append but with lists, you add a list to the list
#With python's ability to store different data types in a single list, you can do something like
friends.extend(lucky_numbers)
print(friends)

friends_2 = ["Kevin", "Karen", "Jim", "David", "Oscar", "Ray", "Toby"]
friends_2.append("Michael")
print(friends_2)

#insert adds an element directly where you specify in the list, it pushes the rest to the right
friends_3 = ["Kevin", "Karen", "Jim", "David", "Oscar", "Ray", "Toby"]
friends_3.insert(1,"Cassidy")
print(friends_3)

#Could actually specify the element you're specifically looking for and not the index position
friends_3.remove("Jim")
print(friends_3)

#clear removes all elements in a list
friends_3.clear()
print(friends_3)

#Pop is like push and pop, it removes last element in the list
friends_pop = ["Green", "Blue", "Red"]
friendo = friends_pop.pop()
print(friends_pop)
print(friendo)

#index is used to search a list for the specified element
print(friends.index("Ray"))

#count actually counts how many of the same element is in the list
count_list = ["red", "blue", "blue", "green", "red", "red"]
print("red appears " + str(count_list.count("red"))+ " times")

#Sort sorts things in ascending order
friends_2.sort()
print(friends_2)

#reverse reverses the list order
friends_2.reverse()
print(friends_2)

#copy copies a list into a variable

pals = friends_2.copy()
print(pals)