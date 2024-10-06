class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean_string = [a.lower() for a in s if a.isalnum()]
        print(clean_string)
        return clean_string == clean_string[::-1]


# Create an instance of the Solution class
solution = Solution()

string = "A man, a plan, a canal: Panama"

# Call the twoSum method
result = solution.isPalindrome(string)

# Print the result
print(result)