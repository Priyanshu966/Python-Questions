while(True):
    try:
        n = int(input("Enter a Natural No\n"))
        break
    except ValueError:
        print("Wrong Input, Try Again")


def getSum(n):
    if n == 0:
        return 0

    return n + getSum(n - 1)

output = getSum(n)
print(output)