def sum_of_unique(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]

    unique_set = set()
    for i in arr:
        unique_set.add(i)

    sum = 0
    for i in unique_set:
        sum += i

    return sum

num_list = [1,2,4,2,3,1,5,1]
ans = sum_of_unique(num_list)
print(ans)


