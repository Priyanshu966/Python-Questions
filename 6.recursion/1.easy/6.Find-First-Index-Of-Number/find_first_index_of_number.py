def find_first_index_helper(arr,num,i):
    if len(arr) == 0 or i >= len(arr):
        return -1

    if arr[i] == num:
        return i

    return find_first_index_helper(arr,num,i + 1)


def find_first_index(arr,num):
    return find_first_index_helper(arr,num,0)


arr = [4,6,3,2,9,6,9,3,1]
num = 3

ans = find_first_index(arr,num)
print(ans)