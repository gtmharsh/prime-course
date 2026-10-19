'''
Input two lists of integers from the user. Merge them into one list and sort the result.
Eg -  
list1 = [1, 2, 7]
list2 = [2, 4, 5]
result = [1, 2, 3, 54, 5, 7]
'''

if __name__ == "__main__":
    list1 = [1, 2, 7]
    list2 = [2, 4, 5]

    result = list1 + list2
    result.sort()

    print(result)