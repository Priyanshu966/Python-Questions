n = int(input("Enter a Number to Reverse\n"))

new_no = 0

while n > 0:
    last_digit = n % 10
    new_no = (new_no * 10) + last_digit
    n = n // 10


print(f"Revered NO is - {new_no}")