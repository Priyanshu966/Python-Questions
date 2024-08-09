# Replace Character Recursively
#
# Given an input string S and two characters c1 and c2, you need to replace every occurrence of character c1 with character c2 in the given string.
# Do this recursively.
# Input Format :
# Line 1 : Input String S
# Line 2 : Character c1 and c2 (separated by space)
# Output Format :
# Updated string
# Constraints :
# 1 <= Length of String S <= 10^6
# Sample Input :
# abacd
# a x
# Sample Output :
# xbxcd

def replace_char_main(string, a, b, i):
    if i < 0:
        return ""

    output = replace_char_main(string, a, b, i - 1)

    if string[i] == a:
        return output + b
    else:
        return output + string[i]


def replace_char(string, a, b):
    return replace_char_main(string, a, b, len(string) - 1)

while True:
    try:
        string = str(input("Enter a string\n"))
        break
    except Exception:
        print("Wrong input, Try Again")

while True:
    try:
        char1 = str(input("Enter a Character to replace\n"))[:1]
        break
    except Exception:
        print("Wrong input, Try Again")

while True:
    try:
        char2 = str(input("Enter a Character to replace with the previous\n"))[:1]
        break
    except Exception:
        print("Wrong input, Try Again")

answer = replace_char(string, char1, char2)
print(answer)

