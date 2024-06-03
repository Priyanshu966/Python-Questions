# Remove X
# Send Feedback
# Given a string, compute recursively a new string where all 'x' chars have been removed.
# Input format :
# String S
# Output format :
# Modified String
# Constraints :
# 1 <= |S| <= 10^3
# where |S| represents the length of string S.
# Sample Input 1 :
# xaxb
# Sample Output 1:
# ab
# Sample Input 2 :
# abc
# Sample Output 2:
# abc
# Sample Input 3 :
# xx
# Sample Output 3:

def remove_x_main(string,i):
    if i < 0:
        return ''

    output = remove_x_main(string,i - 1)

    if string[i] != 'x':
        return output + string[i]
    else:
        return output


def remove_x(string):
    return remove_x_main(string,len(string) - 1)


string = "axbx"
ans = remove_x(string)
print(ans)
