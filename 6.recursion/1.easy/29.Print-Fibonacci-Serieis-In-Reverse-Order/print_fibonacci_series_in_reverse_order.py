def print_fibonacci_rev_main(n, i, j):
    if n == 1:
        return

    output = print_fibonacci_rev_main(n - 1, j, i + j)
    print(i + j,end=" ")
    return output



def print_fibonacci_rev(n):
    if n == 0:
        print(0)
        return
    print_fibonacci_rev_main(n,0,1)

    print("1 0",end=" ")


while True:
    try:
        n = int(input("Enter a positive no\n"))
        if n < 0:
            raise ValueError
        print_fibonacci_rev(n)

        break
    except ValueError:
        print("Wrong Input, Try Again")