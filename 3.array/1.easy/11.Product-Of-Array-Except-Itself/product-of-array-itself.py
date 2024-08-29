# Given an array arr[] of n integers, construct a Product Array prod[] (of the same size) such that prod[i] is equal to the product of all the elements of arr[] except arr[i].

# Input: arr[]  = {10, 3, 5, 6, 2}
# Output: prod[]  = {180, 600, 360, 300, 900}
# 3 * 5 * 6 * 2 product of other array
# elements except 10 is 180
# 10 * 5 * 6 * 2 product of other array
# elements except 3 is 600
# 10 * 3 * 6 * 2 product of other array
# elements except 5 is 360
# 10 * 3 * 5 * 2 product of other array
# elements except 6 is 300
# 10 * 3 * 6 * 5 product of other array
# elements except 2 is 900
#
#
# Input: arr[]  = {1, 2, 3, 4, 5}
# Output: prod[]  = {120, 60, 40, 30, 24 }
# 2 * 3 * 4 * 5  product of other array
# elements except 1 is 120
# 1 * 3 * 4 * 5  product of other array
# elements except 2 is 60
# 1 * 2 * 4 * 5  product of other array
# elements except 3 is 40
# 1 * 2 * 3 * 5  product of other array
# elements except 4 is 30
# 1 * 2 * 3 * 4  product of other array
# elements except 5 is 24

arr = [10,3,5,6,2]
outputArr = []

for i in range(0,len(arr)):
    temp = 1
    for j in range(0,len(arr)):

        if i != j:
            temp = temp * arr[j]

    outputArr.append(temp)

print(outputArr)
