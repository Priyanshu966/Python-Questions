# // Print  *    and  1   and  1   and 1   and  1   and 1
# //        **        22       21      12       23      23
# //        ***       333      321     123      345     456
# //        ****      4444     4321    1234     4567    78910    here n = 4;


n = int(input('Enter a Natural No\n'))

# First Pattern

i = 1

while i <= n:
    j = 1
    while j <= i:
        print('*',end='')
        j = j + 1

    i = i + 1
    print('')

print('\n')

# Second Pattern

i = 1

while i <= n:
    j = 1
    while j <= i:
        print(i,end='')
        j += 1

    print('')
    i += 1

print('\n')

# Third Pattern

i = 1

while i <= n:
    j = i
    while j > 0:
        print(j,end='')
        j -= 1

    print('')
    i += 1

print('\n')


# Fourth Pattern

i = 1

while i <= n:
    j = 1
    while j <= i:
        print(j,end='')
        j += 1

    print('')
    i += 1

print('\n')


# Fifth Pattern

i = 1
count = 1

while i <= n:
    j = 1
    while j <= i:
        print(count,end='')
        count += 1
        j += 1

    print('')
    i += 1

print('\n')


