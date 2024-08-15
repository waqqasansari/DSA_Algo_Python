# Given an array of integers and a target sum, find two elements in the array that add up to the target sum.

def two_sum(arr, target_sum):
    # Edge Case: Check if the array is empty or has only one element
    if len(arr) < 2:
        return None
    
    num_dict = {}
    
    for i, num in enumerate(arr):
        complement = target_sum - num
        print(complement)
        print(num_dict)
        # Check if the complement exists in the dictionary
        if complement in num_dict:
            return (complement, num)
        
        # Store the index of the current number in the dictionary
        num_dict[num] = i

    # If no pair is found, return None
    return None

if __name__ == "__main__":
    A = [0, -1, 2, -3, 1]
    x = -2
    print(two_sum(A, x))