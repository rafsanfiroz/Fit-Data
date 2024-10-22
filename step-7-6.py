# Printing sorted info (name, steps, and rank)
import numpy
def read_data_in_dict(file_name):
    
    data = numpy.loadtxt(file_name, delimiter=",", dtype=str)
    data_dict = {}
    
    for row in data[1:]:
        name = row[0]  # User's name
        steps = numpy.array(row[1:], dtype=int) # Convert the rest to integers
        data_dict[name] = steps
        
    return data_dict

def hourly_to_daily_list(hourly_list):
    #Converts hourly step counts to daily totals.
    return [sum(hourly_list[i:i + 24]) for i in range(0, len(hourly_list), 24)]

def hourly_to_daily(hourly_dict):
    #Converts a dictionary of hourly counts to daily totals.
    return {user_name: hourly_to_daily_list(steps) for user_name, steps in hourly_dict.items()}

def reduce_daily_to_weekly_dict(daily_data):
    #Reduces daily counts to weekly totals for each user.
    return {key: sum(values) for key, values in daily_data.items()}

def compile_user_steps_lists(weekly_data):
     #Compiles user names and weekly step counts into lists.
    return list(weekly_data.keys()), list(weekly_data.values())

def print_sorted_info(user_names, user_steps):
    
    for rank, (name, steps) in enumerate(zip(user_names, user_steps)):
        print(f"{name} has taken {steps} steps in the week, and stands at rank: {rank + 1}

def main():
    
    file_name = "steps.csv"  
    hourly_data = read_data_in_dict(file_name)  
    daily_data = hourly_to_daily(hourly_data)  # Convert to daily totals
    weekly_data = reduce_daily_to_weekly_dict(daily_data) 
    user_names, user_steps = compile_user_steps_lists(weekly_data)  # Compile lists for sorting

    # Sort users based on their weekly step counts
    sorted_data = sorted(zip(user_names, user_steps), key=lambda x: x[1])
    sorted_user_names, sorted_user_steps = zip(*sorted_data)  

    print_sorted_info(sorted_user_names, sorted_user_steps) 

main()
