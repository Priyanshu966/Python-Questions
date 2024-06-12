# Pair star
# Send Feedback
# Given a string S, compute recursively a new string where identical chars that are adjacent in the original string are separated from each other by a "*".
# Input format :
# String S
# Output format :
# Modified string
# Constraints :
# 0 <= |S| <= 1000
# where |S| represents length of string S.
# Sample Input 1 :
# hello
# Sample Output 1:
# hel*lo
# Sample Input 2 :
# aaaa
# Sample Output 2 :
# a*a*a*a

def pair_star_main(string,i):
    if len(string) == 0:
        return string
    if i < 0:
        return ''

    output = pair_star_main(string,i - 1)

    if i != len(string) - 1:
        if string[i] == string[i + 1]:
            return output + string[i] + '*'
        else:
            return output + string[i]
    else:
        return output + string[i]


def pair_star(string):
    return pair_star_main(string,len(string) - 1)


string = 'aaaa'
ans = pair_star(string)
print(ans)

