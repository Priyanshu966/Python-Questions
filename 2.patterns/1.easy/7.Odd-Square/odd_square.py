 # Print 13579
 #       35791
 #       57913
 #       79135
 #       91357   here n = 5

n = int(input('Please enter a Number\n'))

for i in range(1,n + 1):
    for j in range(1,n - i + 2):
        print((2 * i - 1) + (2 * j - 2),end='')
    for j in range(1,i):
        print(2 * j - 1,end='')
    print('')
