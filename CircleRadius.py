# Write a Python program which accepts the radius of a circle from the user and computes area.

from math import pi
Radius = float(input('Enter the radius of the circle: '))
Area = pi * Radius**2
print(f"The area of the circle with radius {Radius} is: {Area}")
