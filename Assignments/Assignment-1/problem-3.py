'''
Ask the user to enter two integers and one float. Convert them all to floats and print their average.
'''

a = int(input("Enter integer 1: "))
b = int(input("Enter integer 2: "))
c = float(input("Enter float: "))

a = float(a)
b = float(b)
avg = a+b+c/3

print(f"Average of the three numbers is: {avg}")