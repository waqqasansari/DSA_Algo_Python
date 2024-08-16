def majority_element(nums):

    count_map = {}
    n = len(nums)

    for num in nums:
        if num in count_map:
            count_map[num] += 1
        else:
            count_map[num] = 1
        
    for num, count in count_map.items():
        if count > n // 2:
            return num


# Example usage
nums1 = [3, 2, 3]
print(f"Majority element in [3, 2, 3]: {majority_element(nums1)}")  # Output: 3

nums2 = [2, 2, 1, 1, 1, 2, 2]
print(f"Majority element in [2, 2, 1, 1, 1, 2, 2]: {majority_element(nums2)}")  # Output: 2