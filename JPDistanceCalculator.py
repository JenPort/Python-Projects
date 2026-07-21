# Calculate the distance between the two points using the distance formula
import math

#Prompts for user to enter coordinates
x1 = int(input("Enter x coordinate of 1st point:"))
y1 = int(input("Enter y coordinate of 1st point:"))

x2 = int(input("Enter x coordinate of 2nd point:"))
y2 = int(input("Enter y coordinate of 2nd point:"))


def distance_calc(a1, b1, a2, b2):
    d = math.sqrt((a2 - a1) ** 2 + (b2 - b1) ** 2)
    print(f"\nDistance: {d}")


distance_calc(x1, y1, x2, y2)
