arr = [3,4,1,9,7,5,2]
n = 7
index = -1

for i in range(len(arr)):
    if arr[i] == n:
        index = i
        break;

print(index)
