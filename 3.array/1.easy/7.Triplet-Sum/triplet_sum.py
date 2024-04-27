# Triplet Sum
# Send Feedback
# You have been given a random integer array/list(ARR) and a number X. Find and return the number of triplets in the array/list which sum to X.
# Note :
# Given array/list can contain duplicate elements.
# Input format :
# The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
#
# First line of each test case or query contains an integer 'N' representing the size of the first array/list.
#
# Second line contains 'N' single space separated integers representing the elements in the array/list.
#
# Third line contains an integer 'X'.
# Output format :
# For each test case, print the total number of triplets present in the array/list.
#
# Output for every test case will be printed in a separate line.
# Constraints :
# 1 <= t <= 50
# 0 <= N <= 10^2
# 0 <= X <= 10^9
# Time Limit: 1 sec
# Sample Input 1:
# 1
# 7
# 1 2 3 4 5 6 7
# 12
# Sample Output 1:
# 5
# Sample Input 2:
# 2
# 7
# 1 2 3 4 5 6 7
# 19
# 9
# 2 -5 8 -6 0 5 10 11 -3
# 10
# Sample Output 2:
# 0
# 5

arr = [2,-5,8,-6,0,5,10,11,-3]

sum = 10
total = 0

i = 0

while i < len(arr):
    j = i + 1
    while j < len(arr):
        k = j + 1
        while k < len(arr):
            if arr[i] + arr[j] + arr[k] == sum:
                total += 1
            k += 1
        j += 1
    i += 1

print(total)

