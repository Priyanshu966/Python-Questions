arr = [3,5,2,8,1,9,4,7,6]

for i in range(len(arr)):
    min_no = arr[i]
    min_index = i
    for j in range(i + 1,len(arr)):
        if arr[j] < min_no:
            min_no = arr[j]
            min_index = j

    arr[min_index] = arr[i]
    arr[i] = min_no

print(arr)

