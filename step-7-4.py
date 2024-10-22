# Computing two lists—one for users, one for steps

import numpy


def read_data_in_dict(file_name):
   
    data = numpy.loadtxt(file_name, delimiter=",", dtype=str)
    
    data_dict = {} 

    # Loop through each row of data starting from index 1 
    for i in range(1, len(data)):
        row = data[i]  # Get the current row of data
        name = row[0]  # The first element is the name (e.g., a person's name)
        
        # Convert the remaining elements of the row to an integer array for steps
        steps = numpy.array(row[1:], dtype=int)
        
        # Store the name as the key and steps as the value in the dictionary
        data_dict[name] = steps
    
    return data_dict  



def hourly_to_daily_list(hourly_list):
    daily_steps = []  
    # Iterate over the hourly list in chunks of 24 (for each day)
    for i in range(0, len(hourly_list), 24):
        day_steps = hourly_list[i:i+24]  # Get the steps for the current day
        daily_step_count = sum(day_steps)  # Sum the hourly steps to get the daily total
        daily_steps.append(daily_step_count)  # Add the daily total to the list
    return daily_steps 


def hourly_to_daily(hourly_dict):
    daily_dict = {}  # Initialize an empty dictionary to store daily data
   
    for user_name in hourly_dict:
        # Convert hourly steps to daily steps for each user and store it in the new dictionary
        daily_dict[user_name] = hourly_to_daily_list(hourly_dict[user_name])
    return daily_dict  # Return the dictionary containing daily steps for each user


def reduce_daily_to_weekly_dict(daily_data):
    new_dict = {}  
    for key in daily_data:
        # Sum the daily steps for each user to get their total weekly steps
        new_dict[key] = sum(daily_data[key])
    return new_dict 


def compile_user_steps_lists(weekly_data):
    user_names_list = [] 
    user_steps_list = []  
    # Loop through each user in the weekly data dictionary
    for key in weekly_data:
        user_names_list.append(key)  # Add the user's name to the names list
        user_steps_list.append(weekly_data[key])  # Add the user's total weekly steps to the steps list
    return user_names_list, user_steps_list  

def main():
    file_name = "steps.csv"  
    hourly_data = read_data_in_dict(file_name)  
    daily_data = hourly_to_daily(hourly_data)  # Convert hourly data to daily totals
    weekly_data = reduce_daily_to_weekly_dict(daily_data)  # Sum daily data to get weekly totals
    user_names, user_steps = compile_user_steps_lists(weekly_data)  # Compile user names and their weekly steps
    print(user_names, user_steps)  # Print the lists of user names and steps


main()  