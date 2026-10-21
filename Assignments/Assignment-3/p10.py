'''
Ask the user for a string and print:
• All unique characters
• The count of unique characters
'''

def unique_char(S):
    unique = set(S)
    count = len(unique)
    print(f"These are {count} unique characters that are: {unique}")

if __name__ == "__main__":
    S = input("Please enter a string: ")
    unique_char(S)