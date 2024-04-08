n = int(input("Enter a Natural No\n"))

while n < 0:
    n = int(input("Wrong Input - (Please Enter again)\n"))



i = 1
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print(f'Sum of {n} Natural no is - {sum}')


