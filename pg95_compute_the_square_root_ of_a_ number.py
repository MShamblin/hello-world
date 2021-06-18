"""
Program: square root how Sir Issac Newton figured it
Author: Mike Shamblin

Purpose:  Compute the square root of a number.

Inputs:number
Outputs:  the program's estimate of the sqaure root 
    using Newton's method of successive approximations, 
    and Python's own estimate using math.sqrt
"""

import math

# Recieve the input number from the user
x = float(input("Enter a positive number: "))

# Initialize the tolerance and estimate
tolerance = 0.000001
estimate = 1.0

# Perform the successive approximations
while True:
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        break

# Output the result
print("The program's estimate: ", estimate)
print("Python's estimate:      ", math.sqrt(x))
