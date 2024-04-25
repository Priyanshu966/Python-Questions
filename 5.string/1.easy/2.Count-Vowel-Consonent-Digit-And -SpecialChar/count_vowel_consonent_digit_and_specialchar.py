def countChar(str):
    v,c,d,s = 0,0,0,0
    for i in str:
        if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
            i = i.lower()
            if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
                v += 1
            else:
                c += 1
        elif (i >= '0' and i <= '9'):
            d += 1
        else:
            s += 1

    return v,c,d,s


str = 'sdffk1234&*sdfj134aeioZAGH'

v,c,d,s = countChar(str)
print(f'Vowels - {v}\nConsonents - {c}\nDigits - {d}\nSpecialChar - {s}')