'''
Let's create a Simple Calculator that performs arithmetic operations.
Create a function calculator(a, b, operation) that performs addition, subtraction, multiplication, or division
based on the operation parameter.
[operation parameter can have values '+', '-', '*', '/']
'''

def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    else:
        print("Incorrect operation")
        return None

if __name__ == "__main__":
    print(calculator(10, 5, '+'))
    print(calculator(10, 5, '-'))    
    print(calculator(10, 5, '*'))    
    print(calculator(10, 5, '/'))
