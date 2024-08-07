# All Indices of Number
#
# Given an array of length N and an integer x, you need to find all the indexes where x is present in the input array. Save all the indexes in an array (in increasing order).
# Do this recursively. Indexing in the array starts from 0.
# Input Format :
# Line 1 : An Integer N i.e. size of array
# Line 2 : N integers which are elements of the array, separated by spaces
# Line 3 : Integer x
# Output Format :
# indexes where x is present in the array (separated by space)
# Constraints :
# 1 <= N <= 10^3
# Sample Input :
# 5
# 9 8 10 8 8
# 8
# Sample Output :
# 1 3 4

def find_index_main(arr,n, i):
    if i < 0:
        return []

    output = find_index_main(arr, n, i - 1)

    if arr[i] == n:
        output.append(i)

    return output


def find_index(arr, n):
    if len(arr) == 0:
        return []

    return find_index_main(arr, n, len(arr) - 1)


arr = [9,8,10,8,8]
n = 8
idx_arr = find_index(arr,n)

for idx in idx_arr:
    print(idx,end=' ')