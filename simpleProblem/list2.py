numbers = [10, 5, 7, 2, 1]
print("Original list content:", numbers)  

numbers[0] = 111
print("\nPrevious list content:", numbers)  

numbers[1] = numbers[4] 
print("Previous list content:", numbers)  

print("\nList's length:", len(numbers))  

###

del numbers[1]  # Removing the second element from the list.
print("New list's length:", len(numbers))  # Printing new list length.
print("\nNew list content:", numbers)  # Printing current list content.

###
