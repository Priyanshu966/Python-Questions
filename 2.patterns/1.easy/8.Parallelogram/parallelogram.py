 # Print *****
 #        *****
 #         *****
 #          *****
 #           *****      here n = 5


n = int(input('Enter a Number\n'))

for i in range(1,n + 1):
    for j in range(1,i):
        print(' ',end='')
    for j in range(1,n + 1):
        print('*',end='')
    print('')