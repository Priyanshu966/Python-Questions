# Palindrome number
# Send Feedback
# Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
# Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121
# Input 2 :
# 1032
# Sample Output 2 :
# false
# Sample Input 1 :
# 121
# Sample Output 1 :
# true
# Sample

import sys
input = int(input("Enter a number\n"))

temp = input

digit_list = []

while temp > 0:
    last_digit = temp % 10
    digit_list.append(last_digit)
    temp = temp // 10

i = 0
j = len(digit_list) - 1
isPalindrome = True

while i < j:
    if digit_list[i] != digit_list[j]:
        print(False)
        sys.exit()

    i = i + 1
    j = j - 1


print(isPalindrome)


