def reverse_inplace(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1


# Example usage
arr = [1, 2, 3, 4, 5]
print("Original array:", arr)

reverse_inplace(arr)
print("Reversed array:", arr)