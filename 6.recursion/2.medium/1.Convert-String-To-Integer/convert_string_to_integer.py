# String to Integer
# Send Feedback
# Write a recursive function to convert a given string into the number it represents. That is input will be a numeric string that contains only numbers, you need to convert the string into corresponding integer and return the answer.
# Input format :
# Numeric string S (string, Eg. "1234")
# Output format :
# Corresponding integer N (int, Eg. 1234)
# Constraints :
# 0 <= |S| <= 9
# where |S| represents length of string S.
# Sample Input 1 :
# 00001231
# Sample Output 1 :
# 1231
# Sample Input 2 :
# 12567
# Sample Output 2 :
# 12567


def str_to_int_main(string,i):
    if len(string) == 0:
        return 0
    if i == 0:
        return ord(string[i]) - ord('0')

    output = str_to_int_main(string,i - 1)

    current_digit = ord(string[i]) - ord('0')
    return output * 10 + current_digit


def str_to_int(string):
    return str_to_int_main(string,len(string) - 1)


string = '12567'
ans = str_to_int(string)
print(ans)
print(type(ans))

