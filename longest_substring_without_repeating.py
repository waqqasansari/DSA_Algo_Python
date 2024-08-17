def length_of_longest_substring(s):
    char_set = set()  # Set to track characters in the current window
    left = 0  # Left pointer for the window
    max_length = 0  # Variable to store the maximum length of substring
    
    for right in range(len(s)):
        while s[right] in char_set:  # While the character is a duplicate
            char_set.remove(s[left])  # Remove character from the set
            print(char_set)
            left += 1  # Contract the window from the left
        char_set.add(s[right])  # Add the new character to the set
        max_length = max(max_length, right - left + 1)  # Update the maximum length
    
    return max_length 

# Example usage
s1 = "abcabcbb"
print(f"Length of longest substring without repeating characters in '{s1}': {length_of_longest_substring(s1)}")  # Output: 3

s2 = "bbbbb"
print(f"Length of longest substring without repeating characters in '{s2}': {length_of_longest_substring(s2)}")  # Output: 1

s3 = "pwwkew"
print(f"Length of longest substring without repeating characters in '{s3}': {length_of_longest_substring(s3)}")  # Output: 3