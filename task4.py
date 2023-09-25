#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912
import math
print("Finds the surface area of a cone")
r = int(input("what is the radius: "))
h = int(input("what is the hight: "))
l = math.sqrt(math.pow(r,2) + math.pow(h,2))
sa = (math.pi * math.pow(r,2)) + (math.pi * r * l)
print(f"the surface area of the cone is {round(sa,2)}cm2")