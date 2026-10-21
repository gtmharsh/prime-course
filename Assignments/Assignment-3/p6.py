'''
Given a list of words:
words = ["apple", "banana", "kiwi", "cherry", "mango"]
Create a dictionary that maps each word to its length.
Example:
{"apple": 5, "banana": 6, "kiwi": 4, ...}
'''

if __name__ == "__main__":
    words = ["apple", "banana", "kiwi", "cherry", "mango"]
    D = {}
    for word in words:
        D[word] = len(word)

    print(D)