def is_subsequence(s, t):

    s_len, t_len = len(s), len(t)

    s_index, t_index = 0, 0

    while t_index < t_len:
        if s_index < s_len and s[s_index] == t[t_index]:
            s_index += 1
        t_index += 1
    
    return s_index == s_len


# Example usage
s1 = "abc"
t1 = "ahbgdc"
print(f"Is '{s1}' a subsequence of '{t1}'? {is_subsequence(s1, t1)}")  # Output: True

s2 = "axc"
t2 = "ahbgdc"
print(f"Is '{s2}' a subsequence of '{t2}'? {is_subsequence(s2, t2)}")  # Output: False