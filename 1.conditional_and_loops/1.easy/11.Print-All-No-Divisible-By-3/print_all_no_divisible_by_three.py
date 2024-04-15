a = int(input("Enter 1st No\n"))
b = int(input("Enter 2nd No\n"))

## First Way

# for i in range(a,b + 1):
#     if i % 3 == 0:
#         print(i)

## Optimize solution

if a % 3 == 0:
    a = a
elif a % 3 == 1:
    a += 2
else:
    a += 1

for i in range(a,b + 1,3):
    print(i)