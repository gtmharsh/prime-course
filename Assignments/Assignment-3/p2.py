'''
Given a list of integers compute the average of all numbers in the list
'''

def avg(L):
    sum = 0
    for i in L:
        sum += i
    return sum/len(L)

if __name__ == "__main__":
    avg = avg([7, 13, 15, 23, 12])
    print(avg)