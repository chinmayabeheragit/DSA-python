# Ask the user to enter a natural number
c0 = int(input("Enter a natural number: "))

# Initialize a step counter
steps = 0

# Check if the input is a valid natural number (greater than 0)
if c0 > 0:
    # Perform the Collatz sequence
    while c0 != 1:
        print(c0)  # Print the current value of c0
        if c0 % 2 == 0:  # If c0 is even
            c0 = c0 // 2
        else:  # If c0 is odd
            c0 = 3 * c0 + 1
        steps += 1  # Increment the step counter

    # Print the final value (1) and the total number of steps
    print(c0)
    print("Total steps:", steps)
else:
    print("The input must be a natural number greater than 0.")
