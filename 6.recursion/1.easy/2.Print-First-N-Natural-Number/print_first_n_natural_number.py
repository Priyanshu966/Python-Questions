def print_first_n_natural_no(n):
    if n <= 0:
        print(-1)
        return
    elif n == 1:
        print(n)
        return

    print_first_n_natural_no(n - 1)
    print(n)

n = int(input('Please Enter a Natural No\n'))
print_first_n_natural_no(n)
