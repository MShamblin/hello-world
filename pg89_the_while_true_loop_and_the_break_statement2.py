# The while True Loop and the break Statement
while True:
    number = int(input("Enter the numeric grade: "))
    if number >= 0 and number <= 100:
        break
    else:
        print("Error:  grade must be between 100 a 0")
print (number) # Just echo the valid input