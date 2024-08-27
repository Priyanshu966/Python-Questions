def print_fibonacci_rev_main(n, i, j):
    if n == 1:
        return

    print(i + j,end=" ")

    return print_fibonacci_rev_main(n - 1, j, i + j)



def print_fibonacci_rev(n):
    if n == 0:
        print(0)
        return
    else:
        print(0,1,end=" ")
    return print_fibonacci_rev_main(n,0,1)


while True:
    try:
        n = int(input("Enter a positive no\n"))
        if n < 0:
            raise ValueError
        print_fibonacci_rev(n)

        break
    except ValueError:
        print("Wrong Input, Try Again")