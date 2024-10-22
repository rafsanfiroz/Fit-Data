# Categorizing data

'''
Categorize the users into three groups based on their average number of steps in a week. Complete a choose_categories() named function to find the group that takes in avg_list and returns a dictionary for the number of members in each category. The categories are defined as follows:

 - Below 5,000 steps are concerning.

 - 5,000 steps or above but below 10,000 are average.

 - 10,000 or more steps are excellent.
'''
import numpy 

def data_to_dict(data):
    # Initialize an empty dictionary to store the member names and their corresponding hourly steps
    data_dict = {}
    
    # Iterate over each row in the data, starting from the second row (index 1) 
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
    
   
    for i in range(0, len(hourly_steps), 24):
        day_steps = hourly_steps[i:i+24]  # Get the steps for the current day (24 hours)
        daily_step_count = sum(day_steps)  # Sum the hourly steps to get the total for the day
        daily_steps.append(daily_step_count)  # Append the daily total to the list
    
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

def main():
  
    data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)
    
    # Convert the loaded data into a dictionary using the data_to_dict function
    data_dict = data_to_dict(data)

    # Initialize an empty dictionary to store daily steps for each member
    daily_step_dict = {}
    
    # Populate daily_step_dict using data_dict and the hourly_to_daily function
    for key in data_dict.keys():
        daily_step_dict[key] = hourly_to_daily(data_dict[key])

    # Compute statistics for each member's daily steps
    stats_dict = compute_stats(daily_step_dict)

    # Separating out a list of average steps for each member
    avg_list = []
    for name in stats_dict:
        stats = stats_dict[name]
        avg_list.append(stats["average"])  # Collect average steps

    # Calling the categorizing function and storing its output in a variable
    categories = choose_categories(avg_list)

    # Print the number of members in each category
    print("Members in each group:", categories)

# Call the main function to execute the program
main()