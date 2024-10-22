# Dictionaries in Python
'''
fitness_list = ["Juliana", 7000, 5500, 10300, 8000, 1200, 2000, 5000]
print("List looks like ", fitness_list)

key = fitness_list[0]
value = fitness_list[1:]

fitness_dictionary = {}
fitness_dictionary[key] = value

print("Dictionary looks like", fitness_dictionary)

# Insert List into dictionary

fitness_list1 = ["Juliana", 7000, 5500, 10300, 8000, 1200, 2000, 5000]
fitness_list2 = ["Ulises", 347, 625, 729, 977, 0, 0, 0]

key1 = fitness_list1[0]
value1 = fitness_list1[1:]
key2 = fitness_list2[0]
value2 = fitness_list2[1:]

fitness_dictionary = {}
fitness_dictionary[key1] = value1
fitness_dictionary[key2] = value2

print("Dictionary looks like", fitness_dictionary)
'''
# Loading data from an external file into a dictionary

import numpy

# Reading data from a file
data = numpy.loadtxt("steps.csv", delimiter = ",", dtype = str)

# Adding data to dictionary
data_dict = {}
for i in range(1, len(data)): # Choosing 1 instead of 0 to skip the header row
    row = data[i] # <--- Picking out a list from data
    name = row[0] # <--- Extracting name
    steps = numpy.array(row[1:], dtype = int) # <--- Extracting list of steps as integer
    data_dict[name] = steps # <--- Adding key:value pair to the dictionary

print(data_dict)

'''
Here’s a breakdown of how dictionaries are used in this code:

1. Reading data from a file: The CSV data is loaded into a NumPy array data using the numpy.loadtxt function. The dtype=str parameter ensures that all data is read as strings.

2. Adding data to the dictionary:

  - A new empty dictionary data_dict is created to store the data.
  - A for loop is used to iterate over each row in the data array, starting from index 1 to skip the header row.
  - For each row, the person’s name is extracted from the first element (row[0]), and the steps taken are extracted as a NumPy array of integers from the remaining elements (row[1:]).
  - A key-value pair is added to the data_dict dictionary, where the key is the person’s name, and the value is the array of steps taken.

3. Printing the dictionary: Finally, the data_dict dictionary is printed to display the stored data.

'''

# Print data for Jasmin

import numpy

# Reading data from a file
data = numpy.loadtxt("steps.csv", delimiter = ",", dtype = str)

# Adding data to dictionary
data_dict = {}
for i in range(1, len(data)): # Choosing 1 instead of 0 to skip the header row
    row = data[i] # <--- Picking out a list from data
    name = row[0] # <--- Extracting name
    steps = numpy.array(row[1:], dtype = int) # <--- Extracting list of steps as integer
    data_dict[name] = steps # <--- Adding key:value pair to the dictionary

print("Number of elements in the dictionary:", len(data_dict))  # Print the number of elements (key-value pairs) in the dictionary named data_dict
print("Lenght of a list of steps:", len(data_dict["Jasmin"])) 