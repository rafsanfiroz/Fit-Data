# Plotting a bubble plot


# Plotting a sorted bar plot

# Next, plot a sorted bar plot to show the sorted data.

# Plotting a pie chart to show the categories of the population

# The next step is to categorize the data using a pie chart.


import numpy
from matplotlib import pyplot

def data_to_dict(data):
    data_dict = {}
    for i in range(1, len(data)):
        row = data[i] # Get the current row of data
        name = row[0] # The first element in the row is the member's name
        steps = numpy.array(row[1:], dtype=int) 
        data_dict[name] = steps 
    return data_dict

def hourly_to_daily(hourly_steps):
    daily_steps = []
    for i in range(0, len(hourly_steps), 24):
        day_steps = hourly_steps[i:i+24]  # Getting steps for each day
        daily_step_count = sum(day_steps)  # Summing steps for the day
        daily_steps.append(daily_step_count)  # Adding to daily_steps list
    return daily_steps

def compute_stats(step_dict):
    stats_dict = {}
    # Calculating statistics for each user
    for key, value in step_dict.items():
        stats_dict[key] = {
            "min": min(value),  # Minimum daily steps
            "max": max(value),  # Maximum daily steps
            "average": numpy.mean(value)  # Calculating average 
        }
    return stats_dict

def choose_categories(avg_list):
    categories = {"concerning": 0, "average": 0, "excellent": 0}
    # Categorizing average steps
    for avg_steps in avg_list:
        if avg_steps < 5000:
            categories["concerning"] += 1 # Increment concerning count
        elif 5000 <= avg_steps < 10000:
            categories["average"] += 1   # Increment average count
        else:
            categories["excellent"] += 1  # Increment excellent count
    return categories

def daily_to_total(daily_steps):
    total_dict = {}
    # Summing up total steps for each user
    for name, steps in daily_steps.items():
        total_dict[name] = sum(steps)
    return total_dict

def find_min_index(input_list):  
    current_min = input_list[0]
    index = 0
    # Finding the index of the minimum value
    for i in range(len(input_list)):
        if input_list[i] < current_min:
            current_min = input_list[i]
            index = i
    return index

def my_sort(user_names, user_steps):
    sorted_user_names = []
    sorted_user_steps = []
    # Sorting users based on their step counts
    for i in range(len(user_steps)):
        min_index = find_min_index(user_steps)
        sorted_user_names.append(user_names[min_index])
        sorted_user_steps.append(user_steps[min_index])
        user_steps[min_index] = float("inf")  # Marking as used
    return sorted_user_names, sorted_user_steps

def plot_line(steps, save_path=""):
    hour_list = range(24)  # Hours in a day
    pyplot.title("Performance over the day")
    pyplot.xlabel("Hour of the day")
    pyplot.ylabel("Number of steps")
    pyplot.plot(hour_list, steps)  # Plotting line graph
    pyplot.savefig(save_path+"plot_line.png")  # Saving the plot
    pyplot.close()  # Closing the plot

def plot_pie(categories, save_path=""):
    # Creating a pie chart for categories
    pyplot.pie(categories.values(), labels=categories.keys())
    pyplot.title("Pie chart for categories")
    pyplot.savefig(save_path+"plot_pie.png")  # Saving the pie chart
    pyplot.close()  # Closing the plot

def plot_bar(sorted_names, sorted_steps, save_path=""):
    # Creating a bar graph
    pyplot.bar(sorted_names, sorted_steps)
    pyplot.xticks(rotation=45)  
    pyplot.tight_layout()  # Adjust layout
    pyplot.savefig(save_path+"plot_bar.png")  # Saving the bar graph
    pyplot.close()  # Closing the plot

def plot_bubbles(daily_step_dict, save_path=""):
    # Creating a bubble plot for daily steps of users
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for name in daily_step_dict:
        pyplot.scatter(days, [name]*7, numpy.array(daily_step_dict[name])/30)  # Adjusting size for visibility
    pyplot.title("Bubble plot for all members")
    pyplot.xlabel("Day of the week")
    pyplot.ylabel("User name")
    pyplot.savefig(save_path+"plot_bubbles.png")  # Saving the bubble plot
    pyplot.close()  # Closing the plot

def main():
    # Loading and processing data
    data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)
    data_dict = data_to_dict(data)

    daily_step_dict = {}
    for key in data_dict.keys():
        daily_step_dict[key] = hourly_to_daily(data_dict[key])

    stats_dict = compute_stats(daily_step_dict)

    avg_list = []
    for name in stats_dict:
        stats = stats_dict[name]
        avg_list.append(stats["average"])

    categories = choose_categories(avg_list)

    total_step_dict = daily_to_total(daily_step_dict)

    unsorted_names = list(total_step_dict.keys())
    unsorted_steps = list(total_step_dict.values())
    sorted_names, sorted_steps = my_sort(unsorted_names, unsorted_steps)

    steps = data_dict["Juliana"][0:24]  
    plot_line(steps, save_path="e:/Documents & Learning/Python/FitData Insights/")

    # Function call to plot the pie chart
    plot_pie(categories, save_path="e:/Documents & Learning/Python/FitData Insights/")

    # Function call to plot sorted bar chart
    plot_bar(sorted_names, sorted_steps, save_path="e:/Documents & Learning/Python/FitData Insights/")

    # Function call to plot the bubble plot
    plot_bubbles(daily_step_dict, save_path="e:/Documents & Learning/Python/FitData Insights/")

main()
