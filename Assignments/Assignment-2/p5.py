'''
Write a function to return the sum of digits of a number, n.
'''
# Method 1
# def digit_sum(n):
#     sum = 0
#     for i in str(n):
#         sum += int(i)
#     return sum


# Method 2 (Pythonic way)
def digit_sum(n):
    return sum(int(digit) for digit in str(n))

if __name__ == "__main__":
    n = int(input("Enter the number, n = "))
    print(digit_sum(n))