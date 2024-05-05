arr = [[1,2,3],[4,5,6],[7,8,9],[6,5,4]]

m = len(arr)
n = len(arr[0])
lar_sum = -9999
lar_sum_index = 0

for i in range(n):
    col_sum = 0
    for j in range(m):
        col_sum += arr[j][i]
    if col_sum > lar_sum:
        lar_sum = col_sum
        lar_sum_index = n

print(lar_sum)

