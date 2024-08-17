def is_anagram(s, t):
    return sorted(s) == sorted(t)

# Example usage
s1 = "anagram"
t1 = "nagaram"
print(f"Is '{t1}' an anagram of '{s1}': {is_anagram(s1, t1)}")  # Output: True

s2 = "rat"
t2 = "car"
print(f"Is '{t2}' an anagram of '{s2}': {is_anagram(s2, t2)}")  # Output: False