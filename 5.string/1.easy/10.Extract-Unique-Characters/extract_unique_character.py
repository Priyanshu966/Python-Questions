# Extract Unique characters
# Send Feedback
# Given a string S, you need to remove all the duplicates. That means, the output string should contain each character only once. The respective order of characters should remain same, as in the input string.
# Input format:
# The first and only line of input contains a string, that denotes the value of S.
# Output format :
# The first and only line of output contains the updated string, as described in the task.
# Constraints :
# 0 <= Length of S <= 10^8
# Time Limit: 1 sec
# Sample Input 1 :
# ababacd
# Sample Output 1 :
# abcd
# Sample Input 2 :
# abcde
# Sample Output 2 :
# abcde

def get_unique(string):
    if len(string) <= 1:
        return string

    unique_dict = {}
    for i in string:
        unique_dict[i] = unique_dict.get(i,0) + 1

    unique_string = ''
    for key,value in unique_dict.items():
        unique_string += key

    return unique_string

string = 'ababacd'
ans = get_unique(string)
print(ans)