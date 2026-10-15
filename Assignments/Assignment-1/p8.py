'''
Take the radius (r) as user input and print the area
User formula:
Area = pi * r **2       (pi = 3.14)
'''

r = float(input("Enter the value of radius of circle: "))
pi = 3.14
area = pi * r **2

print(f"The area of the circle with radius {r} is {area:.2f}")