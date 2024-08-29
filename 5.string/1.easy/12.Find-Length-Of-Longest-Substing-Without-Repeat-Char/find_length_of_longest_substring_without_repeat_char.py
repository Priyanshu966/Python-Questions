# Example 1:
#
# Input: s = ”abcabcbb”
#
# Output: 3
#
# Explanation: The answer is abc with length of 3.
#
# Example 2:
#
# Input: s = ”bbbbb”
#
# Output: 1
#
# Explanation: The answer is b with length of 1 unit
#
# string = input("Enter a string")

def find_longest_len_substring_main(string,i):
    if i < 0:
        return ""

    output = find_longest_len_substring_main(string,i - 1)

    is_repeat = False

    for j in output:
        if string[i] == j:
            is_repeat = True
            break

    if is_repeat == False:
        return output + string[i]
    else:
        return output

def find_longest_len_substring(string):
    return find_longest_len_substring_main(string,len(string) - 1)

string = input("Enter string\n")
answer = find_longest_len_substring(string)
print(f"Longest sting - {answer}\nLength - {len(answer)}")