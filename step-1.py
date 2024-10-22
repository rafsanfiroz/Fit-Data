# Below codes effectively filters out the name and the last step count, providing a cleaner list of daily steps.


fitness_data = ["Juliana", 7000, 5500, 10300, 8000, 1200, 2000, 5000] 

first_index = 0 # represents the position of the first item in the list.
print(fitness_data[first_index]) 

last_index = len(fitness_data) -1  # calculates the position of the last item in the list by getting the total number of items
print(fitness_data[last_index])

fitness_data = ["Juliana", 7000, 5500, 10300, 8000, 1200, 2000, 5000]
slice_list = fitness_data[1:3] #creates a new list that includes the items from index 1 to index 2 of the fitness_data list (the second and third numbers of steps
print(slice_list)

fitness_data = ["Juliana", 7000, 5500, 10300, 8000, 1200, 2000, 5000]
list_daily_steps = [] # empty list which will be used to store step counts

list_daily_steps = fitness_data[1:(len(fitness_data) -1)] # includes only the daily step counts, excluding the first item (the name "Juliana") and the last item (the last step count)
print(list_daily_steps)

list_daily_steps = [7000, 5500, 10300, 8000, 1200, 2000, 5000]
for steps in list_daily_steps:   # go through each number (step count) in the list_daily_steps
    print(steps)

for index in range(5):
  print(index)