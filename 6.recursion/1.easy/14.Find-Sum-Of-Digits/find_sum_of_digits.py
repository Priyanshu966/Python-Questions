# Sum of digits (recursive)
# Send Feedback
# Write a recursive function that returns the sum of the digits of a given integer.
# Input format :
# Integer N
# Output format :
# Sum of digits of N
# Constraints :
# 0 <= N <= 10^9
# Sample Input 1 :
# 12345
# Sample Output 1 :
# 15
# Sample Input 2 :
# 9
# Sample Output 2 :
# 9

def get_digit_sum(num):
    if num < 10:
        return num

    return get_digit_sum(num // 10) + (num % 10)

num = 12345
ans = get_digit_sum(num)
print(ans)
