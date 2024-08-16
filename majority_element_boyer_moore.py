def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        # count += (1 if num == candidate else -1)
        if num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate


# Example usage
nums1 = [3, 2, 3]
print(f"Majority element in [3, 2, 3]: {majority_element(nums1)}")  # Output: 3

nums2 = [2, 2, 1, 1, 1, 2, 2]
print(f"Majority element in [2, 2, 1, 1, 1, 2, 2]: {majority_element(nums2)}")  # Output: 2