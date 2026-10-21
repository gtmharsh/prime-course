'''
Write a program that takes a string from the user and prints the number of 
spaces in the string
'''

def count_space(S):
    count = 0
    for i in S:
        if i == ' ':
            count += 1
    print(f"The string you entered has {count} spaces in it")

if __name__ == "__main__":
    S = input("Enter a string: ")
    count_space(S)