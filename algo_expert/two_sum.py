class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        com_dict = {}
        for i, num in enumerate(nums):
            complement = target - nums[i]
            print(num ,complement)
            
            if complement in com_dict:
                # print('--', com_dict[num], com_dict[complement])
                return [com_dict[complement], i]
                # return (complement, num)
            com_dict[num] = i
        print(com_dict)



# Create an instance of the Solution class
solution = Solution()

# Define your list of numbers and the target
nums = [3,2,4]
target = 6

# Call the twoSum method
result = solution.twoSum(nums, target)

# Print the result
print(result)