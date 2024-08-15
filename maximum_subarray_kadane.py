# max_so_far: Tracks the maximum sum of any subarray found so far.
# max_ending_here: Tracks the sum of the current subarray ending at the current position.
# start and end: Indices of the subarray with the maximum sum.
# temp_start: Temporary start index for the potential new subarray when max_ending_here is reset.



def kadane_algorithm(arr):
    # Handle edge cases
    if not arr:
        return 0, []

    # Initialize variables
    max_so_far = float('-inf')
    max_ending_here = 0
    start = end = 0
    temp_start = 0

    print(f"Initial array: {arr}")
    
    for i in range(len(arr)):
        max_ending_here += arr[i]

        # Print the current state
        print(f"Element {arr[i]} (Index {i}):")
        print(f"  Current max ending here: {max_ending_here}")

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = temp_start
            end = i
            print(f"  New max found:")
            print(f"    Max sum so far: {max_so_far}")
            print(f"    Subarray indices: Start={start}, End={end}")

        if max_ending_here < 0:
            max_ending_here = 0
            temp_start = i + 1
            print(f"  Resetting max ending here to 0.")
            print(f"  New potential start index: {temp_start}")

    # Return the maximum sum and the corresponding subarray
    result_subarray = arr[start:end+1]
    print(f"Final max sum subarray: {result_subarray}")
    print(f"Final max sum: {max_so_far}")
    return max_so_far, result_subarray

# Example usage
arr = [1, -2, 3, 4]
max_sum, best_subarray = kadane_algorithm(arr)
print("Maximum sum subarray:", best_subarray)
print("Maximum sum:", max_sum)