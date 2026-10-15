'''
Write a program to swap values of two numbers entered by the user
'''

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print(f"Value of a is {a} and value of b is {b}")
a, b = b, a
print(f"Value of a is {a} and value of b is {b}")