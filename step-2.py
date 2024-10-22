'''
What requirements do you think we can fulfill at this point?


1. We can partially work on requirement 2 by storing the data in lists (we don’t know about dictionaries yet).

2. We can also compute a statistics summary for a member’s daily activity (requirement 3).

3. We can categorize the members into groups based on their week’s performance. For example, given a threshold of 5000 steps, we can print the list of members that lie in zones red, yellow, or green (requirement 4b).

'''

# Storing daily steps in a list

'''
For requirement 2, proceed in two steps. 

In step 1, separate the user name and hourly data. The idea is to initialize a name variable with the first element of the data list. The rest of the data, beyond the very first element, should be assigned to another hourly_steps named variable/list.

In step 2, reduce the long hourly list of data to a neater daily list of steps because most of the data analysis is to be done on daily steps, not hourly steps. 

'''
# Step 1:

data = ["Juliana", 857, 1178, 1134, 1133, 780, 1017, 821, 1180, 0, 0, 0, 0, 0, 0, 0, 1032, 42, 1129, 1126, 40, 1032, 743, 1194, 993, 1054, 969, 1046, 924, 1064, 1117, 1094, 795, 0, 0, 0, 0, 0, 0, 44, 26, 47, 736, 22, 46, 851, 27, 846, 769, 1071, 942, 1010, 1055, 1011, 834, 1104, 889, 0, 0, 0, 0, 0, 1120, 38, 1190, 1100, 959, 874, 1130, 941, 813, 1106, 934, 1117, 1043, 1053, 997, 1055, 1043, 824,
        1183, 908, 0, 0, 0, 0, 0, 0, 0, 937, 1188, 1145, 747, 1109, 20, 984, 812, 1059, 742, 739, 926, 1188, 1072, 1113, 938, 0, 0, 0, 0, 0, 1067, 26, 29, 45, 722, 796, 32, 28, 36, 1094, 896, 798, 1101, 963, 928, 829, 842, 1136, 1115, 0, 0, 0, 0, 0, 0, 0, 27, 769, 26, 1133, 830, 20, 43, 869, 924, 990, 1000, 963, 768, 1003, 754, 788, 0, 0, 0, 0, 0, 0, 33, 35, 37, 853, 50, 797, 35, 21, 46, 950, 1099]

name = data[0]  # The first element is the user's name
hourly_steps = data[1:] 

# Print the member's name and their hourly steps
print("Member:", name)
print("Hourly steps data:", hourly_steps)


def hourly_to_daily_step(hourly_steps):
    daily_steps = []  # List to store the total steps for each day

    # Loop through the hourly steps in chunks of 24 (each day)
    for i in range(0, len(hourly_steps), 24):
        day_counts = sum(hourly_steps[i:i + 24])  # Sum the steps for the current day
        daily_steps.append(day_counts)  # Append the daily count to the list

    return daily_steps  # Return the list of daily step counts


daily_steps = hourly_to_daily_step(hourly_steps)
print("Daily steps:", daily_steps)  # Display the calculated daily steps

# Compute summary statistics for daily steps
daily_max = max(daily_steps)  # Maximum daily steps
daily_min = min(daily_steps)  # Minimum daily steps
daily_avg = sum(daily_steps) / len(daily_steps)  # Average daily steps

# Print daily steps and summary statistics
print(name + "'s daily steps:", daily_steps)
print("Summary stats for", name)
print("Max: ", daily_max)  # Display maximum steps
print("Min: ", daily_min)  # Display minimum steps
print("Average: ", daily_avg)  # Display average steps

# Function to categorize performance based on average daily steps
def choose_categories(steps):
    if steps < 5000:
        return "concerning"  # Less than 5000 steps is concerning
    elif 5000 <= steps < 10000:
        return "average"  # 5000 to 9999 steps is average
    else:
        return "excellent"  # 10000 steps or more is excellent

# Call the categorization function based on average steps
category = choose_categories(daily_avg)
print("Performance of", name, "this week:", category)  # Display performance category