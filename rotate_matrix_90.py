def rotate_matrix_90_clockwise(matrix):
    # Step 1: Transpose the matrix
    transposed_matrix = [list(row) for row in zip(*matrix)]
    
    # Step 2: Reverse each row of the transposed matrix
    rotated_matrix = [row[::-1] for row in transposed_matrix]
    
    return rotated_matrix

# Example usage:

# Matrix 1
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Matrix 2
matrix2 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# Rotate and print the result
rotated_matrix1 = rotate_matrix_90_clockwise(matrix1)
rotated_matrix2 = rotate_matrix_90_clockwise(matrix2)

print("Rotated Matrix 1:")
for row in rotated_matrix1:
    print(row)

print("\nRotated Matrix 2:")
for row in rotated_matrix2:
    print(row)