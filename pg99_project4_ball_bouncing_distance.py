"""
Program: Ball Bounciness  
Author: Mike Shamblin

Compute the total total distance traveled by a bouncing ball.

1. Significant constants
        none
2. The inputs are
  
3. Computations:
        
4. The outputs are
        
"""
travt = 0
iheight = int(input("Enter initial height from which ball is dropped: "))
bounces = int(input("Enter the number of times the ball is allowed to continue bouncing: "))
travdn1 = iheight
travbackup = (iheight * 0.6)
traveldn2 = (travbackup)
while bounces != 0:10
    travt = (travdn1 + (travbackup*2))
    iheight = travt
    bounces = (bounces - 1)
print("The total travel distance is: ", travt)


