def find_fibonacci(n):
    if n == 0 or n == 1:
        return n
    elif n < 0:
        return -1


    return find_fibonacci(n - 2) + find_fibonacci(n - 1)

n = 6
ans = find_fibonacci(n)
print(ans)