# Nth Fibonacci number
# Send Feedback
# Nth term of fibonacci series F(n) is calculated using following formula -
#     F(n) = F(n-1) + F(n-2),
#     Where, F(1) = F(2) = 1
# Provided N you have to find out the Nth Fibonacci Number.
# Input Format :
# Integer n
# Output Format :
# Nth Fibonacci term i.e. F(n)
# Constraints:
# 1 <= n <= 25
# Sample Input 1:
# 4
# Sample Output 2:
# 3
# Sample Input 1:
# 6
# Sample Output 2:
# 8
import sys

n = int(input("Please Enter a Number\n"))


if n <= 1:
    print(n)
    sys.exit(0)

first = 0
sec = 1
i = 2

while i <= n:
    temp = sec
    sec = first + temp
    first = temp
    i = i + 1

print(sec)
