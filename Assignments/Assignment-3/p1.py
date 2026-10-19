'''
Ask the user for a string and check whether it is a palindrome or not.
A palindrome is a string which is same when we read it forward & backward.
Eg - "madam", "racecar" etc.

[Hint - A palindrome string is equal to the reversed version of the string.
We can use a loop to reverse the string manually.]
'''

def palindrome(s):
    if s == s[::-1]:
        print(f"{s} is a Palindrome")
    else:
        print(f"{s} is not a Palindrome")

if __name__ == "__main__":
    s = input("Enter a string: ")
    palindrome(s)