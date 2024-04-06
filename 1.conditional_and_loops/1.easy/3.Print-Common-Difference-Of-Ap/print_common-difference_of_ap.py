# Arithmetic Progression
# Send Feedback
# You are given first three entries of an arithmetic progression. You have to calculate the common difference and print it.
# Input format:
# The first line of input contains an integer a (1 <= a <= 100)
# The second line of input contains an integer b (1 <= b <= 100)
# The third line of input contains an integer c (1 <= c <= 100)
# Constraints:
# Time Limit: 1 second
# Output format:
# The first and only line of output contains the result.
# Sample Input:
# 1
# 3
# 5
# Sample Output:
# 2


a = int(input("Enter 1st element of an AP\n"))
b = int(input("Enter 2nd element of an AP\n"))
c = int(input("Enter 3rd element of an AP\n"))

if (b - a) != (c - b) :
    print("Give inputs do not form an AP")
else :
    print(f"Common difference of given AP is {b - a}")

