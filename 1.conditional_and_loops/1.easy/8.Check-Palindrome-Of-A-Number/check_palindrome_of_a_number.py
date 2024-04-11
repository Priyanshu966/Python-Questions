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

temp = str(input)


i = 0
j = len(temp) - 1

while i < j:
    if temp[i] != temp[j]:
        print(False)
        sys.exit(0)
    i += 1
    j -= 1

print(True)






