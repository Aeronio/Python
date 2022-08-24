#two * means power, so this is 2 to the 3rd power
print(2**3)

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

#The range() basically specifies how many loops the for loop will go through
print(raise_to_power(3, 3))