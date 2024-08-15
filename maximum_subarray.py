# Given an array arr[] of size N. The task is to find the sum of the contiguous subarray within a arr[] with the largest sum.
# simple brute force approach
def max_sum_subarray(arr):
    n = len(arr)
    max_sum = float('-inf')
    best_subarray = []

    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += arr[end]

            if current_sum > max_sum:
                max_sum = current_sum
                best_subarray = arr[start:end+1]
    
    return best_subarray, max_sum

# Example usage
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
best_subarray, max_sum = max_sum_subarray(arr)
print("Maximum sum subarray:", best_subarray)
print("Maximum sum:", max_sum)