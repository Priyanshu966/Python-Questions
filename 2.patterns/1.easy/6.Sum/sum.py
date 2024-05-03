#  Print  1=1
#         1+2=3
#         1+2+3=6
#         1+2+3+4=10
#         1+2+3+4+5=15  here n = 5

n = int(input('Please Enter a Number\n'))

for i in range(1,n + 1):
    sum = 0
    for j in range(1,i + 1):
        sum += j
        print(j,end='')
        if j != i:
            print('+',end='')
        else:
            print(f'={j}')

