def check_sorted_helper(arr, i):
    if len(arr) <= 1 or i >= len(arr) - 1:
        return True
    if arr[i] > arr[i + 1]:
        return False

    return check_sorted_helper(arr, i + 1)


def check_sorted(arr):
    return check_sorted_helper(arr, 0)


li = [1, 2, 3, 4, 5, 8]
ans = check_sorted(li)
print(ans)