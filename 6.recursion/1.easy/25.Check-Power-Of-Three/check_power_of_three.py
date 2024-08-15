# Given an integer n, return true if it is a power of three.Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.
#
# Example
# 1:
#
# Input: n = 27
# Output: true
# Explanation: 27 = 33
#
# Example
# 2:
#
# Input: n = 0
# Output: false
# Explanation: There is no
# x
# where
# 3
# x = 0.
#
# Example
# 3:
#
# Input: n = -1
# Output: false
# Explanation: There is no
# x
# where
# 3
# x = (-1).
#
# Constraints:
#
# -231 <= n <= 231 - 1

def check_power_of_three_main(n):
    if n == 1:
        return True

    if n % 3 != 0:
        return False
    else:
        return check_power_of_three_main(n // 3)


def check_power_of_three(n):
    if n == 0:
        return False
    if n % 3 != 0:
        return False

    return check_power_of_three_main(n)


while True:
    try:
        n = int(input("Enter a Natural No\n"))
        if n < 0:
            raise ValueError
        ans = check_power_of_three(n)
        print(ans)
        break
    except Exception:
        print("Wrong Input, Try Again\n")
