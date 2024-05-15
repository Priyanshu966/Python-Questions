def get_power(x,y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y == -1:
        return 1/2

    is_negative = False

    if y < 0:
        y = -1 * y
        is_negative = True
    if is_negative == True:
        return 1 / (get_power(x,y - 1) * x)

    return get_power(x,y - 1) * x

ans = get_power(3,-2)
print(ans)