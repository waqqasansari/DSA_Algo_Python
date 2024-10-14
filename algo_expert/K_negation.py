import heapq

def largest_sum_after_k_negations(nums, k):
    # Create a min-heap
    min_heap = nums[:]
    print(min_heap)
    heapq.heapify(min_heap)
    print("-" * 100)
    print(min_heap)

    # Perform k modifications
    for _ in range(k):
        # Pop the smallest element
        smallest = heapq.heappop(min_heap)
        # Negate it
        heapq.heappush(min_heap, -smallest)

    # Calculate the final sum
    return sum(min_heap)

# Example usage
nums = [2, -3, -1, 5, -4]
k = 2
result = largest_sum_after_k_negations(nums, k)
print(result)  # Output should be adjusted based on the modifications