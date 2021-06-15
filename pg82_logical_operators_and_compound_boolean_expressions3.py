import math
number = int(input("Enter the numeric grade: "))
if number >=0 and number <= 100:
    print("The square root of the number you entered is: ", math.sqrt(number))
else:
    print("Error: grade must be between 100 and 0")