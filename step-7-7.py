# Plotting sorted info (name, steps, rank)


import numpy  # Importing numpy for numerical operations
from matplotlib import pyplot  # Importing pyplot for plotting data

def read_data_in_dict(file_name):
    data = numpy.loadtxt(file_name, delimiter=",", dtype=str)  # Load data from CSV
    data_dict = {}
    # Iterate over rows starting from the second row (index 1)
    for i in range(1, len(data)):
        row = data[i]  # Get the current row
        name = row[0]  # First column is the user name
        steps = numpy.array(row[1:], dtype=int)  # Convert remaining columns to integers
        data_dict[name] = steps  # Add to dictionary
    return data_dict

def hourly_to_daily_list(hourly_list):
    """Converts a list of hourly steps into daily total steps."""
    daily_steps = []
    # Process each day (24-hour intervals)
    for i in range(0, len(hourly_list), 24):
        day_steps = hourly_list[i:i+24]  # Slice for 24 hours
        daily_step_count = sum(day_steps)  # Sum the hourly steps for the day
        daily_steps.append(daily_step_count)  # Add to daily list
    return daily_steps

def hourly_to_daily(hourly_dict):
    
    daily_dict = {}
    for user_name in hourly_dict:
        daily_dict[user_name] = hourly_to_daily_list(hourly_dict[user_name])  # Convert each user's data
    return daily_dict

def reduce_daily_to_weekly_dict(daily_data):
    """Summarizes daily data into weekly totals for each user."""
    new_dict = {}
    for key in daily_data:
        new_dict[key] = sum(daily_data[key])  # Sum daily steps to get weekly total
    return new_dict

def compile_user_steps_lists(weekly_data):
    """Compiles user names and their weekly step counts into separate lists."""
    user_names_list = []
    user_steps_list = []
    for key in weekly_data:
        user_names_list.append(key)  # Add user name to list
        user_steps_list.append(weekly_data[key])  # Add corresponding step count
    return user_names_list, user_steps_list

def return_min_index(input_list):
    """Finds the index of the minimum value in a list."""
    current_min = input_list[0]  # Start with the first element
    min_index = 0  
    # Iterate through the list to find the minimum
    for i in range(len(input_list)):
        if input_list[i] < current_min:  # If current value is less than current_min
            current_min = input_list[i]  # Update current_min
            min_index = i  # Update min_index
    return min_index

def my_sort(user_names, user_steps):
    sorted_user_names = []
    sorted_user_steps = []
    # Sort using selection sort
    for i in range(len(user_steps)):
        min_index = return_min_index(user_steps)  # Find index of minimum step count
        sorted_user_names.append(user_names[min_index])  # Add to sorted names list
        sorted_user_steps.append(user_steps[min_index])  # Add to sorted steps list
        user_steps[min_index] = float("inf")  # Mark this step count as used
    return sorted_user_names, sorted_user_steps

def print_sorted_info(user_names, user_steps):
    for i in range(len(user_steps)):
        print(user_names[i], "has taken", user_steps[i],
              "in the week, and stands at rank:", i)

def plot_sorted_info(user_names, user_steps):
    """Plots a bar graph of user step counts."""
    pyplot.bar(user_names, user_steps)  # Create a bar chart
    pyplot.show()  # Display the chart

def main():
    file_name = "steps.csv"  
    hourly_data = read_data_in_dict(file_name)  
    daily_data = hourly_to_daily(hourly_data)  
    weekly_data = reduce_daily_to_weekly_dict(daily_data)  
    user_names, user_steps = compile_user_steps_lists(weekly_data) 
    sorted_user_names, sorted_user_steps = my_sort(user_names, user_steps)  
    print_sorted_info(sorted_user_names, sorted_user_steps) 
    plot_sorted_info(sorted_user_names, sorted_user_steps)  

main()