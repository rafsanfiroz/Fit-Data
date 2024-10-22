# Computing performance statistics

'''
Now, proceed to calculate the statistics for the data. While calculating statistics at the end of the “Importing Libraries” chapter, we calculated the statistics one by one in the main() function. Doing that for all ten members will mess up the structure of your code, making it hard to read, understand, and reuse. To tackle this issue, make a function that will take in the data_dict dictionary and return another dictionary. This output dictionary will have member names as keys, and the values will be another dictionary of statistics.
'''

import numpy  # Importing the numpy library for numerical operations

def data_to_dict(data):
    # Initialize an empty dictionary 
    data_dict = {}
    
    # Iterate over each row in the data, starting from the second row (index 1) 
    for i in range(1, len(data)):
        row = data[i]  # Get the current row of data
        name = row[0]  # The first element in the row is the member's name
        # Convert the remaining elements in the row to a numpy array of integers
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

def main():
    # Load data from a CSV file, specifying the delimiter and data type as strings
    data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)
    
    # Convert the loaded data into a dictionary using the data_to_dict function
    data_dict = data_to_dict(data)

    # Initialize an empty dictionary to store daily steps for each member
    daily_step_dict = {}
    
    # Populate daily_step_dict using data_dict and the hourly_to_daily function
    for key in data_dict:
        # Convert hourly steps to daily steps for each member and store in the dictionary
        daily_step_dict[key] = hourly_to_daily(data_dict[key])

    # Compute statistics for each member's daily steps
    stats_dict = compute_stats(daily_step_dict)
    
    # Print the statistics for each member
    for key in stats_dict:
        print(key, stats_dict[key])  # Display the member name and their stats

# Call the main function to execute the program
main()
