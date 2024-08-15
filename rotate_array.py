#Rotate Array : Rotate an array by a given number of positions.

def reverse_segment(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_array(arr, k):
    n = len(arr)

    # Normalize k to be within the range of the array length
    k = k % n

    # Reverse the whole array
    reverse_segment(arr, 0, n-1)
    print(arr)

    # Reverse the first k elements
    reverse_segment(arr, 0, k-1)
    print(arr)

    # Reverse the remaining elements
    reverse_segment(arr, k, n-1)
    print(arr)


# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Original array:", arr)

rotate_array(arr, k)
print("Rotated array by", k, "positions:", arr)


