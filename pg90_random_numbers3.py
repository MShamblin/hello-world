import random
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
answer = random.randint(smaller, larger)
count = 0
while answer != larger or answer != smaller:
    count += 1
    compNumber = int("The computer guesses... : ", random.randint(smaller, larger))
    if answer < compNumber:
        print("Too small!")
    elif answer > compNumber:
        print("Too large!")
    else:
        print("Yay! I got it in ", count, " tries!")
        break