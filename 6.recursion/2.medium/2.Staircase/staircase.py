# Staircase
# Send Feedback
# A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. Implement a method to count how many possible ways the child can run up to the stairs. You need to return number of possible ways W.
# Input format :
# Integer N
# Output Format :
# Integer W
# Constraints :
# 1 <= N <= 30
# Sample Input 1 :
# 4
# Sample Output 1 :
# 7
# Sample Input 2 :
# 5
# Sample Output 2 :
# 13

def count_steps(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0

    return count_steps(n - 1) + count_steps(n - 2) + count_steps(n - 3)

n = 5
ans = count_steps(n)
print(ans)