def is_valid(s):
    stack = []
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for char in s:
        print(char, stack)
        if char in pairs.keys():
            top_element = stack.pop() if stack else '#'
            if top_element != pairs[char]:
                return False
        else:
            stack.append(char)
    
    return len(stack) == 0


print(is_valid("(((())))"))         # True
print(is_valid("()[]{}"))     # True
print(is_valid("(]"))         # False
print(is_valid("([)]"))       # False
print(is_valid("{[]}"))       # True