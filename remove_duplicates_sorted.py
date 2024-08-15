def remove_duplicates(nums):
    write_index = 1 # Initialize the write index for unique elements

    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[read_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1
    
    return write_index

# Example usage
nums = [1, 1, 2]
new_length = remove_duplicates(nums)
print(new_length)  # Output: 2
print(nums[:new_length])  # Output: [1, 2]


# PRINT STATEMENTS FOR BETTER UNDERSTANDING
# def remove_duplicates(nums):
#     if not nums:
#         return 0
    
#     write_index = 1  # Initialize the write index for unique elements
#     print(f"Initial array: {nums}")
#     print(f"Start processing. Initial write_index: {write_index}")

#     for read_index in range(1, len(nums)):
#         print(f"\nChecking element at index {read_index}: {nums[read_index]}")
#         print(f"Comparing with previous element: {nums[read_index - 1]}")
        
#         if nums[read_index] != nums[read_index - 1]:
#             nums[write_index] = nums[read_index]
#             print(f"Element is unique. Updating position {write_index} with value {nums[read_index]}")
#             write_index += 1
#         else:
#             print(f"Element is a duplicate. No change.")
        
#         print(f"Array state: {nums[:write_index]} + {nums[write_index:]}")
#         print(f"Current write_index: {write_index}")
    
#     print(f"\nFinal array: {nums[:write_index]} with length {write_index}")
#     return write_index

# # Example usage
# nums = [1, 1, 2]
# new_length = remove_duplicates(nums)
# print(f"\nNew length: {new_length}")
# print(f"Modified array: {nums[:new_length]}")