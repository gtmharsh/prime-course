'''
Given a list, print all elements that appear more than once in the list.
[Hint- use sets]
'''

def print_repeat(L):
    seen = set()
    repeat = set()
    for i in L:
        if i in seen:
            repeat.add(i)
        else:
            seen.add(i)
    print(repeat)

if __name__ == "__main__":
    L = [1, 2, 3, 4, 4, 5, 5, 2, 7, 9, 7]
    print_repeat(L)