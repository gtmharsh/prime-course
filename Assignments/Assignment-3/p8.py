'''
Write a program to check whether two lists share no common elements. 
# share no common elements list1 = [1, 2, 3, 4] list2 = [5, 6, 7, 8]
# share common elements list1 = [1, 2, 3] list2 = [3, 4]
[Hint - use sets]
'''

def common_ele(L1, L2):
    S1 = set(L1)
    S2 = set(L2)
    check = False
    for i in S1:
        if i in S2:
            check = True
            break
    if check:
        print(f"There are common elements in {L1} and {L2}")
    else:
        print(f"There are no common elements in {L1} and {L2}")


if __name__ == "__main__":
    L1 = [1, 2, 3, 4]
    L2 = [5, 6, 7, 8]
    L3 = [1, 2, 3]
    L4 = [3, 4]
    common_ele(L1, L2)
    common_ele(L3, L4)

    