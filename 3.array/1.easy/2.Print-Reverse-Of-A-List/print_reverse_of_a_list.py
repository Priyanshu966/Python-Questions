list = [1,2,3,4,5]

## First Method

# j = len(list) - 1
# i = 0
#
# while i < j:
#     temp = list[i]
#     list[i] = list[j]
#     list[j] = temp
#     i += 1
#     j -= 1
#

## Method two

list = list[::-1]






## For printing the list
print(list)


