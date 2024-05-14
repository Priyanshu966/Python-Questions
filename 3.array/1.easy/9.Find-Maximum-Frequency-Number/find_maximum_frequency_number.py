# Maximum Frequency Number
# Send Feedback
# You are given an array of integers that contain numbers in random order. Write a program to find and return the number which occurs the maximum times in the given input.
# If two or more elements contend for the maximum frequency, return the element which occurs in the array first.
# Input Format:
# The first line of input contains an integer, that denotes the value of the size of the array. Let us denote it with the symbol N.
# The following line contains N space separated integers, that denote the value of the elements of the array.
# Output Format :
# The first and only line of output contains most frequent element in the given array.
# Constraints:
# 0 <= N <= 10^8
# Time Limit: 1 sec
# Sample Input 1 :
# 13
# 2 12 2 11 12 2 1 2 2 11 12 2 6
# Sample Output 1 :
# 2
# Sample Input 2 :
# 3
# 1 4 5
# Sample Output 2 :
# 1

def find_max_freq(num_list):
    if len(num_list) <= 1:
        return num_list

    freq_dict = {}
    for i in num_list:
        freq_dict[i] = freq_dict.get(i,0) + 1

    max_freq = -1
    max_freq_num = 0

    for key,value in freq_dict.items():
        if value > max_freq:
            max_freq = value
            max_freq_num = key

    return max_freq_num

# 2 12 2 11 12 2 1 2 2 11 12 2 6
num_list = [2,12,2,11,12,2,1,2,2,11,12,2,6]
ans = find_max_freq(num_list)
print(ans)