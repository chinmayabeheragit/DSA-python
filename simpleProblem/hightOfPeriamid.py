blocks = int(input("Enter the number of blocks: "))

# Initialize height and the number of blocks needed for the current layer
height = 0
layer_blocks = 1

# Build the pyramid while there are enough blocks
while blocks >= layer_blocks:
    # Increase the height by 1 for each completed layer
    height += 1
    # Subtract the blocks used for this layer from the total
    blocks -= layer_blocks
    # Move to the next layer, which requires more blocks
    layer_blocks += 1

# Print the final height of the pyramid
print("The height of the pyramid:", height)
