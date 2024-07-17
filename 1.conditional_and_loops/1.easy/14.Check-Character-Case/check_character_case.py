def check_case(char):
    if char == " " or len(char) > 1:
        return "Wrong Input"

    if char >= 'a' and char <= 'z':
        return "Lower Case"
    elif char >= 'A' and char <= 'Z':
        return "Upper Case"
    else:
        return "Wrong Input"

while True:
    try:
        char = input("Please Enter a Character\n")
        output = check_case(char)
        if output == "Wrong Input":
            raise ValueError
        print(output)
        break
    except ValueError:
        print("Please enter only single alphabetical char")

