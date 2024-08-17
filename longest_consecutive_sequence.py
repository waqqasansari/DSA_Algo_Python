def longest_consecutive(nums):
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Only start counting if num-1 is not in the set
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Count the length of the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            # Update the maximum length
            max_length = max(max_length, current_length)
    
    return max_length

# Example usage
nums1 = [100, 4, 200, 1, 3, 2]
print(f"Length of the longest consecutive sequence in {nums1}: {longest_consecutive(nums1)}")  # Output: 4

nums2 = [0, 1, 2, 3, 4, 5, 6]
print(f"Length of the longest consecutive sequence in {nums2}: {longest_consecutive(nums2)}")  # Output: 7

nums3 = [10, 5, 2, 8, 3, 6, 4, 9, 7]
print(f"Length of the longest consecutive sequence in {nums3}: {longest_consecutive(nums3)}")  # Output: 8