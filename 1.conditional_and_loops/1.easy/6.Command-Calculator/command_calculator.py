# Calculator
# Send Feedback
# Write a program that performs the tasks of a simple calculator. The program should first take an integer as input and then based on that integer perform the task as given below.
# 1. If the input is 1, then 2 integers are taken from the user and their sum is printed.
# 2. If the input is 2, then 2 integers are taken from the user and their difference(1st number - 2nd number) is printed.
# 3. If the input is 3, then 2 integers are taken from the user and their product is printed.
# 4. If the input is 4, then 2 integers are taken from the user and the quotient obtained (on dividing 1st number by 2nd number) is printed.
# 5. If the input is 5, then 2 integers are taken from the user and their remainder(1st number mod 2nd number) is printed.
# 6. If the input is 6, then the program exits.
# 7. For any other input, then print "Invalid Operation".
# Note: Each answer in next line.
# Input format:
# Take integers as input, in accordance to the description of the question.
# Constraints:
# Time Limit: 1 second
# Output format:
# The output lines must be as prescribed in the description of the question.
# Sample Input:
# 3
# 1
# 2
import sys

n = int(input("Enter a No from 1 to 6 in following order--\n1 for sum\n2 for difference\n3 for product\n4 for division\n5 for remainder\n6 for exiting\n"))

while n <= 0 and n >= 7:
    n = int(input("Invalid Operation"))

if n == 6:
    print("exiting the program")
    sys.exit(0)

input1 = int(input("Enter 1st number- "))
input2 = int(input("Enter 2nd number- "))

if n == 1:
    print(input1 + input2)
elif n == 2:
    print(input1 - input2)
elif n == 3:
    print(input1 * input2)
elif n == 4:
    print(input1 / input2)
else:
    print(input1 % input2)
