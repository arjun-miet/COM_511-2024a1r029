import math

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

sides = sorted([a, b, c])

if a + b > c and a + c > b and b + c > a:

    if math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2):
        print("It is a right-angled triangle")
    else:
        print("It is not a right-angled triangle")

    s = (a + b + c) / 2

    area = math.sqrt(s * (s-a) * (s-b) * (s-c))

    print("Area of triangle:", round(area, 2))

else:
    print("Invalid triangle")