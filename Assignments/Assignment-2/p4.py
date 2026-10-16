'''
Write a function to return the count the number of digits in a number, n
'''

def digit_count(n):
    return len(str(n))

if __name__ == "__main__":
    n = int(input("Enter the number, n = "))
    print(digit_count(n))