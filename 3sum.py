def three_sum(nums):
    # Sort the array
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Avoid duplicates for the first element of the triplet
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Two pointers approach
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                
                # Move left and right pointers to the next different elements
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1

    return result

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))