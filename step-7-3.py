# Computing a dictionary—one weekly entry per user

import numpy  

def read_data_in_dict(file_name):
   
    data = numpy.loadtxt(file_name, delimiter=",", dtype=str)
    
    data_dict = {}  # Initialize an empty dictionary to store the data

    # Loop through each row of data starting from index 1 
    for i in range(1, len(data)):
        row = data[i]  
        name = row[0]  
        
        # Convert the remaining elements of the row to an integer array for steps
        steps = numpy.array(row[1:], dtype=int)
        
        # Store the name as the key and steps as the value in the dictionary
        data_dict[name] = steps
    
    return data_dict  # Return the populated dictionary


def hourly_to_daily_list(hourly_list):
    daily_steps = []  
 
    for i in range(0, len(hourly_list), 24):
        day_steps = hourly_list[i:i+24]  # Get the steps for the current day
        daily_step_count = sum(day_steps)  # Sum the hourly steps to get the daily total
        daily_steps.append(daily_step_count)  # Add the daily total to the list
    return daily_steps  


def hourly_to_daily(hourly_dict):
    daily_dict = {}  
    # Loop through each user in the hourly data dictionary
    for user_name in hourly_dict:
        # Convert hourly steps to daily steps for each user and store it in the new dictionary
        daily_dict[user_name] = hourly_to_daily_list(hourly_dict[user_name])
    return daily_dict  


def reduce_daily_to_weekly_dict(daily_data):
    new_dict = {} 
   
    for key in daily_data:
        # Sum the daily steps for each user to get their total weekly steps
        new_dict[key] = sum(daily_data[key])
    return new_dict  # Return the dictionary containing total weekly steps for each user


def main():
    file_name = "steps.csv"  
    hourly_data = read_data_in_dict(file_name)  
    daily_data = hourly_to_daily(hourly_data)  
    weekly_data = reduce_daily_to_weekly_dict(daily_data)  
    print(weekly_data)  



main() 