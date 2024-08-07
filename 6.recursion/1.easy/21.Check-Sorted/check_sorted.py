arr = [1,2,3,4,8,5,9]

def check_sorted_main(arr,i):
    if i == 0:
        return True

    if arr[i] < arr[i - 1]:
        return False

    return check_sorted_main(arr, i - 1)

def check_sorted(arr):
    if len(arr) == 0 or len(arr) == 1:
        return True
    return check_sorted_main(arr,len(arr) - 1)


output = check_sorted(arr)
if output:
    print("Array is Sorted")
else:
    print("Array is not Sorted")
