arr = [1,2,3,4]

for i in range(0,len(arr)):
    for j in range(i + 1, len(arr)):
        print(f'{arr[i]} {arr[j]}')