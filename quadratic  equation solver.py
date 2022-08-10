import math

print("equation has to be in ax^2 + bx + c = 0: ")
a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))

x_value = b ** 2 - 4 * a * c  

if x_value < 0:
    print("The equation has no real solutions")
elif x_value == 0:
    x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print(f"The equation has one solution: {x} ")
else:
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    print(f"The equation has two solutions: {x1} or {x2}")