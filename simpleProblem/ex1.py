# Initial list
hat = [1, 2, 3, 4, 5]

# Step 1: Replace the middle number (index 2) with a user-inputted integer
hat[2] = int(input("Enter an integer to replace the middle number: "))

# Step 2: Remove the last element from the list
hat.pop()

# Step 3: Print the length of the existing list
print("The length of the updated list is:", len(hat))
