# Problem Solving—Integration

# Reading the data (hourly) in a dictionary

'''
Our integration journey starts with reading the hourly data that our client has provided and loading it up into a dictionary.
'''

import numpy


import numpy  # Import the NumPy library for numerical operations

def read_data_in_dict(file_name):
    # Load data from the specified CSV file
    
    data = numpy.loadtxt(file_name, delimiter=",", dtype=str) # The data is separated by commas (delimiter=",") and all values are read as strings (dtype=str)
    
    data_dict = {}  # Initialize an empty dictionary to store the data

   
    for i in range(1, len(data)):
        row = data[i]  # Get the current row of data
        name = row[0]  
        
       
        steps = numpy.array(row[1:], dtype=int)
         # Convert the remaining elements of the row to an integer array for steps
        
        data_dict[name] = steps
    
    return data_dict  # Return the populated dictionary

def main():
    file_name = "steps.csv"  
    hourly_data = read_data_in_dict(file_name)  # Call the function to read data into a dictionary
    print(hourly_data)  # Print the resulting dictionary to see the data


main() 