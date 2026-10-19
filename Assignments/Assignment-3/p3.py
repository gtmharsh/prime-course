'''
Input two lists of integers from the user. Merge them into one list and sort the result.
Eg -  
list1 = [1, 2, 7]
list2 = [2, 4, 5]
result = [1, 2, 3, 54, 5, 7]
'''

def merge_and_sort(L1, L2):
    result = L1 + L2
    result.sort()
    return result

if __name__ == "__main__":
    L1 = [1, 2, 7]
    L2 = [2, 4, 5]

    print(merge_and_sort(L1, L2))