# Plotting a bubble plot


# Plotting a sorted bar plot

# Next, plot a sorted bar plot to show the sorted data.

# Plotting a pie chart to show the categories of the population

# The next step is to categorize the data using a pie chart.


import numpy
from matplotlib import pyplot


def data_to_dict(data):
    # Initialize an empty dictionary to store the data
    data_dict = {}
    # Iterate over each row of the data (starting from the second row)
    for i in range(1, len(data)):
        row = data[i]  # Get the current row
        name = row[0]  # The first element is the user's name
        steps = numpy.array(row[1:], dtype=int)  # Convert the rest of the row to an array of integers
        data_dict[name] = steps  # Store the steps in the dictionary with the name as the key
    return data_dict  

def hourly_to_daily(hourly_steps):
    # Initialize a list to store daily step counts
    daily_steps = []
    
    for i in range(0, len(hourly_steps), 24):
        day_steps = hourly_steps[i:i+24]  # Slice the hourly steps for the current day
        daily_step_count = sum(day_steps)  # Calculate the total steps for the day
        daily_steps.append(daily_step_count)  # Add to the list of daily steps
    return daily_steps 

def compute_stats(step_dict):
    # Initialize an empty dictionary to hold statistics
    stats_dict = {}
   
    for key, value in step_dict.items():
        # Calculate min, max, and average steps for each user
        stats_dict[key] = {
            "min": min(value),
            "max": max(value),
            "average": numpy.mean(value)
        }
    return stats_dict  # Return the dictionary of statistics

def choose_categories(avg_list):
    # Initialize categories for step counts
    categories = {"concerning": 0, "average": 0, "excellent": 0}
    # Classify average steps into categories
    for avg_steps in avg_list:
        if avg_steps < 5000:
            categories["concerning"] += 1  # Increment concerning category
        elif 5000 <= avg_steps < 10000:
            categories["average"] += 1  # Increment average category
        else:
            categories["excellent"] += 1  # Increment excellent category
    return categories  # Return the categorized counts

def daily_to_total(daily_steps):
    # Initialize an empty dictionary for total steps
    total_dict = {}
    # Calculate total steps for each user
    for name, steps in daily_steps.items():
        total_dict[name] = sum(steps)  # Sum the daily steps
    return total_dict  # Return the dictionary of total steps

def find_min_index(input_list):  
    current_min = input_list[0]  # Assume first element is the minimum
    index = 0  # Index of the minimum element
   
    for i in range(len(input_list)):
        if input_list[i] < current_min:
            current_min = input_list[i]  # Update the current minimum
            index = i  # Update the index of the minimum
    return index  # Return the index of the minimum element

def my_sort(user_names, user_steps):
    # Initialize lists to hold sorted user names and steps
    sorted_user_names = []
    sorted_user_steps = []
    # Sort user steps and names
    for i in range(len(user_steps)):
        min_index = find_min_index(user_steps)  # Find the index of the minimum steps
        sorted_user_names.append(user_names[min_index])  # Add the corresponding name to sorted list
        sorted_user_steps.append(user_steps[min_index])  # Add the corresponding steps to sorted list
        user_steps[min_index] = float("inf")  # Mark this step as processed
    return sorted_user_names, sorted_user_steps  # Return the sorted lists

def plot_line(steps, save_path=""):
    # Create a line plot for steps over 24 hours
    hour_list = range(24) 
    pyplot.title("Performance over the day") 
    pyplot.xlabel("Hour of the day")  
    pyplot.ylabel("Number of steps")  
    pyplot.plot(hour_list, steps)  
    pyplot.savefig(save_path + "plot_line.png")  # Save the plot as an image
    pyplot.close()  # Close the plot

def plot_pie(categories, save_path=""):
    # Create a pie chart for step categories
    pyplot.pie(categories.values(), labels=categories.keys())  # Create pie chart with labels
    pyplot.title("Pie chart for categories")  
    pyplot.savefig(save_path + "plot_pie.png")  # Save the pie chart as an image
    pyplot.close()  # Close the plot

def plot_bar(sorted_names, sorted_steps, save_path=""):
    # Create a bar graph for sorted user names and their total steps
    pyplot.bar(sorted_names, sorted_steps)  
    pyplot.xticks(rotation=45)  # Rotate x-axis labels for better visibility
    pyplot.tight_layout()  # Adjust layout to prevent clipping
    pyplot.savefig(save_path + "plot_bar.png")  # Save the bar graph as an image
    pyplot.close()  # Close the plot

def plot_bubbles(daily_step_dict, save_path=""):
    # Create a bubble plot for daily steps per user
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  
    for name in daily_step_dict:
        pyplot.scatter(days, [name] * 7, numpy.array(daily_step_dict[name]) / 30)  # Normalize bubble sizes
    pyplot.title("Bubble plot for all members")  # Title of the bubble plot
    pyplot.xlabel("Day of the week")  # X-axis label
    pyplot.ylabel("User name")  # Y-axis label
    pyplot.savefig(save_path + "plot_bubbles.png")  # Save the bubble plot as an image
    pyplot.close()  # Close the plot

def main():
    # Load step data from a CSV file
    data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)
    data_dict = data_to_dict(data)  # Convert the data to a dictionary

    daily_step_dict = {}
    # Convert hourly steps to daily steps for each user
    for key in data_dict.keys():
        daily_step_dict[key] = hourly_to_daily(data_dict[key])

    stats_dict = compute_stats(daily_step_dict)  # Compute statistics for each user

    avg_list = []
    # Collect average steps for each user
    for name in stats_dict:
        stats = stats_dict[name]
        avg_list.append(stats["average"])

    categories = choose_categories(avg_list)  # Classify users based on average steps

    total_step_dict = daily_to_total(daily_step_dict)  # Calculate total steps for each user

    unsorted_names = list(total_step_dict.keys())  # List of unsorted user names
    unsorted_steps = list(total_step_dict.values())  # List of unsorted total steps
    sorted_names, sorted_steps = my_sort(unsorted_names, unsorted_steps)  # Sort names and steps

    steps = data_dict["Juliana"][0:24]  # Get the first 24 hourly steps for Juliana

    
    plot_line(steps, save_path="e:/Documents & Learning/Python/FitData Insights/")

 
    plot_pie(categories, save_path="e:/Documents & Learning/Python/FitData Insights/")

  
    plot_bar(sorted_names, sorted_steps, save_path="e:/Documents & Learning/Python/FitData Insights/")

   
    plot_bubbles(daily_step_dict, save_path="e:/Documents & Learning/Python/FitData Insights/")

# Execute the main function
main()
