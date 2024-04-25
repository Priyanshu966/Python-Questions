str = 'hello world'



def replaceChar(str,char1,char2):
    newStr = ''
    for i in str:
        if(i == char1):
            newStr += char2
        else:
            newStr += i

    return newStr


ans = replaceChar(str,'l','h')
print(ans)