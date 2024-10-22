# Plotting a sorted bar plot

# Next, plot a sorted bar plot to show the sorted data.

# Plotting a pie chart to show the categories of the population

# The next step is to categorize the data using a pie chart.


import numpy
from matplotlib import pyplot

def data_to_dict(data):
    data_dict = {}
    # Iterate through rows of data starting from the second row (index 1)
    for i in range(1, len(data)):
        row = data[i]
        name = row[0]  # First element is the user name
        steps = numpy.array(row[1:], dtype=int)  # Convert remaining elements to an array of integers
        data_dict[name] = steps  
    return data_dict

def hourly_to_daily(hourly_steps):
    daily_steps = []
    for i in range(0, len(hourly_steps), 24):
        day_steps = hourly_steps[i:i+24]  # Get a slice for one day
        daily_step_count = sum(day_steps)  # Sum the steps for that day
        daily_steps.append(daily_step_count)  # Append the daily total to the list
    return daily_steps

def compute_stats(step_dict):
    stats_dict = {}
    # Calculate statistics for each user's daily steps
    for key, value in step_dict.items():
        stats_dict[key] = {
            "min": min(value),  # Minimum steps in a day
            "max": max(value),  # Maximum steps in a day
            "average": numpy.mean(value)  # Average steps across days
        }
    return stats_dict

def choose_categories(avg_list):
    categories = {"concerning": 0, "average": 0, "excellent": 0}
    # Categorize average steps into three groups
    for avg_steps in avg_list:
        if avg_steps < 5000:
            categories["concerning"] += 1  # Count users with concerning activity
        elif 5000 <= avg_steps < 10000:
            categories["average"] += 1  # Count users with average activity
        else:
            categories["excellent"] += 1  # Count users with excellent activity
    return categories

def daily_to_total(daily_steps):
    total_dict = {}
    # Calculate total steps for each user
    for name, steps in daily_steps.items():
        total_dict[name] = sum(steps)  # Sum the daily steps for each user
    return total_dict

def find_min_index(input_list):
    current_min = input_list[0]  # Initialize with the first element
    index = 0  # Start with index 0
    # Find the index of the minimum value in the list
    for i in range(len(input_list)):
        if input_list[i] < current_min:
            current_min = input_list[i]
            index = i  # Update index if a new minimum is found
    return index

def my_sort(user_names, user_steps):
    sorted_user_names = []
    sorted_user_steps = []
    # Sort users and their corresponding step counts
    for i in range(len(user_steps)):
        min_index = find_min_index(user_steps)  # Find index of minimum steps
        sorted_user_names.append(user_names[min_index])  # Append sorted name
        sorted_user_steps.append(user_steps[min_index])  # Append sorted step count
        user_steps[min_index] = float("inf")  # Mark as used
    return sorted_user_names, sorted_user_steps

def plot_line(steps, save_path=""):
    hour_list = range(24)  # List of hours for x-axis
    # Create a line plot for daily steps
    pyplot.title("Performance Over the Day")
    pyplot.xlabel("Hour of the Day")
    pyplot.ylabel("Number of Steps")
    pyplot.plot(hour_list, steps)  # Plot the steps against hours
    pyplot.savefig(save_path + "plot_line.png")  # Save the plot as an image
    pyplot.close()  # Close the plot to free memory

def plot_pie(categories, save_path=""):
    # Create a pie chart for the category distribution
    pyplot.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%', startangle=140)
    pyplot.title("Distribution of User Activity Categories")  # Title for the pie chart
    pyplot.savefig(save_path + "plot_pie.png")  # Save the pie chart as an image
    pyplot.close()  # Close the plot to free memory

def plot_bar(sorted_names, sorted_steps, save_path=""):
    # Create a bar plot for sorted step counts
    pyplot.bar(sorted_names, sorted_steps, color='skyblue')  # Bar plot with a specified color
    pyplot.title("Sorted User Step Counts")  # Title for the bar plot
    pyplot.xlabel("User Names")  
    pyplot.ylabel("Total Steps")  
    pyplot.xticks(rotation=45, ha='right')  
    pyplot.tight_layout()  
    pyplot.savefig(save_path + "plot_bar.png")  # Save the bar plot as an image
    pyplot.close()  # Close the plot to free memory

def main():
   
    data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)
    data_dict = data_to_dict(data)  # Convert data to a dictionary

    daily_step_dict = {}
    # Calculate daily steps for each user
    for key in data_dict.keys():
        daily_step_dict[key] = hourly_to_daily(data_dict[key])

    stats_dict = compute_stats(daily_step_dict)  # Compute statistics for daily steps

    avg_list = []
    # Prepare a list of average steps for categorization
    for name in stats_dict:
        stats = stats_dict[name]
        avg_list.append(stats["average"])

    categories = choose_categories(avg_list)  # Categorize users based on average steps

    total_step_dict = daily_to_total(daily_step_dict)  # Calculate total steps for each user

    unsorted_names = list(total_step_dict.keys())  # Get unsorted names
    unsorted_steps = list(total_step_dict.values())  # Get unsorted step counts
    sorted_names, sorted_steps = my_sort(unsorted_names, unsorted_steps)  # Sort names and steps

    # Select steps for a line plot from a specific user
    steps = data_dict["Juliana"][0:24]  # Get the first 24 hours of steps for "Juliana"
    plot_line(steps, save_path="e:/Documents & Learning/Python/FitData Insights/")  # Plot line chart

    # Plot the pie chart for category distribution
    plot_pie(categories, save_path="e:/Documents & Learning/Python/FitData Insights/")

    # Plot the sorted bar plot for user step counts
    plot_bar(sorted_names, sorted_steps, save_path="e:/Documents & Learning/Python/FitData Insights/")

# Execute the main function
main()