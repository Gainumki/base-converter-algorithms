# Get an empty variable that will be used for the powers
sus = 0

# Get the number to convert
print("Input the number you want to convert")
number = input()[::-1]
sum_of_digits = 0

# Convert the base10 numbers to the correct base16 digits
for digit in str(number):
    if digit == "A":
        digit = (10)
    elif digit == "B":
        digit = (11)
    elif digit == "C":
        digit = (12)
    elif digit == "D":
        digit = (13)
    elif digit == "E":
        digit = (14)
    elif digit == "F":
        digit = (15)
    
    # Complete the Algorithm
    luigi = int(digit)*pow(16, sus)
    sus = sus + 1
    sum_of_digits += luigi

# Print the Number
print("Your number in base 16 is " + str(sum_of_digits))

