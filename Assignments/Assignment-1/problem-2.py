num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2 if num2 != 0 else "undefined (division by zero)"
print(f"The sum of {num1} and {num2} is: {sum}")
print(f"The difference of {num1} and {num2} is: {difference}")
print(f"The product of {num1} and {num2} is: {product}")
print(f"The quotient of {num1}/{num2} is: {quotient}")