# // Print       1        and     *      and    1
# //            121              ***           232
# //           12321            *****         34543
# //          1234321          *******       4567654

n = int(input("Enter a Natural No\n"))

## 1st Pattern

for i in range(1,n + 1):
    for j in range(1,n - i + 1):
        print(' ',end='')
    for j in range(1,i + 1):
        print(j,end='')
    for j in range(1, i):
        print(i - j,end='')

    print('')

print('\n')

## 2nd Pattern

for i in range(1,n + 1):
    for j in range(1,n - i + 1):
        print(' ',end='')
    for j in range(1,i + 1):
        print('*',end='')
    for j in range(1, i):
        print('*',end='')
    print('')

print('\n')

## 3rd Pattern

for i in range(1,n + 1):
    for j in range(1,n - i + 1):
        print(' ',end='')
    for j in range(1,i + 1):
        print(i + j - 1,end='')
    for j in range(1,i):
        print(2 * i - 2 - j + 1,end='')

    print('')


print('')



