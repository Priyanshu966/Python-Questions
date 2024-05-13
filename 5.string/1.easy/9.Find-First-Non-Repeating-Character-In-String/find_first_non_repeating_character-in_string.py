# First non repeating character
# Send Feedback
# In a given string, find the first non-repeating character .You are given a string, that can contain repeating characters. Your task is to return the first character in this string that does not repeat. i.e., occurs exactly once. The string will contain characters only from English alphabet set, i.e., ('A' - 'Z') and ('a' - 'z'). If there is no non-repeating character print the first character of string.
# Input Format :
# Line 1 : A String , as mentioned above.
# Output Format :
# First non-repeating character
# Sample Input 1 :
# aDcadhc
# Sample Output 1:
# D
# Sample Input 2 :
# gdhIgHada
# Sample Output 2 :
# h

def find_first_non_repeat_char(string):
    if len(string) <= 1:
        return string

    char_dict = {}

    for i in string:
        char_dict[i] = char_dict.get(i,0) + 1

    for key,value in char_dict.items():
        if value == 1:
            return key


string = 'aDcadhc'
ans = find_first_non_repeat_char(string)
print(ans)