# Converting hourly data to daily

'''
Eventually, we want to have one whole number per user. We currently have 168 numbers representing the steps taken per hour of the entire week. We’ll get to one number, but first, let’s slice 24 hours and sum them so that we have steps taken every day of the week instead of every hour. Notice the modular approach to our coding structure. This really comes in handy for integration. The new features keep stacking as helper functions while everything else remains as it was.
'''

import numpy  

def read_data_in_dict(file_name):
    
    
    data = numpy.loadtxt(file_name, delimiter=",", dtype=str)
    
    data_dict = {}  # Initialize an empty dictionary to store the data

   
    for i in range(1, len(data)): # Loop through each row of data starting from index 1 
        row = data[i]  # Get the current row of data
        name = row[0]  # The first element is the name 
        
        
        steps = numpy.array(row[1:], dtype=int) # Convert the remaining elements of the row to an integer array for steps
        
     
        data_dict[name] = steps    # Store the name as the key and steps as the value in the dictionary
    
    return data_dict  



def hourly_to_daily_list(hourly_list):
    daily_steps = []  # Initialize an empty list to store daily step counts
   
    for i in range(0, len(hourly_list), 24): # Iterate over the hourly list in chunks of 24 (for each day)
        day_steps = hourly_list[i:i+24]  # Get the steps for the current day
        daily_step_count = sum(day_steps)  # Sum the hourly steps to get the daily total
        daily_steps.append(daily_step_count)  # Add the daily total to the list
    return daily_steps  

def hourly_to_daily(hourly_dict):
    daily_dict = {}  
   
    for user_name in hourly_dict:
        # Convert hourly steps to daily steps for each user and store it in the new dictionary
        daily_dict[user_name] = hourly_to_daily_list(hourly_dict[user_name])
    return daily_dict  


def main():
    file_name = "steps.csv"  
    hourly_data = read_data_in_dict(file_name)  # Call the function to read data into a dictionary
    daily_data = hourly_to_daily(hourly_data)  # Convert hourly data to daily totals
    print(daily_data) 


main()  