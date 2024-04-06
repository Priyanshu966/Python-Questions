# print ****  1234  1111 4321
#       ****  1234  2222 4321
#       ****  1234  3333 4321
#       ****  1234  4444 4321

n = int(input("Enter a Natural No\n"))

## 1st Pattern
i = 1;

while i <= n :
    j = 1
    while j <= n :
        print("*",end = '')
        j = j + 1

    print('')
    i = i + 1

print('\n')

## 2nd Pattern
i = 1

while i <= n :
    j = 1
    while j <= n :
        print(j,end = '')
        j = j + 1

    print()
    i = i + 1

print('\n')

## 3rd Pattern

i = 1

while i <= n :
    j = 1
    while j <= n :
        print(i,end = '')
        j = j + 1

    i = i + 1
    print('')

print('\n')

## 4th Pattern
i = 1

while i <= n :
    j = n
    while j > 0 :
        print(j,end = '')
        j = j - 1

    i = i + 1
    print('')

print('\n')

## 5th Pattern



