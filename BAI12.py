import math

x = float(input("x = "))
y = float(input("y = "))
a = float(input("a = "))
b = float(input("b = "))
R = float(input("R = "))

d = math.sqrt((x - a)**2 + (y - b)**2)

if d <= R:
    print(True)
else:
    print(False)