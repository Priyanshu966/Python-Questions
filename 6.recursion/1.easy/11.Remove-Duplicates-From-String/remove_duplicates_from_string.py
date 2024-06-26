# Remove Duplicates Recursively
# Send Feedback
# Given a string S, remove consecutive duplicates from it recursively.
# Input Format :
# String S
# Output Format :
# Output string
# Constraints :
# 1 <= |S| <= 10^3
# where |S| represents the length of string
# Sample Input 1 :
# aabccba
# Sample Output 1 :
# abcba
# Sample Input 2 :
# xxxyyyzwwzzz
# Sample Output 2 :
# xyzwz

def remove_duplicates_main(string,i):
    if len(string) <= 1:
        return string
    if i == 0:
        return string[i]

    output = remove_duplicates_main(string,i - 1)

    if output[-1] != string[i]:
        return output + string[i]
    else:
        return output



def remove_duplicates(string):
    return remove_duplicates_main(string,len(string) - 1)


string = "aabcabssfd"
ans = remove_duplicates(string)
print(ans)
