def get_sum(arr,i):
    if i < 0:
        return 0

    return arr[i] + get_sum(arr, i - 1)


def get_mean(arr):
    if len(arr) == 0:
        return 0
    arr_sum = get_sum(arr, len(arr) - 1)
    return arr_sum / len(arr)


arr = [1,2,3,4,5]
ans = get_mean(arr)
print(ans)