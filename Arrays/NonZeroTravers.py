def move_zeros_to_end(arr):
    j = 0  # Pointer to place the next non-zero element

    # Traverse the array
    for i in range(len(arr)):
        if arr[i] != 0:  # If element is non-zero
            arr[j] = arr[i]
            j += 1

    # Fill the remaining positions with zeros
    for i in range(j, len(arr)):
        arr[i] = 0

    return arr


# Input size of the array
n = int(input("Enter the size of the array: "))
arr = []

# Input array elements
print("Enter the elements of the array:")
for _ in range(n):
    arr.append(int(input()))

# Rearrange the array
result = move_zeros_to_end(arr)

# Output the modified array
print("Modified array:", *result)
