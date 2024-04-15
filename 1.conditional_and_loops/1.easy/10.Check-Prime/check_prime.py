n = int(input("Enter a Natural No\n"))

for i in range(2,n):
    if n % i == 0:
        print("Not a prime No")
        break
else:
    print("It is a prime")