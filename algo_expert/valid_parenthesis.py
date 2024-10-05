class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for b in s:
            if b in "[({":
                stack.append(b)
            else:
                if not stack or b == "]" and stack[-1] != "[" or b == ")" and stack[-1] != "(" or b == "}" and stack[-1] != "{":
                    return False
                stack.pop()
        
        return not stack




# Create an instance of the Solution class
solution = Solution()

string = "()[]{"

# Call the twoSum method
result = solution.isValid(string)

# Print the result
print(result)