def max_area(height):
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        min_height = min(height[left], height[right])
        current_area = width * min_height

        max_area = max(current_area, max_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    
    return max_area


# Example usage
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(f"Maximum area for {height1}: {max_area(height1)}")  # Output: 49