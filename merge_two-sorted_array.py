def merge_sorted_array(arr1, arr2):
    i, j = 0, 0
    merged_array = []

    #traversed both arrays and merge them
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
        
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array

ex1 = [1,3,6,4,2,7]
ex2 = [7,23,7,9,8,6]

print(merge_sorted_array(ex1, ex2))