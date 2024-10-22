# Computing required data

'''
Before plotting the graphs, process the data you read into the data you need to plot the visualizations. To calculate the performance statistics of individual users, you need to first obtain a list containing daily steps instead of hourly steps because that is your client’s requirement.

In the main() function, utilize the hourly_to_daily() function and make a dictionary that contains the names as keys and the daily step lists as values.
'''


import numpy 

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
    
    return data_dict  # Return the dictionary

def hourly_to_daily(hourly_steps):
    # Initialize a list to store daily step counts
    daily_steps = []
    
    
    for i in range(0, len(hourly_steps), 24):
        day_steps = hourly_steps[i:i+24]  # Get the steps for the current day (24 hours)
        daily_step_count = sum(day_steps)  # Sum the hourly steps to get the total for the day
        daily_steps.append(daily_step_count)  # Append the daily total to the list
    
    return daily_steps  # Return the list of daily step counts

def main():
    # Load data from a CSV file, specifying the delimiter and data type as strings
    data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)
    
    # Convert the loaded data into a dictionary using the data_to_dict function
    data_dict = data_to_dict(data)

    # Initialize an empty space to store daily steps for each member
    daily_step_dict = {}
    
    # Populate daily_step_dict using data_dict and the hourly_to_daily function
    for key in data_dict:
    
        daily_step_dict[key] = hourly_to_daily(data_dict[key])

    # Print the resulting dictionary of daily step counts for each member
    print(daily_step_dict)

# Call the main function to execute the program
main()




