input = int(input("Enter a natural No\n"))
temp = input

even_sum = 0
odd_sum = 0

i = 0

while i <= temp:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
    i = i + 1

print(f"Total sum of Odd numbers is {odd_sum}")
print(f"Total sum of Even numbers is {even_sum}")
