# Check AB
# Send Feedback
# Suppose you have a string, S, made up of only 'a's and 'b's. Write a recursive function that checks if the string was generated using the following rules:
# a. The string begins with an 'a'
# b. Each 'a' is followed by nothing or an 'a' or "bb"
# c. Each "bb" is followed by nothing or an 'a'
# If all the rules are followed by the given string, return true otherwise return false.
# Input format :
# String S
# Output format :
# 'true' or 'false'
# Constraints :
# 0 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# abb
# Sample Output 1 :
# true
# Sample Input 2 :
# abababa
# Sample Output 2 :
# false


def check_ab_main(string,i):
    if i == len(string):
        return True

    if string[i] == 'a' and i < len(string) - 2:
        if string[i + 1] != 'a' and string[i + 1:i + 4] != 'bb':
            return False
    if string[i] == 'a' and i == len(string) - 2:
        if string[i + 1] != 'a':
            return False
    if i < len(string) - 2 and string[i:i + 3] == 'bb':
        if string[i + 2] != 'a':
            return False

    return check_ab_main(string,i + 1)


def check_ab(string):
    if len(string) == 0:
        return False
    if string[0] != 'a':
        return False
    return check_ab_main(string,0)

string = 'abababa'
ans = check_ab(string)
print(ans)