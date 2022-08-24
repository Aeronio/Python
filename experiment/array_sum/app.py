def array_sum(given_array):
    total = 0
    for value in given_array:
        total += value
    return total

def array_2d_sum(given_array):
    total = 0
    for row in given_array:
        for value in row:
            total += value
    return total

some_array = [1,2,3,4,5]

some_2d_array =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(array_sum(some_array))
print(array_2d_sum(some_2d_array))