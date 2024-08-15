def remove_duplicates(nums):
    write_index = 1
    count = 1
    for read_index in range(1, len(nums)):
        if nums[read_index] == nums[read_index - 1]:
            count += 1
        else:
            count = 1

        if count <= 2:
            nums[write_index] = nums[read_index]
            write_index += 1

    return write_index

# Example usage
nums = [1, 1, 1, 2, 2, 3]
new_length = remove_duplicates(nums)
print(new_length)  # Output: 5
print(nums[:new_length])  # Output: [1, 1, 2, 2, 3]