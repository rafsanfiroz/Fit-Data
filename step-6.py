
# Sorting Information

# Sorting algorithm envisioned

# Step 1: Initialize the sorting process
def sort_list(unsorted_list):
    sorted_list = []  # Create an empty list to store the sorted values

   
    min_value = min(unsorted_list)
    
    sorted_list.append(min_value)
    return sorted_list  # Return the sorted list with the first minimum value

# Test the function with a sample list of steps
steps = [4, 2, 8]
sorted_steps = sort_list(steps)  # Call the sorting function
print(sorted_steps)  # Print the result

# Step 2: Refine the sorting process to find minimum multiple times
def sort_list(unsorted_list):
    sorted_list = []  # Initialize an empty sorted list
    # Loop through the length of the unsorted list
    for i in range(len(unsorted_list)):
        # Find the minimum value in the unsorted list
        min_value = min(unsorted_list)
        # Add the minimum value to the sorted list
        sorted_list.append(min_value)
    return sorted_list  # Return the sorted list (not yet removing values)

# Test the updated function with the same list
steps = [4, 2, 8]
sorted_steps = sort_list(steps)  # Call the sorting function
print(sorted_steps)  # Print the result

# Step 3: Improve by removing the minimum value from the unsorted list
def sort_list(unsorted_list):
    sorted_list = []  # Initialize an empty sorted list
    # Loop through the length of the unsorted list
    for i in range(len(unsorted_list)):
        # Find the minimum value in the unsorted list
        min_value = min(unsorted_list)
        # Add the minimum value to the sorted list
        sorted_list.append(min_value)
        # Remove the minimum value from the unsorted list to avoid duplicates
        unsorted_list.remove(min_value)
    return sorted_list  # Return the sorted list with all values sorted

# Test the fully developed function with the same list
steps = [4, 2, 8]
sorted_steps = sort_list(steps)  # Call the sorting function
print(sorted_steps)  # Print the result