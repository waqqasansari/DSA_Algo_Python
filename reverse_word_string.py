def reverse_word(s):
    s_clean = s.strip()
    s_list = s_clean.split()
    start = 0
    end = len(s_list) - 1
    while start < end:
        s_list[start], s_list[end] = s_list[end], s_list[start]
        start += 1
        end -= 1

    return ' '.join(s_list)

print(reverse_word("the sky is blue"))
