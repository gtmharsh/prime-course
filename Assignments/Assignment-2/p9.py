"""
Write a function is_prime(n) that returns True if n is a prime number and False otherwise, using a loop.

[Hint - 
1. We only check prime for 2 or numbers greater than 2.  is the smallest 
prime number.
2. A  number, , will always get divided by atleast one number in 
range [2, n-1].
9 9
Eg - For number  we'll check in range (2, 8) & it'll get divided by 3. So  is 
non-prime & we'll return false for it.
For number  we'll check in range (2, 6) & it won't get divided by any. So 
is prime & we'll return true for it.]
"""

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range (2, n//2):
            if n % i == 0:
                return False

    return True

if __name__ == "__main__":
    print(is_prime(19))
    print(is_prime(51))
    print(is_prime(59))
    print(is_prime(127))
