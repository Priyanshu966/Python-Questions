# Check Palindrome (recursive)
# Send Feedback
# Check whether a given String S is a palindrome using recursion. Return true or false.
# Input Format :
# String S
# Output Format :
# 'true' or 'false'
# Constraints :
# 0 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# racecar
# Sample Output 1:
# true
# Sample Input 2 :
# ninja
# Sample Output 2:
# false

def check_palindrome_main(string,i,j):
    if i >= j:
        return True

    if string[i] != string[j]:
        return False

    return check_palindrome_main(string,i + 1,j - 1)


def check_palindrome(string):
    return check_palindrome_main(string,0,len(string) - 1)


string = "racecar"
ans = check_palindrome(string)
print(ans)