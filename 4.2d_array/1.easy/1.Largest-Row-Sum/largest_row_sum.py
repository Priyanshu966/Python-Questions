arr = [[1,2,3],[4,5,6],[7,8,9],[6,5,4]]

m = len(arr)
n = len(arr[0])

lar_row_sum = -9999
lar_sum_row = -1
for i in range(m):
    row_sum = 0
    for j in range(n):
        row_sum += arr[i][j]
    if row_sum > lar_row_sum:
        lar_row_sum = row_sum
        lar_sum_row = i

print(f'Largest row is {lar_sum_row} with sum {lar_row_sum}')

