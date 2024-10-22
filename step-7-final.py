import numpy  
from matplotlib import pyplot  # Importing pyplot for plotting data

def read_data_in_dict(file_name):
    
    data = numpy.loadtxt(file_name, delimiter=",", dtype=str)  
    data_dict = {}
    # Iterate over each row starting from the second row (index 1)
    for i in range(1, len(data)):
        row = data[i]  # Get the current row
        name = row[0]  
        steps = numpy.array(row[1:], dtype=int)  
        data_dict[name] = steps  # Add to the dictionary
    return data_dict

def hourly_to_daily_list(hourly_list):
    daily_steps = [] 
    for i in range(0, len(hourly_list), 24):
        day_steps = hourly_list[i:i+24]  # Slice the list for 24 hours
        daily_step_count = sum(day_steps)  # Sum the hourly steps to get daily total
        daily_steps.append(daily_step_count)  # Append to daily steps list
    return daily_steps

def hourly_to_daily(hourly_dict):
    daily_dict = {}
    # Convert each user's hourly data to daily totals
    for user_name in hourly_dict:
        daily_dict[user_name] = hourly_to_daily_list(hourly_dict[user_name])
    return daily_dict

def reduce_daily_to_weekly_dict(daily_data):
    new_dict = {}
    # Sum daily steps for each user to get weekly totals
    for key in daily_data:
        new_dict[key] = sum(daily_data[key])
    return new_dict

def compile_user_steps_lists(weekly_data):
    user_names_list = []
    user_steps_list = []
    # Add user names and their corresponding weekly steps to lists
    for key in weekly_data:
        user_names_list.append(key)
        user_steps_list.append(weekly_data[key])
    return user_names_list, user_steps_list

def return_min_index(input_list):
    current_min = input_list[0]  # Start with the first element as current minimum
    min_index = 0  # Initialize minimum index
    # Iterate through the list to find the minimum value and its index
    for i in range(len(input_list)):
        if input_list[i] < current_min:
            current_min = input_list[i]
            min_index = i
    return min_index

def my_sort(user_names, user_steps):
    sorted_user_names = []
    sorted_user_steps = []
    # Sort using selection sort
    for i in range(len(user_steps)):
        min_index = return_min_index(user_steps)  # Find index of minimum step count
        sorted_user_names.append(user_names[min_index])  # Add user name to sorted list
        sorted_user_steps.append(user_steps[min_index])  # Add step count to sorted list
        user_steps[min_index] = float("inf")  # Mark this step count as used
    return sorted_user_names, sorted_user_steps

def print_sorted_info(user_names, user_steps):
    for i in range(len(user_steps)):
        print(user_names[i], "has taken", user_steps[i],
              "in the week, and stands at rank:", i)

def plot_sorted_info(user_names, user_steps):
    pyplot.bar(user_names, user_steps)  # Create a bar chart
    pyplot.show()  # Display the chart

def main():
    file_name = "steps.csv"  
    hourly_data = read_data_in_dict(file_name)  
    daily_data = hourly_to_daily(hourly_data)  
    weekly_data = reduce_daily_to_weekly_dict(daily_data)  # Sum daily data to get weekly totals
    user_names, user_steps = compile_user_steps_lists(weekly_data)  # Compile lists of names and steps
    sorted_user_names, sorted_user_steps = my_sort(user_names, user_steps)  
    print_sorted_info(sorted_user_names, sorted_user_steps)  # Print sorted info
    plot_sorted_info(sorted_user_names, sorted_user_steps)  # Plot the sorted data

main()