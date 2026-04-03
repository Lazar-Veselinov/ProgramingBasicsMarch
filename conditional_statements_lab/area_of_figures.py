from math import pi
type = input()

if type == "square":
    side = float(input())
    print(f"{side * side:.3f}")
elif type == "rectangle":
    side1 = float(input())
    side2 = float(input())
    print(f"{side1 * side2:.3f}")
elif type == "circle":
    radius = float(input())
    print(f"{pi * radius * radius:.3f}")
elif type == "triangle":
    side = float(input())
    height = float(input())
    print(f"{side * height * 0.5:.3f}")

