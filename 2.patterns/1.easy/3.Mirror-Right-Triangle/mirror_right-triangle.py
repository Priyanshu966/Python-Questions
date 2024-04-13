# print ****  and     *   and   1   and  ****   and  4444
#        ***         **        12        ***         333
#         **        ***       123        **          22
#          *       ****      1234        *           1


n = int(input("Enter a Natural No\n"))

## 1st Pattern

i = 1

while i <= n:
    j = 1
    k = 1
    while j <= i - 1:
        print(' ',end='')
        j += 1

    while k <= n + 1 - i:
        print('*',end='')
        k += 1

    print('')
    i += 1

print('\n')

## 2nd Pattern

i = 1

while i <= n:
    j = 1
    k = 1
    while j <= n - i:
        print(' ',end='')
        j += 1

    while k <= i:
        print('*',end='')
        k += 1
    print('')
    i += 1

print('\n')


## 3rd Pattern

i = 1

while i <= n:
    j = 1
    k = 1
    while j <= n - i:
        print(' ',end='')
        j += 1

    while k <= i:
        print(k,end='')
        k += 1
    print('')
    i += 1

print('\n')

## 4th Pattern

i = 1

while i <= n:
    j = 1
    k = 1

    while k <= n + 1 - i:
        print('*',end='')
        k += 1

    print('')
    i += 1

print('\n')

## 5th Pattern

i = 1

while i <= n:
    j = 1
    k = 1

    while k <= n + 1 - i:
        print(n - i + 1,end='')
        k += 1

    print('')
    i += 1

print('\n')


