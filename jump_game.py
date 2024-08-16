def can_jump(nums):
    max_reachable = 0

    for i in range(len(nums)):
        if i > max_reachable:
            return False
        
        max_reachable = max(max_reachable, i + nums[i])

        if max_reachable >= len(nums) - 1:
            return True
        
    return False
    
# Example usage
nums1 = [2, 3, 1, 1, 4]
print(f"Can jump to the end for [2, 3, 1, 1, 4]: {can_jump(nums1)}")  # Output: True

nums2 = [3, 2, 1, 0, 4]
print(f"Can jump to the end for [3, 2, 1, 0, 4]: {can_jump(nums2)}")  # Output: False