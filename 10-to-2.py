# Set up loop and list
loop = 0
lst = []

# Get the number to convert
num = int(input("Enter a number: "))

# Check if the number can be divided by two
while loop == 0:
    if (num % 2) == 0:
        resto = 0
    else:
        resto = 1
        
    # Save the results in the list    
    lst.append(str(resto))
    
    # Divide by two
    num = (num - resto)/2
    
    # Stop the algorithm when number is 0
    if (num == 0):
        loop = 1
        lst.reverse()
        print(''.join(lst))
