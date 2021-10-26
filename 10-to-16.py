# Import the math library and set up loop and list
import math
loop = 0
lst = []

# Digits we don't need
dontneed = [10, 11, 12, 13, 14, 15]

# Get the number to convert
num = int(input("Enter a number: "))

# Perform the algorithm and save results in list
while loop == 0:
    resto = num - math.trunc(num/16)*16
    num = (math.trunc(num/16))
    if resto not in dontneed:
        lst.append(str(resto))
    elif resto == 10:
        lst.append("A")
    elif resto == 11:
        lst.append("B")
    elif resto == 12:
        lst.append("C")
    elif resto == 13:
        lst.append("D")
    elif resto == 14:
        lst.append("E")
    elif resto == 15:
        lst.append("F")
        
    # End the algorithm and print the result
    if num == 0:
        loop = 1
        lst.reverse()
        print(''.join(lst))
