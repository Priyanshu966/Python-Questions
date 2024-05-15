def get_array_sum_real(arr,i):
    if i < 0:
        return 0
    elif i == 0:
        return arr[i]

    return get_array_sum_real(arr,i - 1) + arr[i]

def get_array_sum(arr):
    return get_array_sum_real(arr,len(arr) - 1)

arr = [1,2,3,4,5]
ans = get_array_sum(arr)
print(ans)