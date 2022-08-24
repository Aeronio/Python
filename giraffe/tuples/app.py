#The key difference between tupples and lists is that tupples are immutable, they cannot be changed once set
#They are denoted with () brackets
coordinates = (4, 5)
print(coordinates[0])
print(coordinates)

#Practical case, store data that will NEVER change in tupples
#List of tupples
coords_list = [(4, 5), (6,7), (8, 9)]
print(coords_list)
print(coords_list[1][0])