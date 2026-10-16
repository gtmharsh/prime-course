'''
Write a function that takes two integers a and b and prints all even numbers between them (inclusive)
'''

# Method 1
# def even_numbers(a, b):
#     if a % 2 == 0:
#         for i in range(a, b+1, 2):
#             print(i)
#     else:
#         for i in range(a+1, b+1, 2):
#             print(i)

# Method 2
def even_numbers(a, b):
    if a % 2 != 0:
        a = a + 1

    for i in range(a, b + 1, 2):
        print(i)


if __name__ == "__main__":
    a = int(input("Enter first number, a = "))
    b = int(input("Enter first number, b = "))
    even_numbers(a, b)
