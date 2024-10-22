# Visualizing data

'''
With data all stored in appropriate data structures, start working on requirement 4, which is the main gist of this project.

Line plot for a day’s activity
For this requirement, pick a 24-value portion for any user and plot it using the matplotlib library. Start with the line plot for a particular user on a particular day.
'''

import numpy  # Importing the numpy library for numerical operations
from matplotlib import pyplot  # Importing pyplot from matplotlib for plotting

def data_to_dict(data):
    # Initialize an empty dictionary to store member names and their corresponding hourly steps
    data_dict = {}
    
    
    for i in range(1, len(data)):
        row = data[i]  # Get the current row of data
        name = row[0]  # The first element in the row is the member's name
        steps = numpy.array(row[1:], dtype=int)
        # Add a key-value pair to the dictionary: member name -> array of steps
        data_dict[name] = steps
    
    return data_dict  # Return the populated dictionary

def hourly_to_daily(hourly_steps):
    # Initialize a list to store daily step counts
    daily_steps = []
    
    # Iterate through the hourly steps in chunks of 24 (representing one day)
    for i in range(0, len(hourly_steps), 24):
        day_steps = hourly_steps[i:i+24]  # Get the steps for the current day (24 hours)
        daily_step_count = sum(day_steps)  # Sum the hourly steps to get the total for the day
        daily_steps.append(daily_step_count)  
    
    return daily_steps  # Return the list of daily step counts

def compute_stats(step_dict):
    # Initialize an empty dictionary to store statistics for each member
    stats_dict = {}
    
    # Iterate over each member's daily steps in the dictionary
    for key, value in step_dict.items():
        # Calculate and store the minimum, maximum, and average steps
        stats_dict[key] = {
            "min": min(value),  # Minimum daily steps
            "max": max(value),  # Maximum daily steps
            "average": numpy.mean(value)  # Average daily steps
        }

    return stats_dict  # Return the dictionary of statistics

def choose_categories(avg_list):
    # Initialize a dictionary to count members in each category
    categories = {"concerning": 0, "average": 0, "excellent": 0}
    
    # Iterate over the average steps to categorize each member
    for avg_steps in avg_list:
        # Categorize based on the average step count
        if avg_steps < 5000:
            categories["concerning"] += 1  # Increment concerning count
        elif 5000 <= avg_steps < 10000:
            categories["average"] += 1  # Increment average count
        else:
            categories["excellent"] += 1  # Increment excellent count

    return categories  # Return the dictionary of categorized counts

def daily_to_total(daily_steps):
    # Initialize a dictionary to store the total steps for each member
    total_dict = {}
    for name, steps in daily_steps.items():
        total_dict[name] = sum(steps)  # Calculate total steps by summing daily steps
    return total_dict  # Return the total steps dictionary

def find_min_index(input_list): 
    current_min = input_list[0]  # Start with the first element as the minimum
    index = 0  # Initialize index for the minimum value
    for i in range(len(input_list)):
        if input_list[i] < current_min:  # Update if a new minimum is found
            current_min = input_list[i]
            index = i
    return index  # Return the index of the minimum value

def my_sort(user_names, user_steps):
    # Initialize lists to store sorted user names and steps
    sorted_user_names = []
    sorted_user_steps = []
    
    # Sort the steps using the selection sort technique
    for i in range(len(user_steps)):
        min_index = find_min_index(user_steps)  # Find the index of the minimum step count
        sorted_user_names.append(user_names[min_index])
        sorted_user_steps.append(user_steps[min_index])
        # Mark the used step count as 'infinity' to avoid re-selection
        user_steps[min_index] = float("inf")

    return sorted_user_names, sorted_user_steps  # Return the sorted lists

def plot_line(steps, save_path=""):
    hour_list = range(24)
    # Create a line plot for the hourly steps
    pyplot.plot(hour_list, steps)
    # Set the title and labels for the plot
    pyplot.title("Performance over the day")
    pyplot.xlabel("Hour of the day")
    pyplot.ylabel("Number of steps")
    pyplot.savefig(save_path + "plot_line.png")
    # Close the plot to free up memory
    pyplot.close()

def main():
    # Load data from a CSV file, specifying the delimiter and data type as strings
    data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)
    
    # Convert the loaded data into a dictionary using the data_to_dict function
    data_dict = data_to_dict(data)

    # Initialize an empty dictionary to store daily steps for each member
    daily_step_dict = {}
    for key in data_dict.keys():
        daily_step_dict[key] = hourly_to_daily(data_dict[key])

    # Compute statistics for each member's daily steps
    stats_dict = compute_stats(daily_step_dict)

    # Create a list of average steps for each member
    avg_list = []
    for name in stats_dict:
        stats = stats_dict[name]
        avg_list.append(stats["average"])  # Collect average steps

    # Categorize members based on their average steps
    categories = choose_categories(avg_list)

    # Calculate total steps for each member
    total_step_dict = daily_to_total(daily_step_dict)

    # Prepare lists for sorting
    unsorted_names = list(total_step_dict.keys())
    unsorted_steps = list(total_step_dict.values())
    
    # Sort names and steps using my_sort function
    sorted_names, sorted_steps = my_sort(unsorted_names, unsorted_steps)

    # Prepare the steps for plotting (selecting the first 24 hours of a specific user)
    steps = data_dict["Juliana"][0:24]  # Adjust the name to choose a different user if needed
    # Call the plot function with the steps data and save path
    plot_line(steps, save_path="e:/Documents & Learning/Python/FitData Insights/")

# Call the main function to execute the program
main()