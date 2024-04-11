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


