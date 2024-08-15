def is_palindrome(s):
    # print(s)
    if s == s[::-1]:
        return True

s1 = "aaabbaaa"   
print(is_palindrome(s1))