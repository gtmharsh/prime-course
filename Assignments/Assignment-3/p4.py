'''
 Given a tuple of integers, create:
• A tuple of all even numbers
• A tuple of all odd numbers
'''

def odd_even_tuple(T):
    even = tuple(num for num in T if num % 2 == 0)
    odd = tuple(num for num in T if num % 2 != 0)

    return even, odd

if __name__ == "__main__":
    T = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    even, odd = odd_even_tuple(T)
    print(f"The even tuple is {even}")
    print(f"The odd tuple is {odd}")