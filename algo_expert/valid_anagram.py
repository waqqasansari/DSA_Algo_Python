# from collections import Counter
def valid_anagram(s, t):
    if len(s) !=  len(t):
        return False

    char_dict = {}

    for char in s:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    
    print(char_dict)

    for char2 in t:
        char_dict[char2] -= 1
    print(char_dict)
    
    for i in char_dict.items():
        print(i[1])
        if i[1] != 0:
            return False
    
    return True
    # return Counter(s) == Counter(t)

s = "anagram"
t = "nagaram"

print(valid_anagram(s,t))