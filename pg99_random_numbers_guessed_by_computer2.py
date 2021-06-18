import random
import math

count = 0
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
answer = random.randint(smaller, larger)
numberofguessesallowed = math.log(answer)
print(numberofguessesallowed)
print("The random number selected between the smaller number and the larger number is: ", answer)
compguess = random.randint(smaller, larger) 
while answer != larger or answer != smaller:
    count += 1
    print("The computer's guess is: ", compguess)  
    if compguess < answer:
        print("Too small!")
    elif compguess > answer:
        print("Too large!")
    else: 
        print("Yay! I got it in ", count, " tries!")