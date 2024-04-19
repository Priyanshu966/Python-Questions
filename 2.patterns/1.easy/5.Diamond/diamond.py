#  Print    *
#          ***
#         *****
#          ***
#           *        here n = 5


n = int(input("Enter a odd No\n"))

half = n // 2 + 1

## For first half
i = 1

while i <= half:
    j = 1
    k = 1
    l = 1
    while j <= half - i:
        print(' ',end='')
        j += 1
    while k <= i:
        print('*',end='')
        k += 1
    while l <= i - 1:
        print('*',end='')
        l += 1
    i += 1
    print('')

## For second half

m = 1

while m <= half - 1:
    j = 1
    k = 1
    l = 1
    while j <= m:
        print(' ',end='')
        j += 1
    while k <= half - m:
        print('*',end='')
        k += 1
    while l <= half - 1 - m :
        print('*',end='')
        l += 1
    m += 1
    print('')



