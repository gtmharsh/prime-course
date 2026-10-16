'''
Write a function that prints the digits of a number, n.
For eg: n = 312, there are 3 digits in it 3, 1 and 2 & we need to print them.

[HINT: The right most digit of a number N is N%10.
And to remove the right most digit from a number, we can do N = N//10] 
'''

def print_digits(n):
    L = []
    while abs(n) > 0:
        L.append(n % 10)
        n = n // 10
    L.reverse()
    print(f"The digits in the number are: {L}")


if __name__ == "__main__":
    n = int(input("Enter the number, n = "))
    print_digits(n)
    