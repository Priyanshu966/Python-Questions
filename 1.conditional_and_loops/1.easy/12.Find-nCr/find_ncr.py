#  Ncr  =   n!                      n!/ {r!*(n - r)!}
#      r!.(n - r)!  in math                          in computer
#


def fact(num):
    if num == 0:
        return 0
    product = 1
    for x in range(2,num + 1):
        product *= x
    return product


n = int(input("Please input n\n"))
r = int(input("Please input r\n"))

ncr = fact(n)/(fact(r) * fact(n - r))
print(ncr)


