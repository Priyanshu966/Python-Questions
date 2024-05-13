def get_highest_freq_word(string):
    words = string.split()

    if len(words) <= 1:
        return string

    freq_dict = {}
    for i in words:
        freq_dict[i] = freq_dict.get(i,0) + 1

    highest_freq = -1
    highest_freq_word = ''
    for key,value in freq_dict.items():
        if value > highest_freq:
            highest_freq = value
            highest_freq_word = key

    return highest_freq_word


s = 'This sentence Contains many many words to choose from'

ans = get_highest_freq_word(s)
print(ans)