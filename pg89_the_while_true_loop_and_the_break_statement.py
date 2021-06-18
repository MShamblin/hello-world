# The while True Loop and the break Statement
theSum = 0.0
while True:
    data = input("Enter a number of just enter to quit: ")
    if data == "":
        break
    number = float(data)
    theSum += number
print("The sum is ", theSum)
