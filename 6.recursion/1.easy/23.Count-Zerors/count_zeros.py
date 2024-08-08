# Count Zeros
#
# Given an integer N, count and return the number of zeros that are present in the given integer using recursion.
# Input Format :
# Integer N
# Output Format :
# Number of zeros in N
# Constraints :
# 0 <= N <= 10^9
# Sample Input 1 :
# 10204
# Sample Output 1 :
# 2
# Sample Input 2 :
# 708000
# Sample Output 2 :
# 4

def count_zeros(n):
    if n < 10:
        if n == 0:
            return 1
        else:
            return 0

    output = count_zeros(n // 10)

    if n % 10 == 0:
        return output + 1
    else:
        return output


while True:
    try:
        n = int(input("Enter a Positive Integral No\n"))

        if n < 0:
            raise ValueError
        break
    except Exception:
        print("Wrong Input, Plz Try Again")

answer = count_zeros(n)
print(answer)
