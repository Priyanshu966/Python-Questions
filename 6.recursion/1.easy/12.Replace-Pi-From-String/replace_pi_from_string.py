def replace_pi_main(string,i):
    if i == 0:
        return ''



def replace_pi(string):
    return replace_pi_main(string,len(string) - 1)


string = "apibcpi"
ans = replace_pi(string)
print(ans)