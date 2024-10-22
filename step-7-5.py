# Sorting the lists according to steps

import numpy
def read_data_in_dict(file_name):
    
    # The data is separated by commas (delimiter=",") and all values are read as strings (dtype=str)
    data = numpy.loadtxt(file_name, delimiter=",", dtype=str)
    
    data_dict = {}  # Initialize an empty dictionary to store the data

    # Loop through each row of data starting from index 1 to skip the header row
    for i in range(1, len(data)):
        row = data[i]  # Get the current row of data
        name = row[0]  # The first element is the name (e.g., a person's name)
        
        # Convert the remaining elements of the row to an integer array for steps
        steps = numpy.array(row[1:], dtype=int)
        
        # Store the name as the key and steps as the value in the dictionary
        data_dict[name] = steps
    
    return data_dict  



def hourly_to_daily_list(hourly_list):
    daily_steps = []  # Initialize an empty list to store daily step counts
    # Iterate over the hourly list in chunks of 24 (for each day)
    for i in range(0, len(hourly_list), 24):
        day_steps = hourly_list[i:i+24]  # Get the steps for the current day
        daily_step_count = sum(day_steps)  # Sum the hourly steps to get the daily total
        daily_steps.append(daily_step_count)  # Add the daily total to the list
    return daily_steps 


def hourly_to_daily(hourly_dict):
    daily_dict = {}
    # Loop through each user in the hourly data dictionary
    for user_name in hourly_dict:
        # Convert hourly steps to daily steps for each user and store it in the new dictionary
        daily_dict[user_name] = hourly_to_daily_list(hourly_dict[user_name])
    return daily_dict  


def reduce_daily_to_weekly_dict(daily_data):
    new_dict = {} 
   
    for key in daily_data:
        # Sum the daily steps for each user to get their total weekly steps
        new_dict[key] = sum(daily_data[key])
    return new_dict  


def compile_user_steps_lists(weekly_data):
    user_names_list = []  # Initialize an empty list for user names
    user_steps_list = []  # Initialize an empty list for user steps
    # Loop through each user in the weekly data dictionary
    for key in weekly_data:
        user_names_list.append(key)  # Add the user's name to the names list
        user_steps_list.append(weekly_data[key])  # Add the user's total weekly steps to the steps list
    return user_names_list, user_steps_list  

def return_min_index(input_list):
    current_min = input_list[0]  
    min_index = 0  # Initialize the index of the minimum value
    # Loop through the input list to find the minimum value and its index
    for i in range(len(input_list)):
        if input_list[i] < current_min:
            current_min = input_list[i]  # Update current minimum
            min_index = i  # Update the index of the minimum value
    return min_index  # Return the index of the minimum value


def my_sort(user_names, user_steps):
    sorted_user_names = []  # Initialize an empty list for sorted user names
    sorted_user_steps = []  # Initialize an empty list for sorted user steps
    # Loop to sort the user steps using a selection sort method
    for i in range(len(user_steps)):
        min_index = return_min_index(user_steps)  # Find the index of the minimum step count
        sorted_user_names.append(user_names[min_index])  # Add the corresponding user name to the sorted list
        sorted_user_steps.append(user_steps[min_index])  # Add the corresponding step count to the sorted list
        user_steps[min_index] = float("inf")  # Mark the minimum step count as "infinity" to exclude it in the next iteration
    return sorted_user_names, sorted_user_steps  


def main():
    file_name = "steps.csv"  
    hourly_data = read_data_in_dict(file_name)  # Read hourly data into a dictionary
    daily_data = hourly_to_daily(hourly_data)  # Convert hourly data to daily totals
    weekly_data = reduce_daily_to_weekly_dict(daily_data)  # Sum daily data to get weekly totals
    user_names, user_steps = compile_user_steps_lists(weekly_data)  # Compile user names and their weekly steps
    sorted_user_names, sorted_user_steps = my_sort(user_names, user_steps)  # Sort users by their weekly step counts
    print(sorted_user_steps, sorted_user_names)  # Print the sorted step counts and user names



main()  