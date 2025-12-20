import math


x=int(input("Enter the x value"))
y=int(input("Enter the y value"))

distance = math.sqrt(x*x + y*y)

print(f"The Euclidean distance from the point (x, y) to the origin (0, 0) is {distance:.3f}")