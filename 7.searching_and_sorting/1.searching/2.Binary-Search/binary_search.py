arr = [1,3,5,6,7,9]
n = 6
index = -1

i = 0
j = len(arr) - 1

while i < j:
    mid = (i + j)//2
    if arr[mid] == n:
        index = mid
        break
    elif n < arr[mid]:
        j = mid - 1
    elif n > arr[mid]:
        i = mid + 1

print(index)