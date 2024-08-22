def get_reverse_main(string,i):
    if i < 0:
        return ""

    output = get_reverse_main(string, i - 1)

    return string[i] + output




def get_reverse(string):
    if len(string) == 0:
        raise ValueError()
    return get_reverse_main(string, len(string) - 1)


while True:
    try:
        string = input("Enter a string to reverse\n")
        answer = get_reverse(string)
        print(answer)
        break
    except Exception:
        print("Wrong Input, Try Again\n")
